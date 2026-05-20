# Marc Mantei — AI Engineer

I build AI automation pipelines, agentic systems, and the orchestration infrastructure that makes them work in production.

10+ years of software engineering, from large-scale data processing pipelines at Netflix (Eyeline Studios) to designing multi-agent architectures and self-hosted AI orchestration stacks. I build the systems that let small teams ship like large ones.

> Built automation infrastructure for [Eyeline Studios'](https://eyelinestudios.com/en/studios/stages) production pipelines at Netflix, processing terabytes across 100+ concurrent data sources with async orchestration and distributed queues.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marcmantei/)
[![Website](https://img.shields.io/badge/marcmantei.com-555?style=flat&logo=safari&logoColor=white)](https://www.marcmantei.com)
[![Email](https://img.shields.io/badge/mail@marcmantei.com-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:mail@marcmantei.com)
[![IMDb](https://img.shields.io/badge/IMDb-F5C518?style=flat&logo=imdb&logoColor=000)](https://www.imdb.com/name/nm15608082/)

---

### What I work with

![Rust](https://img.shields.io/badge/-Rust-555?style=flat-square&logo=rust&logoColor=fff)
![Python](https://img.shields.io/badge/-Python-555?style=flat-square&logo=python&logoColor=fff)
![TypeScript](https://img.shields.io/badge/-TypeScript-555?style=flat-square&logo=typescript&logoColor=fff)
![Docker](https://img.shields.io/badge/-Docker-555?style=flat-square&logo=docker&logoColor=fff)
![Apache Airflow](https://img.shields.io/badge/-Airflow-555?style=flat-square&logo=apacheairflow&logoColor=fff)
![Qdrant](https://img.shields.io/badge/-Qdrant-555?style=flat-square&logo=qdrant&logoColor=fff)
![Prometheus](https://img.shields.io/badge/-Prometheus-555?style=flat-square&logo=prometheus&logoColor=fff)
![Grafana](https://img.shields.io/badge/-Grafana-555?style=flat-square&logo=grafana&logoColor=fff)
![Cloudflare](https://img.shields.io/badge/-Cloudflare-555?style=flat-square&logo=cloudflare&logoColor=fff)
![Linux](https://img.shields.io/badge/-Linux-555?style=flat-square&logo=linux&logoColor=fff)
![Git](https://img.shields.io/badge/-Git-555?style=flat-square&logo=git&logoColor=fff)

---

### GitHub Stats

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=marcmantei&theme=github-dark-blue&hide_border=true&v=2" />
    <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com?user=marcmantei&theme=default&hide_border=true&v=2" />
    <img alt="GitHub Streak" src="https://streak-stats.demolab.com?user=marcmantei&theme=default&hide_border=true&v=2" />
  </picture>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=marcmantei&theme=github-dark&hide_border=true&area=true&v=2" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=marcmantei&theme=github-light&hide_border=true&area=true&v=2" />
  <img alt="Contribution Graph" src="https://github-readme-activity-graph.vercel.app/graph?username=marcmantei&theme=github-light&hide_border=true&area=true&v=2" width="100%" />
</picture>

---

### Current focus

- **AI infrastructure:** self-hosted orchestration stacks with Airflow, Qdrant, and full observability pipelines
- **Multi-agent orchestration:** autonomous AI agents with LLM routing, persistent memory, and webhook-driven automation
- **Code intelligence:** giving AI agents structural understanding of codebases via knowledge graphs and hybrid search

---

### Agent Orchestration

I built and operate a multi-agent AI system that functions as an autonomous software team. I create GitHub issues, and the system handles PRD writing, implementation, CI fixes, and review responses end to end without intervention.

The system uses 3-tier LLM routing: a dispatcher (Claude Opus) analyzes each request, selects relevant skills, and spawns workers (Claude Haiku) for parallel execution. A GitHub App with org-wide webhook delivery via Cloudflare Tunnel and cryptographic signature verification enables automated CI failure response, PR review handling, and issue triage.

- Agent presets and custom automation skills for domain-specific AI workflows
- Worker isolation in git worktrees for parallel autonomous development across multiple repositories
- Persistent memory systems and state tracking across agent sessions
- Full PR lifecycle management: CI failure to auto-fix, review feedback to auto-revision
- 7,300+ automated task commits since January 2025

**Stack:** Rust · Claude Opus/Haiku · Gemini Flash · GitHub App · Cloudflare Tunnel · SQLite · systemd

---

### AI Orchestration Infrastructure

Self-hosted production infrastructure for AI workflow automation, running 12+ Docker services with resource-budgeted orchestration on dedicated hardware.

- Apache Airflow (Scheduler + CeleryExecutor) for DAG-based AI task scheduling, triggering agent workflows via REST API
- Qdrant vector database with GPU acceleration (CUDA) for embedding workloads and semantic search
- Full observability pipeline: OpenTelemetry Collector, Prometheus, Loki (log aggregation), Grafana dashboards, Blackbox synthetic probes, cAdvisor + Node Exporter for container and host metrics
- RBAC per data domain for AI agent access control, audit logging of every agent query, rate limiting, and GDPR sanitization on PII-bearing results
- PostgreSQL + Redis data layer; Traefik reverse proxy with automated TLS
- Tailscale mesh VPN for secure remote access, zero public ports for admin interfaces

**Stack:** Docker Compose · Apache Airflow · Qdrant · PostgreSQL · Redis · Prometheus · Loki · Grafana · OpenTelemetry · Blackbox Exporter · Traefik · Tailscale

---

### Myceliums: Code Knowledge Graph

A code intelligence engine in Rust that parses source code into a queryable knowledge graph, so AI agents understand architecture before they write a single line. Published on [crates.io](https://crates.io/crates/myc).

Instead of letting agents grep through files and guess at structure, Myceliums gives them a structured graph of symbols, call chains, functional modules, and execution flows, all queryable through MCP, a CLI, or a custom Cypher dialect. One search call instead of fifty.

- 6-crate Rust workspace covering core, storage, MCP server, Cypher engine, HTTP server, and CLI
- Parses 23 languages via tree-sitter with two-pass symbol resolution
- Hybrid search: BM25 + vector embeddings (all-MiniLM-L6-v2 via fastembed) + Reciprocal Rank Fusion, with optional cross-encoder reranking (BAAI/bge-reranker-base) and IVF-PQ indexing for large repositories
- Impact analysis: parses git diffs, then BFS through the call graph to find blast radius
- 12 MCP tools with one-command setup for 12 platforms (Claude Code, Cursor, VS Code, Windsurf, Zed, JetBrains, and more)

**Stack:** Rust · tree-sitter · LanceDB · fastembed · all-MiniLM-L6-v2 · graphrs · rmcp · Cypher dialect
