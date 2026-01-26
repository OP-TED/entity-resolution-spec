

# Slot: clusters 


_The set of cluster reference/score pairs representing the candidate clusters_

_that the entity mention in the original request could align to (be equivalent to)._

__





URI: [ers:clusters](https://data.europa.eu/ers/schema/clusters)
Alias: clusters

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |  no  |






## Properties

* Range: [ClusterRef](ClusterRef.md)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:clusters |
| native | ers:clusters |




## LinkML Source

<details>
```yaml
name: clusters
description: 'The set of cluster reference/score pairs representing the candidate
  clusters

  that the entity mention in the original request could align to (be equivalent to).

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: clusters
owner: EntityMentionResolutionResponse
domain_of:
- EntityMentionResolutionResponse
range: ClusterRef
required: true
multivalued: true

```
</details>