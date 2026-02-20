

# Slot: excluded_cluster_ids 


_When this is present, the ERE may use this information to avoid clustering the entity in _

_the listed clusters._

__

_This can be used to notify the ERE that a curator has rejected a previous resolution _

_proposed by the ERE._

__

_As for `proposed_cluster_ids`, the ERE **has no obligation** to fulfil the exclusions, and _

_it remains the ultimate authority to provide the final resolution decision._

__

_Similarly, the exact reaction to this is implementation dependent. In the simplest case, the ERE_

_might just create a singleton cluster with the current entity as member. In a more advanced _

_case, it might recompute the similarity with more advanced algorithms or use updated_

_data._

__





URI: [ere:excluded_cluster_ids](https://data.europa.eu/ers/schema/ere/excluded_cluster_ids)
Alias: excluded_cluster_ids

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
| self | ere:excluded_cluster_ids |
| native | ere:excluded_cluster_ids |




## LinkML Source

<details>
```yaml
name: excluded_cluster_ids
description: "When this is present, the ERE may use this information to avoid clustering\
  \ the entity in \nthe listed clusters.\n\nThis can be used to notify the ERE that\
  \ a curator has rejected a previous resolution \nproposed by the ERE.\n\nAs for\
  \ `proposed_cluster_ids`, the ERE **has no obligation** to fulfil the exclusions,\
  \ and \nit remains the ultimate authority to provide the final resolution decision.\n\
  \nSimilarly, the exact reaction to this is implementation dependent. In the simplest\
  \ case, the ERE\nmight just create a singleton cluster with the current entity as\
  \ member. In a more advanced \ncase, it might recompute the similarity with more\
  \ advanced algorithms or use updated\ndata.\n"
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: excluded_cluster_ids
owner: EntityMentionResolutionRequest
domain_of:
- EntityMentionResolutionRequest
range: string
multivalued: true

```
</details>