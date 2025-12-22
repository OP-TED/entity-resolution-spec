

# Slot: sourceEntityId 


_The ID or URI of the original entity that has been resolved._

__





URI: [ers:sourceEntityId](https://data.europa.eu/ers/schema/sourceEntityId)
Alias: sourceEntityId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityResolutionResponse](EntityResolutionResponse.md) | An entity resolution response sent by the ERE |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:sourceEntityId |
| native | ers:sourceEntityId |




## LinkML Source

<details>
```yaml
name: sourceEntityId
description: 'The ID or URI of the original entity that has been resolved.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: sourceEntityId
owner: EntityResolutionResponse
domain_of:
- EntityResolutionResponse
range: string
required: true

```
</details>