Feature: ERE/ERS interaction upon rebuild requests

  The ERE correctly processes a rebuild request, asynchronously replies with an acknowledgement
	response to it, and it keeps processing resolution requests as usual after the a rebuild.

	
Scenario: The ERE acknowledges a rebuild request

  Upon a rebuild request pushed to the ERE, this asynchronously replies with a response that
	indicates the request has been received and the internal state has been reset. 
When 
	The ERS pushes a rebuild request into the requests channel
Then 
	The ERE asynchronously pushes a rebuild response to the rebuild responses channel that contains:

  requestId: the ID of the rebuild request
  type: "RebuildResponse" # JSON object property, matches the LinkML class in the service schema. 


Scenario: The ERE keeps resolving entities as usually after a rebuild request

	Note that, as in other tests, the exact meaning of "known/unknown entity" depends on the ERE implementation,
  e.g., it has already seen the entity in a previous request, or it is a test ERE, with a pre-loaded 
  set of canonical entities.
Given 
	a rebuild request was pushed to the ERE and the ERE has responded with a rebuild response
When 
	The ERS pushes a resolution request into the ERE requests channel for the entity E
Then 
	The ERE asynchronously pushes an entity resolution object to the responses channel that contains
	either the E entity (if E was unknown) or a canonical entity C with a confidence score above the
	configured threshold (if E is considered equivalent to a known entity C). Namely, a response like:
	
	sourceEntityId: the ID of the entity E
	canonicalEntity: an RDF representation of E or another entity C
	confidenceLevel: 1.0 (if canonicalEntity is E) or a value above the min configured threshold
	type: "EntityResolution" # JSON object type, matches the LinkML class in the service schema

