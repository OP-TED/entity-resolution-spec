

# Class: FullRebuildResponse 


_A response to a `FullRebuildRequest`, confirming that the rebuild process has started._

__

_This should carry the `requestId` attribute._

__





URI: [ers:FullRebuildResponse](https://data.europa.eu/ers/schema/FullRebuildResponse)





```mermaid
 classDiagram
    class FullRebuildResponse
    click FullRebuildResponse href "../FullRebuildResponse/"
      EREResponse <|-- FullRebuildResponse
        click EREResponse href "../EREResponse/"
      
      FullRebuildResponse : metadata
        
      FullRebuildResponse : requestId
        
      FullRebuildResponse : type
        
      
```





## Inheritance
* [EREResponse](EREResponse.md) [ [ERECommunicationArtefact](ERECommunicationArtefact.md)]
    * **FullRebuildResponse**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [requestId](requestId.md) | 1 <br/> [String](String.md) | A string representing the unique ID of the request this response is about | [EREResponse](EREResponse.md) |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | [ERECommunicationArtefact](ERECommunicationArtefact.md) |
| [metadata](metadata.md) | 0..1 <br/> [String](String.md) | An optional arbitrary dictionary of further request metadata | [ERECommunicationArtefact](ERECommunicationArtefact.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:FullRebuildResponse |
| native | ers:FullRebuildResponse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FullRebuildResponse
description: 'A response to a `FullRebuildRequest`, confirming that the rebuild process
  has started.


  This should carry the `requestId` attribute.

  '
from_schema: https://data.europa.eu/ers/schema
is_a: EREResponse

```
</details>

### Induced

<details>
```yaml
name: FullRebuildResponse
description: 'A response to a `FullRebuildRequest`, confirming that the rebuild process
  has started.


  This should carry the `requestId` attribute.

  '
from_schema: https://data.europa.eu/ers/schema
is_a: EREResponse
attributes:
  requestId:
    name: requestId
    description: 'A string representing the unique ID of the request this response
      is about.

      '
    from_schema: https://data.europa.eu/ers/schema
    alias: requestId
    owner: FullRebuildResponse
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
    owner: FullRebuildResponse
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
    owner: FullRebuildResponse
    domain_of:
    - ERECommunicationArtefact
    range: string

```
</details>