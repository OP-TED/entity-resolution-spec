

# Class: EntityMentionResolutionResponse 


_An entity resolution response returned by the ERE._

__

_This is basically a list of candidate clusters to which the entity is deemed to be equivalent._

__

_Note that, for the moment, we don't support batch requests. In future, we might support requests_

_with multiple subjects in the `EntityMention` content (eg, RDF with multiple subjects), in which case _

_we might need to return multiple `EntityMentionResolutionResponse` messages, each with additional _

_properties such as `entityIndex` and `totalEntities`._

__





URI: [ere:EntityMentionResolutionResponse](https://data.europa.eu/ers/schema/ere/EntityMentionResolutionResponse)





```mermaid
 classDiagram
    class EntityMentionResolutionResponse
    click EntityMentionResolutionResponse href "../EntityMentionResolutionResponse/"
      EREResponse <|-- EntityMentionResolutionResponse
        click EREResponse href "../EREResponse/"
      
      EntityMentionResolutionResponse : candidates
        
          
    
        
        
        EntityMentionResolutionResponse --> "1..*" ClusterReference : candidates
        click ClusterReference href "../ClusterReference/"
    

        
      EntityMentionResolutionResponse : entityMentionId
        
          
    
        
        
        EntityMentionResolutionResponse --> "1" EntityMentionIdentifier : entityMentionId
        click EntityMentionIdentifier href "../EntityMentionIdentifier/"
    

        
      EntityMentionResolutionResponse : ereRequestId
        
      EntityMentionResolutionResponse : timestamp
        
      EntityMentionResolutionResponse : type
        
      
```





## Inheritance
* [EREMessage](EREMessage.md)
    * [EREResponse](EREResponse.md)
        * **EntityMentionResolutionResponse**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [entityMentionId](entityMentionId.md) | 1 <br/> [EntityMentionIdentifier](EntityMentionIdentifier.md) | The identifier of the entity mention that has been resolved | direct |
| [candidates](candidates.md) | 1..* <br/> [ClusterReference](ClusterReference.md) | The set of cluster reference/score pairs representing the candidate clusters | direct |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | [EREMessage](EREMessage.md) |
| [ereRequestId](ereRequestId.md) | 1 <br/> [String](String.md) | A string representing the unique ID of an ERE request, or the ID of the reque... | [EREMessage](EREMessage.md) |
| [timestamp](timestamp.md) | 0..1 <br/> [Datetime](Datetime.md) | The time when the message was created | [EREMessage](EREMessage.md) |











## Examples

| Value |
| --- |
| {
  "type": "EntityMentionResolutionResponse",
  "entityMentionId": {
    "requestId": "324fs3r345vx",
    "sourceId": "TEDSWS",
    "entityType": "http://www.w3.org/ns/org#Organization"
  },
  "candidates": [
    { 
      "clusterId": "324fs3r345vx-aa32wa",
      "confidenceScore": 0.91
    },
    { 
      "clusterId": "324fs3r345vx-bb45we",
      "confidenceScore": 0.65
    }
  ],
  "timestamp": "2026-01-14T12:34:59Z",
  "ereRequestId": "324fs3r345vx:01"
}
    
 |

## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:EntityMentionResolutionResponse |
| native | ere:EntityMentionResolutionResponse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EntityMentionResolutionResponse
description: "An entity resolution response returned by the ERE.\n\nThis is basically\
  \ a list of candidate clusters to which the entity is deemed to be equivalent.\n\
  \nNote that, for the moment, we don't support batch requests. In future, we might\
  \ support requests\nwith multiple subjects in the `EntityMention` content (eg, RDF\
  \ with multiple subjects), in which case \nwe might need to return multiple `EntityMentionResolutionResponse`\
  \ messages, each with additional \nproperties such as `entityIndex` and `totalEntities`.\n"
examples:
- value: "{\n  \"type\": \"EntityMentionResolutionResponse\",\n  \"entityMentionId\"\
    : {\n    \"requestId\": \"324fs3r345vx\",\n    \"sourceId\": \"TEDSWS\",\n   \
    \ \"entityType\": \"http://www.w3.org/ns/org#Organization\"\n  },\n  \"candidates\"\
    : [\n    { \n      \"clusterId\": \"324fs3r345vx-aa32wa\",\n      \"confidenceScore\"\
    : 0.91\n    },\n    { \n      \"clusterId\": \"324fs3r345vx-bb45we\",\n      \"\
    confidenceScore\": 0.65\n    }\n  ],\n  \"timestamp\": \"2026-01-14T12:34:59Z\"\
    ,\n  \"ereRequestId\": \"324fs3r345vx:01\"\n}\n    \n"
from_schema: https://data.europa.eu/ers/schema/ere
is_a: EREResponse
attributes:
  entityMentionId:
    name: entityMentionId
    description: "The identifier of the entity mention that has been resolved.\n\n\
      This isn't strictly needed, since the `ereRequestId` already links the response\
      \ to \nthe request's entity mention. Yet, it's reported for convenience.\n"
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    domain_of:
    - EntityMentionResolutionResponse
    range: EntityMentionIdentifier
    required: true
  candidates:
    name: candidates
    description: 'The set of cluster reference/score pairs representing the candidate
      clusters

      that the entity mention in the original request could align to (be equivalent
      to).

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    domain_of:
    - EntityMentionResolutionResponse
    range: ClusterReference
    required: true
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: EntityMentionResolutionResponse
description: "An entity resolution response returned by the ERE.\n\nThis is basically\
  \ a list of candidate clusters to which the entity is deemed to be equivalent.\n\
  \nNote that, for the moment, we don't support batch requests. In future, we might\
  \ support requests\nwith multiple subjects in the `EntityMention` content (eg, RDF\
  \ with multiple subjects), in which case \nwe might need to return multiple `EntityMentionResolutionResponse`\
  \ messages, each with additional \nproperties such as `entityIndex` and `totalEntities`.\n"
examples:
- value: "{\n  \"type\": \"EntityMentionResolutionResponse\",\n  \"entityMentionId\"\
    : {\n    \"requestId\": \"324fs3r345vx\",\n    \"sourceId\": \"TEDSWS\",\n   \
    \ \"entityType\": \"http://www.w3.org/ns/org#Organization\"\n  },\n  \"candidates\"\
    : [\n    { \n      \"clusterId\": \"324fs3r345vx-aa32wa\",\n      \"confidenceScore\"\
    : 0.91\n    },\n    { \n      \"clusterId\": \"324fs3r345vx-bb45we\",\n      \"\
    confidenceScore\": 0.65\n    }\n  ],\n  \"timestamp\": \"2026-01-14T12:34:59Z\"\
    ,\n  \"ereRequestId\": \"324fs3r345vx:01\"\n}\n    \n"
from_schema: https://data.europa.eu/ers/schema/ere
is_a: EREResponse
attributes:
  entityMentionId:
    name: entityMentionId
    description: "The identifier of the entity mention that has been resolved.\n\n\
      This isn't strictly needed, since the `ereRequestId` already links the response\
      \ to \nthe request's entity mention. Yet, it's reported for convenience.\n"
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    alias: entityMentionId
    owner: EntityMentionResolutionResponse
    domain_of:
    - EntityMentionResolutionResponse
    range: EntityMentionIdentifier
    required: true
  candidates:
    name: candidates
    description: 'The set of cluster reference/score pairs representing the candidate
      clusters

      that the entity mention in the original request could align to (be equivalent
      to).

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    alias: candidates
    owner: EntityMentionResolutionResponse
    domain_of:
    - EntityMentionResolutionResponse
    range: ClusterReference
    required: true
    multivalued: true
  type:
    name: type
    description: "The type of the request or result.\n\nAs per LinkML specification,\
      \ `designates_type` is used here in order to allow for this\nslot to tell the\
      \ concrete subclass that an instance (such as a JSON object) belongs to.\n\n\
      In other words, a particular request will have `type` set with values like \n\
      `EntityMentionResolutionRequest` or `EntityResolutionResult`\n"
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    designates_type: true
    alias: type
    owner: EntityMentionResolutionResponse
    domain_of:
    - EREMessage
    range: string
    required: true
  ereRequestId:
    name: ereRequestId
    description: 'A string representing the unique ID of an ERE request, or the ID
      of the request a response is about.

      This **is not** the same as `requestId` + `sourceId`.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    alias: ereRequestId
    owner: EntityMentionResolutionResponse
    domain_of:
    - EREMessage
    range: string
    required: true
  timestamp:
    name: timestamp
    description: 'The time when the message was created. Should be in ISO-8601 format.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    alias: timestamp
    owner: EntityMentionResolutionResponse
    domain_of:
    - EREMessage
    range: datetime

```
</details>