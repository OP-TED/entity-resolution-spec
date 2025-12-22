# ersServiceDataSchema

A LinkML schema for the ERS Services.

URI: https://data.europa.eu/ers/schema

Name: ersServiceDataSchema



## Classes

| Class | Description |
| --- | --- |
| [Entity](Entity.md) | An entity is a representation of a real-world entity, as provided by the ERS |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CanonicalEntity](CanonicalEntity.md) | A canonical entity is an entity that the ERE has created during the resolutio... |
| [Request](Request.md) | Root class to represent all the requests sent to the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityResolutionRequest](EntityResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RebuildRequest](RebuildRequest.md) | A request to reset all the resolutions computed so far and rebuild them as  |
| [RequestOrResponseMixin](RequestOrResponseMixin.md) | Root mixin to represent attributes common to both requests and results |
| [Response](Response.md) | Root class to represent all the responses sent by the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityResolutionResponse](EntityResolutionResponse.md) | An entity resolution response sent by the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ErrorResponse](ErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RebuildResponse](RebuildResponse.md) | A response to a `RebuildRequest`, confirming that the rebuild process has sta... |



## Slots

| Slot | Description |
| --- | --- |
| [canonicalEntity](canonicalEntity.md) | The canonical entity that the ERE has associated to the original entity |
| [confidenceLevel](confidenceLevel.md) | A 0-1 value of how confident the ERE is about associating the original entity |
| [entity](entity.md) | The data about the entity to be resolved |
| [entityData](entityData.md) | A code string representing the entity details (eg, RDF description) |
| [entityDataFormat](entityDataFormat.md) | A string about the MIME format of `entityData` (e |
| [errorDetail](errorDetail.md) | A human readable detailed message about the error that occurred |
| [errorTitle](errorTitle.md) | A human readable brief message about the error that occurred |
| [errorTrace](errorTrace.md) | A string representing a (stack) trace of the error that occurred |
| [errorType](errorType.md) | A string representing the error type, eg, the FQN of the raised exception |
| [id](id.md) | A string containing the entity ID or URI (set by the ERS or, for canonical en... |
| [metadata](metadata.md) | An optional arbitrary dictionary of further request metadata |
| [originator](originator.md) | The ID or URI of the request originator |
| [requestId](requestId.md) | A string representing the unique ID of this request |
| [sourceEntityId](sourceEntityId.md) | The ID or URI of the original entity that has been resolved |
| [type](type.md) | The type of the request or result |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
