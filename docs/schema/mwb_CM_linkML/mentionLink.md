

# Slot: mentionLink 



URI: [ers:mentionLink](ers:mentionLink)
Alias: mentionLink

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CanonicalEntity](CanonicalEntity.md) | No two links can exist for the same entity mention within the entire store |  no  |






## Properties

* Range: [AlignmentLink](AlignmentLink.md)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://publications.europa.eu/ontology/ers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:mentionLink |
| native | http://publications.europa.eu/ontology/ers/mentionLink |




## LinkML Source

<details>
```yaml
name: mentionLink
from_schema: http://publications.europa.eu/ontology/ers
rank: 1000
slot_uri: ers:mentionLink
alias: mentionLink
owner: CanonicalEntity
domain_of:
- CanonicalEntity
range: AlignmentLink
required: true
multivalued: true

```
</details>