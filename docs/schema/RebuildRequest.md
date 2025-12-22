

# Class: RebuildRequest 


_A request to reset all the resolutions computed so far and rebuild them as _

_requests about old entities arrive again (and build new entities from scratch)._

__

_It is expected that the ERE client re-sends all the entities to be resolved again,_

_using `EntityResolutionRequest` messages exactly as the first time the resolutions _

_were built. This implies the a client like the ERS logs/persists the entities it receives_

_to resolve and also saves manual overriding of ERE results._

__





URI: [ers:RebuildRequest](https://data.europa.eu/ers/schema/RebuildRequest)





```mermaid
 classDiagram
    class RebuildRequest
    click RebuildRequest href "../RebuildRequest/"
      Request <|-- RebuildRequest
        click Request href "../Request/"
      
      RebuildRequest : metadata
        
      RebuildRequest : originator
        
      RebuildRequest : requestId
        
      RebuildRequest : type
        
      
```





## Inheritance
* [Request](Request.md) [ [RequestOrResponseMixin](RequestOrResponseMixin.md)]
    * **RebuildRequest**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [requestId](requestId.md) | 1 <br/> [String](String.md) | A string representing the unique ID of this request | [Request](Request.md) |
| [originator](originator.md) | 1 <br/> [String](String.md) | The ID or URI of the request originator | [Request](Request.md) |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | [RequestOrResponseMixin](RequestOrResponseMixin.md) |
| [metadata](metadata.md) | 0..1 <br/> [String](String.md) | An optional arbitrary dictionary of further request metadata | [RequestOrResponseMixin](RequestOrResponseMixin.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:RebuildRequest |
| native | ers:RebuildRequest |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RebuildRequest
description: "A request to reset all the resolutions computed so far and rebuild them\
  \ as \nrequests about old entities arrive again (and build new entities from scratch).\n\
  \nIt is expected that the ERE client re-sends all the entities to be resolved again,\n\
  using `EntityResolutionRequest` messages exactly as the first time the resolutions\
  \ \nwere built. This implies the a client like the ERS logs/persists the entities\
  \ it receives\nto resolve and also saves manual overriding of ERE results.\n"
from_schema: https://data.europa.eu/ers/schema
is_a: Request

```
</details>

### Induced

<details>
```yaml
name: RebuildRequest
description: "A request to reset all the resolutions computed so far and rebuild them\
  \ as \nrequests about old entities arrive again (and build new entities from scratch).\n\
  \nIt is expected that the ERE client re-sends all the entities to be resolved again,\n\
  using `EntityResolutionRequest` messages exactly as the first time the resolutions\
  \ \nwere built. This implies the a client like the ERS logs/persists the entities\
  \ it receives\nto resolve and also saves manual overriding of ERE results.\n"
from_schema: https://data.europa.eu/ers/schema
is_a: Request
attributes:
  requestId:
    name: requestId
    description: 'A string representing the unique ID of this request.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: requestId
    owner: RebuildRequest
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
    owner: RebuildRequest
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
    owner: RebuildRequest
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
    owner: RebuildRequest
    domain_of:
    - RequestOrResponseMixin
    range: string

```
</details>