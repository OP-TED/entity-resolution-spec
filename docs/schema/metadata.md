

# Slot: metadata 


_An optional arbitrary dictionary of further request metadata._

__





URI: [ers:metadata](https://data.europa.eu/ers/schema/metadata)
Alias: metadata

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Request](Request.md) | Root class to represent all the requests sent to the ERE |  no  |
| [RequestOrResponseMixin](RequestOrResponseMixin.md) | Root mixin to represent attributes common to both requests and results |  no  |
| [Response](Response.md) | Root class to represent all the responses sent by the ERE |  no  |
| [EntityResolutionRequest](EntityResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |
| [RebuildRequest](RebuildRequest.md) | A request to reset all the resolutions computed so far and rebuild them as  |  no  |
| [RebuildResponse](RebuildResponse.md) | A response to a `RebuildRequest`, confirming that the rebuild process has sta... |  no  |
| [EntityResolutionResponse](EntityResolutionResponse.md) | An entity resolution response sent by the ERE |  no  |
| [ErrorResponse](ErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:metadata |
| native | ers:metadata |




## LinkML Source

<details>
```yaml
name: metadata
description: 'An optional arbitrary dictionary of further request metadata.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: metadata
owner: RequestOrResponseMixin
domain_of:
- RequestOrResponseMixin
range: string

```
</details>