

# Class: EntityMention 


_An entity mention is a representation of a real-world entity, as provided by the ERS._

_It contains the entity data, along with metadata like type and format.      _

__





URI: [ers:EntityMention](https://data.europa.eu/ers/schema/EntityMention)





```mermaid
 classDiagram
    class EntityMention
    click EntityMention href "../EntityMention/"
      EntityMention : content
        
      EntityMention : contentType
        
      EntityMention : isCanonical
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [contentType](contentType.md) | 0..1 <br/> [String](String.md) | A string about the MIME format of `content` (e | direct |
| [content](content.md) | 0..1 <br/> [String](String.md) | A code string representing the entity mention details (eg, RDF or XML descrip... | direct |
| [isCanonical](isCanonical.md) | 0..1 <br/> [Boolean](Boolean.md) | A boolean flag indicating whether the entity mention is to be considered a ca... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | [entityMention](entityMention.md) | range | [EntityMention](EntityMention.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ers:EntityMention |
| native | ers:EntityMention |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EntityMention
description: "An entity mention is a representation of a real-world entity, as provided\
  \ by the ERS.\nIt contains the entity data, along with metadata like type and format.\
  \      \n"
from_schema: https://data.europa.eu/ers/schema
attributes:
  contentType:
    name: contentType
    description: 'A string about the MIME format of `content` (e.g. text/turtle, application/ld+json)

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    domain_of:
    - EntityMention
  content:
    name: content
    description: 'A code string representing the entity mention details (eg, RDF or
      XML description).

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    domain_of:
    - EntityMention
  isCanonical:
    name: isCanonical
    description: "A boolean flag indicating whether the entity mention is to be considered\
      \ a canonical (the source of truth).\n\nThis is used by the ERS to feed the\
      \ ERE with well known entity mentions (usually for bootstrapping the ERE).\n\
      The confidence level to assign to the cluster created should be 1.0 in this\
      \ case and never overridden by other \nmentions during re-clustering.\n"
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    domain_of:
    - EntityMention
    range: boolean

```
</details>

### Induced

<details>
```yaml
name: EntityMention
description: "An entity mention is a representation of a real-world entity, as provided\
  \ by the ERS.\nIt contains the entity data, along with metadata like type and format.\
  \      \n"
from_schema: https://data.europa.eu/ers/schema
attributes:
  contentType:
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
  content:
    name: content
    description: 'A code string representing the entity mention details (eg, RDF or
      XML description).

      '
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: content
    owner: EntityMention
    domain_of:
    - EntityMention
    range: string
  isCanonical:
    name: isCanonical
    description: "A boolean flag indicating whether the entity mention is to be considered\
      \ a canonical (the source of truth).\n\nThis is used by the ERS to feed the\
      \ ERE with well known entity mentions (usually for bootstrapping the ERE).\n\
      The confidence level to assign to the cluster created should be 1.0 in this\
      \ case and never overridden by other \nmentions during re-clustering.\n"
    from_schema: https://data.europa.eu/ers/schema
    rank: 1000
    alias: isCanonical
    owner: EntityMention
    domain_of:
    - EntityMention
    range: boolean

```
</details>