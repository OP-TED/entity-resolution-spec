

# Slot: identifier 


_The identifier (with the ERS-derived components) of the entity mention._

__





URI: [ers:identifier](https://data.europa.eu/ers/schema/identifier)
Alias: identifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMention](EntityMention.md) | An entity mention is a representation of a real-world entity, as provided by ... |  no  |






## Properties

* Range: [EntityMentionIdentifier](EntityMentionIdentifier.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:identifier |
| native | ers:identifier |




## LinkML Source

<details>
```yaml
name: identifier
description: 'The identifier (with the ERS-derived components) of the entity mention.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: identifier
owner: EntityMention
domain_of:
- EntityMention
range: EntityMentionIdentifier
required: true

```
</details>