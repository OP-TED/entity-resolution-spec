

# Slot: originator 


_The ID or URI of the request originator._

__





URI: [ers:originator](https://data.europa.eu/ers/schema/originator)
Alias: originator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |
| [ERERequest](ERERequest.md) | Root class to represent all the requests sent to the ERE |  no  |
| [FullRebuildRequest](FullRebuildRequest.md) | A request to reset all the resolutions computed so far and rebuild them as  |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:originator |
| native | ers:originator |




## LinkML Source

<details>
```yaml
name: originator
description: 'The ID or URI of the request originator.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: originator
owner: ERERequest
domain_of:
- ERERequest
range: string
required: true

```
</details>