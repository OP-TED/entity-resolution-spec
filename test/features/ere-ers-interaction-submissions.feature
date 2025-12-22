Feature: ERE/ERS interaction for entity resolutions
  Note that in all the tests, the exact meaning of "known/unknown entity" depends on the ERE implementation,
  e.g., it has already seen the entity in a previous request, or it is a test ERE, with a pre-loaded 
  set of canonical entities.

Scenario: A known entity returns the canonical entity it's equivalent to
  
  A resolution request is pushed to the ERE with an entity that is equivalent to a known 
  canonical entity. The canonical entity is returned asynchronously.

  Detailed examples: see ere-test-cases.md, examples 1, 2, 4, 5
	(https://github.com/meaningfy-ws/er-system/blob/feature/ERS1-49/ere-gherkin-tests/test/test_data/analysis/ere-test-cases.md)
  TODO: fix the link after merging into develop

Given 
  An entity C is already known
When 
  The ERS pushes an entity E into the ERE requests channel
And 
  The entity E is equivalent to entity C with a sufficient confidence score
Then 
  The ERE asynchronously pushes an entity resolution object to the responses channel that contains:
  
  sourceEntityId: the ID of the entity C
  canonicalEntity: an RDF representation of C
  confidenceLevel: a value above the min configured threshold (eg, 0.98)
	type: "EntityResolution" # JSON object type, matches the LinkML class in the service schema 


Scenario: An unknown entity resolves to itself

  A resolution request is pushed to the ERE with an unknown entity, which has no equivalents already
	resolved by the ERE
Given 
  The ERE does not know the entity E
When 
  The ERS pushes the entity E into the requests channel
Then 
  The ERE asynchronously pushes an entity resolution object to the responses channel that contains:
  
  sourceEntityId: the ID of the entity E
  canonicalEntity: an RDF representation of E
	confidenceLevel: 1.0 (since the new canonical entity is E itself)
	type: "EntityResolution"


Scenario: An unknown entity without a sufficient similarity to known entities resolves to itself

  A resolution request is pushed to the ERE with an entity that is deemed similar other known
	canonical entities, but all having a confidence score below the set threshold.

	Detailed examples: see ere-test-cases.md, examples 3, 6 
	(https://github.com/meaningfy-ws/er-system/blob/feature/ERS1-49/ere-gherkin-tests/test/test_data/analysis/ere-test-cases.md)
Given 
  The ERE knows the canonical entity C[]
When 
  The ERS pushes the entity E into the requests channel
And 
  The entity E is computed to be similar to entities in C[], but all the confidence scores are less than
  a configured threshold
Then 
  The ERE asynchronously pushes an entity resolution object to the responses channel that contains:
  
  sourceEntityId: the ID of the entity E
  canonicalEntity: an RDF representation of E
	confidenceLevel: 1.0 (since the new canonical entity is E itself)
	type: "EntityResolution"

  TODO: from the point of view of the ERE client, this case is indistinguishable from the 
  "An unknown entity resolves to itself" scenario. A similar test is useful to verify an 
  ERE implementation.
  