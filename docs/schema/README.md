# ersServiceDataSchema

A LinkML schema for the ERS Services.

URI: https://data.europa.eu/ers/schema

Name: ersServiceDataSchema



## Classes

| Class | Description |
| --- | --- |
| [ClusterRef](ClusterRef.md) | A reference to a cluster to which an entity is deemed to belong, with an asso... |
| [EntityMention](EntityMention.md) | An entity mention is a representation of a real-world entity, as provided by ... |
| [EntityMentionIdentifers](EntityMentionIdentifers.md) | A container that groups the attributes needed to identify an entity mention i... |
| [EREMessage](EREMessage.md) | Root abstraction to represent attributes common to both requests and results |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ERERequest](ERERequest.md) | Root class to represent all the requests sent to the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ResetRequest](ResetRequest.md) | A request to reset all the resolutions computed so far and possibly rebuild t... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EREResponse](EREResponse.md) | Root class to represent all the responses sent by the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ResetResponse](ResetResponse.md) | A response to a `ResetRequest`, confirming that the rebuild process has start... |



## Slots

| Slot | Description |
| --- | --- |
| [clusterId](clusterId.md) | The identifier of the cluster/canonical entity that is considered equivalent ... |
| [clusters](clusters.md) | The set of cluster reference/score pairs representing the candidate clusters |
| [confidenceScore](confidenceScore.md) | A 0-1 value of how confident the ERE is about the equivalence between the sub... |
| [content](content.md) | A code string representing the entity mention details (eg, RDF or XML descrip... |
| [contentType](contentType.md) | A string about the MIME format of `content` (e |
| [entityMention](entityMention.md) | The data about the entity to be resolved |
| [entityType](entityType.md) | A string representing the entity type (based on CET) |
| [ereRequestId](ereRequestId.md) | A string representing the unique ID of an ERE request, or the ID of the reque... |
| [errorDetail](errorDetail.md) | A human readable detailed message about the error that occurred |
| [errorTitle](errorTitle.md) | A human readable brief message about the error that occurred |
| [errorTrace](errorTrace.md) | A string representing a (stack) trace of the error that occurred |
| [errorType](errorType.md) | A string representing the error type, eg, the FQN of the raised exception |
| [excludedClusterIds](excludedClusterIds.md) | When this is present, the resolution must not bin the entity mention into any... |
| [isCanonical](isCanonical.md) | A boolean flag indicating whether the entity mention is to be considered a ca... |
| [maxResultClusters](maxResultClusters.md) | An optional hint to the ERE about the maximum number of clusters to be return... |
| [requestId](requestId.md) | A string representing the unique ID of the request made to the ERS system |
| [sourceId](sourceId.md) | The ID or URI of the ERS client that originated the request |
| [timestamp](timestamp.md) | The time when the message was created |
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
