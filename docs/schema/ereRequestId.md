

# Slot: ereRequestId 


_A string representing the unique ID of an ERE request, or the ID of the request a response is about._

_This **is not** the same as `requestId` + `sourceId`._

__





URI: [ers:ereRequestId](https://data.europa.eu/ers/schema/ereRequestId)
Alias: ereRequestId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |
| [EREMessage](EREMessage.md) | Root abstraction to represent attributes common to both requests and results |  no  |
| [FullRebuildRequest](FullRebuildRequest.md) | A request to reset all the resolutions computed so far and possibly rebuild t... |  no  |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |  no  |
| [ERERequest](ERERequest.md) | Root class to represent all the requests sent to the ERE |  no  |
| [FullRebuildResponse](FullRebuildResponse.md) | A response to a `FullRebuildRequest`, confirming that the rebuild process has... |  no  |
| [EREResponse](EREResponse.md) | Root class to represent all the responses sent by the ERE |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:ereRequestId |
| native | ers:ereRequestId |




## LinkML Source

<details>
```yaml
name: ereRequestId
description: 'A string representing the unique ID of an ERE request, or the ID of
  the request a response is about.

  This **is not** the same as `requestId` + `sourceId`.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: ereRequestId
owner: EREMessage
domain_of:
- EREMessage
range: string
required: true

```
</details>