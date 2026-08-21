"""Runs the same orchestrator pipeline against two task sets:
known-CVE tasks and fresh/undocumented-bug tasks, unmodified between runs.

TODO: implement task loading and per-task result collection.
"""


def run_benchmark(task_set_path: str) -> list[dict]:
    raise NotImplementedError
