# S1 BPMN Improved Diagram: Guide & Explanation

## What Changed

The updated `s1-bpmn.mmd` incorporates all recommendations from the gap analysis. Here's what's new:

### 1. **Four Swimlanes (Was 3, Now 5 Including Stores)**

#### Original:
- TED-SWS Pipeline
- ER System
- Entity Resolution Engine

#### Improved:
- 🔵 **TED-SWS Pipeline** – Same as before (client)
- 🟢 **ER System (Orchestration)** – Expanded with link curation logic
- 🔴 **Entity Resolution Engine** – Same as before (matcher/linker)
- 🟡 **Link Curation** – **NEW** – Manual/rule-based curation decisions
- 💾 **State Stores** – **NEW** – Canonical Registry, Link-Store, Cache

### 2. **Three Decision Gateways (Was 1, Now 3)**

| Gateway | Question | Paths |
|---------|----------|-------|
| **E3** | Cache Hit?<br/>Resolution required? | No → Return cached ID<br/>Yes → Send to ERE |
| **E6** | All links above<br/>acceptance-threshold? | Yes → Auto-accept<br/>No → Send to curator |
| **C2** | Curator Decision? | Accept → Canonical Registry<br/>Reject → Link-Store<br/>Manage → Both |

### 3. **Three Curation Paths (Missing Before)**

Each path has different consequences:

```
Curation → Accept   → Integrate to Canonical Registry (confidence = +1)
        → Reject   → Update Link-Store (confidence = -1)
        → Manage   → Update both stores with new confidence values
```

### 4. **Explicit State Store Updates**

**Old**: "Integrate Resolution Result" (vague)
**New**:
- Accept → "Write to Canonical Registry (integrate link)"
- Reject → "Write to Link-Store (mark -1 confidence)"
- Manage → "Update Both Stores (new confidence)"

### 5. **Message Flows with Specificity**

| From | To | Message |
|------|-----|---------|
| TED-SWS | ER System | **Entity Mention Representation** |
| ER System | ERE | **Resolution Request** |
| ERE | ER System | **Alignment Links** |
| ER System | Curator | **Candidate Links** |
| Curator | Stores | **Link Decision** (different per action) |
| Stores | ER System | **Canonical ID** (draft or final) |

---

## How to Read the Diagram

### Happy Path 1: Cache Hit
```
TED-SWS submits → ER System checks cache → Found → Return cached ID → TED-SWS receives
```

### Happy Path 2: Automated Resolution (High Confidence)
```
TED-SWS submits → ER System sends to ERE → ERE returns links → All above threshold
  → Auto-accept top link → Canonical Registry integrates → Return final ID → TED-SWS
```

### Path 3: Manual Curation (Below Threshold)
```
TED-SWS submits → ER System sends to ERE → ERE returns links → Some below threshold
  → Present to curator → Curator accepts/rejects/manages → Update appropriate store
  → Retrieve final ID → Return to TED-SWS
```

---

## Key Improvements vs. Original

| Aspect | Original | Improved |
|--------|----------|----------|
| **Swimlanes** | 3 (TED, ERS, ERE) | 5 (added Curation + Stores) |
| **Decision Gates** | 1 (cache hit) | 3 (cache hit, threshold, curation) |
| **Curation Paths** | None | 3 explicit paths (Accept/Reject/Manage) |
| **State Updates** | Implicit | Explicit (different stores per decision) |
| **Message Flows** | Generic ("result") | Specific ("Alignment Links", "Candidate Links") |
| **Confidence Scoring** | Hidden | Explicit (threshold gate, curation decision) |
| **Link Rejection Path** | Missing | Shown (confidence = -1) |
| **Curator Involvement** | Not represented | Distinct swimlane with decision logic |

---

## Architecture Principles Applied

✅ **Separation of Concerns**: Curator is independent actor, not hidden in ER System
✅ **Explicit Decision Logic**: Three gateways show different branching paths
✅ **State Store Differentiation**: Accept/Reject/Manage lead to different stores
✅ **Message Specificity**: Data flowing between actors is named (not generic "result")
✅ **Two-Phase Architecture**: Automated resolution + manual curation both shown
✅ **Domain Model Traceability**: Alignment, Cluster, CanonicalEntity all visible in flows

---

## Next Steps in Enterprise Architect

When you build this in EA, follow this sequence:

### Phase 1: Create Swimlanes/Pools
1. Create 5 pools: TED-SWS, ER System, ERE, Link Curation, State Stores
2. Set pool orientation (left-to-right or top-to-bottom)

### Phase 2: Add Tasks & Events
3. In each pool, add tasks/events (circles for start/end, rectangles for tasks)
4. Use diamonds for gateways (E3, E6, C2)

### Phase 3: Connect Internal Flows
5. Within each pool, connect tasks with sequence flows (solid arrows)
6. Label decision flows (Yes/No or specific decision)

### Phase 4: Add Message Flows
7. Between pools, add message flows (dotted arrows)
8. Label with data structures (Entity Mention, Alignment Links, etc.)

### Phase 5: Add Data Objects (Optional)
9. Add data stores (Canonical Registry, Link-Store, Cache) as data object symbols
10. Connect with data associations (references)

---

## Diagram Statistics

- **Swimlanes/Pools**: 5
- **Tasks**: 17 (including message labels)
- **Gateways**: 3
- **Message Flows**: 9
- **Internal Flows**: ~30
- **Decision Paths**: 3 (Accept/Reject/Manage)
- **State Stores**: 3 (Canonical Registry, Link-Store, Cache)

---

## Questions for Review

Before you build in EA, confirm:

1. **Curator Involvement**: Should curation be automatic (rules-based) or human-driven? Both shown here.
2. **Async vs. Sync**: Does TED-SWS wait for curation (sync) or get draft ID immediately (async)? Diagram shows async (ER System retrieves final ID after curation).
3. **Re-Resolution Loop**: Should reject path trigger re-resolution? Not shown here (open question).
4. **State Store Details**: Are Canonical Registry, Link-Store, and Cache three separate systems, or three tables in one? Diagram assumes separate.

---

## References

- **Gap Analysis**: See `S1_BPMN_Gap_Analysis.adoc` for detailed reasoning
- **Task Log**: See `logs/2025-01-10_S1_BPMN_gap_analysis.log` for findings
- **Conceptual Model**: See `conceptual-model.mmd` for domain entities (EntityMention, Alignment, Cluster, CanonicalEntity)
- **ERS_MDR PDF**: See `inbox/ERS_MDR (1).pdf` for business logic source
