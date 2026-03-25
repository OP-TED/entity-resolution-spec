

# Slot: ere_request_id 


_A string representing the unique ID of an ERE request, or the ID of the request a response is about._

_This **is not** the same as `request_id` + `source_id`._

__

_Note on notification responses: as per ERE contract, an `EntityMentionResolutionResponse` message_

_can originate from within the ERE, without any previous request counterpart, as a notification of_

_resolution update. In this case, `ere_request_id` has the prefix `ereNotification:`._

__





URI: [ere:ere_request_id](https://data.europa.eu/ers/schema/ere/ere_request_id)
Alias: ere_request_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |
| [EREResponse](EREResponse.md) | Root class to represent all the responses sent by the ERE |  no  |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |
| [EREMessage](EREMessage.md) | Root abstraction to represent attributes common to both requests and results |  no  |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |  no  |
| [ERERequest](ERERequest.md) | Root class to represent all the requests sent to the ERE |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:ere_request_id |
| native | ere:ere_request_id |




## LinkML Source

<details>
```yaml
name: ere_request_id
description: 'A string representing the unique ID of an ERE request, or the ID of
  the request a response is about.

  This **is not** the same as `request_id` + `source_id`.


  Note on notification responses: as per ERE contract, an `EntityMentionResolutionResponse`
  message

  can originate from within the ERE, without any previous request counterpart, as
  a notification of

  resolution update. In this case, `ere_request_id` has the prefix `ereNotification:`.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: ere_request_id
owner: EREMessage
domain_of:
- EREMessage
range: string
required: true

```
</details>