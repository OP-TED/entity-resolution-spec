

# Slot: candidates 



URI: [ere:candidates](https://data.europa.eu/ers/schema/ere/candidates)
Alias: candidates

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decision](Decision.md) | Canonical placement of an entity mention to a cluster |  no  |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |  no  |
| [UserAction](UserAction.md) | Immutable record of a curator action on an entity mention resolution |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:candidates |
| native | ere:candidates |




## LinkML Source

<details>
```yaml
name: candidates
alias: candidates
domain_of:
- EntityMentionResolutionResponse
- Decision
- UserAction
range: string

```
</details>