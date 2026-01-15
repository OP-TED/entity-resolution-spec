

# Slot: requestIdentifier 



URI: [ers:requestIdentifier](ers:requestIdentifier)
Alias: requestIdentifier

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
| self | ers:requestIdentifier |
| native | http://publications.europa.eu/ontology/ers/requestIdentifier |




## LinkML Source

<details>
```yaml
name: requestIdentifier
from_schema: http://publications.europa.eu/ontology/ers
rank: 1000
slot_uri: ers:requestIdentifier
alias: requestIdentifier
owner: RequestRecord
domain_of:
- RequestRecord
range: uri
required: true
multivalued: false

```
</details>