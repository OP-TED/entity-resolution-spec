

# Slot: requestId 


_A string representing the unique ID of the request made to the ERS system. In general, this is unique_

_only within the scope of the source and the entity type, ie, within `sourceId` and `entityType`. _

__

_Moreover, this is **not** the same as `ereRequestId`, which instead, is internal to the ERE and is _

_used to match responses to requests._

__





URI: [ers:requestId](https://data.europa.eu/ers/schema/requestId)
Alias: requestId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |  no  |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |
| [EntityMentionIdentifers](EntityMentionIdentifers.md) | A container that groups the attributes needed to identify an entity mention i... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:requestId |
| native | ers:requestId |




## LinkML Source

<details>
```yaml
name: requestId
description: "A string representing the unique ID of the request made to the ERS system.\
  \ In general, this is unique\nonly within the scope of the source and the entity\
  \ type, ie, within `sourceId` and `entityType`. \n\nMoreover, this is **not** the\
  \ same as `ereRequestId`, which instead, is internal to the ERE and is \nused to\
  \ match responses to requests.\n"
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: requestId
owner: EntityMentionIdentifers
domain_of:
- EntityMentionIdentifers
range: string
required: true

```
</details>