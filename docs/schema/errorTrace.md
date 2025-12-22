

# Slot: errorTrace 


_A string representing a (stack) trace of the error that occurred._

__

_This is optional and typically used for debugging purposes only, since_

_exposing this kind of server-side information is a security risk._

__





URI: [ers:errorTrace](https://data.europa.eu/ers/schema/errorTrace)
Alias: errorTrace

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ErrorResponse](ErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:errorTrace |
| native | ers:errorTrace |




## LinkML Source

<details>
```yaml
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

```
</details>