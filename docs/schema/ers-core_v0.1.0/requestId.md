

# Slot: requestId 



URI: [ers:requestId](https://data.europa.eu/ers/schema/requestId)
Alias: requestId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EREResponse](EREResponse.md) | Root class to represent all the responses sent by the ERE |  no  |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |
| [ERERequest](ERERequest.md) | Root class to represent all the requests sent to the ERE |  no  |
| [FullRebuildRequest](FullRebuildRequest.md) | A request to reset all the resolutions computed so far and rebuild them as  |  no  |
| [EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response sent by the ERE |  no  |
| [FullRebuildResponse](FullRebuildResponse.md) | A response to a `FullRebuildRequest`, confirming that the rebuild process has... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:requestId |
| native | ers:requestId |




## LinkML Source

<details>
```yaml
name: requestId
alias: requestId
domain_of:
- ERERequest
- EREResponse
range: string

```
</details>