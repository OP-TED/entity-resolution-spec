

# Slot: confidenceScore 


_A 0-1 value of how confident the ERE is about the equivalence between the subject entity mention_

_and the target canonical entity._

__





URI: [ere:confidenceScore](https://data.europa.eu/ers/schema/ere/confidenceScore)
Alias: confidenceScore

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AlignmentLink](AlignmentLink.md) | An alignment link representing a possible equivalence between an entity menti... |  no  |






## Properties

* Range: [Float](Float.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:confidenceScore |
| native | ere:confidenceScore |




## LinkML Source

<details>
```yaml
name: confidenceScore
description: 'A 0-1 value of how confident the ERE is about the equivalence between
  the subject entity mention

  and the target canonical entity.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: confidenceScore
owner: AlignmentLink
domain_of:
- AlignmentLink
range: float
required: true

```
</details>