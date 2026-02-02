

# Slot: errorType 


_A string representing the error type, eg, the FQN of the raised exception._

__

_This corresponds to RFC-9457's `type`._

__





URI: [ere:errorType](https://data.europa.eu/ers/schema/ere/errorType)
Alias: errorType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:errorType |
| native | ere:errorType |




## LinkML Source

<details>
```yaml
name: errorType
description: 'A string representing the error type, eg, the FQN of the raised exception.


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

```
</details>