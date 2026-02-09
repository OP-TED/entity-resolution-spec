# Architecture Diagrams Index

This folder contains architecture diagrams referenced by the ERSys Architecture Document and the ERS–ERE Technical Contract. The diagrams are provided as rendered images (`.png`) and represent **authoritative architectural views** at different abstraction levels.

Unless stated otherwise, these diagrams are **normative at their stated level** and are intended to be read together with the accompanying textual sections of the architecture document. Some diagrams provide high-level context, while others zoom into specific concerns such as messaging, governance, or deployment.

---

## Context and layering diagrams

* `L0.png`
  System context diagram showing ERSys in relation to external actors and surrounding systems.

* `L1.png`
  High-level functional decomposition of the ER System, identifying major responsibilities and boundaries.

* `L2 - Application Cooperation Overview.png`
  Application-level cooperation view showing how ERS, ERE, and related applications interact at runtime.

---

## Contract and integration diagrams

* `L2 - Contract Realisation and Messaging Mediation (ERS-ERE).png`
  Structural view of the ERS–ERE technical contract, illustrating contract realisation by both components and mediation via messaging middleware.

* `ERS messages.png`
  Overview of message types produced and consumed by ERS.

* `ere messages.png`
  Overview of message types produced and consumed by ERE.

* `preview messages.png`
  Message flows related to preview or provisional resolution outcomes.

* `submit decision messages.png`
  Message flows related to the submission of governed resolution decisions.

* `statistics messages.png`
  Messages exchanged for reporting and statistics purposes.

---

## Governance and persistence views

* `canonical registry.png`
  View of the canonical registry and its role in maintaining governed canonical identifiers.

* `decision store.png`
  Diagram illustrating the storage and lifecycle of resolution decisions.

* `system of records.png`
  Overview of authoritative source systems and their relationship to ERSys.

---

## Technology and deployment diagrams

* `Technology choices.png`
  Summary of selected and candidate technologies used within ERSys.

* `Technology deployment.png`
  Reference deployment architecture illustrating runtime components and their relationships.

---

## Notes

* Diagram filenames correspond to figures referenced in the architecture document; titles in the document may be more descriptive than filenames.
* Some diagrams are intentionally high-level and omit implementation details; others focus on specific concerns (messaging, governance, deployment).
* Behavioural details and step-by-step flows are documented separately using Mermaid sequence diagrams.
* Where both simplified and detailed views exist, the architecture document always indicates which view is normative for the given section.
