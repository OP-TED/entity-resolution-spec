

# Slot: metadata 


_An optional arbitrary dictionary of further request metadata._

__





URI: [ers:metadata](https://data.europa.eu/ers/schema/metadata)
Alias: metadata

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EREResponse](EREResponse.md) | Root class to represent all the responses sent by the ERE |  no  |
| [ERECommunicationArtefact](ERECommunicationArtefact.md) | Root abstraction to represent attributes common to both requests and results |  no  |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |
| [ERERequest](ERERequest.md) | Root class to represent all the requests sent to the ERE |  no  |
| [FullRebuildRequest](FullRebuildRequest.md) | A request to reset all the resolutions computed so far and rebuild them as  |  no  |
| [EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response sent by the ERE |  no  |
| [FullRebuildResponse](FullRebuildResponse.md) | A response to a `FullRebuildRequest`, confirming that the rebuild process has... |  no  |






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
owner: ERECommunicationArtefact
domain_of:
- ERECommunicationArtefact
range: string

```
</details>