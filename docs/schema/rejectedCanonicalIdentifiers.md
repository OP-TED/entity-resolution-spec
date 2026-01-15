

# Slot: rejectedCanonicalIdentifiers 


_When this is present, the request is a refresh request: it is asking that the entity _

_is resolved again and the clusters/canonical entities that were previously proposed _

_as resolution are now ignored._

__

_The exact reaction to this is implementation dependent. In the simplest case, the ERE_

_might just create a singleton cluster with this entity as member. In a more advanced _

_case, it might recompute the similarity with more advanced algorithms or use updated_

_data._

__





URI: [ers:rejectedCanonicalIdentifiers](https://data.europa.eu/ers/schema/rejectedCanonicalIdentifiers)
Alias: rejectedCanonicalIdentifiers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |






## Properties

* Range: [Uri](Uri.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:rejectedCanonicalIdentifiers |
| native | ers:rejectedCanonicalIdentifiers |




## LinkML Source

<details>
```yaml
name: rejectedCanonicalIdentifiers
description: "When this is present, the request is a refresh request: it is asking\
  \ that the entity \nis resolved again and the clusters/canonical entities that were\
  \ previously proposed \nas resolution are now ignored.\n\nThe exact reaction to\
  \ this is implementation dependent. In the simplest case, the ERE\nmight just create\
  \ a singleton cluster with this entity as member. In a more advanced \ncase, it\
  \ might recompute the similarity with more advanced algorithms or use updated\n\
  data.\n"
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: rejectedCanonicalIdentifiers
owner: EntityMentionResolutionRequest
domain_of:
- EntityMentionResolutionRequest
range: uri
multivalued: true

```
</details>