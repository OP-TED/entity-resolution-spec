

# Slot: identifier 


_Unique identifier for the canonical entity._





URI: [ere:identifier](https://data.europa.eu/ers/schema/ere/identifier)
Alias: identifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CanonicalEntityIdentifier](CanonicalEntityIdentifier.md) | A logical identity construct providing a stable identity anchor |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:identifier |
| native | ere:identifier |




## LinkML Source

<details>
```yaml
name: identifier
description: Unique identifier for the canonical entity.
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: identifier
owner: CanonicalEntityIdentifier
domain_of:
- CanonicalEntityIdentifier
range: string
required: true

```
</details>