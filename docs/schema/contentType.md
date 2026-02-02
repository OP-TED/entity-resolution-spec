

# Slot: contentType 


_A string about the MIME format of `content` (e.g. text/turtle, application/ld+json)_

__





URI: [ere:contentType](https://data.europa.eu/ers/schema/ere/contentType)
Alias: contentType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMention](EntityMention.md) | An entity mention is a representation of a real-world entity, as provided by ... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:contentType |
| native | ere:contentType |




## LinkML Source

<details>
```yaml
name: contentType
description: 'A string about the MIME format of `content` (e.g. text/turtle, application/ld+json)

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: contentType
owner: EntityMention
domain_of:
- EntityMention
range: string
required: true

```
</details>