"""Sequences planner -> recon -> exploit -> privesc agents and carries state
between them for a single engagement run.

TODO: implement the run loop, including re-planning when an agent reports
failure or unexpected findings.
"""


def run_engagement(objective: str, target: str, scope: dict) -> dict:
    raise NotImplementedError
