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


class ERECommunicationArtefact(ConfiguredBaseModel):
    """
    Root abstraction to represent attributes common to both requests and results.
    This is modelled as a mixin in LinkML (so that it can't be instantiated directly).

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://data.europa.eu/ers/schema',
         'mixin': True})

    type: Literal["ERECommunicationArtefact"] = Field(default="ERECommunicationArtefact", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['ERECommunicationArtefact', 'EntityMention']} })
    metadata: Optional[str] = Field(default=None, description="""An optional arbitrary dictionary of further request metadata.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERECommunicationArtefact']} })


class ERERequest(ERECommunicationArtefact):
    """
    Root class to represent all the requests sent to the ERE.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://data.europa.eu/ers/schema',
         'mixins': ['ERECommunicationArtefact']})

    requestId: str = Field(default=..., description="""A string representing the unique ID of this request.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest', 'EREResponse']} })
    originator: str = Field(default=..., description="""The ID or URI of the request originator.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest']} })
    creationTime: Optional[datetime ] = Field(default=None, description="""The timestamp when the request was created.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest']} })
    type: Literal["ERERequest"] = Field(default="ERERequest", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['ERECommunicationArtefact', 'EntityMention']} })
    metadata: Optional[str] = Field(default=None, description="""An optional arbitrary dictionary of further request metadata.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERECommunicationArtefact']} })


class EREResponse(ERECommunicationArtefact):
    """
    Root class to represent all the responses sent by the ERE.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://data.europa.eu/ers/schema',
         'mixins': ['ERECommunicationArtefact']})

    requestId: str = Field(default=..., description="""A string representing the unique ID of the request this response is about.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest', 'EREResponse']} })
    type: Literal["EREResponse"] = Field(default="EREResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['ERECommunicationArtefact', 'EntityMention']} })
    metadata: Optional[str] = Field(default=None, description="""An optional arbitrary dictionary of further request metadata.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERECommunicationArtefact']} })


class EntityMentionResolutionRequest(ERERequest):
    """
    An entity resolution request sent to the ERE, containing the entity to be resolved.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'examples': [{'description': 'a regular request',
                       'value': '{\n'
                                '  "type": '
                                '"EntityMentionResolutionRequest",            \n'
                                '  "entityMention": \n'
                                '  { \n'
                                '    "type": "http://www.w3.org/ns/org#Organization",\n'
                                '    // As said above, there is always a way to '
                                'compute this\n'
                                '    "identifier": '
                                '"http://data.europa.eu/ers/id/324fs3r345vx-aa32wa",\n'
                                '    "payload": "epd:ent005 a org:Organization; ...   '
                                'cccev:telephone \\"+44 1924306780\\" .",\n'
                                '    "dataFormat": "text/turtle",\n'
                                '    // As Said above, this is optional and JSON-LD is '
                                'just an example of what it could rendered.\n'
                                '    "jsonRepresentation": {\n'
                                '      "@context": {\n'
                                '        "org": "http://www.w3.org/ns/org#",\n'
                                '        "cccev": '
                                '"https://data.europa.eu/cc/cefact/code/"\n'
                                '      },\n'
                                '      "@id": '
                                '"http://data.europa.eu/ers/id/324fs3r345vx-aa32wa",\n'
                                '      "@type": "org:Organization",\n'
                                '      "cccev:telephone": "+44 1924306780"\n'
                                '    }\n'
                                '  },\n'
                                '  "requestId": "324fs3r345vx",\n'
                                '  "originator": "TED SWS pipeline",\n'
                                '  "creationTime": "2026-01-14T12:34:56Z",\n'
                                '  "metadata": {\n'
                                '    "originator system": "VocBench editor",\n'
                                '    "originator timestamp": "23748737643"\n'
                                '  }\n'
                                '}\n'},
                      {'description': 'a refresh request (ie, carrying a rejection '
                                      'list)',
                       'value': '{\n'
                                '  "type": '
                                '"EntityMentionResolutionRequest",            \n'
                                '  "entityMention": \n'
                                '  { \n'
                                '    "type": "http://www.w3.org/ns/org#Organization",\n'
                                '    "identifier": '
                                '"http://data.europa.eu/ers/id/324fs3r345vx-aa32wa",\n'
                                '    "payload": "epd:ent005 a org:Organization; ...   '
                                'cccev:telephone \\"+44 1924306780\\" .",\n'
                                '    "dataFormat": "text/turtle"\n'
                                '  },\n'
                                '  "rejectedCanonicalIdentifiers": [\n'
                                '    '
                                '"http://data.europa.eu/ers/id/324fs3r345vx-bb45we",\n'
                                '    '
                                '"http://data.europa.eu/ers/id/324fs3r345vx-cc67ui"\n'
                                '  ],\n'
                                '  "requestId": "324fs3r345vx01",\n'
                                '  "originator": "TED SWS pipeline",\n'
                                '  "creationTime": "2026-01-14T12:40:56Z"\n'
                                '}\n'}],
         'from_schema': 'https://data.europa.eu/ers/schema'})

    entityMention: EntityMention = Field(default=..., description="""The data about the entity to be resolved.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionRequest']} })
    rejectedCanonicalIdentifiers: Optional[list[str]] = Field(default=[], description="""When this is present, the request is a refresh request: it is asking that the entity 
is resolved again and the clusters/canonical entities that were previously proposed 
as resolution are now ignored.

The exact reaction to this is implementation dependent. In the simplest case, the ERE
might just create a singleton cluster with this entity as member. In a more advanced 
case, it might recompute the similarity with more advanced algorithms or use updated
data.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionRequest']} })
    requestId: str = Field(default=..., description="""A string representing the unique ID of this request.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest', 'EREResponse']} })
    originator: str = Field(default=..., description="""The ID or URI of the request originator.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest']} })
    creationTime: Optional[datetime ] = Field(default=None, description="""The timestamp when the request was created.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest']} })
    type: Literal["EntityMentionResolutionRequest"] = Field(default="EntityMentionResolutionRequest", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['ERECommunicationArtefact', 'EntityMention']} })
    metadata: Optional[str] = Field(default=None, description="""An optional arbitrary dictionary of further request metadata.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERECommunicationArtefact']} })


class EntityMentionResolutionResponse(EREResponse):
    """
    An entity resolution response sent by the ERE.

    This links an `AlignmentLinkSet`, to represent possible resolutions (see the attribute definition).

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'examples': [{'value': '{\n'
                                '  "type": "EntityMentionResolutionResponse",\n'
                                '  "requestId": "324fs3r345vx",\n'
                                '  "alignmentLinkSet": {\n'
                                '    "subjectEntityMentionIdentifier": '
                                '"http://data.europa.eu/ers/id/324fs3r345vx-q11rea",\n'
                                '    "alignmentOptions": [\n'
                                '      { \n'
                                '        "canonicalIdentifier": '
                                '"http://data.europa.eu/ers/id/324fs3r345vx-aa32wa",\n'
                                '        "confidenceScore": 0.91\n'
                                '      },\n'
                                '      { \n'
                                '        "canonicalIdentifier": '
                                '"http://data.europa.eu/ers/id/324fs3r345vx-bb45we",\n'
                                '        "confidenceScore": 0.65\n'
                                '      }\n'
                                '    ]\n'
                                '  }\n'
                                '}\n'
                                '    \n'}],
         'from_schema': 'https://data.europa.eu/ers/schema'})

    alignmentLinkSet: AlignmentLinkSet = Field(default=..., description="""The set of alignment links representing the candidate canonical entities/clusters
that the entity mention in the original request could align to (be equivalent to).

**Note**: for the moment, this is not multi-valued, since we don't support batch requests (yet?),
thus there is only one set in a response, that resolves for the single entity mention in the
original request (with multiple alignment candidates). If, in the future, we support batch requests,
then we might need to return one alignment link set per entity mention in a request.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionResponse']} })
    requestId: str = Field(default=..., description="""A string representing the unique ID of the request this response is about.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest', 'EREResponse']} })
    type: Literal["EntityMentionResolutionResponse"] = Field(default="EntityMentionResolutionResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['ERECommunicationArtefact', 'EntityMention']} })
    metadata: Optional[str] = Field(default=None, description="""An optional arbitrary dictionary of further request metadata.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERECommunicationArtefact']} })


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
    requestId: str = Field(default=..., description="""A string representing the unique ID of the request this response is about.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest', 'EREResponse']} })
    type: Literal["EREErrorResponse"] = Field(default="EREErrorResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['ERECommunicationArtefact', 'EntityMention']} })
    metadata: Optional[str] = Field(default=None, description="""An optional arbitrary dictionary of further request metadata.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERECommunicationArtefact']} })


class EntityMention(ConfiguredBaseModel):
    """
    An entity mention is a representation of a real-world entity in the ERS. It must have 
    a data content and a data format, so that components like the ERE can use them for resolution.

    Moreover, an entity mention must have a computed identifier (see below).

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://data.europa.eu/ers/schema'})

    identifier: str = Field(default=..., description="""An URI identifying the entity.

While mandatory, this can be computed, using same function that depends on the entity payload.
In that case, **there must be** a single function in the whole ERS (including the ERE) that
computes the same identifier for the same payload, eg, a hash, an RDF URI extractor. This is
needed for the resolution results to refer to the correct request entities.        
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })
    type: str = Field(default=..., description="""A string representing the entity type URI (based on CET).

Note that we don't use the `designates_type` thing here, since entities or canonical entities 
are always used in clearly distinct contexts.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERECommunicationArtefact', 'EntityMention']} })
    datFormat: Optional[str] = Field(default=None, description="""A string about the MIME format of `payload` (e.g. text/turtle, application/ld+json)
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })
    payload: Optional[str] = Field(default=None, description="""A code string representing the entity details (eg, RDF description).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })
    jsonRepresentation: Optional[str] = Field(default=None, description="""An optional JSON representation of the entity, which is usually achieved from the payload.
This is mainly useful for the curation app.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })


class AlignmentLinkSet(ConfiguredBaseModel):
    """
    A set of alignment links to a referred entity.

    Each link in the set represents an entity that might be equivalent to the referred entity,
    see `AlignmentLink` for details.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://data.europa.eu/ers/schema'})

    subjectEntityMentionIdentifier: str = Field(default=..., description="""The identifier of the entity mention that is the subject of these alignment links.
This must match the `identifier` attribute of an `EntityMention` that a resolution response
refers to.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AlignmentLinkSet']} })
    alignmentOptions: list[AlignmentLink] = Field(default=..., description="""A list of possible matches (alignment links) between the subject entity mention
and candidate canonical entities.

It is recommended that these are sorted by descending confidence score, although
that is not mandatory.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AlignmentLinkSet']} })


class AlignmentLink(ConfiguredBaseModel):
    """
    An alignment link representing a possible equivalence between an entity mention in the
    `AlignmentLinkSet` the link belongs to, and a canonical entity, together with a confidence score.

    A semi-formal representation:

    ```
      for each (canonicalIdentifier, cconfidenceScore) in AlignmentLinkSet.alignmentOptions:
        entity(subjectEntityMentionIdentifier)  ==  entity(mentionIdentifier) 
          with score = confidenceScore
    ```

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://data.europa.eu/ers/schema'})

    canonicalIdentifier: str = Field(default=..., description="""The identifier of the cluster/canonical entity that is considered equivalent to the
subject entity mention in the `AlignmentLinkSet` the link belongs to.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AlignmentLink']} })
    confidenceScore: float = Field(default=..., description="""A 0-1 value of how confident the ERE is about the equivalence between the subject entity mention
and the target canonical entity.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AlignmentLink']} })


class FullRebuildRequest(ERERequest):
    """
    A request to reset all the resolutions computed so far and rebuild them as 
    requests about old entities arrive again (and build new entities from scratch).

    It is expected that the ERE client re-sends all the entities to be resolved again,
    using `EntityMentionResolutionRequest` messages exactly as the first time the resolutions 
    were built. This implies the a client like the ERS logs/persists the entities it receives
    to resolve and also saves manual overriding of ERE results.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://data.europa.eu/ers/schema'})

    requestId: str = Field(default=..., description="""A string representing the unique ID of this request.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest', 'EREResponse']} })
    originator: str = Field(default=..., description="""The ID or URI of the request originator.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest']} })
    creationTime: Optional[datetime ] = Field(default=None, description="""The timestamp when the request was created.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest']} })
    type: Literal["FullRebuildRequest"] = Field(default="FullRebuildRequest", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['ERECommunicationArtefact', 'EntityMention']} })
    metadata: Optional[str] = Field(default=None, description="""An optional arbitrary dictionary of further request metadata.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERECommunicationArtefact']} })


class FullRebuildResponse(EREResponse):
    """
    A response to a `FullRebuildRequest`, confirming that the rebuild process has started.

    This should carry the `requestId` attribute.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://data.europa.eu/ers/schema'})

    requestId: str = Field(default=..., description="""A string representing the unique ID of the request this response is about.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERERequest', 'EREResponse']} })
    type: Literal["FullRebuildResponse"] = Field(default="FullRebuildResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['ERECommunicationArtefact', 'EntityMention']} })
    metadata: Optional[str] = Field(default=None, description="""An optional arbitrary dictionary of further request metadata.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ERECommunicationArtefact']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ERECommunicationArtefact.model_rebuild()
ERERequest.model_rebuild()
EREResponse.model_rebuild()
EntityMentionResolutionRequest.model_rebuild()
EntityMentionResolutionResponse.model_rebuild()
EREErrorResponse.model_rebuild()
EntityMention.model_rebuild()
AlignmentLinkSet.model_rebuild()
AlignmentLink.model_rebuild()
FullRebuildRequest.model_rebuild()
FullRebuildResponse.model_rebuild()
