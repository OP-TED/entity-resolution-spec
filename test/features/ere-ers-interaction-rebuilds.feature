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

  `requestId`: the ID of the rebuild request
  `type: "RebuildResponse"`, a JSON object property, matches the LinkML class in the service schema.


Scenario: The ERE keeps resolving entities as usually after a rebuild request

	Note that, as in other tests, the exact meaning of "known/unknown entity" depends on the ERE implementation,
  e.g., it has already seen the entity in a previous request, or it is a test ERE, with a pre-loaded 
  set of canonical entities.
Given 
	a rebuild request was pushed to the ERE and the ERE has responded with a rebuild response
When 
	The ERS pushes a resolution request into the ERE requests channel for the entity E
Then 
	The ERE asynchronously pushes an entity resolution object to the responses channel, within the
	configured system timeout. The response is like 
	[a regular resolution response](ere-ers-interaction-submissions.feature), possibly with a new
	alignment set associated to the requested entity (with respect to the alignments returned before 
	the rebuild).
