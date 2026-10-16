# Marc Mantei · Senior AI Engineer

**Forward Deployed Engineer** · AI systems, platforms, advisory · based in Germany

I build self-regulating AI systems: closed control loops that plan, implement, review and ship software, each with a measured signal, a setpoint and a proof. The human approves; the system operates.

More than ten years of workflow automation, from Netflix's virtual production stages to AI systems that ship software on their own. Now: founder of SupportPilot, building Shipyard and Myceliums. Open for senior AI engineering roles, freelance projects in AI workflow automation, and advisory.

> At [Eyeline Studios](https://eyelinestudios.com/en/studios/stages) (Netflix) I built key production tools for the virtual production stages (LED volumes, volumetric capture, the Light Dome) and automated terabyte-scale data workflows across 100+ sources, with C++/Python API bridges and global CI/CD.

[![Website](https://img.shields.io/badge/marcmantei.com-0B0B0A?style=flat&logo=safari&logoColor=white)](https://www.marcmantei.com)
[![Intro call](https://img.shields.io/badge/Request_an_intro_call-4A9B6E?style=flat&logo=googlecalendar&logoColor=white)](https://cal.marcmantei.com/marc/intro-meeting)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marcmantei/)
[![Email](https://img.shields.io/badge/mail@marcmantei.com-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:mail@marcmantei.com)
[![IMDb](https://img.shields.io/badge/IMDb-F5C518?style=flat&logo=imdb&logoColor=000)](https://www.imdb.com/name/nm15608082/)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/commit-graph-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/commit-graph-light.svg" />
  <img alt="Commit activity over the last 53 weeks: a weekly curve on a square-root scale above a daily heatmap" src="assets/commit-graph-dark.svg" width="100%" />
</picture>

---

### Shipyard · A self-hosted platform where AI ships software

AI agents write code fast, but unattended output is hard to trust. Shipyard turns an approved plan into merged software: independent AI workers build, review and fix each issue, wave by wave. Every automated decision runs inside a closed control loop with a measured signal, a hard cap and an escalation path to a human. In production since May 2026.

![Shipyard Mission Control: the fleet in one sentence, and only what needs a person on top](assets/shipyard-mission-control.webp)

*Mission Control, live: the fleet in one sentence, and only what needs a person on top.*

Shipyard opened **267 pull requests** on its own across 10 repositories. **240 were merged**: 75 by its own merge gates, 165 by me. About 90% of the commits in my repositories over the last six months were written by it. Over 1 billion tokens metered, 276 PRs through its AI reviewer (as of 24 Sep 2026).

- **11 plans shipped end to end**, each closed only after its acceptance check passed in a throwaway container
- **125 PRs sent back to be fixed**: the reviewer found something at least once in 125 pull requests, twice in 30, three times in 6
- **81 escalations since July**: when the error stops falling or the round budget runs out, it stops and asks. It raised 78 of them itself
- **1 plan → 7 merged PRs**: a terrain generator went from one approval to seven merged pull requests for €16.23 of model time at list price

![A loop's flight recorder: error, judge and confidence per round, and which of six rules stopped it](assets/shipyard-flight-recorder.webp)

*A loop's flight recorder: error, judge and confidence per round, and which of six rules stopped it.*

Six loop families, nested by timescale, so every ring can stop what runs inside it: the eval loop on every AI output, the build loop per issue, the cascade every ten minutes, the hill-climbing engine every six hours. The review budget is earned by the size of the problem (3 to 8 rounds), and loop state lives on the PR itself, so it survives restarts. Guardrails are structural: the worker that builds a PR never reviews it, and no agent merges its own work.

[Control loop atlas](https://www.marcmantei.com/shipyard/index.html) · [Loop sheet](https://www.marcmantei.com/shipyard/control-loops.html)

**Stack:** Python · Apache Airflow · FastAPI · Claude · Grok · PostgreSQL · Redis · Langfuse · OpenTelemetry · Prometheus · Grafana · Loki · Docker

---

### SupportPilot · An AI support desk that earns its autonomy

Any model can write a plausible support email. The hard part is knowing when one is safe to send unread. SupportPilot drafts replies from the knowledge base and live order or booking data, checks every order number, tracking number and price against it, and lets unit-tested code, not the model, decide what needs a human. It is Shipyard's merge-gate loop, applied to customer email. Pre-launch.

![SupportPilot: a customer asks where her order is; the draft quotes live order data and waits for approval](assets/supportpilot-inbox.webp)

**7** hard gates before any auto-send · **4** possible outcomes per draft · **1,798** backend tests on SQLite and Postgres · **1,061** commits in 29 days, merges not counted

---

### Myceliums · A code knowledge graph for AI agents

Coding agents answer structural questions by grepping and reading whole files, which burns context and still misses indirect callers. Myceliums is a local Rust engine that parses a repository into a graph of symbols, calls, communities and execution flows, and serves it over MCP. One tool call returns callers, blast radius or a Cypher result as compact text. Open source (Apache-2.0), v0.3.2, fully local: no cloud, no telemetry.

![Gin's call graph as built by Myceliums: 1,261 connected symbols, colored by package](assets/myceliums-call-graph.webp)

*Gin's call graph as built by Myceliums: 1,261 connected symbols, colored by package.*

<p>
  <img src="assets/myceliums-cli.webp" alt="myc analyze indexes Gin in 390 ms of parsing, then a Cypher query lists every caller of ClientIP" width="49%" />
  <img src="assets/myceliums-mcp.webp" alt="One MCP call on a one-line change returns callers and callees in about 243 tokens" width="49%" />
</p>

*Left: `myc analyze` indexes Gin in 390 ms of parsing, then a Cypher query lists every caller of `ClientIP`. Right: one MCP call on a one-line change returns its callers and callees in about 243 tokens.*

Benchmarked on six open-source repos (Django, FastAPI, Tokio, Express, Zod, Gin): **~99.8% fewer tokens** and ~94% fewer tool calls than file-reading agents.

**23** languages parsed · **54** MCP tools for agents · **14** one-command integrations · **~60k** lines of Rust

[Website](https://myceliums.marcmantei.com) · [GitHub](https://github.com/marcmantei/myceliums) · [crates.io](https://crates.io/crates/myc)

**Stack:** Rust · tree-sitter · LanceDB · fastembed · MCP · Cypher

---

### What I work with

![Python](https://img.shields.io/badge/-Python-555?style=flat-square&logo=python&logoColor=fff)
![Rust](https://img.shields.io/badge/-Rust-555?style=flat-square&logo=rust&logoColor=fff)
![TypeScript](https://img.shields.io/badge/-TypeScript-555?style=flat-square&logo=typescript&logoColor=fff)
![Claude](https://img.shields.io/badge/-Claude-555?style=flat-square&logo=anthropic&logoColor=fff)
![MCP](https://img.shields.io/badge/-MCP-555?style=flat-square&logo=modelcontextprotocol&logoColor=fff)
![Apache Airflow](https://img.shields.io/badge/-Airflow-555?style=flat-square&logo=apacheairflow&logoColor=fff)
![FastAPI](https://img.shields.io/badge/-FastAPI-555?style=flat-square&logo=fastapi&logoColor=fff)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-555?style=flat-square&logo=postgresql&logoColor=fff)
![Redis](https://img.shields.io/badge/-Redis-555?style=flat-square&logo=redis&logoColor=fff)
![Docker](https://img.shields.io/badge/-Docker-555?style=flat-square&logo=docker&logoColor=fff)
![Langfuse](https://img.shields.io/badge/-Langfuse-555?style=flat-square)
![OpenTelemetry](https://img.shields.io/badge/-OpenTelemetry-555?style=flat-square&logo=opentelemetry&logoColor=fff)
![Prometheus](https://img.shields.io/badge/-Prometheus-555?style=flat-square&logo=prometheus&logoColor=fff)
![Grafana](https://img.shields.io/badge/-Grafana-555?style=flat-square&logo=grafana&logoColor=fff)
![GitHub Actions](https://img.shields.io/badge/-GitHub_Actions-555?style=flat-square&logo=githubactions&logoColor=fff)
![Linux](https://img.shields.io/badge/-Linux-555?style=flat-square&logo=linux&logoColor=fff)

<sub>The commit graph above is rendered by [`scripts/commit_graph.py`](scripts/commit_graph.py) and refreshed daily by a GitHub Action: no third-party service, private repositories counted, their names never published.</sub>
