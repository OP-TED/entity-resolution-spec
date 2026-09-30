

# Slot: current_placement 


_The accepted cluster for this mention (latest from ERE or curator)._

__





URI: [ere:current_placement](https://data.europa.eu/ers/schema/ere/current_placement)
Alias: current_placement

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decision](Decision.md) | Canonical placement of an entity mention to a cluster |  no  |






## Properties

* Range: [ClusterReference](ClusterReference.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:current_placement |
| native | ere:current_placement |




## LinkML Source

<details>
```yaml
name: current_placement
description: 'The accepted cluster for this mention (latest from ERE or curator).

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: current_placement
owner: Decision
domain_of:
- Decision
range: ClusterReference
required: true

```
</details>