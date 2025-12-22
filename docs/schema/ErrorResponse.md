

# Class: ErrorResponse 


_Response sent by the ERE when some error/exception occurs while processing a request._

_For instance, this may happen if the request is malformed or some internal error happens._

__

_The attributes of this class are based on [RFC-9457](https://datatracker.ietf.org/doc/html/rfc9457)._

__





URI: [ers:ErrorResponse](https://data.europa.eu/ers/schema/ErrorResponse)





```mermaid
 classDiagram
    class ErrorResponse
    click ErrorResponse href "../ErrorResponse/"
      Response <|-- ErrorResponse
        click Response href "../Response/"
      
      ErrorResponse : errorDetail
        
      ErrorResponse : errorTitle
        
      ErrorResponse : errorTrace
        
      ErrorResponse : errorType
        
      ErrorResponse : metadata
        
      ErrorResponse : requestId
        
      ErrorResponse : type
        
      
```





## Inheritance
* [Response](Response.md) [ [RequestOrResponseMixin](RequestOrResponseMixin.md)]
    * **ErrorResponse**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [errorType](errorType.md) | 1 <br/> [String](String.md) | A string representing the error type, eg, the FQN of the raised exception | direct |
| [errorTitle](errorTitle.md) | 0..1 <br/> [String](String.md) | A human readable brief message about the error that occurred | direct |
| [errorDetail](errorDetail.md) | 0..1 <br/> [String](String.md) | A human readable detailed message about the error that occurred | direct |
| [errorTrace](errorTrace.md) | 0..1 <br/> [String](String.md) | A string representing a (stack) trace of the error that occurred | direct |
| [requestId](requestId.md) | 1 <br/> [String](String.md) | A string representing the unique ID of the request this response is about | [Response](Response.md) |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | [RequestOrResponseMixin](RequestOrResponseMixin.md) |
| [metadata](metadata.md) | 0..1 <br/> [String](String.md) | An optional arbitrary dictionary of further request metadata | [RequestOrResponseMixin](RequestOrResponseMixin.md) |











## Examples

| Value |
| --- |
| {
  "type": "ErrorResponse",
  "requestId": "324fs3r345vx",
  "errorType": "ere.exceptions.MalformedRequestError",
  "errorTitle": "The entity data is missing in the request",
  "errorDetail": "The 'entity' attribute is required in EntityResolutionRequest message",
  // Optional and not recommended for production use
  "errorTrace": "Traceback (most recent call last):\n  File \"/app/ere/service.py\", line 45, in process_request\n..."
}
 |

## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:ErrorResponse |
| native | ers:ErrorResponse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ErrorResponse
description: 'Response sent by the ERE when some error/exception occurs while processing
  a request.

  For instance, this may happen if the request is malformed or some internal error
  happens.


  The attributes of this class are based on [RFC-9457](https://datatracker.ietf.org/doc/html/rfc9457).

  '
examples:
- value: "{\n  \"type\": \"ErrorResponse\",\n  \"requestId\": \"324fs3r345vx\",\n\
    \  \"errorType\": \"ere.exceptions.MalformedRequestError\",\n  \"errorTitle\"\
    : \"The entity data is missing in the request\",\n  \"errorDetail\": \"The 'entity'\
    \ attribute is required in EntityResolutionRequest message\",\n  // Optional and\
    \ not recommended for production use\n  \"errorTrace\": \"Traceback (most recent\
    \ call last):\\n  File \\\"/app/ere/service.py\\\", line 45, in process_request\\\
    n...\"\n}\n"
from_schema: https://data.europa.eu/ers/schema
is_a: Response
attributes:
  errorType:
    name: errorType
    description: 'A string representing the error type, eg, the FQN of the raised
      exception.


      This corresponds to RFC-9457''s `type`.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    domain_of:
    - ErrorResponse
    required: true
  errorTitle:
    name: errorTitle
    description: 'A human readable brief message about the error that occurred.


      This corresponds to RFC-9457''s `title`.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    domain_of:
    - ErrorResponse
  errorDetail:
    name: errorDetail
    description: 'A human readable detailed message about the error that occurred.


      This corresponds to RFC-9457''s `detail`.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    domain_of:
    - ErrorResponse
  errorTrace:
    name: errorTrace
    description: 'A string representing a (stack) trace of the error that occurred.


      This is optional and typically used for debugging purposes only, since

      exposing this kind of server-side information is a security risk.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    domain_of:
    - ErrorResponse

```
</details>

### Induced

<details>
```yaml
name: ErrorResponse
description: 'Response sent by the ERE when some error/exception occurs while processing
  a request.

  For instance, this may happen if the request is malformed or some internal error
  happens.


  The attributes of this class are based on [RFC-9457](https://datatracker.ietf.org/doc/html/rfc9457).

  '
examples:
- value: "{\n  \"type\": \"ErrorResponse\",\n  \"requestId\": \"324fs3r345vx\",\n\
    \  \"errorType\": \"ere.exceptions.MalformedRequestError\",\n  \"errorTitle\"\
    : \"The entity data is missing in the request\",\n  \"errorDetail\": \"The 'entity'\
    \ attribute is required in EntityResolutionRequest message\",\n  // Optional and\
    \ not recommended for production use\n  \"errorTrace\": \"Traceback (most recent\
    \ call last):\\n  File \\\"/app/ere/service.py\\\", line 45, in process_request\\\
    n...\"\n}\n"
from_schema: https://data.europa.eu/ers/schema
is_a: Response
attributes:
  errorType:
    name: errorType
    description: 'A string representing the error type, eg, the FQN of the raised
      exception.


      This corresponds to RFC-9457''s `type`.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: errorType
    owner: ErrorResponse
    domain_of:
    - ErrorResponse
    range: string
    required: true
  errorTitle:
    name: errorTitle
    description: 'A human readable brief message about the error that occurred.


      This corresponds to RFC-9457''s `title`.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: errorTitle
    owner: ErrorResponse
    domain_of:
    - ErrorResponse
    range: string
  errorDetail:
    name: errorDetail
    description: 'A human readable detailed message about the error that occurred.


      This corresponds to RFC-9457''s `detail`.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: errorDetail
    owner: ErrorResponse
    domain_of:
    - ErrorResponse
    range: string
  errorTrace:
    name: errorTrace
    description: 'A string representing a (stack) trace of the error that occurred.


      This is optional and typically used for debugging purposes only, since

      exposing this kind of server-side information is a security risk.

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: errorTrace
    owner: ErrorResponse
    domain_of:
    - ErrorResponse
    range: string
  requestId:
    name: requestId
    description: 'A string representing the unique ID of the request this response
      is about.

      '
    from_schema: https://data.europa.eu/ers/schema
    alias: requestId
    owner: ErrorResponse
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
    owner: ErrorResponse
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
    owner: ErrorResponse
    domain_of:
    - RequestOrResponseMixin
    range: string

```
</details>