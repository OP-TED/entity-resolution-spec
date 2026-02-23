

# Slot: last_snapshot 


_Timestamp of the last resolution operation for this source._

_Used to determine if a refreshBulk or other update is needed._

__





URI: [ere:last_snapshot](https://data.europa.eu/ers/schema/ere/last_snapshot)
Alias: last_snapshot

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LookupState](LookupState.md) | Tracks the resolution state for entity mentions from a particular source |  no  |






## Properties

* Range: [Datetime](Datetime.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:last_snapshot |
| native | ere:last_snapshot |




## LinkML Source

<details>
```yaml
name: last_snapshot
description: 'Timestamp of the last resolution operation for this source.

  Used to determine if a refreshBulk or other update is needed.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: last_snapshot
owner: LookupState
domain_of:
- LookupState
range: datetime
required: true

```
</details>