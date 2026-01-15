

# Slot: creationTime 


_The timestamp when the request was created._

__





URI: [ers:creationTime](https://data.europa.eu/ers/schema/creationTime)
Alias: creationTime

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FullRebuildRequest](FullRebuildRequest.md) | A request to reset all the resolutions computed so far and rebuild them as  |  no  |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |
| [ERERequest](ERERequest.md) | Root class to represent all the requests sent to the ERE |  no  |






## Properties

* Range: [Datetime](Datetime.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:creationTime |
| native | ers:creationTime |




## LinkML Source

<details>
```yaml
name: creationTime
description: 'The timestamp when the request was created.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: creationTime
owner: ERERequest
domain_of:
- ERERequest
range: datetime

```
</details>