# Examples and test cases for the ERE

## Summary

- [Examples and test cases for the ERE](#examples-and-test-cases-for-the-ere)
  - [Summary](#summary)
  - [Example 1: Organisations with minor detail variations](#example-1-organisations-with-minor-detail-variations)
  - [Example 2: Procedures with different procedure numbers (Negative case)](#example-2-procedures-with-different-procedure-numbers-negative-case)
  - [Example 3: Organisations with minor detail variations -- Resolution with excluded identifiers](#example-3-organisations-with-minor-detail-variations----resolution-with-excluded-identifiers)



## Example 1: Organisations with minor detail variations

This is about the Bulgarian Commission on Protection of Competition. The [test data](../notices/deduplicated_organizations/group1/) have two entities having all of legal name, address and contact details matching perfectly.

Outcome: equivalent entities with high confidence.

**Request**:

```javascript
{
  "type": "EntityMentionResolutionRequest",
  "entityMention": 
  { 
    // This is an instance of the EntityMention class (see the LinkML schema)
    "type": "http://www.w3.org/ns/org#Organization",
    "identifier": "http://data.europa.eu/ers/id/324fs3r345vx-ted-sws-pipeline",
    "payload": "<SEE BELOW>",
    "dataFormat": "text/turtle"
  },
  "requestId": "324fs3r345vx",
  "originator": "TED SWS pipeline",
  "metadata": {
    "originator system": "VocBench editor",
    "originator timestamp": "23748737643"
  }
}
```

This is the content of the `payload` for this example:

```javascript
PREFIX cccev: <http://data.europa.eu/m8g/>
PREFIX dct:   <http://purl.org/dc/terms/>
PREFIX ep:    <http://eprints.org/ontology/>
PREFIX epd:   <http://data.europa.eu/a4g/resource/>
PREFIX epo:   <http://data.europa.eu/a4g/ontology#>
PREFIX locn:  <http://www.w3.org/ns/locn#>
PREFIX org:   <http://www.w3.org/ns/org#>
PREFIX owl:   <http://www.w3.org/2002/07/owl#>
PREFIX ql:    <http://semweb.mmlab.be/ns/ql#>
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rml:   <http://semweb.mmlab.be/ns/rml#>
PREFIX rr:    <http://www.w3.org/ns/r2rml#>
PREFIX skos:  <http://www.w3.org/2004/02/skos/core#>
PREFIX tedm:  <http://data.europa.eu/a4g/mapping/sf-rml/>
PREFIX time:  <http://www.w3.org/2006/time#>
PREFIX xsd:   <http://www.w3.org/2001/XMLSchema#>

epd:id_2023-S-210-661238_ReviewerOrganisation_LLhJHMi9mby8ixbkfyGoWj
  rdf:type                    org:Organization;
  epo:hasLegalName            "Комисия за защита на конкуренцията"@bg;
  epo:hasPrimaryContactPoint  epd:id_2023-S-210-661238_ReviewerContactPoint_LLhJHMi9mby8ixbkfyGoWj;
  cccev:registeredAddress     epd:id_2023-S-210-661238_ReviewerOrganisationAddress_LLhJHMi9mby8ixbkfyGoWj
.

epd:id_2023-S-210-661238_ReviewerContactPoint_LLhJHMi9mby8ixbkfyGoWj
  rdf:type                cccev:ContactPoint;
  epo:hasFax              "+359 29807315";
  epo:hasInternetAddress  "http://www.cpc.bg"^^xsd:anyURI;
  cccev:email             "delovodstvo@cpc.bg";
  cccev:telephone         "+359 29356113" .

epd:id_2023-S-210-661238_ReviewerOrganisationAddress_LLhJHMi9mby8ixbkfyGoWj
  rdf:type            locn:Address;
  epo:hasCountryCode  <http://publications.europa.eu/resource/authority/country/BGR>;
  locn:postCode       "1000";
  locn:postName       "София";
  locn:thoroughfare   "бул. Витоша № 18" .
```

*Note*: in the following RDF abstracts, we will omit the namespace declarations.

As you can see, The data have a triple-centric description of the entity to resolve, plus linked entities. The ERE is supposed to resolve the former, possibly using the linked entities (such as addresses or contact points).

*Note*: `identifier` is derived from the request data. It can be done in serveral ways. For the purpose of this example, the URI `http://data.europa.eu/ers/id/324fs3r345vx-ted-sws-pipeline` is built by simple concatenation of request id and originator.

**Resolution**:

In this case, we have a canonical entity with high confidence matching score (due to key fields being identical):

```javascript
{
  "type": "EntityMentionResolutionResponse",
  "requestId": "324fs3r345vx",
  "alignmentLinkSet": {
    "subjectEntityMentionIdentifier": "http://data.europa.eu/ers/id/324fs3r345vx-ted-sws-pipeline",
    "alignmentOptions": [
      {
        "canonicalIdentifier": "http://data.europa.eu/ers/id/324fs3r345vxaa32wa",
        "confidenceScore": 0.91
      },
      {
        "canonicalIdentifier": "http://data.europa.eu/ers/id/324fs3r345vxbb45we",
        "confidenceScore": 0.65
      }
    ]
  }
}
```

*Note*: `http://data.europa.eu/ers/id/324fs3r345vxaa32wa` and `http://data.europa.eu/ers/id/324fs3r345vxbb45we` correspond to canonical URIs annotating clusters of entity mentions. Payload of the entity mentions is irrelevant and therefore not presented in this example.


---

## Example 2: Procedures with different procedure numbers (Negative case)

This test validates that the ERE correctly identifies distinct procurement procedures at the same institution despite similar descriptions. The procedure number is a crucial discriminator. [Sample data here](../procedures/group4/).

Outcome: distinct entities with low confidence match.

**Request**:

```javascript
{
  "type": "EntityMentionResolutionRequest",
  "entityMention": 
  { 
    // This is an instance of the EntityMention class (see the LinkML schema)
    "type": "http://www.w3.org/ns/org#Procedure",
    "identifier": "http://data.europa.eu/ers/id/324fs3r345vx-ted-sws-pipeline",
    "payload": "<SEE BELOW>",
    "dataFormat": "text/turtle"
  },
  "requestId": "324fs3r345vx",
  "originator": "TED SWS pipeline",
  "metadata": {
    "originator timestamp": "23748737643"
  }
}
```

Entity data:

```javascript
epd:id_2023-S-211-665742_Procedure_faF7Q5dyoGpXu3Ru4RGg73
  rdf:type                            epo:Procedure;
  epo:hasDescription                  "Prestação de cuidados de enfermagem, para o serviço de nefrologia e transplantação renal - Unidade de hemodialise, do Centro Hospitalar Universitário Lisboa Norte, Epe."@pt;
  epo:hasLegalBasis                   <http://publications.europa.eu/resource/authority/legal-basis/32014L0024>;
  epo:hasProcedureType                <http://publications.europa.eu/resource/authority/procurement-procedure-type/neg-wo-call>;
  epo:hasProcurementScopeDividedIntoLot epd:id_2023-S-211-665742_Lot_DgNm7RuiSQ47VBTvdrHsRv;
  epo:hasPurpose                      epd:id_2023-S-211-665742_ProcedurePurpose_faF7Q5dyoGpXu3Ru4RGg73;
  epo:hasTitle                        "Procedimento n.º 239X000323"@pt;
  epo:isCoveredByGPA                  false;
  epo:isSubjectToProcedureSpecificTerm epd:id_2023-S-211-665742_DirectAwardTerm_C5nS5y4XErvUqzRNMARW8r
.

epd:id_2023-S-211-665742_ProcedurePurpose_faF7Q5dyoGpXu3Ru4RGg73
  rdf:type                    epo:Purpose;
  epo:hasContractNatureType   <http://publications.europa.eu/resource/authority/contract-nature/services>;
  epo:hasMainClassification   <http://data.europa.eu/cpv/cpv/85141200> .
```

**Resolution**:

No match found above the confidence threshold, the ERE creates a new canonical URI for the incoming entity:

```javascript
{
  "type": "EntityMentionResolutionResponse",
  "requestId": "324fs3r345vx",
  "alignmentLinkSet": {
    "subjectEntityMentionIdentifier": "http://data.europa.eu/ers/id/324fs3r345vx-ted-sws-pipeline",
    "alignmentOptions": [
      {
        "canonicalIdentifier": "http://data.europa.eu/ers/id/324fs3r345vxwer4rq",
        "confidenceScore": 1.0
      }
    ]
  }
}
```


## Example 3: Organisations with minor detail variations -- Resolution with excluded identifiers
This example is built on top of Example 1 and presents a case when a subsequent
resolution request is submitted to obtain other URIs than the provided two.

**Request**:

```javascript
{
  "type": "EntityMentionResolutionRequest",
  "entityMention": {
    "type": "http://www.w3.org/ns/org#Organization",
    "identifier": "http://data.europa.eu/ers/id/324fs3r345vx-ted-sws-pipeline",
    "payload": "<SEE PAYLOAD FOR EXAMPLE 1>",
    "dataFormat": "text/turtle"
  },
  "rejectedCanonicalIdentifiers": [
    "http://data.europa.eu/ers/id/324fs3r345vxaa32wa",
    "http://data.europa.eu/ers/id/324fs3r345vxbb45we"
  ],
  "requestId": "324fs3r345a4fr",
  "originator": "TED SWS pipeline",
  "creationTime": "2026-01-15T14:50:56Z"
}
```


**Resolution**:

In this case, no other match was found besides the two URIs that have been excluded and therefore a new canonical URI is returned:

```javascript
{
  "type": "EntityMentionResolutionResponse",
  "requestId": "324fs3r345a4fr",
  "alignmentLinkSet": {
    "subjectEntityMentionIdentifier": "http://data.europa.eu/ers/id/324fs3r345vx-ted-sws-pipeline",
    "alignmentOptions": [
      {
        "canonicalIdentifier": "http://data.europa.eu/ers/id/324fs3r345vuaa3990",
        "confidenceScore": 1.0
      }
    ]
  }
}
```