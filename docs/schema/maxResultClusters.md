

# Slot: maxResultClusters 


_An optional hint to the ERE about the maximum number of clusters to be returned_

_in the response. This can be used to limit the size of the response._

__

_In general, this is a hint for the ERE, it may ignore it and use a configuration_

_parameter instead (or use a combination of the two limits)._

__





URI: [ers:maxResultClusters](https://data.europa.eu/ers/schema/maxResultClusters)
Alias: maxResultClusters

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |






## Properties

* Range: [Integer](Integer.md)

* Minimum Value: 1




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:maxResultClusters |
| native | ers:maxResultClusters |




## LinkML Source

<details>
```yaml
name: maxResultClusters
description: 'An optional hint to the ERE about the maximum number of clusters to
  be returned

  in the response. This can be used to limit the size of the response.


  In general, this is a hint for the ERE, it may ignore it and use a configuration

  parameter instead (or use a combination of the two limits).

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: maxResultClusters
owner: EntityMentionResolutionRequest
domain_of:
- EntityMentionResolutionRequest
range: integer
minimum_value: 1

```
</details>