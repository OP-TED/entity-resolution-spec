

# Slot: action_type 


_The type of action the curator performed_





URI: [ere:action_type](https://data.europa.eu/ers/schema/ere/action_type)
Alias: action_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UserAction](UserAction.md) | Immutable record of a curator action on an entity mention resolution |  no  |






## Properties

* Range: [UserActionType](UserActionType.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:action_type |
| native | ere:action_type |




## LinkML Source

<details>
```yaml
name: action_type
description: The type of action the curator performed
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: action_type
owner: UserAction
domain_of:
- UserAction
range: UserActionType
required: true

```
</details>