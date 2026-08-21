"""Reconnaissance agent: enumerates the authorized lab target (services,
versions, exposed endpoints) and reports structured findings to the planner.

TODO: wrap standard recon tooling (e.g., nmap, service fingerprinting) behind
an agent interface the planner can call and interpret.
"""


class ReconAgent:
    def enumerate(self, target: str, scope: dict) -> dict:
        raise NotImplementedError
