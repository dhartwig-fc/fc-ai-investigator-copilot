# AI Investigator Copilot Reference Architecture

Implementation Architecture for AI-Enabled Financial Crime Investigation Support

---

## Executive Summary

The AI Investigator Copilot Reference Architecture describes how financial crime analytics, intelligence outputs and AI-enabled investigation workflows can be connected into a practical implementation model.

This architecture supports the transition from analytical detection to investigator-ready intelligence.

The objective is to demonstrate how structured analytical outputs can be transformed into explainable alert rationales, investigator summaries, evidence packs, intelligence reports, case packages and conversational investigation support.

This repository implements selected components of the AI Investigator Copilot architecture defined within the Financial Crime Analytics Showcase.

---

## Architectural Position

The AI Investigator Copilot sits between financial crime analytics and human investigation workflows.

```text
Emerging Threat Intelligence
        ↓
Financial Crime Analytics
        ↓
Network Intelligence
        ↓
Case Intelligence
        ↓
Orchestration Layer
        ↓
AI Investigator Copilot
        ↓
Investigator Decision Support
        ↓
Case Management
```

The Copilot does not replace detection systems, analytics models or human investigators.

It converts analytical findings into operational intelligence products that support investigator decision-making.

---

## Relationship To The Showcase

The Financial Crime Analytics Showcase defines the target-state Financial Crime Intelligence Platform.

This prototype repository demonstrates how selected elements of that platform can be implemented.

```text
Financial Crime Analytics Showcase
        ↓
AI Investigator Copilot Architecture
        ↓
Investigation Support Flow
        ↓
Prototype Implementation
        ↓
Future Production Platform
```

The showcase explains the business and capability architecture.

This repository demonstrates the implementation pattern.

---

## Core Architecture

```text
Structured Analytics Output
        ↓
Prompt Framework
        ↓
AI Generation Layer
        ↓
Investigation Intelligence Product
        ↓
Human Investigator Review
```

The current implementation focuses on generating investigator-ready outputs from structured alert and analytics data.

Future versions may introduce retrieval, orchestration, APIs, agent collaboration and case management integration.

---

## Intelligence Inputs

The Copilot may consume intelligence and analytical outputs from multiple domains.

| Input Source | Example Outputs |
|------------|-----------------|
| Network Intelligence | Relationship patterns, ownership links, connected entities |
| TBML Analytics | Trade anomalies, pricing gaps, route risk, counterparty indicators |
| Correspondent Banking Analytics | Payment corridor risk, nested relationship risk, counterparty exposure |
| Capital Markets Analytics | Trading anomalies, market abuse indicators, behavioural patterns |
| Sanctions Exposure Analytics | Ownership exposure, vessel risk, shadow fleet indicators |
| Emerging Threat Intelligence | Typology updates, geopolitical alerts, sanctions evasion intelligence |

These inputs provide the factual basis for AI-generated investigation support.

---

## Investigation Support Workflows

The architecture supports a staged investigation intelligence workflow.

```text
01 Alert Rationale Generation
        ↓
02 Investigator Summary Generation
        ↓
03 Evidence Pack Generation
        ↓
04 Intelligence Report Generation
        ↓
05 Case Package Generation
        ↓
06 Conversational Copilot
```

Each workflow transforms structured analytical findings into a more investigator-friendly output.

---

## Workflow 01 – Alert Rationale Generation

### Purpose

Explain why an alert was generated.

### Input

Structured alert data, risk indicators and model outputs.

### Output

A clear investigator-readable rationale explaining:

- What triggered the alert
- Which risk indicators contributed
- Why the behaviour is suspicious
- What evidence supports the alert
- What the investigator should review first

---

## Workflow 02 – Investigator Summary Generation

### Purpose

Create a concise case summary for investigator review.

### Input

Alert rationale, analytical findings, entity information and supporting evidence.

### Output

An investigator summary covering:

- Subject overview
- Key risk indicators
- Relevant transactions or relationships
- Initial risk assessment
- Suggested investigation focus

---

## Workflow 03 – Evidence Pack Generation

### Purpose

Assemble supporting evidence into a structured review package.

### Input

Transaction data, entity relationships, risk scores, analytics outputs and typology indicators.

### Output

An evidence pack containing:

- Key facts
- Risk indicators
- Supporting data points
- Relationship evidence
- Analytics references
- Investigation notes

---

## Workflow 04 – Intelligence Report Generation

### Purpose

Produce a structured intelligence report suitable for investigation escalation.

### Input

Evidence pack, investigation summary and contextual intelligence.

### Output

An intelligence report containing:

- Executive summary
- Risk narrative
- Typology assessment
- Evidence summary
- Confidence assessment
- Recommended next steps

---

## Workflow 05 – Case Package Generation

### Purpose

Prepare structured documentation suitable for downstream case management workflows.

### Input

Intelligence report, evidence pack, alert rationale and investigation notes.

### Output

A case package containing:

- Case overview
- Investigation rationale
- Evidence summary
- Risk assessment
- Supporting intelligence
- Recommended disposition

---

## Workflow 06 – Conversational Copilot

### Purpose

Allow investigators to interact with investigation intelligence using natural language.

### Input

Case package, evidence pack, analytical outputs and approved knowledge sources.

### Output

Conversational support for questions such as:

- Why was this alert generated?
- What are the strongest risk indicators?
- Which transactions matter most?
- What evidence supports escalation?
- What should I review next?
- How should this case be summarised?

---

## Technical Components

| Component | Purpose |
|----------|---------|
| Sample Data | Structured example alerts, entities and case data |
| Prompt Templates | Reusable instructions for AI-generated outputs |
| Python Workflows | Scripts that transform inputs into outputs |
| Output Templates | Markdown intelligence products generated by the workflows |
| Architecture Documentation | Reference architecture and implementation guidance |
| Archived Prototype | Original proof-of-concept baseline |

---

## Current Repository Structure

```text
fc-prot02-ai-investigator-copilot
│
├── architecture
│   └── reference-architecture
│
├── prompts
│   ├── alert-rationale
│   ├── investigator-summary
│   ├── evidence-pack
│   ├── intelligence-report
│   ├── case-package
│   └── conversational-copilot
│
├── outputs
│   ├── alert-rationale
│   ├── investigator-summary
│   ├── evidence-pack
│   ├── intelligence-report
│   └── case-package
│
├── sample-data
│   ├── alerts
│   ├── entities
│   └── cases
│
├── python
│   └── workflows
│
├── notebooks
│   └── prototypes
│
└── archive
    └── prototype-v1
```

---

## Prototype Implementation Pattern

The initial implementation pattern is intentionally simple.

```text
JSON Alert Input
        ↓
Prompt Template
        ↓
Python Workflow
        ↓
AI Generation
        ↓
Markdown Intelligence Output
```

This proves the core concept before introducing additional complexity.

The first technical milestone is:

```text
sample-data/alerts/tbml001_alert.json
        ↓
prompts/alert-rationale/alert_rationale_prompt.md
        ↓
python/workflows/alert_rationale_generator.py
        ↓
outputs/alert-rationale/tbml001_alert_rationale.md
```

---

## Future Production Architecture

A future production implementation may include:

```text
Analytics Platforms
        ↓
API Layer
        ↓
Agent Orchestration
        ↓
Retrieval-Augmented Generation Layer
        ↓
Copilot Services
        ↓
Investigator User Interface
        ↓
Case Management Platform
```

This would allow the Copilot to operate within enterprise investigation environments while maintaining governance, traceability and human oversight.

---

## Governance Principles

The architecture is designed around the following principles:

- Human investigator accountability
- Explainable generated outputs
- Traceable source evidence
- Controlled prompt management
- Clear separation between analytics and AI-generated interpretation
- Auditability of generated intelligence products
- Governance over model, prompt and output quality

The Copilot supports investigation decision-making but does not replace investigator judgement.

---

## Implementation Roadmap

| Phase | Capability | Status |
|------|------------|--------|
| Phase 1 | Repository structure | Complete |
| Phase 2 | Alert rationale generation | Next |
| Phase 3 | Investigator summary generation | Planned |
| Phase 4 | Evidence pack generation | Planned |
| Phase 5 | Intelligence report generation | Planned |
| Phase 6 | Case package generation | Planned |
| Phase 7 | Conversational Copilot workflow | Planned |
| Phase 8 | Agent orchestration | Future |
| Phase 9 | RAG integration | Future |
| Phase 10 | Case management integration | Future |

---

## Design Philosophy

The prototype follows a simple design philosophy:

```text
Start with structured analytics.
Generate explainable intelligence.
Preserve human oversight.
Scale into agentic workflows later.
```

This avoids over-engineering the early implementation while creating a clean path towards more advanced AI-enabled investigation capabilities.

---

## Related Repositories

### Financial Crime Analytics Showcase

Business architecture, capability design and investigation support model.

https://github.com/dhartwig-fc/fc-01-financial-crime-analytics-showcase

### AI Investigator Copilot Showcase

Detailed capability architecture for the AI Investigator Copilot.

https://github.com/dhartwig-fc/fc-01-financial-crime-analytics-showcase/tree/main/05-ai-investigator-copilot

### Transformation AI Lab

Experimentation environment for RAG, agents, MCP and orchestration patterns.

https://github.com/dhartwig-fc/fc-rm02-transformation-ai-lab

### Emerging Threat Intelligence

Threat monitoring, horizon scanning and typology intelligence repository.

https://github.com/dhartwig-fc/fc-08-emerging-threat-intelligence

---

## Key Message

The AI Investigator Copilot Reference Architecture shows how analytical detection can be operationalised into investigator-ready intelligence.

The prototype begins with a simple workflow:

```text
Analytics Output
        ↓
AI-Generated Alert Rationale
        ↓
Investigator Review
```

and evolves towards a complete investigation intelligence platform capable of supporting alert triage, evidence assembly, intelligence reporting, case packaging and conversational investigation support.
