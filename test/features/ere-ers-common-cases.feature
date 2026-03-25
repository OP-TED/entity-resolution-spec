Feature: ERE/ERS common case interactions

  Note that in all the tests, the exact meaning of "known/unknown entity" depends on the ERE implementation,
  e.g., it has already seen the entity in a previous request, or it is a test ERE, with a pre-loaded 
  set of canonical entities.

Scenario: A resolution request returns existing cluster candidate references
  
  A resolution request is pushed to the ERE with an entity E, which is known to be equivalent to
  other canonical entities and with sufficiently high confidence scores. The ERE asynchronously returns
  the cluster IDs represented by such canonical entities.

  Detailed examples: see [ere-test-cases.md](../test_data/analysis/ere-test-cases.md), 
  examples 1, 2, 4, 5
Given 
  Entity clusters C1, C2, C3 are already known to the ERE
When 
  The ERS pushes a resolution request for an entity mention E into the ERE requests channel
And 
  The entity E is estimated to be equivalent to the canonical entities of C1, C2, C3,
  with sufficiently high confidence scores
Then 
  The ERE asynchronously pushes an `EntityMentionResolutionResponse` object that contains:
  
  - Common response properties:
    - `request_id`: the original request ID
    - `type`: "EntityMentionResolutionResponse"
    - `entity_mention_id`: an instance of `EntityMentionIdentifier` with 
      `source_id`, `request_id`,`entity_type` equal to the mention in the original request and
      corresponding to E taken from the original request
    - These are common to all responses and we won't repeat them in the following

  
  - `candidates`: a list of `ClusterReference` objects such like:`
  - `{ "cluster_id": <identifier(Ci)>, "confidence_score": <score(E, Ci)>}`
    for i = 0..3
  - All of `score(E, Ci)` are above the confidence threshold configured in the ERE
    
  Returning the cluster references in score order is not required, though it's recommended.
  Having 3 items in the result is arbitrary. In general, it depends on how many clusters are found and on the
  ERE configuration (e.g., top N results, confidence threshold, or both).


Scenario: A resolution request returns a new singleton cluster reference

  A resolution request is pushed to the ERE with an unknown entity, which has no equivalents already
	resolved by the ERE
Given 
  The ERE does not know the entity E (ie, it has no equivalent cluster for it)
When 
  The ERS pushes the entity E into the requests channel
Then 
  The ERE asynchronously pushes an entity resolution object to the responses channel that contains
  a reference to one cluster only.
  The response has the same format as in the previous scenario.
  The cluster ID in the response is formed based on `canonicalID(requestId, sourceId, entityType)`, ie, 
  on the function, described in the technical contract, which computes the canonical ID from the
  composite key of an entity mention.

