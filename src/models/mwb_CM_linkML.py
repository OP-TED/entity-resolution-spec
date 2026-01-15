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
version = "None"


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


linkml_meta = LinkMLMeta({'default_prefix': 'http://publications.europa.eu/ontology/ers/',
     'default_range': 'string',
     'description': 'Mapping Workbench project v2',
     'id': 'http://publications.europa.eu/ontology/ers',
     'imports': ['linkml:types'],
     'name': 'ERS',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mwb': {'prefix_prefix': 'mwb',
                          'prefix_reference': 'http://meaningfy.ws/mbw/'}},
     'source_file': 'resources/schema/mwb_CM_linkML.yaml'} )

class DecisionAction(str, Enum):
    ersCOLONacceptTop = "ers:acceptTop"
    ersCOLONacceptAlternative = "ers:acceptAlternative"
    ersCOLONrejectAll = "ers:rejectAll"
    """
    This could mean just reverting back to default Cluster, or it could mean also sending a new request to resolve the same entity (this time with negative cluster examples) ... TBD
    """


class DecissionStatus(str, Enum):
    ersCOLONautomaticConfident = "ers:automaticConfident"
    ersCOLONpendingManualReview = "ers:pendingManualReview"
    ersCOLONmanuallyReviewed = "ers:manuallyReviewed"


class EntityType(str, Enum):
    ersCOLONorganisation = "ers:organisation"
    ersCOLONprocedure = "ers:procedure"



class AlignmentLink(ConfiguredBaseModel):
    """
    Represents either manual or automatic alignment. It can be also used to represent uncertain automatic alignments. Note:Uncertain automatic alignments will be used in the web curation app to show alternative alignments, but they'll never be used as a \"primary\" link provided for link curation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ers:AlignmentLink',
         'from_schema': 'http://publications.europa.eu/ontology/ers'})

    mentionIdentifier: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['AlignmentLink'], 'slot_uri': 'ers:mentionIdentifier'} })
    canonicalIdentifier: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['AlignmentLink'], 'slot_uri': 'ers:canonicalIdentifier'} })
    confidenceScore: float = Field(default=..., description="""This indicates a confidence of belonging to a cluster:0 - 1 :automatically computed -1 :rejected by a person""", json_schema_extra = { "linkml_meta": {'domain_of': ['AlignmentLink'], 'slot_uri': 'ers:confidenceScore'} })


class AlignmentLinkSet(ConfiguredBaseModel):
    """
    The alignment link set is a collection of alignment links that form a set of possible alignments for the same entity. Usually the link set serves as a decision context defined by the alternative alignment links automatically derived. Then it is called a DecisionContext. In addition, to make a decission in the UI, it is necessary to access the entity representation, and the canonical entities representations. Note:There is no distinction between the main (canonical) and alternative (potential) alignments. This is determined by the confidence score (link with the highest score links to the canonical entity). Optionally, the list can be sorted by score in descending order.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ers:AlignmentLinkSet',
         'from_schema': 'http://publications.europa.eu/ontology/ers'})

    subjectMentionIdentifier: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['AlignmentLinkSet'], 'slot_uri': 'ers:subjectMentionIdentifier'} })
    alignmentOption: list[AlignmentLink] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['AlignmentLinkSet'], 'slot_uri': 'ers:alignmentOption'} })
    defaultAlignment: AlignmentLink = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['AlignmentLinkSet'], 'slot_uri': 'ers:defaultAlignment'} })


class CanonicalEntity(ConfiguredBaseModel):
    """
    No two links can exist for the same entity mention within the entire store. The alignment links MUST be to distinct entity mentions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ers:CanonicalEntity',
         'from_schema': 'http://publications.europa.eu/ontology/ers'})

    identifier: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CanonicalEntity', 'EntityMention'],
         'slot_uri': 'ers:identifier'} })
    created: datetime  = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CanonicalEntity', 'RequestRecord'], 'slot_uri': 'ers:created'} })
    mentionLink: list[AlignmentLink] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CanonicalEntity'], 'slot_uri': 'ers:mentionLink'} })


class CanonicalEntityRegistry(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ers:CanonicalEntityRegistry',
         'from_schema': 'http://publications.europa.eu/ontology/ers'})

    canonicalEntity: Optional[list[CanonicalEntity]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['CanonicalEntityRegistry'], 'slot_uri': 'ers:canonicalEntity'} })


class CommunicationArtefact(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ers:CommunicationArtefact',
         'from_schema': 'http://publications.europa.eu/ontology/ers'})

    pass


class Decission(ConfiguredBaseModel):
    """
    The decision object captures what (integration) action shall be taken given a DeciusionContex. Integration needed in 2 context when a response comes from ERE , we need to (step 1) store the alternatives + (step 2) automatically accept the top alternative if it is above and (step 3) upsert it into the canonical entity registry For automated actions ... For user actions ... The decision-making integration logic is as follows:1) Accepting the automatic alignment confidenceScore of the proposed alignment is left as is. 2) Reassigning the mention to another proposed entity confidenceScore of the chosen alignment is set to 1.0 confidenceScore of the proposed alignment is set to -1.0 other alternative alignments are note affected 2) Rejecting the automatic alignment confidenceScore of both proposed alignment and alternative alignments is set to -1.0
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ers:Decission',
         'from_schema': 'http://publications.europa.eu/ontology/ers'})

    indetifier: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Decission'], 'slot_uri': 'ers:indetifier'} })
    createdAt: datetime  = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Decission'], 'slot_uri': 'ers:createdAt'} })
    updatedAt: datetime  = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Decission'], 'slot_uri': 'ers:updatedAt'} })
    acceptedAlignment: Optional[AlignmentLink] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Decission'], 'slot_uri': 'acceptedAlignment'} })
    acceptedLink: Optional[AlignmentLink] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Decission'], 'slot_uri': 'ers:acceptedLink'} })
    chosenAlternativeLink: Optional[AlignmentLink] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Decission'], 'slot_uri': 'chosenAlternativeLink'} })
    decisionContext: AlignmentLinkSet = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Decission'], 'slot_uri': 'ers:decisionContext'} })
    decisionStatus: DecissionStatus = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Decission'], 'slot_uri': 'ers:decisionStatus'} })
    decisionAction: DecisionAction = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Decission'], 'slot_uri': 'ers:decisionAction'} })


class DecissionsStore(ConfiguredBaseModel):
    """
    Working store Stores data for knowing the choice context training machine learning models
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ers:DecissionsStore',
         'from_schema': 'http://publications.europa.eu/ontology/ers'})

    decision: Optional[list[Decission]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['DecissionsStore'], 'slot_uri': 'ers:decision'} })


class EntityMention(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ers:EntityMention',
         'from_schema': 'http://publications.europa.eu/ontology/ers'})

    identifier: str = Field(default=..., description="""Derived by a direct transformation/computing of available fields. Derived from the payload, i.e. getting the URI of the entityMention RDF payload. The ID is minted by the system, based on directly deriving it from the request ID + originator ID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CanonicalEntity', 'EntityMention'],
         'slot_uri': 'ers:identifier'} })
    parsedDataRepresentation: str = Field(default=..., description="""data are parsed/computed before storage in the ERS. Note:this could be lazy parsing because it is only for LinkCuration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention'], 'slot_uri': 'ers:parsedDataRepresentation'} })
    type: EntityType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention', 'RequestRecord'], 'slot_uri': 'ers:type'} })


class RequestRecord(ConfiguredBaseModel):
    """
    This is stored in the system of records.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ers:RequestRecord',
         'from_schema': 'http://publications.europa.eu/ontology/ers'})

    requestIdentifier: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['RequestRecord'], 'slot_uri': 'ers:requestIdentifier'} })
    originatorIdentifier: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['RequestRecord'], 'slot_uri': 'ers:originatorIdentifier'} })
    created: datetime  = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CanonicalEntity', 'RequestRecord'], 'slot_uri': 'ers:created'} })
    dataFormat: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['RequestRecord'], 'slot_uri': 'ers:dataFormat'} })
    payload: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['RequestRecord'], 'slot_uri': 'ers:payload'} })
    entityMention: Optional[EntityMention] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['RequestRecord'], 'slot_uri': 'ers:entityMention'} })
    type: EntityType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention', 'RequestRecord'], 'slot_uri': 'ers:type'} })


class SystemOfRequestRecords(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ers:SystemOfRequestRecords',
         'from_schema': 'http://publications.europa.eu/ontology/ers'})

    record: Optional[list[RequestRecord]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['SystemOfRequestRecords'], 'slot_uri': 'ers:record'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AlignmentLink.model_rebuild()
AlignmentLinkSet.model_rebuild()
CanonicalEntity.model_rebuild()
CanonicalEntityRegistry.model_rebuild()
CommunicationArtefact.model_rebuild()
Decission.model_rebuild()
DecissionsStore.model_rebuild()
EntityMention.model_rebuild()
RequestRecord.model_rebuild()
SystemOfRequestRecords.model_rebuild()
