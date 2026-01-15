

# Slot: alignmentOptions 


_A list of possible matches (alignment links) between the subject entity mention_

_and candidate canonical entities._

__

_It is recommended that these are sorted by descending confidence score, although_

_that is not mandatory._

__





URI: [ers:alignmentOptions](https://data.europa.eu/ers/schema/alignmentOptions)
Alias: alignmentOptions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AlignmentLinkSet](AlignmentLinkSet.md) | A set of alignment links to a referred entity |  no  |






## Properties

* Range: [AlignmentLink](AlignmentLink.md)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:alignmentOptions |
| native | ers:alignmentOptions |




## LinkML Source

<details>
```yaml
name: alignmentOptions
description: 'A list of possible matches (alignment links) between the subject entity
  mention

  and candidate canonical entities.


  It is recommended that these are sorted by descending confidence score, although

  that is not mandatory.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: alignmentOptions
owner: AlignmentLinkSet
domain_of:
- AlignmentLinkSet
range: AlignmentLink
required: true
multivalued: true

```
</details>