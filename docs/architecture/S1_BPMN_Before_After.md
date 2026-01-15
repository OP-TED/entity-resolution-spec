# S1 BPMN: Before & After Comparison

## Side-by-Side Structure

### BEFORE (Original s1-bpmn.mmd)

```
TED-SWS Pipeline
  └─ Submit → Receive ID → [End]

ER System (Monolithic)
  └─ Receive → Validate → Cache Hit?
     ├─ No  → Send to ERE → Receive Result → Integrate → Return ID
     └─ Yes → Determine ID → Return ID

ERE (Atomic)
  └─ Receive → Resolve → Return Result
```

**Problems:**
- ❌ Link curation missing entirely
- ❌ Cache hit returns immediately (correct) but logic is confusing
- ❌ "Integrate Result" is vague (unclear what happens)
- ❌ No explicit curation actor
- ❌ No distinction between state stores
- ❌ Confidence scoring hidden
- ❌ No acceptance-threshold gate

---

### AFTER (Improved s1-bpmn.mmd)

```
TED-SWS Pipeline
  └─ Submit Entity Mention → Receive Canonical ID → [End]

ER System (Orchestration)
  ├─ Receive → Validate → Cache Hit?
  │  ├─ No  → Send to ERE
  │  │  └─ Receive Links → Above Threshold?
  │  │     ├─ Yes → Auto-Accept → Retrieve ID from Registry
  │  │     └─ No  → Present to Curator → Receive Decision → Retrieve ID
  │  └─ Yes → Return Cached ID
  └─ Return Canonical ID to TED-SWS

ERE (Atomic)
  └─ Receive → Match & Link → Return Alignment Links with Confidence

Link Curation (NEW)
  ├─ Review Candidates & Confidence
  └─ Decision?
     ├─ Accept → Write to Canonical Registry
     ├─ Reject → Write to Link-Store
     └─ Manage → Update Both Stores

State Stores (NEW)
  ├─ Canonical Registry (entity state, cluster assignments)
  ├─ Link-Store (alignment decisions, confidence audit trail)
  └─ Cache (resolved identifiers)
```

**Improvements:**
- ✅ Link curation explicitly modeled as 4th swimlane
- ✅ Three decision gateways (Cache, Threshold, Curator choice)
- ✅ Three distinct curation paths with different state updates
- ✅ Confidence scoring made explicit throughout
- ✅ State stores differentiated (different paths → different stores)
- ✅ Accept/Reject/Manage paths are distinct and traceable
- ✅ Message flows labeled with specific data structures

---

## Key Differences Table

| Aspect | Before | After |
|--------|--------|-------|
| **Number of Swimlanes** | 3 | 5 (added Curation + Stores) |
| **Swimlane for Curator** | ❌ Not represented | ✅ Explicit "Link Curation" pool |
| **Swimlane for Stores** | ❌ Not represented | ✅ Explicit "State Stores" pool |
| **Decision Gates** | 1 (Cache hit?) | 3 (Cache?, Threshold?, Curation decision?) |
| **Curation Paths** | ❌ None | ✅ 3 distinct (Accept/Reject/Manage) |
| **State Updates** | Implicit "Integrate" | ✅ Explicit per path (Registry/Link-Store/Both) |
| **Confidence Scoring** | ❌ Hidden | ✅ Visible in multiple places |
| **Acceptance-Threshold** | ❌ Not shown | ✅ Explicit gateway (E6) |
| **Link Rejection Path** | ❌ Not shown | ✅ Shown (confidence = -1) |
| **Message Flow Labels** | Generic ("result") | ✅ Specific ("Alignment Links", "Candidate Links") |
| **Async Behavior** | ❌ Unclear | ✅ Shown (retrieve from registry after curation) |

---

## Flow Paths: Before vs. After

### Happy Path 1: Cache Hit

**Before:**
```
Submit → Validate → Cache hit? (Yes) → Determine ID → Return ID
```
*Unclear which "cache" and what "determine" means*

**After:**
```
Submit → Validate → Cache Hit? (Yes) → Return Cached Canonical ID → TED-SWS receives
```
*Explicit: ER System consults Cache store, returns immediately*

---

### Happy Path 2: Automated High-Confidence Resolution

**Before:**
```
Submit → Validate → Cache miss (No) → Send to ERE → Receive Result → Integrate → Return ID
```
*Vague: What is "result"? What does "integrate" do? Which store?*

**After:**
```
Submit → Validate → Cache miss (No) → Send to ERE → Receive Alignment Links
  → All Above Threshold? (Yes) → Auto-Accept → Retrieve ID from Canonical Registry → Return ID
```
*Explicit: ERE returns links with confidence, threshold gate filters, auto-accept integrates to Canonical Registry*

---

### New Path: Below-Threshold Requires Curation

**Before:**
❌ *Not modeled*

**After:**
```
Submit → Validate → Cache miss → Send to ERE → Receive Alignment Links
  → All Above Threshold? (No) → Present to Curator

Curator reviews → Decision?
  ├─ Accept → Integrate Link to Canonical Registry
  ├─ Reject → Write to Link-Store (confidence -1)
  └─ Manage → Update Both Stores with new confidence

Retrieve ID from Registry → Return to TED-SWS
```
*Explicit three-way decision with different consequences*

---

## Data Flow: Before vs. After

### Before (Generic)

```
TED-SWS --"resolution request"--> ER System
ER System --"resolution request"--> ERE
ERE --"resolution result"--> ER System
ER System --"canonical identifier"--> TED-SWS
```
*No indication of what data is in "request" or "result"*

### After (Specific)

```
TED-SWS --"Entity Mention Representation"--> ER System
ER System --"Resolution Request"--> ERE
ERE --"Alignment Links (with confidence scores)"--> ER System
ER System --"Candidate Links"--> Curator
Curator --"Link Decision"--> State Stores
State Stores --"Canonical ID"--> ER System
ER System --"Canonical ID"--> TED-SWS
```
*Clear what data moves where*

---

## Conceptual Model Alignment

### Before
- ❌ EntityMention – Not visible
- ❌ Alignment – Hidden in "result"
- ❌ Cluster – Not visible
- ❌ CanonicalEntity – Implicit in ID
- ❌ SystemOfRecords – Not shown

### After
- ✅ EntityMention – Explicit in "Entity Mention Representation"
- ✅ Alignment – Explicit as "Alignment Links" message
- ✅ Cluster – Explicit in curation decision (select which cluster)
- ✅ CanonicalEntity – Explicit in "Canonical Registry" state store
- ✅ SystemOfRecords – Explicit (Canonical Registry + Link-Store + Cache)

---

## BPMN Notation Improvements

| Aspect | Before | After |
|--------|--------|-------|
| **Pools** | 3 pools | 5 pools (better separation) |
| **Gateways** | 1 diamond | 3 diamonds (all labeled clearly) |
| **Tasks** | Generic names ("Determine", "Integrate") | Specific names ("Accept Top Link", "Write to Registry") |
| **Message Flows** | 4 dotted arrows | 9 dotted arrows (comprehensive) |
| **Data Objects** | Implicit | Explicit (3 state stores shown) |
| **Decision Labels** | Implicit (Yes/No) | Explicit (decision questions) |

---

## Implementation Sequence for EA

When you build this in Enterprise Architect, follow this order:

1. **Create 5 pools** (swimlanes)
   - TED-SWS Pipeline
   - ER System (Orchestration)
   - Entity Resolution Engine
   - Link Curation
   - State Stores

2. **Add start/end events** to TED-SWS pool

3. **Add tasks to ER System pool** (9 tasks)
   - Receive Resolution Request
   - Validate & Register Request
   - Send Resolution Request to ERE
   - Receive Alignment Links + Confidence Scores
   - Auto-Accept Top Confidence Link
   - Present Candidates to Curator
   - Receive Curation Decision
   - Retrieve Final Canonical ID from Registry

4. **Add gateways to ER System** (2 gateways)
   - Cache Hit? (Yes/No split)
   - All Links Above Threshold? (Yes/No split)

5. **Add tasks to ERE pool** (3 tasks)
   - Receive Resolution Request
   - Match & Link Entity
   - Return Alignment Links with Confidence Scores

6. **Add gateway to Curation pool** (1 gateway)
   - Curator Decision? (Accept/Reject/Manage)

7. **Add 3 state stores** (data objects)
   - Canonical Registry
   - Link-Store
   - Cache

8. **Connect all message flows** between pools (9 dotted arrows)

9. **Label all message flows** with specific data

10. **Apply colors/styling** for clarity

---

## Ready to Start?

✅ **Mermaid diagram**: `s1-bpmn.mmd` (updated)
✅ **Guide & explanation**: `S1_BPMN_Improved_Guide.md`
✅ **Gap analysis**: `S1_BPMN_Gap_Analysis.adoc`
✅ **This comparison**: `S1_BPMN_Before_After.md`

**Next step**: Build it in Enterprise Architect following the implementation sequence above.

Need step-by-step EA guidance? I can provide detailed instructions for each EA tool operation.
