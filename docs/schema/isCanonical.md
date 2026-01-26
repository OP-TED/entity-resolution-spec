

# Slot: isCanonical 


_A boolean flag indicating whether the entity mention is to be considered a canonical (the source of truth)._

__

_This is used by the ERS to feed the ERE with well known entity mentions (usually for bootstrapping the ERE)._

_The confidence level to assign to the cluster created should be 1.0 in this case and never overridden by other _

_mentions during re-clustering._

__





URI: [ers:isCanonical](https://data.europa.eu/ers/schema/isCanonical)
Alias: isCanonical

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMention](EntityMention.md) | An entity mention is a representation of a real-world entity, as provided by ... |  no  |






## Properties

* Range: [Boolean](Boolean.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:isCanonical |
| native | ers:isCanonical |




## LinkML Source

<details>
```yaml
name: isCanonical
description: "A boolean flag indicating whether the entity mention is to be considered\
  \ a canonical (the source of truth).\n\nThis is used by the ERS to feed the ERE\
  \ with well known entity mentions (usually for bootstrapping the ERE).\nThe confidence\
  \ level to assign to the cluster created should be 1.0 in this case and never overridden\
  \ by other \nmentions during re-clustering.\n"
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: isCanonical
owner: EntityMention
domain_of:
- EntityMention
range: boolean

```
</details>