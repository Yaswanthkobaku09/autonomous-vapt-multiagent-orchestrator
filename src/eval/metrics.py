"""Success rate, time-to-exploit, and false-positive rate, computed
separately for the known-CVE set and the fresh-bug set so the
generalization gap between them is directly visible.

TODO: false-positive rate requires independently re-verifying each
claimed success against ground truth, not trusting the exploit agent's
self-report.
"""


def success_rate(results: list[dict]) -> float:
    raise NotImplementedError


def false_positive_rate(results: list[dict], verified_ground_truth: list[bool]) -> float:
    raise NotImplementedError
