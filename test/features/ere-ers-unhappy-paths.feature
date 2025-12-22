Feature: ERE/ERS interaction upon rebuild requests

This feature describes what happens in cases like malformed requests, system errors, or alike

Scenario: The ERE replies with an error response to a malformed request

When 
	The ERS pushes the malformed request into the ERE requests channel
Then 
	The ERE asynchronously pushes an error response to the responses channel that looks like:

	requestId: the ID of the malformed request
	errorMessage: a description of the error
	type: "ErrorResponse" # JSON object property, matches the LinkML class in the service schema.
