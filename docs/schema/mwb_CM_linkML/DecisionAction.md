# Enum: DecisionAction 



URI: [http://publications.europa.eu/ontology/ers/DecisionAction](http://publications.europa.eu/ontology/ers/DecisionAction)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ers:acceptTop | None |  |
| ers:acceptAlternative | None |  |
| ers:rejectAll | None | This could mean just reverting back to default Cluster, or it could mean also... |




## Slots

| Name | Description |
| ---  | --- |
| [decisionAction](decisionAction.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: http://publications.europa.eu/ontology/ers






## LinkML Source

<details>
```yaml
name: DecisionAction
from_schema: http://publications.europa.eu/ontology/ers
rank: 1000
permissible_values:
  ers:acceptTop:
    text: ers:acceptTop
  ers:acceptAlternative:
    text: ers:acceptAlternative
  ers:rejectAll:
    text: ers:rejectAll
    description: This could mean just reverting back to default Cluster, or it could
      mean also sending a new request to resolve the same entity (this time with negative
      cluster examples) ... TBD

```
</details>