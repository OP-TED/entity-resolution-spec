

# Slot: entity 


_The data about the entity to be resolved._

__





URI: [ers:entity](https://data.europa.eu/ers/schema/entity)
Alias: entity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityResolutionRequest](EntityResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |






## Properties

* Range: [Entity](Entity.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:entity |
| native | ers:entity |




## LinkML Source

<details>
```yaml
name: entity
description: 'The data about the entity to be resolved.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: entity
owner: EntityResolutionRequest
domain_of:
- EntityResolutionRequest
range: Entity
required: true

```
</details>