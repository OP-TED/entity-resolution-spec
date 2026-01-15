

# Slot: errorDetail 


_A human readable detailed message about the error that occurred._

__

_This corresponds to RFC-9457's `detail`._

__





URI: [ers:errorDetail](https://data.europa.eu/ers/schema/errorDetail)
Alias: errorDetail

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
| self | ers:errorDetail |
| native | ers:errorDetail |




## LinkML Source

<details>
```yaml
name: errorDetail
description: 'A human readable detailed message about the error that occurred.


  This corresponds to RFC-9457''s `detail`.

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: errorDetail
owner: EREErrorResponse
domain_of:
- EREErrorResponse
range: string

```
</details>