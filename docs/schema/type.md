

# Slot: type 



URI: [ers:type](https://data.europa.eu/ers/schema/type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Request](Request.md) | Root class to represent all the requests sent to the ERE |  no  |
| [EntityResolutionRequest](EntityResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |
| [RequestOrResponseMixin](RequestOrResponseMixin.md) | Root mixin to represent attributes common to both requests and results |  no  |
| [RebuildRequest](RebuildRequest.md) | A request to reset all the resolutions computed so far and rebuild them as  |  no  |
| [CanonicalEntity](CanonicalEntity.md) | A canonical entity is an entity that the ERE has created during the resolutio... |  no  |
| [Response](Response.md) | Root class to represent all the responses sent by the ERE |  no  |
| [EntityResolutionResponse](EntityResolutionResponse.md) | An entity resolution response sent by the ERE |  no  |
| [RebuildResponse](RebuildResponse.md) | A response to a `RebuildRequest`, confirming that the rebuild process has sta... |  no  |
| [Entity](Entity.md) | An entity is a representation of a real-world entity, as provided by the ERS |  no  |
| [ErrorResponse](ErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:type |
| native | ers:type |




## LinkML Source

<details>
```yaml
name: type
alias: type
domain_of:
- RequestOrResponseMixin
- Entity
range: string

```
</details>