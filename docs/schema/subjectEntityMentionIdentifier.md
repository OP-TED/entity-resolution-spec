

# Slot: subjectEntityMentionIdentifier 


_The identifier of the entity mention that is the subject of these alignment links._

_This must match the `identifier` attribute of an `EntityMention` that a resolution response_

_refers to._

__





URI: [ers:subjectEntityMentionIdentifier](https://data.europa.eu/ers/schema/subjectEntityMentionIdentifier)
Alias: subjectEntityMentionIdentifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AlignmentLinkSet](AlignmentLinkSet.md) | A set of alignment links to a referred entity |  no  |






## Properties

* Range: [Uri](Uri.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:subjectEntityMentionIdentifier |
| native | ers:subjectEntityMentionIdentifier |




## LinkML Source

<details>
```yaml
name: subjectEntityMentionIdentifier
description: 'The identifier of the entity mention that is the subject of these alignment
  links.

  This must match the `identifier` attribute of an `EntityMention` that a resolution
  response

  refers to.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: subjectEntityMentionIdentifier
owner: AlignmentLinkSet
domain_of:
- AlignmentLinkSet
range: uri
required: true

```
</details>