

# Slot: metadata 


_JSON metadata providing context (e.g., curator notes, reasoning)._

__





URI: [ere:metadata](https://data.europa.eu/ers/schema/ere/metadata)
Alias: metadata

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UserAction](UserAction.md) | Immutable record of a curator action on an entity mention resolution |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:metadata |
| native | ere:metadata |




## LinkML Source

<details>
```yaml
name: metadata
description: 'JSON metadata providing context (e.g., curator notes, reasoning).

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: metadata
owner: UserAction
domain_of:
- UserAction
range: string

```
</details>