

# Slot: payload 



URI: [ers:payload](ers:payload)
Alias: payload

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RequestRecord](RequestRecord.md) | This is stored in the system of records |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://publications.europa.eu/ontology/ers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:payload |
| native | http://publications.europa.eu/ontology/ers/payload |




## LinkML Source

<details>
```yaml
name: payload
from_schema: http://publications.europa.eu/ontology/ers
rank: 1000
slot_uri: ers:payload
alias: payload
owner: RequestRecord
domain_of:
- RequestRecord
range: string
required: true
multivalued: false

```
</details>