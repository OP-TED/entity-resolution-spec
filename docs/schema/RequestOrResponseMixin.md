

# Class: RequestOrResponseMixin 


_Root mixin to represent attributes common to both requests and results._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [ers:RequestOrResponseMixin](https://data.europa.eu/ers/schema/RequestOrResponseMixin)





```mermaid
 classDiagram
    class RequestOrResponseMixin
    click RequestOrResponseMixin href "../RequestOrResponseMixin/"
      RequestOrResponseMixin <|-- Request
        click Request href "../Request/"
      RequestOrResponseMixin <|-- Response
        click Response href "../Response/"
      
      RequestOrResponseMixin : metadata
        
      RequestOrResponseMixin : type
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | direct |
| [metadata](metadata.md) | 0..1 <br/> [String](String.md) | An optional arbitrary dictionary of further request metadata | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Request](Request.md) | Root class to represent all the requests sent to the ERE |
| [Response](Response.md) | Root class to represent all the responses sent by the ERE |









## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:RequestOrResponseMixin |
| native | ers:RequestOrResponseMixin |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RequestOrResponseMixin
description: 'Root mixin to represent attributes common to both requests and results.

  '
from_schema: https://data.europa.eu/ers/schema
abstract: true
mixin: true
attributes:
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
    domain_of:
    - RequestOrResponseMixin
    - Entity
    required: true
  metadata:
    name: metadata
    description: 'An optional arbitrary dictionary of further request metadata.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    domain_of:
    - RequestOrResponseMixin

```
</details>

### Induced

<details>
```yaml
name: RequestOrResponseMixin
description: 'Root mixin to represent attributes common to both requests and results.

  '
from_schema: https://data.europa.eu/ers/schema
abstract: true
mixin: true
attributes:
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
    owner: RequestOrResponseMixin
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
    owner: RequestOrResponseMixin
    domain_of:
    - RequestOrResponseMixin
    range: string

```
</details>