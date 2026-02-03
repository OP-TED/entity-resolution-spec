# Architecture Sequence Diagrams

This folder contains Mermaid (`.mmd`) sequence diagrams used in, or referenced by, the ERSys architecture documentation and the ERS–ERE technical contract.

The diagrams are organised to support **different levels of abstraction**:

* **Simplified diagrams** are used directly in architecture and contract documents to communicate intent, roles, and guarantees without implementation noise.
* **Non-simplified (detailed) diagrams** provide additional context and should be consulted when deeper understanding is required, for example during implementation, review, or troubleshooting. They are not all reproduced verbatim in the architecture document but remain authoritative supporting artefacts.

Only Mermaid source files are listed below. Generated images or archives are excluded.

---

## End-to-end overview diagrams

* `E2E-resolution-cycle.mmd`
  Full end-to-end resolution cycle across ERS, ERE, and supporting components.

* `E2E-resolution-cycle(simplified).mmd`
  Simplified end-to-end view used in the architecture document for high-level explanation.

---

## Shared participants

* `_participants.mmd`
  Common participant definitions reused across multiple sequence diagrams to ensure naming consistency.

---

## Spine A — Resolve Entity Mention

* `spine-A-Resolve-EntityMention.mmd`
  Detailed sequence for the primary entity resolution flow, including internal processing steps.

* `spine-A-Resolve-EntityMention(simplified).mmd`
  Contract- and architecture-level view of the resolve operation, used in documentation.

---

## Spine B — ERS–ERE asynchronous exchange

* `spine-B-ERS-ERE-async-exchange.mmd`
  Detailed asynchronous interaction between ERS and ERE, including proposal delivery and integration.

* `spine-B-ERS-ERE-async-exchange(simplified).mmd`
  Simplified contract-level representation of the ERS–ERE exchange, focusing on obligations and semantics.

---

## Spine C — Canonical lookup

* `spine-C-Lookup.mmd`
  Sequence describing lookup of the current governed canonical assignment.

---

## Spine D — Curation loop

* `spine-D-Curation-loop.mmd`
  Detailed human-in-the-loop curation sequence, including governance effects.

* `spine-D-Curation-loop(simplified).mmd`
  Simplified curation loop used for architectural explanation.

---

## Spine E — Rebuild

* `spine-E-rebuild.mmd`
  Detailed rebuild sequence illustrating possible internal behaviours during a rebuild.

* `spine-E-rebuild(simplified).mmd`
  High-level rebuild semantics as referenced in the contract and architecture documents.

---

## Notes

* Simplified diagrams are the **primary references** in normative architecture and contract documents.
* Detailed diagrams are **supporting artefacts** and may include illustrative or informative steps that are intentionally omitted from simplified views.
* All diagrams share a consistent vocabulary aligned with the ERSys architecture, ADRs, and glossary.
