

# Slot: clusterId 


_The identifier of the cluster/canonical entity that is considered equivalent to the_

_subject entity mention that an `EntityMentionResolutionResponse` refers to._

__





URI: [ers:clusterId](https://data.europa.eu/ers/schema/clusterId)
Alias: clusterId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClusterReference](ClusterReference.md) | A reference to a cluster to which an entity is deemed to belong, with an asso... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:clusterId |
| native | ers:clusterId |




## LinkML Source

<details>
```yaml
name: clusterId
description: 'The identifier of the cluster/canonical entity that is considered equivalent
  to the

  subject entity mention that an `EntityMentionResolutionResponse` refers to.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: clusterId
owner: ClusterReference
domain_of:
- ClusterReference
range: string
required: true

```
</details>