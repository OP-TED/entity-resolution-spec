

# Class: Response 


_Root class to represent all the responses sent by the ERE._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [ers:Response](https://data.europa.eu/ers/schema/Response)





```mermaid
 classDiagram
    class Response
    click Response href "../Response/"
      RequestOrResponseMixin <|-- Response
        click RequestOrResponseMixin href "../RequestOrResponseMixin/"
      

      Response <|-- EntityResolutionResponse
        click EntityResolutionResponse href "../EntityResolutionResponse/"
      Response <|-- ErrorResponse
        click ErrorResponse href "../ErrorResponse/"
      Response <|-- RebuildResponse
        click RebuildResponse href "../RebuildResponse/"
      

      Response : metadata
        
      Response : requestId
        
      Response : type
        
      
```





## Inheritance
* **Response** [ [RequestOrResponseMixin](RequestOrResponseMixin.md)]
    * [EntityResolutionResponse](EntityResolutionResponse.md)
    * [ErrorResponse](ErrorResponse.md)
    * [RebuildResponse](RebuildResponse.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [requestId](requestId.md) | 1 <br/> [String](String.md) | A string representing the unique ID of the request this response is about | direct |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | [RequestOrResponseMixin](RequestOrResponseMixin.md) |
| [metadata](metadata.md) | 0..1 <br/> [String](String.md) | An optional arbitrary dictionary of further request metadata | [RequestOrResponseMixin](RequestOrResponseMixin.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:Response |
| native | ers:Response |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Response
description: 'Root class to represent all the responses sent by the ERE.

  '
from_schema: https://data.europa.eu/ers/schema
abstract: true
mixins:
- RequestOrResponseMixin
attributes:
  requestId:
    name: requestId
    description: 'A string representing the unique ID of the request this response
      is about.

      '
    from_schema: https://data.europa.eu/ers/schema
    domain_of:
    - Request
    - Response
    required: true

```
</details>

### Induced

<details>
```yaml
name: Response
description: 'Root class to represent all the responses sent by the ERE.

  '
from_schema: https://data.europa.eu/ers/schema
abstract: true
mixins:
- RequestOrResponseMixin
attributes:
  requestId:
    name: requestId
    description: 'A string representing the unique ID of the request this response
      is about.

      '
    from_schema: https://data.europa.eu/ers/schema
    alias: requestId
    owner: Response
    domain_of:
    - Request
    - Response
    range: string
    required: true
  type:
    name: type
    description: "The type of the request or result.\n\nAs per LinkML specification,\
      \ `designates_type` is used here in order to allow for this\nslot to tell the\
      \ concrete subclass that an instance (such as a JSON object) belongs to.\n\n\
      In other words, a particular request will have `type` set with values like \n\
      `EntityResolutionRequest` or `EntityResolutionResult`\n"
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    designates_type: true
    alias: type
    owner: Response
    domain_of:
    - RequestOrResponseMixin
    - Entity
    range: string
    required: true
  metadata:
    name: metadata
    description: 'An optional arbitrary dictionary of further request metadata.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: metadata
    owner: Response
    domain_of:
    - RequestOrResponseMixin
    range: string

```
</details>