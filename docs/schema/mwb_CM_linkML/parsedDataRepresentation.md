

# Slot: parsedDataRepresentation 


_data are parsed/computed before storage in the ERS. Note:this could be lazy parsing because it is only for LinkCuration._





URI: [ers:parsedDataRepresentation](ers:parsedDataRepresentation)
Alias: parsedDataRepresentation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMention](EntityMention.md) |  |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://publications.europa.eu/ontology/ers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:parsedDataRepresentation |
| native | http://publications.europa.eu/ontology/ers/parsedDataRepresentation |




## LinkML Source

<details>
```yaml
name: parsedDataRepresentation
description: data are parsed/computed before storage in the ERS. Note:this could be
  lazy parsing because it is only for LinkCuration.
from_schema: http://publications.europa.eu/ontology/ers
rank: 1000
slot_uri: ers:parsedDataRepresentation
alias: parsedDataRepresentation
owner: EntityMention
domain_of:
- EntityMention
range: string
required: true
multivalued: false

```
</details>