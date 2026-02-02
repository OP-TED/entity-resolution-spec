

# Slot: contentType 


_A string about the MIME format of `content` (e.g. text/turtle, application/ld+json)_

__





URI: [ers:contentType](https://data.europa.eu/ers/schema/contentType)
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


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:contentType |
| native | ers:contentType |




## LinkML Source

<details>
```yaml
name: contentType
description: 'A string about the MIME format of `content` (e.g. text/turtle, application/ld+json)

  '
from_schema: https://data.europa.eu/ers/schema
rank: 1000
alias: contentType
owner: EntityMention
domain_of:
- EntityMention
range: string
required: true

```
</details>