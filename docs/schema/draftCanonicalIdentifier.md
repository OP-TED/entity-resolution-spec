

# Slot: draftCanonicalIdentifier 


_An optional URI representing a draft canonical identifier for the entity mention_

_in this request._

__

_The ERS creates this when it still doesn't know anything about an entity resolution, for _

_the purpose of quickly replying something and postpone a final resolution to when the _

_ERE has it. The ERE must use this ID when it creates a new (typically singleton) cluster_

_for this entity mention, if it can't associate the entity to any cluster it already knows._

__





URI: [ers:draftCanonicalIdentifier](https://data.europa.eu/ers/schema/draftCanonicalIdentifier)
Alias: draftCanonicalIdentifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |






## Properties

* Range: [Uri](Uri.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:draftCanonicalIdentifier |
| native | ers:draftCanonicalIdentifier |




## LinkML Source

<details>
```yaml
name: draftCanonicalIdentifier
description: "An optional URI representing a draft canonical identifier for the entity\
  \ mention\nin this request.\n\nThe ERS creates this when it still doesn't know anything\
  \ about an entity resolution, for \nthe purpose of quickly replying something and\
  \ postpone a final resolution to when the \nERE has it. The ERE must use this ID\
  \ when it creates a new (typically singleton) cluster\nfor this entity mention,\
  \ if it can't associate the entity to any cluster it already knows.\n"
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: draftCanonicalIdentifier
owner: EntityMentionResolutionRequest
domain_of:
- EntityMentionResolutionRequest
range: uri

```
</details>