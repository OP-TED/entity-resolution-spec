

# Slot: identifiedBy 


_The identification triad of the entity mention._

__





URI: [ere:identifiedBy](https://data.europa.eu/ers/schema/ere/identifiedBy)
Alias: identifiedBy

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


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:identifiedBy |
| native | ere:identifiedBy |




## LinkML Source

<details>
```yaml
name: identifiedBy
description: 'The identification triad of the entity mention.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: identifiedBy
owner: EntityMention
domain_of:
- EntityMention
range: EntityMentionIdentifier
required: true

```
</details>