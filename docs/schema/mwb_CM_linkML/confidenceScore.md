

# Slot: confidenceScore 


_This indicates a confidence of belonging to a cluster:0 - 1 :automatically computed -1 :rejected by a person_





URI: [ers:confidenceScore](ers:confidenceScore)
Alias: confidenceScore

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AlignmentLink](AlignmentLink.md) | Represents either manual or automatic alignment |  no  |






## Properties

* Range: [Double](Double.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://publications.europa.eu/ontology/ers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:confidenceScore |
| native | http://publications.europa.eu/ontology/ers/confidenceScore |




## LinkML Source

<details>
```yaml
name: confidenceScore
description: This indicates a confidence of belonging to a cluster:0 - 1 :automatically
  computed -1 :rejected by a person
from_schema: http://publications.europa.eu/ontology/ers
rank: 1000
slot_uri: ers:confidenceScore
alias: confidenceScore
owner: AlignmentLink
domain_of:
- AlignmentLink
range: double
required: true
multivalued: false

```
</details>