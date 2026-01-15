# ERS

Mapping Workbench project v2

URI: http://publications.europa.eu/ontology/ers

Name: ERS



## Classes

| Class | Description |
| --- | --- |
| [AlignmentLink](AlignmentLink.md) | Represents either manual or automatic alignment |
| [AlignmentLinkSet](AlignmentLinkSet.md) | The alignment link set is a collection of alignment links that form a set of ... |
| [CanonicalEntity](CanonicalEntity.md) | No two links can exist for the same entity mention within the entire store |
| [CanonicalEntityRegistry](CanonicalEntityRegistry.md) |  |
| [CommunicationArtefact](CommunicationArtefact.md) |  |
| [Decission](Decission.md) | The decision object captures what (integration) action shall be taken given a... |
| [DecissionsStore](DecissionsStore.md) | Working store Stores data for knowing the choice context training machine lea... |
| [EntityMention](EntityMention.md) |  |
| [RequestRecord](RequestRecord.md) | This is stored in the system of records |
| [SystemOfRequestRecords](SystemOfRequestRecords.md) |  |



## Slots

| Slot | Description |
| --- | --- |
| [acceptedAlignment](acceptedAlignment.md) |  |
| [acceptedLink](acceptedLink.md) |  |
| [alignmentOption](alignmentOption.md) |  |
| [canonicalEntity](canonicalEntity.md) |  |
| [canonicalIdentifier](canonicalIdentifier.md) |  |
| [chosenAlternativeLink](chosenAlternativeLink.md) |  |
| [confidenceScore](confidenceScore.md) | This indicates a confidence of belonging to a cluster:0 - 1 :automatically co... |
| [created](created.md) |  |
| [createdAt](createdAt.md) |  |
| [dataFormat](dataFormat.md) |  |
| [decision](decision.md) |  |
| [decisionAction](decisionAction.md) |  |
| [decisionContext](decisionContext.md) |  |
| [decisionStatus](decisionStatus.md) |  |
| [defaultAlignment](defaultAlignment.md) |  |
| [entityMention](entityMention.md) |  |
| [identifier](identifier.md) |  |
| [indetifier](indetifier.md) |  |
| [mentionIdentifier](mentionIdentifier.md) |  |
| [mentionLink](mentionLink.md) |  |
| [originatorIdentifier](originatorIdentifier.md) |  |
| [parsedDataRepresentation](parsedDataRepresentation.md) | data are parsed/computed before storage in the ERS |
| [payload](payload.md) |  |
| [record](record.md) |  |
| [requestIdentifier](requestIdentifier.md) |  |
| [subjectMentionIdentifier](subjectMentionIdentifier.md) |  |
| [type](type.md) |  |
| [updatedAt](updatedAt.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [DecisionAction](DecisionAction.md) |  |
| [DecissionStatus](DecissionStatus.md) |  |
| [EntityType](EntityType.md) |  |


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
