

# Class: EREErrorResponse 


_Response sent by the ERE when some error/exception occurs while processing a request._

_For instance, this may happen if the request is malformed or some internal error happens._

__

_The attributes of this class are based on [RFC-9457](https://datatracker.ietf.org/doc/html/rfc9457)._

__





URI: [ere:EREErrorResponse](https://data.europa.eu/ers/schema/ere/EREErrorResponse)





```mermaid
 classDiagram
    class EREErrorResponse
    click EREErrorResponse href "../EREErrorResponse/"
      EREResponse <|-- EREErrorResponse
        click EREResponse href "../EREResponse/"
      
      EREErrorResponse : ereRequestId
        
      EREErrorResponse : errorDetail
        
      EREErrorResponse : errorTitle
        
      EREErrorResponse : errorTrace
        
      EREErrorResponse : errorType
        
      EREErrorResponse : timestamp
        
      EREErrorResponse : type
        
      
```





## Inheritance
* [EREMessage](EREMessage.md)
    * [EREResponse](EREResponse.md)
        * **EREErrorResponse**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [errorType](errorType.md) | 1 <br/> [String](String.md) | A string representing the error type, eg, the FQN of the raised exception | direct |
| [errorTitle](errorTitle.md) | 0..1 <br/> [String](String.md) | A human readable brief message about the error that occurred | direct |
| [errorDetail](errorDetail.md) | 0..1 <br/> [String](String.md) | A human readable detailed message about the error that occurred | direct |
| [errorTrace](errorTrace.md) | 0..1 <br/> [String](String.md) | A string representing a (stack) trace of the error that occurred | direct |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | [EREMessage](EREMessage.md) |
| [ereRequestId](ereRequestId.md) | 1 <br/> [String](String.md) | A string representing the unique ID of an ERE request, or the ID of the reque... | [EREMessage](EREMessage.md) |
| [timestamp](timestamp.md) | 0..1 <br/> [Datetime](Datetime.md) | The time when the message was created | [EREMessage](EREMessage.md) |











## Examples

| Value |
| --- |
| {
  "type": "EREErrorResponse",
  "requestId": "324fs3r345vx",
  "errorType": "ere.exceptions.MalformedRequestError",
  "errorTitle": "The entity data is missing in the request",
  "errorDetail": "The 'entity' attribute is required in EntityMentionResolutionRequest message",
  // Optional and not recommended for production use
  "errorTrace": "Traceback (most recent call last):\n  File \"/app/ere/service.py\", line 45, in process_request\n..."
}
 |

## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:EREErrorResponse |
| native | ere:EREErrorResponse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EREErrorResponse
description: 'Response sent by the ERE when some error/exception occurs while processing
  a request.

  For instance, this may happen if the request is malformed or some internal error
  happens.


  The attributes of this class are based on [RFC-9457](https://datatracker.ietf.org/doc/html/rfc9457).

  '
examples:
- value: "{\n  \"type\": \"EREErrorResponse\",\n  \"requestId\": \"324fs3r345vx\"\
    ,\n  \"errorType\": \"ere.exceptions.MalformedRequestError\",\n  \"errorTitle\"\
    : \"The entity data is missing in the request\",\n  \"errorDetail\": \"The 'entity'\
    \ attribute is required in EntityMentionResolutionRequest message\",\n  // Optional\
    \ and not recommended for production use\n  \"errorTrace\": \"Traceback (most\
    \ recent call last):\\n  File \\\"/app/ere/service.py\\\", line 45, in process_request\\\
    n...\"\n}\n"
from_schema: https://data.europa.eu/ers/schema/ere
is_a: EREResponse
attributes:
  errorType:
    name: errorType
    description: 'A string representing the error type, eg, the FQN of the raised
      exception.


      This corresponds to RFC-9457''s `type`.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    domain_of:
    - EREErrorResponse
    required: true
  errorTitle:
    name: errorTitle
    description: 'A human readable brief message about the error that occurred.


      This corresponds to RFC-9457''s `title`.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    domain_of:
    - EREErrorResponse
  errorDetail:
    name: errorDetail
    description: 'A human readable detailed message about the error that occurred.


      This corresponds to RFC-9457''s `detail`.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    domain_of:
    - EREErrorResponse
  errorTrace:
    name: errorTrace
    description: 'A string representing a (stack) trace of the error that occurred.


      This is optional and typically used for debugging purposes only, since

      exposing this kind of server-side information is a security risk.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    domain_of:
    - EREErrorResponse

```
</details>

### Induced

<details>
```yaml
name: EREErrorResponse
description: 'Response sent by the ERE when some error/exception occurs while processing
  a request.

  For instance, this may happen if the request is malformed or some internal error
  happens.


  The attributes of this class are based on [RFC-9457](https://datatracker.ietf.org/doc/html/rfc9457).

  '
examples:
- value: "{\n  \"type\": \"EREErrorResponse\",\n  \"requestId\": \"324fs3r345vx\"\
    ,\n  \"errorType\": \"ere.exceptions.MalformedRequestError\",\n  \"errorTitle\"\
    : \"The entity data is missing in the request\",\n  \"errorDetail\": \"The 'entity'\
    \ attribute is required in EntityMentionResolutionRequest message\",\n  // Optional\
    \ and not recommended for production use\n  \"errorTrace\": \"Traceback (most\
    \ recent call last):\\n  File \\\"/app/ere/service.py\\\", line 45, in process_request\\\
    n...\"\n}\n"
from_schema: https://data.europa.eu/ers/schema/ere
is_a: EREResponse
attributes:
  errorType:
    name: errorType
    description: 'A string representing the error type, eg, the FQN of the raised
      exception.


      This corresponds to RFC-9457''s `type`.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    alias: errorType
    owner: EREErrorResponse
    domain_of:
    - EREErrorResponse
    range: string
    required: true
  errorTitle:
    name: errorTitle
    description: 'A human readable brief message about the error that occurred.


      This corresponds to RFC-9457''s `title`.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    alias: errorTitle
    owner: EREErrorResponse
    domain_of:
    - EREErrorResponse
    range: string
  errorDetail:
    name: errorDetail
    description: 'A human readable detailed message about the error that occurred.


      This corresponds to RFC-9457''s `detail`.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    alias: errorDetail
    owner: EREErrorResponse
    domain_of:
    - EREErrorResponse
    range: string
  errorTrace:
    name: errorTrace
    description: 'A string representing a (stack) trace of the error that occurred.


      This is optional and typically used for debugging purposes only, since

      exposing this kind of server-side information is a security risk.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    alias: errorTrace
    owner: EREErrorResponse
    domain_of:
    - EREErrorResponse
    range: string
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
    owner: EREErrorResponse
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
    owner: EREErrorResponse
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
    owner: EREErrorResponse
    domain_of:
    - EREMessage
    range: datetime

```
</details>