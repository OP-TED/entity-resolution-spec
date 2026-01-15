

# Slot: originatorIdentifier 



URI: [ers:originatorIdentifier](ers:originatorIdentifier)
Alias: originatorIdentifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RequestRecord](RequestRecord.md) | This is stored in the system of records |  no  |






## Properties

* Range: [Uri](Uri.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://publications.europa.eu/ontology/ers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:originatorIdentifier |
| native | http://publications.europa.eu/ontology/ers/originatorIdentifier |




## LinkML Source

<details>
```yaml
name: originatorIdentifier
from_schema: http://publications.europa.eu/ontology/ers
rank: 1000
slot_uri: ers:originatorIdentifier
alias: originatorIdentifier
owner: RequestRecord
domain_of:
- RequestRecord
range: uri
required: true
multivalued: false

```
</details>