"""Planning agent: takes a scoped engagement objective and produces an ordered
attack-path strategy for the recon/exploit/privesc agents to execute.

TODO: implement plan generation and re-planning on sub-agent failure/new
recon findings (the plan is not fixed upfront — it updates as agents report back).
"""


class PlannerAgent:
    def plan(self, objective: str, known_state: dict) -> list[dict]:
        raise NotImplementedError

    def replan(self, current_plan: list[dict], new_findings: dict) -> list[dict]:
        raise NotImplementedError
