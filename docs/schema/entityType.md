

# Slot: entityType 


_A string representing the entity type (based on CET). This is typically a URI._

__

_Note that this is at this level, and not at `EntityMention`, since, as said above, _

_it's needed to identify the entity, even when its content is not present. For the same_

_reason, it's used both for `EREResolutionRequest` and `EREResolutionResponse` messages., _

__





URI: [ers:entityType](https://data.europa.eu/ers/schema/entityType)
Alias: entityType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |  no  |
| [EntityMentionIdentifers](EntityMentionIdentifers.md) | A container that groups the attributes needed to identify an entity mention i... |  no  |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |






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
description: "A string representing the entity type (based on CET). This is typically\
  \ a URI.\n\nNote that this is at this level, and not at `EntityMention`, since,\
  \ as said above, \nit's needed to identify the entity, even when its content is\
  \ not present. For the same\nreason, it's used both for `EREResolutionRequest` and\
  \ `EREResolutionResponse` messages., \n"
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: entityType
owner: EntityMentionIdentifers
domain_of:
- EntityMentionIdentifers
range: string
required: true

```
</details>