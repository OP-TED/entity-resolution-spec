

# Slot: entityMention 


_The data about the entity to be resolved. Note that, at least for the moment, we don't support_

_batch requests, so this property is single-valued._

__





URI: [ers:entityMention](https://data.europa.eu/ers/schema/entityMention)
Alias: entityMention

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |






## Properties

* Range: [EntityMention](EntityMention.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:entityMention |
| native | ers:entityMention |




## LinkML Source

<details>
```yaml
name: entityMention
description: 'The data about the entity to be resolved. Note that, at least for the
  moment, we don''t support

  batch requests, so this property is single-valued.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: entityMention
owner: EntityMentionResolutionRequest
domain_of:
- EntityMentionResolutionRequest
range: EntityMention
required: true

```
</details>