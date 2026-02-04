Feature: ERE/ERS idempotent requests

  This feature tests idempotent interactions with the ERE.

Scenario: Repeated regular resolution request returns the same result

  This is true if no full rebuilds or requests with rejected clusters have happened in between.

Given
  That the ERE has previously replied to a resolution request for an entity E
  (with or without excluded clusters)
And
  No `FullBuildRequest` has been pushed since the previous resolution
And
  No resolution request about the same entity mention that contains excluded clusters 
  has been pushed since the previous resolution
When
  The ERS pushes again the same resolution request for the entity E into the ERE requests channel
Then 
  The ERE asynchronously pushes an `EntityMentionResolutionResponse` object that contains the
  same set of `candidateClusters` as in the previous response for E, including their confidence score.

  Since returning the cluster references in score order is not required, such order doesn't apply to 
  this invariant, i.e., the second result can come in a different order for the cluster references.


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


Scenario: Rejected clusters affect later resolution requests

  If a request excludes some clusters, then all the requests that follow will have the same exclusions.

Given
  That the ERE has previously replied to a resolution request for an entity E, with
  a set `R[]` of excluded cluster IDs in the request
And
  A resolution request for the same entity E is pushed again, with no excluded clusters
Then
  The response to the new request must not contain any cluster in R[].

  We assume that the reply to the first request doesn't contain R[] either, as per the 
  corresponding scenario in the [common cases feature](ere-ers-common-cases.feature).



Scenario: Multiple resolution requests containing excluded clusters cause the respective exclusions to be merged

  If multiple requests exclude multiple clusters for the same entity, then the ERE must exclude them
  all in subsequent responses.

Given
  The ERE has received a resolution request for an entity E, which excludes
  a set `R1[]` of cluster IDs
And
  The ERE has replied to the initial request with a set of candidate clusters R2[]
When
  A new resolution about E is sent that contains R2[] as excluded clusters
Then
  The ERE response doesn't contain any cluster ID in R1[] or R2[].


Scenario: Multiple resolution requests with multiple rejections affect later resolution requests

  If multiple requests exclude multiple clusters for the same entity, then the ERE must exclude them
  all in subsequent responses. This is a combination of the two previous scenarios.
Given
  The same pre-conditions as "Multiple resolution requests containing excluded clusters cause the respective exclusions to be merged"
And
  The request with R2[] has been sent and replied
When
  A new resolution about E is sent that contains no excluded clusters
Then
  The ERE response doesn't contain any cluster ID in R1[] or R2[].
