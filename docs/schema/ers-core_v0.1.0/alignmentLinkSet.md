

# Slot: alignmentLinkSet 


_The set of alignment links representing the candidate canonical entities/clusters_

_that the entity mention in the original request could align to (be equivalent to)._

__

_**Note**: for the moment, this is not multi-valued, since we don't support batch requests (yet?),_

_thus there is only one set in a response, that resolves for the single entity mention in the_

_original request (with multiple alignment candidates). If, in the future, we support batch requests,_

_then we might need to return one alignment link set per entity mention in a request._

__





URI: [ers:alignmentLinkSet](https://data.europa.eu/ers/schema/alignmentLinkSet)
Alias: alignmentLinkSet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response sent by the ERE |  no  |






## Properties

* Range: [AlignmentLinkSet](AlignmentLinkSet.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:alignmentLinkSet |
| native | ers:alignmentLinkSet |




## LinkML Source

<details>
```yaml
name: alignmentLinkSet
description: 'The set of alignment links representing the candidate canonical entities/clusters

  that the entity mention in the original request could align to (be equivalent to).


  **Note**: for the moment, this is not multi-valued, since we don''t support batch
  requests (yet?),

  thus there is only one set in a response, that resolves for the single entity mention
  in the

  original request (with multiple alignment candidates). If, in the future, we support
  batch requests,

  then we might need to return one alignment link set per entity mention in a request.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: alignmentLinkSet
owner: EntityMentionResolutionResponse
domain_of:
- EntityMentionResolutionResponse
range: AlignmentLinkSet
required: true

```
</details>