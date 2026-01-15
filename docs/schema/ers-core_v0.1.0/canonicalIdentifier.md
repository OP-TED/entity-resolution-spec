

# Slot: canonicalIdentifier 


_The identifier of the cluster/canonical entity that is considered equivalent to the_

_subject entity mention in the `AlignmentLinkSet` the link belongs to._

__





URI: [ers:canonicalIdentifier](https://data.europa.eu/ers/schema/canonicalIdentifier)
Alias: canonicalIdentifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AlignmentLink](AlignmentLink.md) | An alignment link representing a possible equivalence between an entity menti... |  no  |






## Properties

* Range: [Uri](Uri.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:canonicalIdentifier |
| native | ers:canonicalIdentifier |




## LinkML Source

<details>
```yaml
name: canonicalIdentifier
description: 'The identifier of the cluster/canonical entity that is considered equivalent
  to the

  subject entity mention in the `AlignmentLinkSet` the link belongs to.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: canonicalIdentifier
owner: AlignmentLink
domain_of:
- AlignmentLink
range: uri
required: true

```
</details>