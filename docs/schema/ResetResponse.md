

# Class: ResetResponse 


_A response to a `ResetRequest`, confirming that the rebuild process has started._

__

_As for all the requests, this carries the `ereRequestId`, which matches the reset request being_

_acknowledged._

__





URI: [ers:ResetResponse](https://data.europa.eu/ers/schema/ResetResponse)





```mermaid
 classDiagram
    class ResetResponse
    click ResetResponse href "../ResetResponse/"
      EREResponse <|-- ResetResponse
        click EREResponse href "../EREResponse/"
      
      ResetResponse : ereRequestId
        
      ResetResponse : timestamp
        
      ResetResponse : type
        
      
```





## Inheritance
* [EREMessage](EREMessage.md)
    * [EREResponse](EREResponse.md)
        * **ResetResponse**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | [EREMessage](EREMessage.md) |
| [ereRequestId](ereRequestId.md) | 1 <br/> [String](String.md) | A string representing the unique ID of an ERE request, or the ID of the reque... | [EREMessage](EREMessage.md) |
| [timestamp](timestamp.md) | 0..1 <br/> [Datetime](Datetime.md) | The time when the message was created | [EREMessage](EREMessage.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:ResetResponse |
| native | ers:ResetResponse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ResetResponse
description: 'A response to a `ResetRequest`, confirming that the rebuild process
  has started.


  As for all the requests, this carries the `ereRequestId`, which matches the reset
  request being

  acknowledged.

  '
from_schema: https://data.europa.eu/ers/schema
is_a: EREResponse

```
</details>

### Induced

<details>
```yaml
name: ResetResponse
description: 'A response to a `ResetRequest`, confirming that the rebuild process
  has started.


  As for all the requests, this carries the `ereRequestId`, which matches the reset
  request being

  acknowledged.

  '
from_schema: https://data.europa.eu/ers/schema
is_a: EREResponse
attributes:
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
    owner: ResetResponse
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
    owner: ResetResponse
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
    owner: ResetResponse
    domain_of:
    - EREMessage
    range: datetime

```
</details>