

# Slot: requestId 



URI: [ers:requestId](https://data.europa.eu/ers/schema/requestId)
Alias: requestId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Request](Request.md) | Root class to represent all the requests sent to the ERE |  no  |
| [EntityResolutionRequest](EntityResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |
| [RebuildRequest](RebuildRequest.md) | A request to reset all the resolutions computed so far and rebuild them as  |  no  |
| [Response](Response.md) | Root class to represent all the responses sent by the ERE |  no  |
| [EntityResolutionResponse](EntityResolutionResponse.md) | An entity resolution response sent by the ERE |  no  |
| [RebuildResponse](RebuildResponse.md) | A response to a `RebuildRequest`, confirming that the rebuild process has sta... |  no  |
| [ErrorResponse](ErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |






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
- Request
- Response
range: string

```
</details>