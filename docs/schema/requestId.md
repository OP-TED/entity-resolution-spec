

# Slot: requestId 


_A string representing the unique ID of the request made to the ERS system. In general, this is unique_

_only within the scope of the source and the entity type, ie, within `sourceId` and `entityType`. _

__

_Moreover, this is **not** the same as `ereRequestId`, which instead, is internal to the ERE and is _

_used to match responses to requests._

__





URI: [ere:requestId](https://data.europa.eu/ers/schema/ere/requestId)
Alias: requestId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionIdentifier](EntityMentionIdentifier.md) | A container that groups the attributes needed to identify an entity mention i... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:requestId |
| native | ere:requestId |




## LinkML Source

<details>
```yaml
name: requestId
description: "A string representing the unique ID of the request made to the ERS system.\
  \ In general, this is unique\nonly within the scope of the source and the entity\
  \ type, ie, within `sourceId` and `entityType`. \n\nMoreover, this is **not** the\
  \ same as `ereRequestId`, which instead, is internal to the ERE and is \nused to\
  \ match responses to requests.\n"
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: requestId
owner: EntityMentionIdentifier
domain_of:
- EntityMentionIdentifier
range: string
required: true

```
</details>