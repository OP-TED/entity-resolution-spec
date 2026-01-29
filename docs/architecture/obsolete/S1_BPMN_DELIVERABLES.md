# S1 BPMN Improvement: Complete Deliverables

## Summary

You now have a **complete blueprint** for improving the S1 BPMN diagram to match the ERS_MDR conceptual flow. All documents and diagrams are in `/docs/architecture/`.

---

## What You Have

### 1. **Updated Mermaid Diagram**
📄 **`s1-bpmn.mmd`** (UPDATED)
- 5 swimlanes: TED-SWS, ER System, ERE, Link Curation, State Stores
- 3 decision gateways: Cache hit, threshold acceptance, curation decision
- 9 message flows with specific data labels
- 3 curation paths (Accept/Reject/Manage)
- Explicit state store references
- Ready to render in Mermaid Live Editor
- Ready to be imported/recreated in Enterprise Architect

### 2. **Analysis Documents**
📋 **`S1_BPMN_Gap_Analysis.adoc`**
- Executive summary of gaps
- Current state analysis (strengths + weaknesses)
- 8 critical gaps identified with detailed explanation
- 5 structural recommendations
- Proposed end-state structure with swimlanes and message flows
- BPMN notation issues to address
- Alignment with conceptual-model.mmd entities

### 3. **Implementation Guides**
📘 **`S1_BPMN_Improved_Guide.md`**
- What changed and why
- How to read the diagram
- Three happy paths explained
- Architecture principles applied
- Step-by-step guide for building in EA
- Questions for review before you start

📗 **`S1_BPMN_Before_After.md`**
- Side-by-side structure comparison
- Problems in original vs. improvements in new version
- Key differences in table format
- Flow paths: before vs. after
- Data flow comparison
- Conceptual model alignment
- Implementation sequence for EA (10 steps)

### 4. **Task Log**
📋 **`logs/2025-01-10_S1_BPMN_gap_analysis.log`**
- Complete analysis record
- Key findings and critical observations
- 4 ADRs identified for future recording
- Validation checklist

---

## Visual Reference: The Improved Diagram

### File: `s1-bpmn.mmd`

```
🔵 TED-SWS Pipeline
  ├─ Start
  ├─ Submit Entity Mention for Resolution
  ├─ Receive Canonical Identifier
  └─ End

🟢 ER System (Orchestration)
  ├─ Receive Resolution Request
  ├─ Validate & Register Request
  ├─ 🔄 Cache Hit? (Decision)
  │  ├─ No  → Send to ERE
  │  │       └─ Receive Alignment Links + Confidence
  │  │           ├─ 🔄 All Above Threshold? (Decision)
  │  │           │  ├─ Yes → Auto-Accept → Retrieve ID from Registry
  │  │           │  └─ No  → Present to Curator
  │  └─ Yes → Return Cached ID
  └─ Retrieve Final Canonical ID from Registry

🔴 Entity Resolution Engine
  ├─ Receive Resolution Request
  ├─ Match & Link Entity
  └─ Return Alignment Links with Confidence Scores

🟡 Link Curation
  ├─ Review Candidate Links & Confidence
  ├─ 🔄 Curator Decision? (Decision)
  │  ├─ Accept  → Accept Top Link → Write to Canonical Registry
  │  ├─ Reject  → Reject All Links → Write to Link-Store
  │  └─ Manage  → Manage Confidence → Update Both Stores

💾 State Stores
  ├─ Canonical Registry (canonical entity state, cluster assignments)
  ├─ Link-Store (alignment decisions, confidence audit trail)
  └─ Cache (resolved entity identifiers)
```

### Message Flows

```
TED-SWS --[Entity Mention Representation]--> ER System
ER System --[Resolution Request]--> ERE
ERE --[Alignment Links]--> ER System
ER System --[Candidate Links]--> Link Curation
Link Curation --[Integrate Link]--> Canonical Registry
Link Curation --[Reject Links]--> Link-Store
Link Curation --[Update Confidence]--> Canonical Registry / Link-Store
Canonical Registry --[Canonical ID]--> ER System
Cache --[Cached ID]--> ER System
ER System --[Canonical ID]--> TED-SWS
```

---

## What's Different from Original

| Feature | Original | Improved |
|---------|----------|----------|
| Swimlanes | 3 | **5** (added Curation + Stores) |
| Decision gates | 1 | **3** (cache, threshold, decision) |
| Curation paths | ❌ None | ✅ **3** (Accept/Reject/Manage) |
| State update logic | Implicit | **Explicit** per path |
| Confidence scoring | Hidden | **Visible** in flow |
| Message specificity | Generic | **Specific** (Entity Mention, Alignment Links, etc.) |
| Link rejection | Not shown | **Shown** (confidence = -1) |

---

## How to Use These Documents

### For Review
1. **Start**: Read `S1_BPMN_Before_After.md` (5 min) – See what changed and why
2. **Understand**: Read `S1_BPMN_Improved_Guide.md` (10 min) – Understand the three paths
3. **Deep Dive**: Read `S1_BPMN_Gap_Analysis.adoc` (15 min) – Full gap analysis and rationale

### For Building in EA
1. **View Diagram**: Open `s1-bpmn.mmd` in Mermaid Live Editor (visual reference)
2. **Follow Guide**: Use the "Next Steps in Enterprise Architect" section from `S1_BPMN_Improved_Guide.md`
3. **Execute**: Follow the 10-step implementation sequence from `S1_BPMN_Before_After.md`

### For Discussion/Validation
- **Gap Analysis** - Use to discuss with stakeholders why each change is needed
- **Before/After** - Use to show what's being improved and why
- **Guide** - Use for training/onboarding others on the new structure

---

## Key Decisions Embedded in This Diagram

These are **implicit architectural decisions** that should be formalized as ADRs:

### 1. **Link Curation as Independent Actor**
- **Question**: Should curation be explicit in the architecture?
- **Answer in Diagram**: Yes – separate "Link Curation" swimlane
- **Rationale**: Enables flexibility (human, rules-based, or hybrid), clearer responsibility boundaries

### 2. **Three Decision Gateways**
- **Question**: What are the decision points in the resolution workflow?
- **Answer in Diagram**: Cache hit? → Threshold acceptance? → Curation decision?
- **Rationale**: Matches ERS_MDR's explicit workflow

### 3. **State Store Differentiation**
- **Question**: Do Accept and Reject paths lead to the same state store?
- **Answer in Diagram**: No – Accept → Canonical Registry, Reject → Link-Store
- **Rationale**: Enables audit trail, decision reversal, different operational semantics

### 4. **Confidence Scoring as First-Class**
- **Question**: Is confidence metadata or business logic?
- **Answer in Diagram**: Business logic – drives threshold gate and curation decisions
- **Rationale**: Confidence determines automation vs. manual review

### 5. **Asynchronous Resolution Response** (Implicit)
- **Question**: Does TED-SWS wait for curation, or is it async?
- **Answer in Diagram**: Async (ER System retrieves final ID from registry after curation completes)
- **Rationale**: Supports long-running curation workflows without blocking TED-SWS

---

## Next Steps

### Immediate (This Week)
- [ ] Review `S1_BPMN_Before_After.md` with team
- [ ] Confirm diagram matches your understanding of ERS_MDR workflow
- [ ] Identify any missing elements or alternative flows

### Short Term (This Sprint)
- [ ] Build diagram in Enterprise Architect using the 10-step sequence
- [ ] Export from EA back to Mermaid to version control
- [ ] Record ADRs for the 5 key decisions above

### Medium Term
- [ ] Compare S3 (lookup) diagram to ensure consistency with S1
- [ ] Create L3 (Component) diagrams for ER System internals
- [ ] Specify OpenAPI/AsyncAPI contracts for inter-actor communication

---

## Files Created/Updated

```
docs/architecture/
├── s1-bpmn.mmd                          ✅ UPDATED (5 swimlanes, 3 gates)
├── S1_BPMN_Gap_Analysis.adoc            ✅ NEW (detailed gap analysis)
├── S1_BPMN_Improved_Guide.md            ✅ NEW (implementation guide)
├── S1_BPMN_Before_After.md              ✅ NEW (comparison + EA steps)
├── S1_BPMN_DELIVERABLES.md              ✅ NEW (this file)
└── logs/
    └── 2025-01-10_S1_BPMN_gap_analysis.log  ✅ NEW (task log)
```

---

## Questions?

Before you start building in EA, confirm:

1. **Curator Role**: Is curation always required, or only when confidence is low?
   - *Diagram shows: Required for below-threshold links*

2. **Async Timing**: How long can curation take? Is TED-SWS okay waiting?
   - *Diagram shows: ER System retrieves final ID after curation*

3. **Re-Resolution**: If curator rejects all links, should system auto-retry with ERE?
   - *Diagram doesn't show retry – open question*

4. **State Store Technology**: Are Registry/Link-Store/Cache separate systems or tables?
   - *Diagram is technology-agnostic – shows logical separation*

5. **Message Format**: What's the exact schema for Alignment Links, Entity Mention Representation?
   - *Document OpenAPI/AsyncAPI specs once diagram is approved*

---

## References

- **Gap Analysis**: `S1_BPMN_Gap_Analysis.adoc`
- **ERS_MDR PDF**: `inbox/ERS_MDR (1).pdf`
- **Conceptual Model**: `conceptual-model.mmd`
- **Project Claude Config**: `.claude/CLAUDE.md`

---

## Task Summary

✅ **Completed**:
- Analyzed S1 BPMN against ERS_MDR conceptual flow
- Identified 8 critical gaps
- Created improved Mermaid diagram (5 swimlanes, 3 decision gates)
- Documented findings in AsciiDoc
- Provided implementation guides for EA
- Created before/after comparison

⏭️ **Next**: Build diagram in Enterprise Architect (user's work)

---

**Date**: 2025-01-10
**Author**: Architecture Analysis
**Status**: Ready for EA Implementation
