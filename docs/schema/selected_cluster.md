

# Slot: selected_cluster 


_The cluster selected by the curator (if action was ACCEPT_TOP_

_or ACCEPT_ALTERNATIVE). NULL if action was REJECT_ALL._

__





URI: [ere:selected_cluster](https://data.europa.eu/ers/schema/ere/selected_cluster)
Alias: selected_cluster

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UserAction](UserAction.md) | Immutable record of a curator action on an entity mention resolution |  no  |






## Properties

* Range: [ClusterReference](ClusterReference.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:selected_cluster |
| native | ere:selected_cluster |




## LinkML Source

<details>
```yaml
name: selected_cluster
description: 'The cluster selected by the curator (if action was ACCEPT_TOP

  or ACCEPT_ALTERNATIVE). NULL if action was REJECT_ALL.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: selected_cluster
owner: UserAction
domain_of:
- UserAction
range: ClusterReference

```
</details>