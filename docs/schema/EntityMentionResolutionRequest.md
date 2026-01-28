

# Class: EntityMentionResolutionRequest 


_An entity resolution request sent to the ERE, containing the entity to be resolved._

__





URI: [ers:EntityMentionResolutionRequest](https://data.europa.eu/ers/schema/EntityMentionResolutionRequest)





```mermaid
 classDiagram
    class EntityMentionResolutionRequest
    click EntityMentionResolutionRequest href "../EntityMentionResolutionRequest/"
      EntityMentionIdentifers <|-- EntityMentionResolutionRequest
        click EntityMentionIdentifers href "../EntityMentionIdentifers/"
      ERERequest <|-- EntityMentionResolutionRequest
        click ERERequest href "../ERERequest/"
      
      EntityMentionResolutionRequest : entityMention
        
          
    
        
        
        EntityMentionResolutionRequest --> "1" EntityMention : entityMention
        click EntityMention href "../EntityMention/"
    

        
      EntityMentionResolutionRequest : entityType
        
      EntityMentionResolutionRequest : ereRequestId
        
      EntityMentionResolutionRequest : excludedClusterIds
        
      EntityMentionResolutionRequest : requestId
        
      EntityMentionResolutionRequest : sourceId
        
      EntityMentionResolutionRequest : timestamp
        
      EntityMentionResolutionRequest : type
        
      
```





## Inheritance
* [EREMessage](EREMessage.md)
    * [ERERequest](ERERequest.md)
        * **EntityMentionResolutionRequest** [ [EntityMentionIdentifers](EntityMentionIdentifers.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [entityMention](entityMention.md) | 1 <br/> [EntityMention](EntityMention.md) | The data about the entity to be resolved | direct |
| [excludedClusterIds](excludedClusterIds.md) | * <br/> [String](String.md) | When this is present, the resolution must not bin the entity mention into any... | direct |
| [sourceId](sourceId.md) | 1 <br/> [String](String.md) | The ID or URI of the ERS client that originated the request | [EntityMentionIdentifers](EntityMentionIdentifers.md) |
| [requestId](requestId.md) | 1 <br/> [String](String.md) | A string representing the unique ID of the request made to the ERS system | [EntityMentionIdentifers](EntityMentionIdentifers.md) |
| [entityType](entityType.md) | 1 <br/> [String](String.md) | A string representing the entity type (based on CET) | [EntityMentionIdentifers](EntityMentionIdentifers.md) |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | [EREMessage](EREMessage.md) |
| [ereRequestId](ereRequestId.md) | 1 <br/> [String](String.md) | A string representing the unique ID of an ERE request, or the ID of the reque... | [EREMessage](EREMessage.md) |
| [timestamp](timestamp.md) | 0..1 <br/> [Datetime](Datetime.md) | The time when the message was created | [EREMessage](EREMessage.md) |











## Examples

| Value |
| --- |
| {
  "type": "EntityMentionResolutionRequest",
  "requestId": "324fs3r345vx",
  "sourceId": "TEDSWS",
  "entityType": "http://www.w3.org/ns/org#Organization",
  "entityMention": 
  { 
    "content": "epd:ent005 a org:Organization; ...   cccev:telephone \"+44 1924306780\" .",
    "contentType": "text/turtle"
  },
  "timestamp": "2026-01-14T12:34:56Z",
  "maxResultClusters": 5, // to limit the response size
  // As said, we need this internal ID and it can be auto-generated (eg, with UUIDs)
  "ereRequestId": "324fs3r345vx:01"
}
 |
| {
  "type": "EntityMentionResolutionRequest",
  "requestId": "324fs3r345vxab",
  "sourceId": "TEDSWS",
  "entityType": "http://www.w3.org/ns/org#Organization",
  "entityMention": 
  { 
    "content": "epd:ent005 a org:Organization; ...   cccev:telephone \"+44 1924306780\" .",
    "contentType": "text/turtle"
  },
  "excludedClusterIds": [
    "324fs3r345vx-bb45we",
    "324fs3r345vx-cc67ui"
  ],
  "timestamp": "2026-01-14T12:40:56Z",
  "ereRequestId": "324fs3r345vxab:01"
}
 |

## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:EntityMentionResolutionRequest |
| native | ers:EntityMentionResolutionRequest |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EntityMentionResolutionRequest
description: 'An entity resolution request sent to the ERE, containing the entity
  to be resolved.

  '
examples:
- value: "{\n  \"type\": \"EntityMentionResolutionRequest\",\n  \"requestId\": \"\
    324fs3r345vx\",\n  \"sourceId\": \"TEDSWS\",\n  \"entityType\": \"http://www.w3.org/ns/org#Organization\"\
    ,\n  \"entityMention\": \n  { \n    \"content\": \"epd:ent005 a org:Organization;\
    \ ...   cccev:telephone \\\"+44 1924306780\\\" .\",\n    \"contentType\": \"text/turtle\"\
    \n  },\n  \"timestamp\": \"2026-01-14T12:34:56Z\",\n  \"maxResultClusters\": 5,\
    \ // to limit the response size\n  // As said, we need this internal ID and it\
    \ can be auto-generated (eg, with UUIDs)\n  \"ereRequestId\": \"324fs3r345vx:01\"\
    \n}\n"
  description: a regular request
- value: "{\n  \"type\": \"EntityMentionResolutionRequest\",\n  \"requestId\": \"\
    324fs3r345vxab\",\n  \"sourceId\": \"TEDSWS\",\n  \"entityType\": \"http://www.w3.org/ns/org#Organization\"\
    ,\n  \"entityMention\": \n  { \n    \"content\": \"epd:ent005 a org:Organization;\
    \ ...   cccev:telephone \\\"+44 1924306780\\\" .\",\n    \"contentType\": \"text/turtle\"\
    \n  },\n  \"excludedClusterIds\": [\n    \"324fs3r345vx-bb45we\",\n    \"324fs3r345vx-cc67ui\"\
    \n  ],\n  \"timestamp\": \"2026-01-14T12:40:56Z\",\n  \"ereRequestId\": \"324fs3r345vxab:01\"\
    \n}\n"
  description: a re-rebuild request (ie, carrying a rejection list)
from_schema: https://data.europa.eu/ers/schema
is_a: ERERequest
mixins:
- EntityMentionIdentifers
attributes:
  entityMention:
    name: entityMention
    description: 'The data about the entity to be resolved. Note that, at least for
      the moment, we don''t support

      batch requests, so this property is single-valued.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    domain_of:
    - EntityMentionResolutionRequest
    range: EntityMention
    required: true
  excludedClusterIds:
    name: excludedClusterIds
    description: "When this is present, the resolution must not bin the entity mention\
      \ into any of the\nlisted clusters. This can be used to reject a previous resolution\
      \ proposed by the ERE.\n\nThe exact reaction to this is implementation dependent.\
      \ In the simplest case, the ERE\nmight just create a singleton cluster with\
      \ this entity as member. In a more advanced \ncase, it might recompute the similarity\
      \ with more advanced algorithms or use updated\ndata.\n\nTODO: Can this be revised?\
      \ What does it happen if an exclusion was made by mistake?\n"
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    domain_of:
    - EntityMentionResolutionRequest
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: EntityMentionResolutionRequest
description: 'An entity resolution request sent to the ERE, containing the entity
  to be resolved.

  '
examples:
- value: "{\n  \"type\": \"EntityMentionResolutionRequest\",\n  \"requestId\": \"\
    324fs3r345vx\",\n  \"sourceId\": \"TEDSWS\",\n  \"entityType\": \"http://www.w3.org/ns/org#Organization\"\
    ,\n  \"entityMention\": \n  { \n    \"content\": \"epd:ent005 a org:Organization;\
    \ ...   cccev:telephone \\\"+44 1924306780\\\" .\",\n    \"contentType\": \"text/turtle\"\
    \n  },\n  \"timestamp\": \"2026-01-14T12:34:56Z\",\n  \"maxResultClusters\": 5,\
    \ // to limit the response size\n  // As said, we need this internal ID and it\
    \ can be auto-generated (eg, with UUIDs)\n  \"ereRequestId\": \"324fs3r345vx:01\"\
    \n}\n"
  description: a regular request
- value: "{\n  \"type\": \"EntityMentionResolutionRequest\",\n  \"requestId\": \"\
    324fs3r345vxab\",\n  \"sourceId\": \"TEDSWS\",\n  \"entityType\": \"http://www.w3.org/ns/org#Organization\"\
    ,\n  \"entityMention\": \n  { \n    \"content\": \"epd:ent005 a org:Organization;\
    \ ...   cccev:telephone \\\"+44 1924306780\\\" .\",\n    \"contentType\": \"text/turtle\"\
    \n  },\n  \"excludedClusterIds\": [\n    \"324fs3r345vx-bb45we\",\n    \"324fs3r345vx-cc67ui\"\
    \n  ],\n  \"timestamp\": \"2026-01-14T12:40:56Z\",\n  \"ereRequestId\": \"324fs3r345vxab:01\"\
    \n}\n"
  description: a re-rebuild request (ie, carrying a rejection list)
from_schema: https://data.europa.eu/ers/schema
is_a: ERERequest
mixins:
- EntityMentionIdentifers
attributes:
  entityMention:
    name: entityMention
    description: 'The data about the entity to be resolved. Note that, at least for
      the moment, we don''t support

      batch requests, so this property is single-valued.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: entityMention
    owner: EntityMentionResolutionRequest
    domain_of:
    - EntityMentionResolutionRequest
    range: EntityMention
    required: true
  excludedClusterIds:
    name: excludedClusterIds
    description: "When this is present, the resolution must not bin the entity mention\
      \ into any of the\nlisted clusters. This can be used to reject a previous resolution\
      \ proposed by the ERE.\n\nThe exact reaction to this is implementation dependent.\
      \ In the simplest case, the ERE\nmight just create a singleton cluster with\
      \ this entity as member. In a more advanced \ncase, it might recompute the similarity\
      \ with more advanced algorithms or use updated\ndata.\n\nTODO: Can this be revised?\
      \ What does it happen if an exclusion was made by mistake?\n"
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: excludedClusterIds
    owner: EntityMentionResolutionRequest
    domain_of:
    - EntityMentionResolutionRequest
    range: string
    multivalued: true
  sourceId:
    name: sourceId
    description: "The ID or URI of the ERS client that originated the request. This\
      \ identifies an application or a \nperson accessing the ERS system.\n"
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: sourceId
    owner: EntityMentionResolutionRequest
    domain_of:
    - EntityMentionIdentifers
    range: string
    required: true
  requestId:
    name: requestId
    description: "A string representing the unique ID of the request made to the ERS\
      \ system. In general, this is unique\nonly within the scope of the source and\
      \ the entity type, ie, within `sourceId` and `entityType`. \n\nMoreover, this\
      \ is **not** the same as `ereRequestId`, which instead, is internal to the ERE\
      \ and is \nused to match responses to requests.\n"
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: requestId
    owner: EntityMentionResolutionRequest
    domain_of:
    - EntityMentionIdentifers
    range: string
    required: true
  entityType:
    name: entityType
    description: "A string representing the entity type (based on CET). This is typically\
      \ a URI.\n\nNote that this is at this level, and not at `EntityMention`, since,\
      \ as said above, \nit's needed to identify the entity, even when its content\
      \ is not present. For the same\nreason, it's used both for `EREResolutionRequest`\
      \ and `EREResolutionResponse` messages., \n"
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: entityType
    owner: EntityMentionResolutionRequest
    domain_of:
    - EntityMentionIdentifers
    range: string
    required: true
  type:
    name: type
    description: "The type of the request or result.\n\nAs per LinkML specification,\
      \ `designates_type` is used here in order to allow for this\nslot to tell the\
      \ concrete subclass that an instance (such as a JSON object) belongs to.\n\n\
      In other words, a particular request will have `type` set with values like \n\
      `EntityMentionResolutionRequest` or `EntityResolutionResult`\n"
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    designates_type: true
    alias: type
    owner: EntityMentionResolutionRequest
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
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: ereRequestId
    owner: EntityMentionResolutionRequest
    domain_of:
    - EREMessage
    range: string
    required: true
  timestamp:
    name: timestamp
    description: 'The time when the message was created. Should be in ISO-8601 format.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: timestamp
    owner: EntityMentionResolutionRequest
    domain_of:
    - EREMessage
    range: datetime

```
</details>