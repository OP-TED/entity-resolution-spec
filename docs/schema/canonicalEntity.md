

# Slot: canonicalEntity 


_The canonical entity that the ERE has associated to the original entity._

_This includes the canonical entity URI and its type._

__





URI: [ers:canonicalEntity](https://data.europa.eu/ers/schema/canonicalEntity)
Alias: canonicalEntity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityResolutionResponse](EntityResolutionResponse.md) | An entity resolution response sent by the ERE |  no  |






## Properties

* Range: [CanonicalEntity](CanonicalEntity.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:canonicalEntity |
| native | ers:canonicalEntity |




## LinkML Source

<details>
```yaml
name: canonicalEntity
description: 'The canonical entity that the ERE has associated to the original entity.

  This includes the canonical entity URI and its type.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: canonicalEntity
owner: EntityResolutionResponse
domain_of:
- EntityResolutionResponse
range: CanonicalEntity
required: true

```
</details>