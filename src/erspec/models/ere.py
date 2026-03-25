from __future__ import annotations 

from datetime import (
    datetime
)
from enum import Enum 
from typing import (
    Literal,
    Optional
)

from pydantic import (
    Field
)

from .core import (
    ClusterReference,
    EntityMention,
    EntityMentionIdentifier
)

from erspec.models.pydantic_model import PydanticModel


metamodel_version = "None"
version = "0.1.0"


class UserActionType(str, Enum):
    """
    Types of curator actions on entity mention resolutions
    """
    ACCEPT_TOP = "ACCEPT_TOP"
    """
    Curator accepted the top candidate from ERE
    """
    ACCEPT_ALTERNATIVE = "ACCEPT_ALTERNATIVE"
    """
    Curator selected an alternative candidate
    """
    REJECT_ALL = "REJECT_ALL"
    """
    Curator rejected all candidates
    """



class EREMessage(PydanticModel):
    """Root abstraction to represent attributes common to both requests and results.
This is modelled as a mixin in LinkML (so that it can't be instantiated directly)."""
    type: Literal["EREMessage"] = Field(default="EREMessage", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.

Note on notification responses: as per ERE contract, an `EntityMentionResolutionResponse` message
can originate from within the ERE, without any previous request counterpart, as a notification of
resolution update. In this case, `ere_request_id` has the prefix `ereNotification:`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class ERERequest(EREMessage):
    """Root class to represent all the requests sent to the ERE."""
    type: Literal["ERERequest"] = Field(default="ERERequest", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.

Note on notification responses: as per ERE contract, an `EntityMentionResolutionResponse` message
can originate from within the ERE, without any previous request counterpart, as a notification of
resolution update. In this case, `ere_request_id` has the prefix `ereNotification:`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EREResponse(EREMessage):
    """Root class to represent all the responses sent by the ERE."""
    type: Literal["EREResponse"] = Field(default="EREResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.

Note on notification responses: as per ERE contract, an `EntityMentionResolutionResponse` message
can originate from within the ERE, without any previous request counterpart, as a notification of
resolution update. In this case, `ere_request_id` has the prefix `ereNotification:`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EntityMentionResolutionRequest(ERERequest):
    """An entity resolution request sent to the ERE, containing the entity to be resolved."""
    entity_mention: EntityMention = Field(default=..., description="""The data about the entity to be resolved. Note that, at least for the moment, we don't support
batch requests, so this property is single-valued.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionRequest']} })
    proposed_cluster_ids: Optional[list[str]] = Field(default=[], description="""When this is present, the ERE may use this information to try to cluster the entity in one of 
the listed clusters.

In particular, when an initial request about an entity isn't answered within a timeout, 
a subsequent new request can be sent about the same entity and with the canonical ID of it
as a single proposed cluster ID. This suggests the ERE that it can create a new singleton cluster
with the entity as its initial only member and its canonical ID as the cluster ID. The ERE
can evolve such a cluster later, when further similar entities are sent in, or when it 
has had more time to associate the initial entity to others. 

Whatever, the case, the ERE **has no obligation** to fulfil the proposal, how it reacts to 
this list is implementation dependent, and the ERE remains the ultimate authority to provide 
the final resolution decision.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionRequest']} })
    excluded_cluster_ids: Optional[list[str]] = Field(default=[], description="""When this is present, the ERE may use this information to avoid clustering the entity in 
the listed clusters.

This can be used to notify the ERE that a curator has rejected a previous resolution 
proposed by the ERE.

As for `proposed_cluster_ids`, the ERE **has no obligation** to fulfil the exclusions, and 
it remains the ultimate authority to provide the final resolution decision.

Similarly, the exact reaction to this is implementation dependent. In the simplest case, the ERE
might just create a singleton cluster with the current entity as member. In a more advanced 
case, it might recompute the similarity with more advanced algorithms or use updated
data.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionRequest']} })
    type: Literal["EntityMentionResolutionRequest"] = Field(default="EntityMentionResolutionRequest", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.

Note on notification responses: as per ERE contract, an `EntityMentionResolutionResponse` message
can originate from within the ERE, without any previous request counterpart, as a notification of
resolution update. In this case, `ere_request_id` has the prefix `ereNotification:`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EntityMentionResolutionResponse(EREResponse):
    """An entity resolution response returned by the ERE.

This is basically a list of candidate clusters to which the entity is deemed to be equivalent.

Note that, for the moment, we don't support batch requests. In future, we might support requests
with multiple subjects in the `EntityMention` content (eg, RDF with multiple subjects), in which case 
we might need to return multiple `EntityMentionResolutionResponse` messages, each with additional 
properties such as `entityIndex` and `totalEntities`."""
    entity_mention_id: EntityMentionIdentifier = Field(default=..., description="""The identifier of the entity mention that has been resolved.

This isn't strictly needed, since the `ere_request_id` already links the response to 
the request's entity mention. Yet, it's reported for convenience.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionResponse']} })
    candidates: list[ClusterReference] = Field(default=..., description="""The set of cluster reference/score pairs representing the candidate clusters
that the entity mention in the original request could align to (be equivalent to).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'UserAction', 'EntityMentionResolutionResponse']} })
    type: Literal["EntityMentionResolutionResponse"] = Field(default="EntityMentionResolutionResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.

Note on notification responses: as per ERE contract, an `EntityMentionResolutionResponse` message
can originate from within the ERE, without any previous request counterpart, as a notification of
resolution update. In this case, `ere_request_id` has the prefix `ereNotification:`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EREErrorResponse(EREResponse):
    """Response sent by the ERE when some error/exception occurs while processing a request.
For instance, this may happen if the request is malformed or some internal error happens.

The attributes of this class are based on [RFC-9457](https://datatracker.ietf.org/doc/html/rfc9457)."""
    error_type: str = Field(default=..., description="""A string representing the error type, eg, the FQN of the raised exception.

This corresponds to RFC-9457's `type`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREErrorResponse']} })
    error_title: Optional[str] = Field(default=None, description="""A human readable brief message about the error that occurred.

This corresponds to RFC-9457's `title`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREErrorResponse']} })
    error_detail: Optional[str] = Field(default=None, description="""A human readable detailed message about the error that occurred.

This corresponds to RFC-9457's `detail`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREErrorResponse']} })
    error_trace: Optional[str] = Field(default=None, description="""A string representing a (stack) trace of the error that occurred.

This is optional and typically used for debugging purposes only, since
exposing this kind of server-side information is a security risk.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREErrorResponse']} })
    type: Literal["EREErrorResponse"] = Field(default="EREErrorResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.

Note on notification responses: as per ERE contract, an `EntityMentionResolutionResponse` message
can originate from within the ERE, without any previous request counterpart, as a notification of
resolution update. In this case, `ere_request_id` has the prefix `ereNotification:`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })

