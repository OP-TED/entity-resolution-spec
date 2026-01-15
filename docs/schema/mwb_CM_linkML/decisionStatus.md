

# Slot: decisionStatus 



URI: [ers:decisionStatus](ers:decisionStatus)
Alias: decisionStatus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decission](Decission.md) | The decision object captures what (integration) action shall be taken given a... |  no  |






## Properties

* Range: [DecissionStatus](DecissionStatus.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://publications.europa.eu/ontology/ers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:decisionStatus |
| native | http://publications.europa.eu/ontology/ers/decisionStatus |




## LinkML Source

<details>
```yaml
name: decisionStatus
from_schema: http://publications.europa.eu/ontology/ers
rank: 1000
slot_uri: ers:decisionStatus
alias: decisionStatus
owner: Decission
domain_of:
- Decission
range: DecissionStatus
required: true
multivalued: false

```
</details>