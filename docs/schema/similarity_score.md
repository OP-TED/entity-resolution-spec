

# Slot: similarity_score 


_A 0-1 score representing the pairwise comparison between a mention and a cluster (likely_

_based on a representative representation)._

__





URI: [ere:similarity_score](https://data.europa.eu/ers/schema/ere/similarity_score)
Alias: similarity_score

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClusterReference](ClusterReference.md) | A reference to a cluster to which an entity is deemed to belong, with an asso... |  no  |






## Properties

* Range: [Float](Float.md)

* Required: True

* Minimum Value: 0

* Maximum Value: 1




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:similarity_score |
| native | ere:similarity_score |




## LinkML Source

<details>
```yaml
name: similarity_score
description: 'A 0-1 score representing the pairwise comparison between a mention and
  a cluster (likely

  based on a representative representation).

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: similarity_score
owner: ClusterReference
domain_of:
- ClusterReference
range: float
required: true
minimum_value: 0.0
maximum_value: 1.0

```
</details>