Feature: ERE/ERS interaction upon rebuild requests

  The ERE replies to a full rebuild request with an acknowledgement response.
	
	After that, past resolutions are possibly recomputed. Since this is optional and implementation-dependent,
	we don't specifically test it here, and possibly, it has to be an implementation-level test.
	
	However, the ERE must remember excluded clusters across rebuilds, so this is covered in a scenario below.
	
  TODO: per-type rebuild requests.


Scenario: The ERE acknowledges a rebuild request

  Upon a full rebuild request pushed to the ERE, this asynchronously replies with a response that
	indicates the request has been received and the internal state has been reset. 
When 
	The ERS pushes an instance of `FullBuildRequest` into the requests channel
Then 
	The ERE asynchronously pushes an instance of `FullRebuildResponse` to the rebuild responses channel.
	
	As for all responses, this has `ereRequestId` se to the ERE request ID, and `type` set to `FullRebuildResponse`.

	
Scenario: The ERE keeps resolving entities as usually after a rebuild request

	Note that, as in other tests, the exact meaning of "known/unknown entity" depends on the ERE implementation, see
	the ERE contract section on full rebuilds.
Given 
	a rebuild request was pushed to the ERE and the ERE has responded with a rebuild response
When 
	The ERS pushes a resolution request into the ERE requests channel for the entity E
Then 
	The ERE asynchronously pushes an entity resolution object to the responses channel, within the
	configured system timeout. The response is like 
	[a regular resolution response](ere-ers-common-cases.feature), possibly with a new
	set of cluster references.


Scenario: Rejected clusters are preserved across full rebuilds

Given
  The ERE has received a resolution request for an entity E, which excludes
  a set `R[]` of cluster IDs
And
  The ERE has replied to the initial request
And
  A `FullBuildRequest` has been pushed since the previous resolution
When
  A new resolution about E is sent that contains no excluded clusters
Then
  The ERE response after a full rebuild doesn't contain any cluster ID in R[].