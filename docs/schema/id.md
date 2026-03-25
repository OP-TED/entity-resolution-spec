

# Slot: id 



URI: [ere:id](https://data.europa.eu/ers/schema/ere/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UserAction](UserAction.md) | Immutable record of a curator action on an entity mention resolution |  no  |
| [Decision](Decision.md) | Canonical placement of an entity mention to a cluster |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:id |
| native | ere:id |




## LinkML Source

<details>
```yaml
name: id
alias: id
domain_of:
- Decision
- UserAction
range: string

```
</details>