

# Slot: source_id 



URI: [ere:source_id](https://data.europa.eu/ers/schema/ere/source_id)
Alias: source_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LookupState](LookupState.md) | Tracks the resolution state for entity mentions from a particular source |  no  |
| [EntityMentionIdentifier](EntityMentionIdentifier.md) | A container that groups the attributes needed to identify an entity mention i... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:source_id |
| native | ere:source_id |




## LinkML Source

<details>
```yaml
name: source_id
alias: source_id
domain_of:
- EntityMentionIdentifier
- LookupState
range: string

```
</details>