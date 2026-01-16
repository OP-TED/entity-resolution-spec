

# Slot: errorTitle 


_A human readable brief message about the error that occurred._

__

_This corresponds to RFC-9457's `title`._

__





URI: [ers:errorTitle](https://data.europa.eu/ers/schema/errorTitle)
Alias: errorTitle

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:errorTitle |
| native | ers:errorTitle |




## LinkML Source

<details>
```yaml
name: errorTitle
description: 'A human readable brief message about the error that occurred.


  This corresponds to RFC-9457''s `title`.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: errorTitle
owner: EREErrorResponse
domain_of:
- EREErrorResponse
range: string

```
</details>