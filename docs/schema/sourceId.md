

# Slot: sourceId 


_The ID or URI of the ERS client that originated the request. This identifies an application or a _

_person accessing the ERS system._

__





URI: [ers:sourceId](https://data.europa.eu/ers/schema/sourceId)
Alias: sourceId

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
| self | ers:sourceId |
| native | ers:sourceId |




## LinkML Source

<details>
```yaml
name: sourceId
description: "The ID or URI of the ERS client that originated the request. This identifies\
  \ an application or a \nperson accessing the ERS system.\n"
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: sourceId
owner: EntityMentionIdentifers
domain_of:
- EntityMentionIdentifers
range: string
required: true

```
</details>