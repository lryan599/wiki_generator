#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"

SKIP_CONDA="${SKIP_CONDA:-0}"
LOAD_ENV_FILE="${LOAD_ENV_FILE:-1}"
ENV_FILE="${ENV_FILE:-${REPO_ROOT}/.env}"

MKDOCS_HOST="${MKDOCS_HOST:-0.0.0.0}"
MKDOCS_PORT="${MKDOCS_PORT:-8765}"
MKDOCS_CONFIG="${MKDOCS_CONFIG:-${REPO_ROOT}/mkdocs.yml}"

API_HOST="${API_HOST:-0.0.0.0}"
API_PORT="${API_PORT:-8010}"
API_APP="${API_APP:-open_deep_research.retrieval_api:app}"
API_RELOAD="${API_RELOAD:-0}"

LOG_DIR="${LOG_DIR:-${REPO_ROOT}/logs}"
MKDOCS_LOG="${MKDOCS_LOG:-${LOG_DIR}/mkdocs.log}"
API_LOG="${API_LOG:-${LOG_DIR}/retrieval_api.log}"
PID_FILE="${PID_FILE:-${LOG_DIR}/wiki_services.pid}"

cd "${REPO_ROOT}"
mkdir -p "${LOG_DIR}"


PYTHON_BIN="${PYTHON_BIN:-python}"

if [[ "${LOAD_ENV_FILE}" == "1" && -f "${ENV_FILE}" ]]; then
  set -a
  # shellcheck source=/dev/null
  source "${ENV_FILE}"
  set +a
fi

"${PYTHON_BIN}" - <<'PY'
import importlib.util
import sys

missing = [
    module
    for module in ("mkdocs", "fastapi", "uvicorn", "open_deep_research")
    if importlib.util.find_spec(module) is None
]
if missing:
    print("Missing required Python modules: " + ", ".join(missing), file=sys.stderr)
    print("Install dependencies in the active environment before starting services.", file=sys.stderr)
    sys.exit(1)
PY

: > "${MKDOCS_LOG}"
: > "${API_LOG}"

mkdocs_cmd=(
  "${PYTHON_BIN}" -m mkdocs serve
  -f "${MKDOCS_CONFIG}"
  --dev-addr "${MKDOCS_HOST}:${MKDOCS_PORT}"
)

api_cmd=(
  "${PYTHON_BIN}" -m uvicorn "${API_APP}"
  --host "${API_HOST}"
  --port "${API_PORT}"
)

if [[ "${API_RELOAD}" == "1" ]]; then
  api_cmd+=(--reload)
fi

pids=()
names=()
logs=()

start_service() {
  local name="$1"
  local log_file="$2"
  shift 2

  {
    echo "== $(date -Is) starting ${name}"
    printf 'command:'
    printf ' %q' "$@"
    echo
    exec "$@"
  } >> "${log_file}" 2>&1 &

  local pid=$!
  pids+=("${pid}")
  names+=("${name}")
  logs+=("${log_file}")
  echo "${name} started: pid=${pid}, log=${log_file}"
}

cleanup() {
  local pid
  for pid in "${pids[@]:-}"; do
    if kill -0 "${pid}" >/dev/null 2>&1; then
      kill "${pid}" >/dev/null 2>&1 || true
    fi
  done
  wait >/dev/null 2>&1 || true
  rm -f "${PID_FILE}"
}

trap cleanup INT TERM EXIT

start_service "mkdocs" "${MKDOCS_LOG}" "${mkdocs_cmd[@]}"
start_service "retrieval_api" "${API_LOG}" "${api_cmd[@]}"

{
  printf 'mkdocs=%s\n' "${pids[0]}"
  printf 'retrieval_api=%s\n' "${pids[1]}"
} > "${PID_FILE}"

cat <<EOF

Services are running.
MkDocs:        http://${MKDOCS_HOST}:${MKDOCS_PORT}
Retrieval API: http://${API_HOST}:${API_PORT}
PID file:      ${PID_FILE}

Press Ctrl+C to stop both services.
EOF

set +e
wait -n
status=$?
set -e

for i in "${!pids[@]}"; do
  pid="${pids[$i]}"
  if ! kill -0 "${pid}" >/dev/null 2>&1; then
    echo "${names[$i]} exited with status ${status}; see ${logs[$i]}" >&2
    break
  fi
done

exit "${status}"
