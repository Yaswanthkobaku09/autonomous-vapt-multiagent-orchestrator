# Autonomous VAPT Multi-Agent Orchestrator

PhD portfolio project — Tier V, AI in offensive security. Measure the real gap between
"an LLM agent can exploit a known CVE" and "an LLM agent can find and exploit something
novel" — the gap every 2026 benchmark keeps surfacing.

**Authorized-use only.** This project is designed to run exclusively against
intentionally vulnerable lab targets you own or are explicitly authorized to test
(e.g., a local VulnHub/HTB-style VM, a deliberately vulnerable container set). It is a
research and portfolio artifact, not a tool for testing systems you don't have permission
to test.

## The gap

2024–2026 research established that LLM agents can autonomously exploit *known* one-day
vulnerabilities at high rates — GPT-4 exploited 87% of a 15-CVE dataset given only the
advisory text. But 2026 benchmarks tell a very different story on *novel* targets:
CVE-Bench's best agent framework exploited only up to 13% of real web-app vulnerabilities
in a genuine zero-day setting, and DARPA's AI Cyber Challenge specifically inserted fresh,
never-seen bugs into production codebases to rule out memorization — because CTF-style
benchmarks are otherwise contaminated by public writeups the model may have memorized.
The open question isn't "can agents hack" — it's *how much of their success is
generalization versus memorization*, and multi-agent architectures (planner + recon +
exploit + privesc) are the current attempt to close that gap by decomposing the problem
the way a human red-teamer would.

## The project

- Build a small multi-agent orchestrator: a **planning agent** that strategizes attack
  paths, and specialized **recon**, **exploitation**, and **privilege-escalation** agents
  that execute sub-tasks against a local vulnerable lab
- Evaluate on two test sets under the *same* architecture to directly measure the
  generalization gap the field reports:
  1. **Known-CVE set** — public, documented vulnerabilities (expect high success, per
     Fang et al.)
  2. **Fresh-bug set** — a small number of bugs you deliberately insert or configure into
     the lab yourself, unseen anywhere publicly (expect the CVE-Bench-style drop)
- Report success rate, time-to-exploit, and false-positive rate (claimed exploitation
  that doesn't actually reproduce) for both sets

## Status

Scaffold stage — agent roles and orchestration interfaces defined, implementations
pending. No live target integration yet.

## Repository layout

```
src/
  agents/        planner, recon, exploit, and privilege-escalation agent stubs
  orchestrator/  pipeline that sequences agents and passes state between them
  eval/          benchmark runner (known-CVE set vs. fresh-bug set) and metrics
data/            lab target configs and benchmark task definitions (not committed)
```

## Roadmap

1. Stand up a local, isolated vulnerable lab (VM or containers) you fully own
2. Implement the planner + recon agents against a known-CVE task and confirm the
   pipeline can reach a documented exploit
3. Add the exploit and privesc agents; measure end-to-end success on the known-CVE set
4. Insert a small set of fresh, undocumented bugs into the same lab; re-run the identical
   pipeline unmodified and report the generalization gap between the two sets

## Related work

- Fang et al., "LLM Agents can Autonomously Exploit One-day Vulnerabilities" (2024)
- "Automation-Exploit: A Multi-Agent LLM Framework for Adaptive Offensive Security with
  Digital Twin-Based Risk-Mitigated Exploitation" (arXiv, 2026)
- CyberGym / CVE-Bench (ICLR 2026) — real-world agentic cybersecurity benchmarks
- DARPA AI Cyber Challenge (AIxCC) — Atlantis (winning CRS) and the open-sourced
  finalist systems
- OWASP GenAI Security Project — Agentic Top 10 (2026)

## License

MIT
