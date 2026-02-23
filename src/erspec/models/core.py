from __future__ import annotations 

from datetime import (
    datetime
)
from enum import Enum 
from typing import (
    Optional
)

from pydantic import (
    Field
)

from erspec.models.pydantic_model import PydanticModel


metamodel_version = "None"
version = "0.1.0"


class EntityType(str, Enum):
    """
    Types of entities that can be resolved
    """
    ORGANISATION = "ORGANISATION"
    """
    An organization entity
    """
    PROCEDURE = "PROCEDURE"
    """
    A procurement procedure entity
    """


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



class EntityMention(PydanticModel):
    """An entity mention is a representation of a real-world entity, as provided by the ERS.
It contains the entity data, along with metadata like type and format."""
    identifiedBy: EntityMentionIdentifier = Field(default=..., description="""The identification triad of the entity mention.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })
    content_type: str = Field(default=..., description="""A string about the MIME format of `content` (e.g. text/turtle, application/ld+json)
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })
    content: str = Field(default=..., description="""A code string representing the entity mention details (eg, RDF or XML description).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })
    parsed_representation: Optional[str] = Field(default=None, description="""JSON representation of the parsed entity data.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })


class EntityMentionIdentifier(PydanticModel):
    """A container that groups the attributes needed to identify an entity mention in a resolution request
or response.

As per ERS architectural decision, in the whole ERS and ERE systems, there is always a deterministic
method to build a canonical identifier from the combination of `sourceId`, `requestId` and `entityType`
(eg, string concatenation plus some prefix). Similarly, a cluster ID (mentioned in various places in 
in this hereby ERE service schema) can be built from an entity that is initially the only cluster member."""
    source_id: str = Field(default=..., description="""The ID or URI of the ERS client that originated the request. This identifies an application or a 
person accessing the ERS system.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifier', 'LookupState']} })
    request_id: str = Field(default=..., description="""A string representing the unique ID of the request made to the ERS system. In general, this is unique
only within the scope of the source and the entity type, ie, within `sourceId` and `entityType`. 

Moreover, this is **not** the same as `ereRequestId`, which instead, is internal to the ERE and is 
used to match responses to requests.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifier']} })
    entity_type: str = Field(default=..., description="""A string representing the entity type (based on CET). This is typically a URI.

Note that this is at this level, and not at `EntityMention`, since, as said above, 
it's needed to identify the entity, even when its content is not present. For the same
reason, it's used both for `EREResolutionRequest` and `EREResolutionResponse` messages.,
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifier']} })


class LookupState(PydanticModel):
    """Tracks the resolution state for entity mentions from a particular source.
Records when the source was last resolved against the canonical clustering."""
    source_id: str = Field(default=..., description="""The ID or URI of the ERS client (originator) for which we track lookup state.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifier', 'LookupState']} })
    last_snapshot: datetime  = Field(default=..., description="""Timestamp of the last resolution operation for this source.
Used to determine if a refreshBulk or other update is needed.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['LookupState']} })


class ClusterReference(PydanticModel):
    """A reference to a cluster to which an entity is deemed to belong, with an associated confidence and similarity scores.

A cluster is a set of entity mentions that have been determined to refer to the same real-world entity.
Each cluster has a unique clusterId.

A cluster reference is used to report the association between an entity mention and a cluster 
of equivalence."""
    cluster_id: str = Field(default=..., description="""The identifier of the cluster/canonical entity that is considered equivalent to the
subject entity mention that an `EntityMentionResolutionResponse` refers to.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClusterReference']} })
    confidence_score: float = Field(default=..., description="""A 0-1 value of how confident the ERE is about the equivalence between the subject entity mention
and the target canonical entity.
""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['ClusterReference']} })
    similarity_score: float = Field(default=..., description="""A 0-1 score representing the pairwise comparison between a mention and a cluster (likely
based on a representative representation).
""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['ClusterReference']} })


class Decision(PydanticModel):
    """Canonical placement of an entity mention to a cluster.
Represents the latest resolution decision (from ERE or curator override)."""
    id: str = Field(default=..., description="""Unique decision identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'UserAction']} })
    about_entity_mention: EntityMentionIdentifier = Field(default=..., description="""The entity mention being resolved""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'UserAction']} })
    current_placement: ClusterReference = Field(default=..., description="""The accepted cluster for this mention (latest from ERE or curator).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision']} })
    candidates: list[ClusterReference] = Field(default=..., description="""Top-N alternative clusters proposed by ERE (for curation UI preview).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'UserAction', 'EntityMentionResolutionResponse']} })
    created_at: datetime  = Field(default=..., description="""When the decision was first created""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'UserAction']} })
    updated_at: Optional[datetime ] = Field(default=None, description="""When the decision was last updated (ERE refresh or curator action)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision']} })


class UserAction(PydanticModel):
    """Immutable record of a curator action on an entity mention resolution.
Stored in the User Action Log for traceability and training.

NOT related to ERE messages; represents curator intent only."""
    id: str = Field(default=..., description="""Unique audit trail entry identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'UserAction']} })
    about_entity_mention: EntityMentionIdentifier = Field(default=..., description="""The entity mention the curator acted upon""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'UserAction']} })
    candidates: list[ClusterReference] = Field(default=..., description="""The candidate clusters presented to the curator for selection.
Ordered by confidence (same as shown in curation UI).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'UserAction', 'EntityMentionResolutionResponse']} })
    selected_cluster: Optional[ClusterReference] = Field(default=None, description="""The cluster selected by the curator (if action was ACCEPT_TOP
or ACCEPT_ALTERNATIVE). NULL if action was REJECT_ALL.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['UserAction']} })
    action_type: UserActionType = Field(default=..., description="""The type of action the curator performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['UserAction']} })
    actor: str = Field(default=..., description="""User ID or identifier of the curator who performed the action""", json_schema_extra = { "linkml_meta": {'domain_of': ['UserAction']} })
    created_at: datetime  = Field(default=..., description="""Timestamp when the curator action was recorded""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'UserAction']} })
    metadata: Optional[str] = Field(default=None, description="""JSON metadata providing context (e.g., curator notes, reasoning).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['UserAction']} })


class CanonicalEntityIdentifier(PydanticModel):
    """A logical identity construct providing a stable identity anchor.
Represents a cluster of equivalent entity mentions."""
    identifier: str = Field(default=..., description="""Unique identifier for the canonical entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CanonicalEntityIdentifier']} })
    equivalent_to: list[EntityMentionIdentifier] = Field(default=..., description="""Entity mentions that have been resolved to this canonical entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CanonicalEntityIdentifier']} })

