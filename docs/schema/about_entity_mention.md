

# Slot: about_entity_mention 



URI: [ere:about_entity_mention](https://data.europa.eu/ers/schema/ere/about_entity_mention)
Alias: about_entity_mention

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
| self | ere:about_entity_mention |
| native | ere:about_entity_mention |




## LinkML Source

<details>
```yaml
name: about_entity_mention
alias: about_entity_mention
domain_of:
- Decision
- UserAction
range: string

```
</details>