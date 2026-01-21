# ersServiceDataSchema

A LinkML schema for the ERS Services.

URI: https://data.europa.eu/ers/schema

Name: ersServiceDataSchema



## Classes

| Class | Description |
| --- | --- |
| [AlignmentLink](AlignmentLink.md) | An alignment link representing a possible equivalence between an entity menti... |
| [AlignmentLinkSet](AlignmentLinkSet.md) | A set of alignment links to a referred entity |
| [EntityMention](EntityMention.md) | An entity mention is a representation of a real-world entity in the ERS |
| [ERECommunicationArtefact](ERECommunicationArtefact.md) | Root abstraction to represent attributes common to both requests and results |
| [ERERequest](ERERequest.md) | Root class to represent all the requests sent to the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FullRebuildRequest](FullRebuildRequest.md) | A request to reset all the resolutions computed so far and rebuild them as  |
| [EREResponse](EREResponse.md) | Root class to represent all the responses sent by the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response sent by the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FullRebuildResponse](FullRebuildResponse.md) | A response to a `FullRebuildRequest`, confirming that the rebuild process has... |



## Slots

| Slot | Description |
| --- | --- |
| [alignmentLinkSet](alignmentLinkSet.md) | The set of alignment links representing the candidate canonical entities/clus... |
| [alignmentOptions](alignmentOptions.md) | A list of possible matches (alignment links) between the subject entity menti... |
| [canonicalIdentifier](canonicalIdentifier.md) | The identifier of the cluster/canonical entity that is considered equivalent ... |
| [confidenceScore](confidenceScore.md) | A 0-1 value of how confident the ERE is about the equivalence between the sub... |
| [creationTime](creationTime.md) | The timestamp when the request was created |
| [datFormat](datFormat.md) | A string about the MIME format of `payload` (e |
| [draftCanonicalIdentifier](draftCanonicalIdentifier.md) | An optional URI representing a draft canonical identifier for the entity ment... |
| [entityMention](entityMention.md) | The data about the entity to be resolved |
| [entityType](entityType.md) | A string representing the entity type URI (based on CET) |
| [errorDetail](errorDetail.md) | A human readable detailed message about the error that occurred |
| [errorTitle](errorTitle.md) | A human readable brief message about the error that occurred |
| [errorTrace](errorTrace.md) | A string representing a (stack) trace of the error that occurred |
| [errorType](errorType.md) | A string representing the error type, eg, the FQN of the raised exception |
| [identifier](identifier.md) | An URI identifying the entity |
| [jsonRepresentation](jsonRepresentation.md) | An optional JSON representation of the entity, which is usually achieved from... |
| [metadata](metadata.md) | An optional arbitrary dictionary of further request metadata |
| [originator](originator.md) | The ID or URI of the request originator |
| [payload](payload.md) | A code string representing the entity details (eg, RDF description) |
| [rejectedCanonicalIdentifiers](rejectedCanonicalIdentifiers.md) | When this is present, the request is a refresh request: it is asking that the... |
| [requestId](requestId.md) | A string representing the unique ID of this request |
| [subjectEntityMentionIdentifier](subjectEntityMentionIdentifier.md) | The identifier of the entity mention that is the subject of these alignment l... |
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
