Feature: ERE/ERS interaction for entity resolutions
  Note that in all the tests, the exact meaning of "known/unknown entity" depends on the ERE implementation,
  e.g., it has already seen the entity in a previous request, or it is a test ERE, with a pre-loaded 
  set of canonical entities.

Scenario: A known entity returns the canonical entity it's equivalent to
  
  A resolution request is pushed to the ERE with an entity that is equivalent to a known 
  canonical entity. The canonical entity is returned asynchronously.

  Detailed examples: see [ere-test-cases.md](../test_data/analysis/ere-test-cases.md), 
  examples 1, 2, 4, 5
Given 
  Entity clusters C1, C2, C3 are already known to the ERE
When 
  The ERS pushes an entity E into the ERE requests channel
And 
  The entity E is estimated to be equivalent to the canonical entities of C1, C2, C3,
  with sufficiently high confidence scores
Then 
  The ERE asynchronously pushes an EntityMentionResolutionResponse object that contains:
  
  - Common response properties:
    - `requestId`: the original request ID
    - `type`: "EntityMentionResolutionResponse"
    - Possibly, other response properties (e.g., `metadata`)
    - These are common to all responses and we won't repeat them in the following
  
  - `alignmentLinkSet.subjectMentionIdentifier`: the ID of the entity E
    This is also common to all resolution responses and we won't repeat it again
  
  - `alignmentLinkSet.alignmentOptions`: a list of
  - `alignmentLink[i] = { canonicalIdentifier: Ci.canonicalId, confidenceScore: score[i]}`
    for i = 0..3, where score[i] is the confidence score for the equivalence between E and Ci.canonicalEntity
    
  Returning the links in score order is not required, though it's recommended.
  Having 3 items in the result is arbitrary, it depends on how many clusters are found and on the
  ERE configuration (e.g., top N results, confidence threshold, or both).


Scenario: An unknown entity resolves to itself

  A resolution request is pushed to the ERE with an unknown entity, which has no equivalents already
	resolved by the ERE
Given 
  The ERE does not know the entity E (ie, it has no equivalent cluster for it)
When 
  The ERS pushes the entity E into the requests channel
Then 
  The ERE asynchronously pushes an entity resolution object to the responses channel that contains
  an alignment set, as other resolution response cases, the set having only one alignment link,
  ans the link contains has `canonicalIdentifier` set with the `draftCanonicalIdentifier` in the 
  original request. 
  

Scenario: An unknown entity without a sufficient similarity to known entities resolves to itself

  A resolution request is pushed to the ERE with an entity that is deemed similar other known
	canonical entities, but all having a confidence score below the set threshold.

	Detailed examples: see ere-test-cases.md, examples 3, 6 
	(https://github.com/meaningfy-ws/er-system/blob/feature/ERS1-49/ere-gherkin-tests/test/test_data/analysis/ere-test-cases.md)
Given 
  The ERE knows the canonical entities in a set of clusters C[]
When 
  The ERS pushes the entity E into the requests channel
And 
  The entity E is computed to be similar to entities in C[], but all the confidence scores are less than
  a configured threshold
Then 
  The ERE behaves as in the 'unknown entity resolves to itself' scenario, ie, it returns that
  bins the entity in a new singleton cluster, with the `draftCanonicalIdentifier` as the canonical ID.


Scenario: A resolution request with rejected canonical IDs returns a different cluster

  ERE reacts to rejections of previously suggested canonical entities by returning
  a different canonical entity in the response.
  
  Typically, we expect that the ERE creates a new singleton cluster for the entity, but it may also 
  return an alternative known cluster, eg, after a rebuild-all request or upon internal re-evaluation 
  decisions (note to developers: different unit tests might be useful for coverage).
    
  The case where `draftCanonicalIdentifier` is in one of the `rejectedCanonicalIdentifiers` 
  is an error, see the unhappy paths feature file.

When 
  The ERS pushes a resolution request for an entity into the requests channel
And
  The request has a set `R[]` as `rejectedCanonicalIdentifiers`, none of them being the
  `draftCanonicalIdentifier`
Then
  The ERE returns a resolution response such that none of `alignmentLink.canonicalIdentifier 
  is in `R[]`.
