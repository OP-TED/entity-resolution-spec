

# Slot: candidates 


_The set of cluster reference/score pairs representing the candidate clusters_

_that the entity mention in the original request could align to (be equivalent to)._

__





URI: [ere:candidates](https://data.europa.eu/ers/schema/ere/candidates)
Alias: candidates

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |  no  |






## Properties

* Range: [ClusterReference](ClusterReference.md)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:candidates |
| native | ere:candidates |




## LinkML Source

<details>
```yaml
name: candidates
description: 'The set of cluster reference/score pairs representing the candidate
  clusters

  that the entity mention in the original request could align to (be equivalent to).

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: candidates
owner: EntityMentionResolutionResponse
domain_of:
- EntityMentionResolutionResponse
range: ClusterReference
required: true
multivalued: true

```
</details>