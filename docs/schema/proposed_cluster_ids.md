

# Slot: proposed_cluster_ids 


_When this is present, the ERE may use this information to try to cluster the entity in one of _

_the listed clusters._

__

_In particular, when an initial request about an entity isn't answered within a timeout, _

_a subsequent new request can be sent about the same entity and with the canonical ID of it_

_as a single proposed cluster ID. This suggests the ERE that it can create a new singleton cluster_

_with the entity as its initial only member and its canonical ID as the cluster ID. The ERE_

_can evolve such a cluster later, when further similar entities are sent in, or when it _

_has had more time to associate the initial entity to others. _

__

_Whatever, the case, the ERE **has no obligation** to fulfil the proposal, how it reacts to _

_this list is implementation dependent, and the ERE remains the ultimate authority to provide _

_the final resolution decision._

__





URI: [ere:proposed_cluster_ids](https://data.europa.eu/ers/schema/ere/proposed_cluster_ids)
Alias: proposed_cluster_ids

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:proposed_cluster_ids |
| native | ere:proposed_cluster_ids |




## LinkML Source

<details>
```yaml
name: proposed_cluster_ids
description: "When this is present, the ERE may use this information to try to cluster\
  \ the entity in one of \nthe listed clusters.\n\nIn particular, when an initial\
  \ request about an entity isn't answered within a timeout, \na subsequent new request\
  \ can be sent about the same entity and with the canonical ID of it\nas a single\
  \ proposed cluster ID. This suggests the ERE that it can create a new singleton\
  \ cluster\nwith the entity as its initial only member and its canonical ID as the\
  \ cluster ID. The ERE\ncan evolve such a cluster later, when further similar entities\
  \ are sent in, or when it \nhas had more time to associate the initial entity to\
  \ others. \n\nWhatever, the case, the ERE **has no obligation** to fulfil the proposal,\
  \ how it reacts to \nthis list is implementation dependent, and the ERE remains\
  \ the ultimate authority to provide \nthe final resolution decision.\n"
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: proposed_cluster_ids
owner: EntityMentionResolutionRequest
domain_of:
- EntityMentionResolutionRequest
range: string
multivalued: true

```
</details>