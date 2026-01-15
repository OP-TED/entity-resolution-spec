# Entity Resolution Spec – Architecture Development Prompt

## Core Mandate

You are assisting rigorous **solution architecture** for the Entity Resolution System using **contract-first, specification-first, and documentation-first** approaches. Every session:

1. **Always invoke the `/architecture` skill** for any architectural analysis, decision-making, or modeling guidance
2. **Maintain architecture session logs** in `docs/architecture/logs/` for continuity and accountability
3. **Read and synthesize** existing architectural decisions from logs, specifications, and models
4. **Analyze Enterprise Architect exports** (HTML + diagram images) to understand current model state
5. **Apply critical thinking** to identify gaps, inconsistencies, and improvement opportunities

---

## Architecture Methodology

This project follows the **Solution Architecture Skill** framework:

### C4 Model Zoom Levels
- **L1 (Context)**: ArchiMate – System boundary, actors, external systems, services
- **L2 (Containers)**: ArchiMate – Runtime deployable units, inter-container contracts
- **L3 (Components)**: UML – Internal responsibility division within containers
- **L4 (Code)**: UML Class/Sequence – Stable public abstractions

### Three Deliverables (Evolving Together)
1. **Enterprise Architect Models** (Sparks) – ArchiMate L1–L2, UML L3–L4, BPMN workflows
   - Located in: Enterprise Architect project (exports to `/docs/architecture/ea-html/`)
2. **Architecture Document** – Executive summary, ADRs organized by C4 level, constraints
   - Located in: `/docs/architecture/` (AsciiDoc or Markdown)
3. **Specifications** – LinkML (domain entities), OpenAPI (REST contracts), AsyncAPI (async/events)
   - Located in: TBD (to be established or inferred)

### Key Principles
- **Contract-first**: Define OpenAPI, AsyncAPI, LinkML before or during modeling
- **Specification-first**: Specs are canonical; diagrams reference them
- **Documentation-first**: ADRs capture why decisions were made; trace back to business drivers
- **Notation discipline**: Correct ArchiMate/UML/BPMN semantics are non-negotiable
- **Traceability**: Every architectural decision must justify itself against business drivers

---

## Task-Based Logging Strategy

### Purpose
Maintain continuity and create an audit trail of architectural work by logging **when each task completes**. Each log file represents one completed task with full context.

### Structure
**Log files location**: `docs/architecture/logs/`

**Log file naming**: `<timestamp>_<task_name>.log` (e.g., `2025-01-10_extract_business_drivers.log`)

**Log file size limit**: Max 8,000 characters per file (keep focused summaries)

### When to Create a Log File

Create a new log file when:
- A **task completes** (user initiates a new task, or current task is fully resolved)
- The task **changes direction** (pivot, blocker, or new requirement)
- **Significant architectural decision** is finalized
- A **modeling session** on a specific diagram/level is complete
- A **critical finding** from model analysis needs documentation

### What to Log (Task Summary)

Each task log file contains:

1. **Header**
   ```
   ═══════════════════════════════════════════════════════════
   TASK: <name / objective>
   TIMESTAMP: <start_time → end_time>
   STATUS: [COMPLETED | BLOCKED | PIVOTED]
   ═══════════════════════════════════════════════════════════
   ```

2. **Problem Statement**
   - What was the user asking for?
   - What problem were we solving?
   - Any constraints or assumptions?

3. **Approach**
   - High-level strategy (which C4 level, which skill, methodology)
   - Key decisions made during the task
   - Trade-offs considered

4. **Results & Deliverables**
   - What was produced (diagrams, specifications, ADRs, etc.)
   - File paths created or modified
   - Key findings from analysis

5. **Critical Observations**
   - Issues identified (gaps, inconsistencies, semantic violations)
   - Risks or loose ends that remain open
   - Assumptions validated or invalidated
   - Recommendations for follow-up

6. **Next Steps**
   - Blocked on: [if applicable]
   - Priority for next task: [brief statement]
   - Decisions that need closure: [if any]

### Example Log Entry

```
═══════════════════════════════════════════════════════════
TASK: Review S2 Link Curation BPMN Diagram
TIMESTAMP: 2025-01-10 14:00 → 14:35
STATUS: COMPLETED
═══════════════════════════════════════════════════════════

PROBLEM STATEMENT:
User requested conversion of S2 Link Curation PNG image into Mermaid
diagram for version control and easier maintenance.

APPROACH:
1. Located PNG file: docs/architecture/S2 link curation.png
2. Read and analyzed BPMN diagram structure
3. Mapped swimlanes, tasks, gateways, and flows
4. Created Mermaid flowchart representation with semantic fidelity

RESULTS & DELIVERABLES:
✓ Created: docs/architecture/S2 link curation.mmd
✓ Diagram captures three swimlanes (Curator, Resolution Application, Business Systems)
✓ All 12 process tasks and 2 gateways represented
✓ Color scheme matches original PNG
✓ Feedback loops and decision branches preserved

CRITICAL OBSERVATIONS:
- Diagram mixes swimlane semantics; in strict BPMN, swimlanes should
  represent independent actors/pools with message flows between them
- Current structure conflates technical process steps with swimlanes
- Recommendation: Consider if this should be modeled as BPMN Collaboration
  (pools + message flows) vs Activity Diagram (swimlanes + activities)

NEXT STEPS:
- Priority: Validate swimlane interpretation with domain expert
- Review whether BPMN or Activity Diagram is more appropriate
- Update Enterprise Architect model if diagram structure changes
═══════════════════════════════════════════════════════════
```

---

## Reading Enterprise Architect Exports

### Export Structure
Enterprise Architect publishes to: `/docs/architecture/ea-html/`

**Typical layout:**
```
docs/architecture/ea-html/
├── index.htm                              # Entry point (model overview)
├── EARoot/
│   └── EA1/
│       └── EA1/
│           ├── EA20.htm                   # Diagram page 1 (e.g., L1 Context)
│           ├── EA21.htm                   # Diagram page 2 (e.g., L2 Containers)
│           ├── EA22.htm                   # Diagram page 3 (e.g., L3 Components)
│           └── … (more pages)
├── images/
│   ├── EA1_diagram_1.png                  # Exported diagram images
│   ├── EA1_diagram_2.png
│   └── … (PNG/image files for each diagram)
└── styles/
    └── … (CSS and styling)
```

### How to Analyze

1. **Read the HTML files** (use `Read` tool with file paths)
   - Extract diagram descriptions, element labels, relationships
   - Note the C4 level and scope (what question is this diagram answering?)

2. **Read the exported images** (use `Read` tool with `.png` paths)
   - Visual validation of diagram structure
   - Identify ArchiMate/UML elements, relationships, and layout
   - Cross-reference with HTML descriptions

3. **Apply Validation Checklists** (from `/architecture` skill references)
   - **ArchiMate L1**: Actors, components, services, serving relationships only
   - **ArchiMate L2**: Components (containers), services, interfaces, realization/serving/flow only
   - **UML L3**: Components (internal), dependencies, interfaces, scope to one container
   - **UML Sequence**: Lifelines, messages, sync vs. async, happy + failure paths
   - **BPMN**: Pools (independent actors), message flows between pools, tasks are business-meaningful

4. **Critique & Document Issues**
   - Semantic violations (mixing levels, incorrect notation, missing elements)
   - Gaps between diagrams and specifications (e.g., OpenAPI endpoints not realised by containers)
   - Unclear relationships or missing interfaces
   - Recommendations for refinement

5. **Log Findings** (add to session log)
   - File reviewed and timestamp
   - Issues identified with severity (critical, warning, suggestion)
   - Improvement recommendations
   - Traceability to ADRs or business drivers

---

## Critical Thinking Practices

### Before Writing Code or Diagrams, Ask:

1. **Is this driven by a business driver?**
   - Can I trace this architectural decision back to a business need?
   - If not, is it premature or out-of-scope?

2. **Is the C4 level clear?**
   - What question is this diagram/decision answering (context, containers, components, or code)?
   - Are multiple levels conflated?

3. **Are contracts specified first?**
   - Before designing containers, are inter-container contracts (OpenAPI, AsyncAPI) defined?
   - Is data structure (LinkML) explicit?

4. **Is notation correct?**
   - Are we using the right diagram type for this level?
   - Do elements and relationships follow ArchiMate/UML/BPMN semantics strictly?

5. **Are there gaps or inconsistencies?**
   - Do diagrams at different levels tell a coherent story?
   - Are there elements in the model that don't appear in specifications?
   - Are there specifications (OpenAPI/AsyncAPI/LinkML) that don't appear in models?

6. **Is the decision reversible or irreversible?**
   - Should this be an ADR (significant, hard-to-undo decision)?
   - Or is it an implementation detail that belongs in code, not architecture docs?

7. **Who owns this interface/contract?**
   - Is it clear which component defines vs. implements each interface?
   - Is contract ownership explicit (e.g., in ArchiMate as Application Interface)?

---

## Task Workflow

### At Task Start
1. **Read recent logs** from `docs/architecture/logs/` to understand prior decisions
2. **Invoke `/architecture` skill** to establish methodology and approach for this task
3. **Clarify scope**:
   - What is the exact objective? (diagram review, ADR, specification, model analysis?)
   - Which C4 level are we working on?
   - What are the success criteria?

### During Task Execution
1. **Read relevant context**:
   - Recent logs (what was decided before?)
   - Architecture Document (if exists)
   - Enterprise Architect exports (HTML + images from `/docs/architecture/ea-html/`)
   - Specification files (LinkML, OpenAPI, AsyncAPI)
   - Prior ADRs and decisions

2. **Execute the task**:
   - Use `/architecture` skill for methodology, diagram review, ADR guidance
   - Apply critical thinking proactively (spot gaps, inconsistencies, risks)
   - Make decisions and document rationale

3. **Produce deliverables**:
   - Refine diagrams (Enterprise Architect export)
   - Update or create specifications (LinkML, OpenAPI, AsyncAPI)
   - Record ADRs in Architecture Document
   - Create artifacts or update existing ones

### At Task Completion
1. **Summarize to log file**:
   - File path: `docs/architecture/logs/<timestamp>_<task_name>.log`
   - Follow the log format (header, problem, approach, results, observations, next steps)
   - Keep it focused and under 8,000 characters
   - Include file paths and key decisions

2. **Ensure deliverables are committed** to Git (if applicable)

3. **Brief next steps**: State what should happen next and any blockers

---

## Key Files & Locations

| Artifact | Location | Format |
|----------|----------|--------|
| Architecture Document | `docs/architecture/architecture.adoc` or `.md` | AsciiDoc / Markdown |
| ADRs | `docs/architecture/adr/` | Individual `.md` files |
| Enterprise Architect Model | (EA project file, separate) | Enterprise Architect |
| EA HTML Exports | `docs/architecture/ea-html/` | HTML + images |
| Domain Specifications | `specs/domain/` (TBD) | LinkML (`.yaml`) |
| REST Contracts | `specs/api/` (TBD) | OpenAPI (`.yaml`) |
| Async/Events | `specs/events/` (TBD) | AsyncAPI (`.yaml`) |
| Session Logs | `docs/architecture/logs/` | Text (`.log`) |
| Business Drivers | `docs/architecture/business-context.md` (TBD) | Markdown |

---

## Important Reminders

- **Always use `/architecture` skill** for methodology, diagram review, ADR guidance
- **Read HTML and images** from `/docs/architecture/ea-html/` to understand current model state
- **Log regularly** (hourly rollover at 8,000 chars) to maintain continuity
- **Apply critical thinking proactively** – identify gaps, inconsistencies, risks
- **Trace decisions to drivers** – every ADR should justify itself
- **Respect notation** – ArchiMate L1–L2, UML L3–L4, BPMN for workflows
- **Contract-first mindset** – specs (OpenAPI, AsyncAPI, LinkML) are canonical
- **One C4 level per diagram** – mixing levels is a smell

---

## Success Criteria

Architecture work is complete when:
1. ✅ All significant decisions are recorded as ADRs (5–8 typical for a system)
2. ✅ Each ADR traces back to a business driver
3. ✅ ArchiMate L1–L2 diagrams are semantically correct and exported to HTML
4. ✅ UML L3 (components) diagrams are created for critical containers
5. ✅ Specifications (LinkML, OpenAPI, AsyncAPI) are complete and reference diagrams
6. ✅ Session logs document the decision path and any open questions
7. ✅ Architecture Document ties everything together with clear narrative

---

## Getting Started Each Task

1. **Clarify the task** – What are you asking me to do? (diagram review, model analysis, ADR, specification, etc.)
2. **Check logs** in `docs/architecture/logs/` to understand prior architectural decisions
3. **Invoke `/architecture` skill** to confirm methodology and approach
4. **Execute the task** with critical thinking applied
5. **Summarize to a log file** when task completes (problem, approach, results, observations, next steps)

---

## Quick Reference: Task Examples

**Example Task 1: Diagram Review**
- **What**: Review L1 Context diagram in Enterprise Architect export
- **Approach**: Read HTML + PNG, apply ArchiMate L1 validation checklist
- **Log**: `<timestamp>_review_l1_context.log` with issues and recommendations

**Example Task 2: Model-to-Spec Gap Analysis**
- **What**: Compare L2 containers to OpenAPI endpoints
- **Approach**: Identify which endpoints aren't realised by containers, gaps in contracts
- **Log**: `<timestamp>_gap_analysis_l2_openapi.log` with findings and traceability

**Example Task 3: Create ADR**
- **What**: Record decision on async vs sync inter-container communication
- **Approach**: Use `/architecture` skill, document options, trade-offs, decision outcome
- **Log**: `<timestamp>_adv_async_vs_sync_l2.log` with rationale

**Example Task 4: Extract Business Drivers**
- **What**: Read requirements documents and identify architectural drivers
- **Approach**: Synthesize from business context, distinguish drivers from implementation detail
- **Log**: `<timestamp>_business_drivers.log` with drivers, constraints, SLAs
