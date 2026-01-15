

# Slot: identifier 


_An URI identifying the entity._

__

_While mandatory, this can be computed, using same function that depends on the entity payload._

_In that case, **there must be** a single function in the whole ERS (including the ERE) that_

_computes the same identifier for the same payload, eg, a hash, an RDF URI extractor. This is_

_needed for the resolution results to refer to the correct request entities.        _

__





URI: [ers:identifier](https://data.europa.eu/ers/schema/identifier)
Alias: identifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMention](EntityMention.md) | An entity mention is a representation of a real-world entity in the ERS |  no  |






## Properties

* Range: [Uri](Uri.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:identifier |
| native | ers:identifier |




## LinkML Source

<details>
```yaml
name: identifier
description: "An URI identifying the entity.\n\nWhile mandatory, this can be computed,\
  \ using same function that depends on the entity payload.\nIn that case, **there\
  \ must be** a single function in the whole ERS (including the ERE) that\ncomputes\
  \ the same identifier for the same payload, eg, a hash, an RDF URI extractor. This\
  \ is\nneeded for the resolution results to refer to the correct request entities.\
  \        \n"
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: identifier
owner: EntityMention
domain_of:
- EntityMention
range: uri
required: true

```
</details>