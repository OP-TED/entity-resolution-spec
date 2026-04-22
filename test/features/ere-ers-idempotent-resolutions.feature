Feature: ERE/ERS idempotent requests

  This feature defines the idempotency contract between ERS and ERE: what ERE can expect
  when the same request arrives more than once, and what ERS guarantees about repeated submissions.


Scenario Outline: Repeated regular resolution request returns the same result

  This is true if the ERE doesn't do any re-clustering or rebuild operation between the requests.

Given
  That the ERE has previously replied to a resolution request {Req} for an entity E
  (with or without excluded clusters)
And
  No `EntityMentionResolutionResponse` has been emitted with `ere_request_id` having the ‘ereNotification:’ prefix
  and `entity_mention_id` pointing to E (ie, no internal updates happened, see the contract document)
When
  ERS pushes again the same resolution request {Req} for the entity E into the ERE request channel
Then
  The ERE asynchronously pushes an `EntityMentionResolutionResponse` object that contains the
  same set of `candidates` as in the previous response for E, including their confidence score.

  Since ERS selects the canonical assignment positionally (`candidates[0]`), the ordering of candidates
  must also be stable across repeated requests — the same best candidate must appear first each time.

  This applies to the following variants of {Req}:
    | Req                                                                                    |
    | a regular resolution request without `proposed_cluster_ids` or `excluded_cluster_ids` |
    | a resolution request with values for `proposed_cluster_ids`                           |
    | a resolution request with values for `excluded_cluster_ids`                           |


Scenario: ERS does not forward a second resolution request for the same triad with different content

  ERS enforces idempotency at submission time: if an entity mention triad is submitted a second
  time with different content, ERS rejects the conflict before it reaches ERE. From ERE's
  perspective, each triad arrives at most once with a consistent payload.

Given
  ERS has already received and forwarded a resolution request for entity mention triad T
  with content C1
When
  A second submission arrives for the same triad T with different content C2
Then
  ERS rejects the second submission as a conflict
  And no second resolution request for triad T is published to the ERE channel
