Feature: ERE/ERS unhappy path interactions

  This feature describes what happens when ERE emits structurally invalid messages to ERS,
  or when a resolution request involves an entity type that ERE does not support.


Scenario Outline: A structurally invalid ERE message is discarded and the system continues operating

  When ERE emits a malformed or incomplete message to the ERS response channel, ERS discards
  the message without raising an error back to ERE and continues processing subsequent messages.

When
  ERE emits a "{fault_type}" message to the ERS response channel
Then
  The message is discarded without raising an error
And
  The system continues to accept and process subsequent valid outcomes

  Examples:
    | fault_type                   |
    | missing cluster identifier   |
    | missing mention triad fields |
    | empty message body           |
    | non-JSON payload             |


Scenario: ERE replies with an error response to a malformed resolution request

  When ERS publishes a resolution request that is structurally invalid, ERE must reply with
  an `EREErrorResponse` on the ERS response channel.

  Contract reference: resources/schemas/er-schema-v0.1.0.json (EREErrorResponse)

When
  ERS pushes a malformed resolution request into the ERE request channel
Then
  ERE asynchronously pushes an error response to the ERS response channel containing:
  - `ere_request_id`: the ID of the malformed request
  - `error_title` / `error_detail`: a human-readable description of the error
  - `type`: "EREErrorResponse"


Scenario: An entity mention with an unsupported entity type is rejected by ERE

  ERE only handles entity types it supports. When it receives a resolution request for an
  unknown type, it must return an error response. ERS will not forward requests for types
  not listed in the service schema.

  Contract reference: resources/schemas/ere-service-schema-v0.1.0.yaml (supported entity types)

When
  ERS pushes a resolution request for an entity mention with an unsupported entity type
Then
  ERE returns an `EREErrorResponse` indicating the entity type is not supported
And
  No cluster reference is included in the response
