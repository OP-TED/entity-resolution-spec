

# Slot: entityType 


_A string representing the entity type URI (based on CET)._

__

_Note that we don't use the `designates_type` thing here, nor the `type` attribute, since _

_we don't have entity mention subclasses for now, and the instances of this class don't _

_need any disambiguation._

__

_Also note this has nothing to do with the `type` attribute of requests/responses._

__





URI: [ers:entityType](https://data.europa.eu/ers/schema/entityType)
Alias: entityType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMention](EntityMention.md) | An entity mention is a representation of a real-world entity in the ERS |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:entityType |
| native | ers:entityType |




## LinkML Source

<details>
```yaml
name: entityType
description: "A string representing the entity type URI (based on CET).\n\nNote that\
  \ we don't use the `designates_type` thing here, nor the `type` attribute, since\
  \ \nwe don't have entity mention subclasses for now, and the instances of this class\
  \ don't \nneed any disambiguation.\n\nAlso note this has nothing to do with the\
  \ `type` attribute of requests/responses.\n"
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: entityType
owner: EntityMention
domain_of:
- EntityMention
range: string
required: true

```
</details>