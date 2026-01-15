

# Slot: jsonRepresentation 


_An optional JSON representation of the entity, which is usually achieved from the payload._

_This is mainly useful for the curation app._

__





URI: [ers:jsonRepresentation](https://data.europa.eu/ers/schema/jsonRepresentation)
Alias: jsonRepresentation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMention](EntityMention.md) | An entity mention is a representation of a real-world entity in the ERS |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:jsonRepresentation |
| native | ers:jsonRepresentation |




## LinkML Source

<details>
```yaml
name: jsonRepresentation
description: 'An optional JSON representation of the entity, which is usually achieved
  from the payload.

  This is mainly useful for the curation app.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: jsonRepresentation
owner: EntityMention
domain_of:
- EntityMention
range: string

```
</details>