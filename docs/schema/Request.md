

# Class: Request 


_Root class to represent all the requests sent to the ERE._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [ers:Request](https://data.europa.eu/ers/schema/Request)





```mermaid
 classDiagram
    class Request
    click Request href "../Request/"
      RequestOrResponseMixin <|-- Request
        click RequestOrResponseMixin href "../RequestOrResponseMixin/"
      

      Request <|-- EntityResolutionRequest
        click EntityResolutionRequest href "../EntityResolutionRequest/"
      Request <|-- RebuildRequest
        click RebuildRequest href "../RebuildRequest/"
      

      Request : metadata
        
      Request : originator
        
      Request : requestId
        
      Request : type
        
      
```





## Inheritance
* **Request** [ [RequestOrResponseMixin](RequestOrResponseMixin.md)]
    * [EntityResolutionRequest](EntityResolutionRequest.md)
    * [RebuildRequest](RebuildRequest.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [requestId](requestId.md) | 1 <br/> [String](String.md) | A string representing the unique ID of this request | direct |
| [originator](originator.md) | 1 <br/> [String](String.md) | The ID or URI of the request originator | direct |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | [RequestOrResponseMixin](RequestOrResponseMixin.md) |
| [metadata](metadata.md) | 0..1 <br/> [String](String.md) | An optional arbitrary dictionary of further request metadata | [RequestOrResponseMixin](RequestOrResponseMixin.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:Request |
| native | ers:Request |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Request
description: 'Root class to represent all the requests sent to the ERE.

  '
from_schema: https://data.europa.eu/ers/schema
abstract: true
mixins:
- RequestOrResponseMixin
attributes:
  requestId:
    name: requestId
    description: 'A string representing the unique ID of this request.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    domain_of:
    - Request
    - Response
    required: true
  originator:
    name: originator
    description: 'The ID or URI of the request originator.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    domain_of:
    - Request
    required: true

```
</details>

### Induced

<details>
```yaml
name: Request
description: 'Root class to represent all the requests sent to the ERE.

  '
from_schema: https://data.europa.eu/ers/schema
abstract: true
mixins:
- RequestOrResponseMixin
attributes:
  requestId:
    name: requestId
    description: 'A string representing the unique ID of this request.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: requestId
    owner: Request
    domain_of:
    - Request
    - Response
    range: string
    required: true
  originator:
    name: originator
    description: 'The ID or URI of the request originator.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: originator
    owner: Request
    domain_of:
    - Request
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
    owner: Request
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
    owner: Request
    domain_of:
    - RequestOrResponseMixin
    range: string

```
</details>