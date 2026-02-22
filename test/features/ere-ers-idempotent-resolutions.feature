Feature: ERE/ERS idempotent requests

  This feature tests idempotent interactions with the ERE.


Scenario Outline: Repeated regular resolution request returns the same result

  This is true if the ERE doesn't do any re-clustering or rebuild operation between the requests.

Given
  That the ERE has previously replied to a resolution request {Req} for an entity E
  (with or without excluded clusters)
And
  No `EntityMentionResolutionResponse` has been emitted with `ere_request_id` having the ‘ereNotification:’ prefix
  and `entity_mention_id` pointing to E (ie, no internal updates happened, see the contract document)
When
  The ERS pushes again the same resolution request {Req} for the entity E into the ERE requests channel
Then 
  The ERE asynchronously pushes an `EntityMentionResolutionResponse` object that contains the
  same set of `candidates` as in the previous response for E, including their confidence score.

  Since returning the cluster references in score order is not required, such order doesn't apply to 
  this invariant, i.e., the second result can come in a different order for the cluster references.

  This applies to the following variants of {Req}:
    | Req                                                                 |
    | a regular resolution request without neither `proposed_cluster_ids` nor `excluded_cluster_ids`                    |
    | a resolution request with values for `proposed_cluster_ids` |
    | a resolution request with values for `excluded_cluster_ids` |
    | a resolution request with values for both `proposed_cluster_ids` and `excluded_cluster_ids` |

  TODO: we have to decide if to support the last case about combos.
