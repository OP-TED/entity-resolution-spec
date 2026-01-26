from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "0.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'ers',
     'default_range': 'string',
     'description': 'A LinkML schema for the ERS Services.',
     'id': 'https://data.europa.eu/ers/schema',
     'imports': ['linkml:types'],
     'name': 'ersServiceDataSchema',
     'prefixes': {'ers': {'prefix_prefix': 'ers',
                          'prefix_reference': 'https://data.europa.eu/ers/schema/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': 'resources/schema/ers-core_v0.1.0.yaml'} )


class EREMessage(ConfiguredBaseModel):
    """
    Root abstraction to represent attributes common to both requests and results.
    This is modelled as a mixin in LinkML (so that it can't be instantiated directly).

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://data.europa.eu/ers/schema'})

    type: Literal["EREMessage"] = Field(default="EREMessage", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ereRequestId: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `requestId` + `sourceId`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class ERERequest(EREMessage):
    """
    Root class to represent all the requests sent to the ERE.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://data.europa.eu/ers/schema'})

    type: Literal["ERERequest"] = Field(default="ERERequest", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ereRequestId: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `requestId` + `sourceId`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EREResponse(EREMessage):
    """
    Root class to represent all the responses sent by the ERE.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://data.europa.eu/ers/schema'})

    type: Literal["EREResponse"] = Field(default="EREResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ereRequestId: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `requestId` + `sourceId`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EntityMentionIdentifers(ConfiguredBaseModel):
    """
    A container that groups the attributes needed to identify an entity mention in a resolution request
    or response.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://data.europa.eu/ers/schema',
         'mixin': True})

    sourceId: str = Field(default=..., description="""The ID or URI of the ERS client that originated the request. This identifies an application or a 
person accessing the ERS system.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifers']} })
    requestId: str = Field(default=..., description="""A string representing the unique ID of the request made to the ERS system. In general, this is unique
only within the scope of the source and the entity type, ie, within `sourceId` and `entityType`. 

Moreover, this is **not** the same as `ereRequestId`, which instead, is internal to the ERE and is 
used to match responses to requests.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifers']} })
    entityType: str = Field(default=..., description="""A string representing the entity type (based on CET). This is typically a URI.

Note that this is at this level, and not at `EntityMention`, since, as said above, 
it's needed to identify the entity, even when its content is not present. For the same
reason, it's used both for `EREResolutionRequest` and `EREResolutionResponse` messages., 
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifers']} })


class EntityMentionResolutionRequest(EntityMentionIdentifers, ERERequest):
    """
    An entity resolution request sent to the ERE, containing the entity to be resolved.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'examples': [{'description': 'a regular request',
                       'value': '{\n'
                                '  "type": "EntityMentionResolutionRequest",\n'
                                '  "requestId": "324fs3r345vx",\n'
                                '  "sourceId": "TEDSWS",\n'
                                '  "entityType": '
                                '"http://www.w3.org/ns/org#Organization",\n'
                                '  "entityMention": \n'
                                '  { \n'
                                '    "content": "epd:ent005 a org:Organization; ...   '
                                'cccev:telephone \\"+44 1924306780\\" .",\n'
                                '    "contentType": "text/turtle"\n'
                                '  },\n'
                                '  "timestamp": "2026-01-14T12:34:56Z",\n'
                                '  // as said above, true to tell it is a cluster '
                                'representative (false is the default)\n'
                                '  "isCanonical": false,\n'
                                '  "maxResultClusters": 5, // to limit the response '
                                'size\n'
                                '  // As said, we need this internal ID and it can be '
                                'auto-generated (eg, with UUIDs)\n'
                                '  "ereRequestId": "324fs3r345vx:01"\n'
                                '}\n'},
                      {'description': 'a refresh request (ie, carrying a rejection '
                                      'list)',
                       'value': '{\n'
                                '  "type": "EntityMentionResolutionRequest",\n'
                                '  "requestId": "324fs3r345vxab",\n'
                                '  "sourceId": "TEDSWS",\n'
                                '  "entityType": '
                                '"http://www.w3.org/ns/org#Organization",\n'
                                '  "entityMention": \n'
                                '  { \n'
                                '    "content": "epd:ent005 a org:Organization; ...   '
                                'cccev:telephone \\"+44 1924306780\\" .",\n'
                                '    "contentType": "text/turtle"\n'
                                '  },\n'
                                '  "rejectedCanonicalIdentifiers": [\n'
                                '    '
                                '"http://data.europa.eu/ers/id/324fs3r345vx-bb45we",\n'
                                '    '
                                '"http://data.europa.eu/ers/id/324fs3r345vx-cc67ui"\n'
                                '  ],\n'
                                '  "timestamp": "2026-01-14T12:40:56Z",\n'
                                '  "ereRequestId": "324fs3r345vxab:01"\n'
                                '}\n'}],
         'from_schema': 'https://data.europa.eu/ers/schema',
         'mixins': ['EntityMentionIdentifers']})

    entityMention: EntityMention = Field(default=..., description="""The data about the entity to be resolved. Note that, at least for the moment, we don't support
batch requests, so this property is single-valued.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionRequest']} })
    maxResultClusters: Optional[int] = Field(default=None, description="""An optional hint to the ERE about the maximum number of clusters to be returned
in the response. This can be used to limit the size of the response.

In general, this is a hint for the ERE, it may ignore it and use a configuration
parameter instead (or use a combination of the two limits).
""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionRequest']} })
    excludedClusterIds: Optional[list[str]] = Field(default=[], description="""When this is present, the resolution must not bin the entity mention into any of the
listed clusters. This can be used to reject a previous resolution proposed by the ERE.

The exact reaction to this is implementation dependent. In the simplest case, the ERE
might just create a singleton cluster with this entity as member. In a more advanced 
case, it might recompute the similarity with more advanced algorithms or use updated
data.

TODO: Can this be revised? What does it happen if an exclusion was made by mistake?
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionRequest']} })
    sourceId: str = Field(default=..., description="""The ID or URI of the ERS client that originated the request. This identifies an application or a 
person accessing the ERS system.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifers']} })
    requestId: str = Field(default=..., description="""A string representing the unique ID of the request made to the ERS system. In general, this is unique
only within the scope of the source and the entity type, ie, within `sourceId` and `entityType`. 

Moreover, this is **not** the same as `ereRequestId`, which instead, is internal to the ERE and is 
used to match responses to requests.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifers']} })
    entityType: str = Field(default=..., description="""A string representing the entity type (based on CET). This is typically a URI.

Note that this is at this level, and not at `EntityMention`, since, as said above, 
it's needed to identify the entity, even when its content is not present. For the same
reason, it's used both for `EREResolutionRequest` and `EREResolutionResponse` messages., 
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifers']} })
    type: Literal["EntityMentionResolutionRequest"] = Field(default="EntityMentionResolutionRequest", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ereRequestId: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `requestId` + `sourceId`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EntityMentionResolutionResponse(EntityMentionIdentifers, EREResponse):
    """
    An entity resolution response returned by the ERE.

    This is basically a list of candidate clusters to which the entity is deemed to be equivalent.

    Note that, for the moment, we don't support batch requests. In future, we might support requests
    with multiple subjects in the `EntityMention` content (eg, RDF with multiple subjects), in which case 
    we might need to return multiple `EntityMentionResolutionResponse` messages, each with additional 
    properties such as `entityIndex` and `totalEntities`.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'examples': [{'value': '{\n'
                                '  "type": "EntityMentionResolutionResponse",\n'
                                '  "requestId": "324fs3r345vx",\n'
                                '  "sourceId": "TEDSWS",\n'
                                '  "entityType": '
                                '"http://www.w3.org/ns/org#Organization",\n'
                                '  "clusters": [\n'
                                '    { \n'
                                '      "clusterId": "324fs3r345vx-aa32wa",\n'
                                '      "confidenceScore": 0.91\n'
                                '    },\n'
                                '    { \n'
                                '      "clusterId": "324fs3r345vx-bb45we",\n'
                                '      "confidenceScore": 0.65\n'
                                '    }\n'
                                '  ],\n'
                                '  "timestamp": "2026-01-14T12:34:59Z",\n'
                                '  "ereRequestId": "324fs3r345vx:01"\n'
                                '}\n'
                                '    \n'}],
         'from_schema': 'https://data.europa.eu/ers/schema',
         'mixins': ['EntityMentionIdentifers']})

    clusters: list[ClusterRef] = Field(default=..., description="""The set of cluster reference/score pairs representing the candidate clusters
that the entity mention in the original request could align to (be equivalent to).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionResponse']} })
    sourceId: str = Field(default=..., description="""The ID or URI of the ERS client that originated the request. This identifies an application or a 
person accessing the ERS system.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifers']} })
    requestId: str = Field(default=..., description="""A string representing the unique ID of the request made to the ERS system. In general, this is unique
only within the scope of the source and the entity type, ie, within `sourceId` and `entityType`. 

Moreover, this is **not** the same as `ereRequestId`, which instead, is internal to the ERE and is 
used to match responses to requests.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifers']} })
    entityType: str = Field(default=..., description="""A string representing the entity type (based on CET). This is typically a URI.

Note that this is at this level, and not at `EntityMention`, since, as said above, 
it's needed to identify the entity, even when its content is not present. For the same
reason, it's used both for `EREResolutionRequest` and `EREResolutionResponse` messages., 
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifers']} })
    type: Literal["EntityMentionResolutionResponse"] = Field(default="EntityMentionResolutionResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ereRequestId: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `requestId` + `sourceId`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EREErrorResponse(EREResponse):
    """
    Response sent by the ERE when some error/exception occurs while processing a request.
    For instance, this may happen if the request is malformed or some internal error happens.

    The attributes of this class are based on [RFC-9457](https://datatracker.ietf.org/doc/html/rfc9457).

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'examples': [{'value': '{\n'
                                '  "type": "EREErrorResponse",\n'
                                '  "requestId": "324fs3r345vx",\n'
                                '  "errorType": '
                                '"ere.exceptions.MalformedRequestError",\n'
                                '  "errorTitle": "The entity data is missing in the '
                                'request",\n'
                                '  "errorDetail": "The \'entity\' attribute is '
                                'required in EntityMentionResolutionRequest message",\n'
                                '  // Optional and not recommended for production use\n'
                                '  "errorTrace": "Traceback (most recent call '
                                'last):\\n  File \\"/app/ere/service.py\\", line 45, '
                                'in process_request\\n..."\n'
                                '}\n'}],
         'from_schema': 'https://data.europa.eu/ers/schema'})

    errorType: str = Field(default=..., description="""A string representing the error type, eg, the FQN of the raised exception.

This corresponds to RFC-9457's `type`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREErrorResponse']} })
    errorTitle: Optional[str] = Field(default=None, description="""A human readable brief message about the error that occurred.

This corresponds to RFC-9457's `title`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREErrorResponse']} })
    errorDetail: Optional[str] = Field(default=None, description="""A human readable detailed message about the error that occurred.

This corresponds to RFC-9457's `detail`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREErrorResponse']} })
    errorTrace: Optional[str] = Field(default=None, description="""A string representing a (stack) trace of the error that occurred.

This is optional and typically used for debugging purposes only, since
exposing this kind of server-side information is a security risk.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREErrorResponse']} })
    type: Literal["EREErrorResponse"] = Field(default="EREErrorResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ereRequestId: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `requestId` + `sourceId`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EntityMention(ConfiguredBaseModel):
    """
    An entity mention is a representation of a real-world entity, as provided by the ERS.
    It contains the entity data, along with metadata like type and format.      

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://data.europa.eu/ers/schema'})

    contentType: Optional[str] = Field(default=None, description="""A string about the MIME format of `content` (e.g. text/turtle, application/ld+json)
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })
    content: Optional[str] = Field(default=None, description="""A code string representing the entity mention details (eg, RDF or XML description).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })
    isCanonical: Optional[bool] = Field(default=None, description="""A boolean flag indicating whether the entity mention is to be considered a canonical (the source of truth).

This is used by the ERS to feed the ERE with well known entity mentions (usually for bootstrapping the ERE).
The confidence level to assign to the cluster created should be 1.0 in this case and never overridden by other 
mentions during re-clustering.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })


class ClusterRef(ConfiguredBaseModel):
    """
    A reference to a cluster to which an entity is deemed to belong, with an associated confidence score.

    A cluster is a set of entity mentions that have been determined to refer to the same real-world entity.
    Each cluster has a unique clusterId.

    A cluster reference is used to report the association between an entity mention and a cluster 
    of equivalence.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://data.europa.eu/ers/schema'})

    clusterId: str = Field(default=..., description="""The identifier of the cluster/canonical entity that is considered equivalent to the
subject entity mention that an `EntityMentionResolutionResponse` refers to.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClusterRef']} })
    confidenceScore: float = Field(default=..., description="""A 0-1 value of how confident the ERE is about the equivalence between the subject entity mention
and the target canonical entity.
""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['ClusterRef']} })


class ResetRequest(ERERequest):
    """
    A request to reset all the resolutions computed so far and possibly rebuild them as 
    requests about old entities arrive again (and build new entities from scratch as usually).

    It is expected that the ERE client re-sends all the entities to be resolved again,
    using `EntityMentionResolutionRequest` messages exactly as the first time the resolutions 
    were built. This implies the a client like the ERS logs/persists the entities it receives
    to resolve and also saves manual overriding of ERE results.

    Moreover:
    * The ERE must keep track of past `EntityMention` marked as canonical.
    * The ERE must retain requests with `excludedClusterIds` and apply them again when the 
      same entity mention is re-sent after the reset. TODO: see notes about this properties,
      on the possible need of withdrawing exclusions.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://data.europa.eu/ers/schema'})

    type: Literal["ResetRequest"] = Field(default="ResetRequest", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ereRequestId: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `requestId` + `sourceId`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class ResetResponse(EREResponse):
    """
    A response to a `ResetRequest`, confirming that the rebuild process has started.

    As for all the requests, this carries the `ereRequestId`, which matches the reset request being
    acknowledged.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://data.europa.eu/ers/schema'})

    type: Literal["ResetResponse"] = Field(default="ResetResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ereRequestId: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `requestId` + `sourceId`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
EREMessage.model_rebuild()
ERERequest.model_rebuild()
EREResponse.model_rebuild()
EntityMentionIdentifers.model_rebuild()
EntityMentionResolutionRequest.model_rebuild()
EntityMentionResolutionResponse.model_rebuild()
EREErrorResponse.model_rebuild()
EntityMention.model_rebuild()
ClusterRef.model_rebuild()
ResetRequest.model_rebuild()
ResetResponse.model_rebuild()
