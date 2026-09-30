# Enum: UserActionType 




_Types of curator actions on entity mention resolutions_



URI: [ere:UserActionType](https://data.europa.eu/ers/schema/ere/UserActionType)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ACCEPT_TOP | None | Curator accepted the top candidate from ERE |
| ACCEPT_ALTERNATIVE | None | Curator selected an alternative candidate |
| REJECT_ALL | None | Curator rejected all candidates |




## Slots

| Name | Description |
| ---  | --- |
| [action_type](action_type.md) | The type of action the curator performed |





## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere






## LinkML Source

<details>
```yaml
name: UserActionType
description: Types of curator actions on entity mention resolutions
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
permissible_values:
  ACCEPT_TOP:
    text: ACCEPT_TOP
    description: Curator accepted the top candidate from ERE
  ACCEPT_ALTERNATIVE:
    text: ACCEPT_ALTERNATIVE
    description: Curator selected an alternative candidate
  REJECT_ALL:
    text: REJECT_ALL
    description: Curator rejected all candidates

```
</details>