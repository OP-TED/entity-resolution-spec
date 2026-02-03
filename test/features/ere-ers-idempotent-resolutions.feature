Feature: ERE/ERS idempotent requests

  This feature tests that ERE resolution request are idempotent.

Scenario: Repeated regular resolution request returns the same result

Given
  That the ERE has previously replied to a resolution request for an entity E, with
  no excluded cluster IDs in the request
And
  No `FullBuildRequest` has been pushed since the previous resolution
When
  The ERS pushes again the same resolution request for the entity E into the ERE requests channel
Then 
  The ERE asynchronously pushes an `EntityMentionResolutionResponse` object that contains the
  same set of `candidateClusters` as in the previous response for E, including their confidence score.

  Since returning the cluster references in score order is not required, the order this invariant
  doesn't apply to that, the second result can come in a different order for the cluster references.


Scenario: Repeated resolution request with rejected clusters returns the same result

  This is very similar to the previous scenario about a regular request, but considers that requests
  with filtered clusters are also idempotent.

Given
  That the ERE has previously replied to a resolution request for an entity E, with
  a set `R[]` of excluded cluster IDs in the request
And
  No `FullBuildRequest` has been pushed since the previous resolution
When
  The ERS sends again the same resolution request for the entity E and the same set `R[]` as `excludedClusterIds`
Then 
  The ERE asynchronously pushes an `EntityMentionResolutionResponse` object that contains the
  same set of `candidateClusters` as in the previous response for E, including the same confidence scores.
  
  Thus, the response excludes the same clusters.


Scenario Outline: Rejected clusters don't affect later regular resolution requests

  If a resolution request about E yields a set of candidate clusters, a request excluding 
  some of those clusters will do so in the result, however, any further request without
  exclusions must return the same original set of candidate clusters.
  
  In other words, requests with excluded clusters don't change the ERE internal state, since
  the ERE has only a consulting role and final decisions on clustering are an ERS's responsibility.

  Examples:
    | excludedCardinality |
    | 1                   |
    | 2                   |
      
Given
  That the ERE has previously replied to a resolution request for an entity E, with
  no excluded cluster IDs in the request, yielding a set of candidate clusters C[]
And
  That the ERE has also replied to a resolution request for the same entity E, with
  a set `R[]` of excluded cluster IDs, such that some clusters in C[] are in R[]
And
  R[] has <excludedCardinality> entries
And
  No `FullBuildRequest` has been pushed since the previous resolution
When
  The ERS pushes again the original resolution request for the entity E, with no excluded clusters
Then 
  The ERE asynchronously pushes an `EntityMentionResolutionResponse` object that contains the
  same set of `candidateClusters` C[] as in the first response for E, including their confidence score.
