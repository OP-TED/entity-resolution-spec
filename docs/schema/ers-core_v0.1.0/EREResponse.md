

# Class: EREResponse 


_Root class to represent all the responses sent by the ERE._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [ers:EREResponse](https://data.europa.eu/ers/schema/EREResponse)





```mermaid
 classDiagram
    class EREResponse
    click EREResponse href "../EREResponse/"
      ERECommunicationArtefact <|-- EREResponse
        click ERECommunicationArtefact href "../ERECommunicationArtefact/"
      

      EREResponse <|-- EntityMentionResolutionResponse
        click EntityMentionResolutionResponse href "../EntityMentionResolutionResponse/"
      EREResponse <|-- EREErrorResponse
        click EREErrorResponse href "../EREErrorResponse/"
      EREResponse <|-- FullRebuildResponse
        click FullRebuildResponse href "../FullRebuildResponse/"
      

      EREResponse : metadata
        
      EREResponse : requestId
        
      EREResponse : type
        
      
```





## Inheritance
* **EREResponse** [ [ERECommunicationArtefact](ERECommunicationArtefact.md)]
    * [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md)
    * [EREErrorResponse](EREErrorResponse.md)
    * [FullRebuildResponse](FullRebuildResponse.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [requestId](requestId.md) | 1 <br/> [String](String.md) | A string representing the unique ID of the request this response is about | direct |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | [ERECommunicationArtefact](ERECommunicationArtefact.md) |
| [metadata](metadata.md) | 0..1 <br/> [String](String.md) | An optional arbitrary dictionary of further request metadata | [ERECommunicationArtefact](ERECommunicationArtefact.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:EREResponse |
| native | ers:EREResponse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EREResponse
description: 'Root class to represent all the responses sent by the ERE.

  '
from_schema: https://data.europa.eu/ers/schema
abstract: true
mixins:
- ERECommunicationArtefact
attributes:
  requestId:
    name: requestId
    description: 'A string representing the unique ID of the request this response
      is about.

      '
    from_schema: https://data.europa.eu/ers/schema
    domain_of:
    - ERERequest
    - EREResponse
    required: true

```
</details>

### Induced

<details>
```yaml
name: EREResponse
description: 'Root class to represent all the responses sent by the ERE.

  '
from_schema: https://data.europa.eu/ers/schema
abstract: true
mixins:
- ERECommunicationArtefact
attributes:
  requestId:
    name: requestId
    description: 'A string representing the unique ID of the request this response
      is about.

      '
    from_schema: https://data.europa.eu/ers/schema
    alias: requestId
    owner: EREResponse
    domain_of:
    - ERERequest
    - EREResponse
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
    owner: EREResponse
    domain_of:
    - ERECommunicationArtefact
    - EntityMention
    range: string
    required: true
  metadata:
    name: metadata
    description: 'An optional arbitrary dictionary of further request metadata.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: metadata
    owner: EREResponse
    domain_of:
    - ERECommunicationArtefact
    range: string

```
</details>