import asyncio
from datetime import datetime, timezone

from scripts.retry_failed_threads import (
    extract_state_values,
    list_error_threads_after,
    list_threads_after,
    save_thread_markdown,
)


def test_extract_state_values_accepts_snapshot_dict():
    assert extract_state_values({"values": {"final_report": "# Wiki"}}) == {
        "final_report": "# Wiki"
    }


def test_save_thread_markdown_exports_final_report(tmp_path):
    class FakeThreads:
        async def get_state(self, thread_id):
            assert thread_id == "thread-1"
            return {
                "values": {
                    "final_report": "# Wiki",
                    "wiki_entry_name": "H13钢",
                }
            }

    class FakeClient:
        threads = FakeThreads()

    path = asyncio.run(
        save_thread_markdown(
            FakeClient(),
            {"thread_id": "thread-1", "metadata": {}},
            output_dir=tmp_path,
        )
    )

    assert path == tmp_path / "H13钢.md"
    assert path.read_text(encoding="utf-8") == "# Wiki"


def test_list_error_threads_after_stops_after_cutoff():
    calls = []

    class FakeThreads:
        async def search(self, **kwargs):
            calls.append(kwargs)
            return [
                {
                    "thread_id": "new",
                    "updated_at": "2026-06-18T00:00:00Z",
                },
                {
                    "thread_id": "old",
                    "updated_at": "2026-06-17T23:59:59Z",
                },
            ]

    class FakeClient:
        threads = FakeThreads()

    threads = asyncio.run(
        list_error_threads_after(
            FakeClient(),
            datetime(2026, 6, 18, 0, 0, tzinfo=timezone.utc),
        )
    )

    assert [thread["thread_id"] for thread in threads] == ["new"]
    assert len(calls) == 1


def test_list_threads_after_all_omits_status_filter():
    calls = []

    class FakeThreads:
        async def search(self, **kwargs):
            calls.append(kwargs)
            return []

    class FakeClient:
        threads = FakeThreads()

    asyncio.run(
        list_threads_after(
            FakeClient(),
            datetime(2026, 6, 18, 0, 0, tzinfo=timezone.utc),
            status=None,
        )
    )

    assert "status" not in calls[0]


def test_list_threads_after_supports_exclusive_upper_bound():
    class FakeThreads:
        async def search(self, **kwargs):
            return [
                {
                    "thread_id": "too-new",
                    "updated_at": "2026-06-25T00:00:00Z",
                },
                {
                    "thread_id": "in-window",
                    "updated_at": "2026-06-24T23:59:59Z",
                },
                {
                    "thread_id": "too-old",
                    "updated_at": "2026-06-20T23:59:59Z",
                },
            ]

    class FakeClient:
        threads = FakeThreads()

    threads = asyncio.run(
        list_threads_after(
            FakeClient(),
            datetime(2026, 6, 21, 0, 0, tzinfo=timezone.utc),
            before_utc=datetime(2026, 6, 25, 0, 0, tzinfo=timezone.utc),
            status="idle",
        )
    )

    assert [thread["thread_id"] for thread in threads] == ["in-window"]
