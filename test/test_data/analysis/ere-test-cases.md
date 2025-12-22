# Examples and test cases for the ERE

## Summary

- [Example 1: Organisations with minor detail variations](#example-1-organisations-with-minor-detail-variations)
- [Example 2: Organisations with case-insensitive name matching](#example-2-organisations-with-case-insensitive-name-matching)
- [Example 3: Organisations with similar but distinct identities Negative case](#example-3-organisations-with-similar-but-distinct-identities-negative-case)
- [Example 4: Procedures with identical fundamental properties](#example-4-procedures-with-identical-fundamental-properties)
- [Example 5: Procedures with same title and identifier Match case](#example-5-procedures-with-same-title-and-identifier-match-case)
- [Example 6: Procedures with different procedure numbers Negative case](#example-6-procedures-with-different-procedure-numbers-negative-case)



## Example 1: Organisations with minor detail variations

This is about the Bulgarian Commission on Protection of Competition. The [test data](../notices/deduplicated_organizations/group1/) have two entities having all of legal name, address and contact details matching perfectly.

Outcome: equivalent entities with high confidence.

**Request**:

```javascript
{
  "type": "EntityResolutionRequest",
  "entity": 
  { 
    // This is an instance of the Entity class (see the LinkML schema)
    "type": "http://www.w3.org/ns/org#Organization",
    "id": "https://publications.europa.eu/resource/authority/a4g/resource/id_2023-S-210-661238_ReviewerOrganisation_LLhJHMi9mby8ixbkfyGoWj",
    "entityData": "<SEE BELOW>",
    "entityDataFormat": "text/turtle"
  },
  "requestId": "324fs3r345vx",
  "originator": "TED SWS pipeline",
  "metadata": {
    "originator system": "VocBench editor",
    "originator timestamp": "23748737643"
  }
}
```

This is the content of the `entityData` for this example:

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

**Resolution**:

In this case, we have a canonical entity with high confidence matching score (due to key fields being identical):

```javascript
{
  "type": "EntityResolution",
  "sourceEntityId": "https://publications.europa.eu/resource/authority/a4g/resource/id_2023-S-210-661238_ReviewerOrganisation_LLhJHMi9mby8ixbkfyGoWj",
  "confidenceLevel": 0.98,
  "requestId": "324fs3r345vx"
  "canonicalEntity": 
  {
    "type": "http://www.w3.org/ns/org#Organization",
    "id": "https://publications.europa.eu/resource/authority/a4g/resource/id_2023-S-210-662860_ReviewerOrganisation_LLhJHMi9mby8ixbkfyGoWj",
    "entityData": "<SEE BELOW>",
    "entityDataFormat": "text/turtle"
  }
}
```

This is the content for `entityData`:

```javascript
epd:id_2023-S-210-662860_ReviewerOrganisation_LLhJHMi9mby8ixbkfyGoWj
  rdf:type                    org:Organization;
  epo:hasLegalName            "Комисия за защита на конкуренцията"@bg;
  epo:hasPrimaryContactPoint  epd:id_2023-S-210-662860_ReviewerContactPoint_LLhJHMi9mby8ixbkfyGoWj;
  cccev:registeredAddress     epd:id_2023-S-210-662860_ReviewerOrganisationAddress_LLhJHMi9mby8ixbkfyGoWj
.

epd:id_2023-S-210-662860_ReviewerContactPoint_LLhJHMi9mby8ixbkfyGoWj
  rdf:type                cccev:ContactPoint;
  epo:hasFax              "+359 29807315";
  epo:hasInternetAddress  "http://www.cpc.bg"^^xsd:anyURI;
  cccev:email             "delovodstvo@cpc.bg";
  cccev:telephone         "+359 29356113" .

epd:id_2023-S-210-662860_ReviewerOrganisationAddress_LLhJHMi9mby8ixbkfyGoWj
  rdf:type            locn:Address;
  epo:hasCountryCode  <http://publications.europa.eu/resource/authority/country/BGR>;
  locn:postCode       "1000";
  locn:postName       "София";
  locn:thoroughfare   "бул. Витоша № 18" .
```



---

## Example 2: Organisations with case-insensitive name matching

This test case involves two German contractor organisations from the same procurement procedure, where the entity names differ only in capitalization of one character ("SE" vs "Se"), [sample data here](../notices/deduplicated_procedures/group3/).

Outcome: equivalent entities with high confidence.

**Request**:

```javascript
{
  "type": "EntityResolutionRequest",
  "entity": 
  { 
    "type": "http://www.w3.org/ns/org#Organization",
    "id": "http://data.europa.eu/a4g/resource/id_2023-S-210-661039_ContractorOrganisation_KoxN6kkynnWenCXubDp4jC",
    "entityData": "<SEE BELOW>",
    "entityDataFormat": "text/turtle"
  },
  "requestId": "case2-661039-KoxN",
  "originator": "TED SWS pipeline"
}
```

Entity data:

```javascript
epd:id_2023-S-210-661039_ContractorOrganisation_KoxN6kkynnWenCXubDp4jC
  rdf:type                org:Organization;
  epo:hasLegalName        "Eiffage Rail NL der Eiffage Infra-Bau SE"@de;
  cccev:registeredAddress epd:id_2023-S-210-661039_ContractorOrganisationAddress_KoxN6kkynnWenCXubDp4jC
.

epd:id_2023-S-210-661039_ContractorOrganisationAddress_KoxN6kkynnWenCXubDp4jC
  rdf:type            locn:Address;
  epo:hasCountryCode  <http://publications.europa.eu/resource/authority/country/DEU>;
  epo:hasNutsCode     <http://data.europa.eu/nuts/code/DEA55>;
  locn:postCode       "44652";
  locn:postName       "Herne";
  locn:thoroughfare   "Landgrafenstr. 29" .
```

**Resolution**:

The system should match despite the case difference ("SE" vs "Se" in the legal suffix):

```javascript
{
  "type": "EntityResolution",
  "sourceEntityId": "http://data.europa.eu/a4g/resource/id_2023-S-210-661039_ContractorOrganisation_KoxN6kkynnWenCXubDp4jC",
  "confidenceLevel": 0.95,
  "requestId": "case2-661039-KoxN",
  "canonicalEntity": 
  {
    "type": "http://www.w3.org/ns/org#Organization",
    "id": "http://data.europa.eu/a4g/resource/id_2023-S-210-661039_ContractorOrganisationModification_4jxq5KuyAaGTzG5CNj9Ycp",
    "entityData": "<SEE BELOW>",
    "entityDataFormat": "text/turtle"
  }
}
```

Canonical entity data:

```javascript
epd:id_2023-S-210-661039_ContractorOrganisationModification_4jxq5KuyAaGTzG5CNj9Ycp
  rdf:type                org:Organization;
  epo:hasLegalName        "Eiffage Rail NL der Eiffage Infra-Bau Se"@de;
  cccev:registeredAddress epd:id_2023-S-210-661039_ContractorOrganisationAddressModification_4jxq5KuyAaGTzG5CNj9Ycp
.

epd:id_2023-S-210-661039_ContractorOrganisationAddressModification_4jxq5KuyAaGTzG5CNj9Ycp
  rdf:type            locn:Address;
  epo:hasCountryCode  <http://publications.europa.eu/resource/authority/country/DEU>;
  epo:hasNutsCode     <http://data.europa.eu/nuts/code/DEA55>;
  locn:postCode       "44652";
  locn:postName       "Herne";
  locn:thoroughfare   "Landgrafenstr. 29" .
```

---

## Example 3: Organisations with similar but distinct identities (Negative case)

This case tests a French administrative tribunal where two URIs with similar names should NOT match because they represent different organizational units - a tribunal vs. its administrative office (greffe). [Sample data here](../notices/deduplicated_organizations/group2/).

Outcome: low confidence similarity, distinct entities.

**Request**:

```javascript
{
  "type": "EntityResolutionRequest",
  "entity": 
  { 
    "type": "http://www.w3.org/ns/org#Organization",
    "id": "http://data.europa.eu/a4g/resource/id_2023-S-210-661197_ReviewerOrganisation_bdZjimbzCaRXbeYeBmF94j",
    "entityData": "<SEE BELOW>",
    "entityDataFormat": "text/turtle"
  },
  "requestId": "case3-neg-tribunal",
  "originator": "TED SWS pipeline"
}
```

Entity data:

```javascript
epd:id_2023-S-210-661197_ReviewerOrganisation_bdZjimbzCaRXbeYeBmF94j
  rdf:type                org:Organization;
  epo:hasLegalName        "tribunal administratif de Paris"@fr;
  cccev:registeredAddress epd:id_2023-S-210-661197_ReviewerOrganisationAddress_bdZjimbzCaRXbeYeBmF94j
.

epd:id_2023-S-210-661197_ReviewerOrganisationAddress_bdZjimbzCaRXbeYeBmF94j
  rdf:type            locn:Address;
  epo:hasCountryCode  <http://publications.europa.eu/resource/authority/country/FRA>;
  locn:postName       "Paris" .
```

**Resolution**:

The system finds no match above the confidence threshold. In the sample data, the closest candidate is the "greffe" (clerk's office), but they are distinct organizational entities. Since no match is found, the ERE creates a new canonical entity from the incoming entity:

The incoming entity becomes a new canonical entity with confidence 1.0.

```javascript
{
  "type": "EntityResolution",
  "sourceEntityId": "http://data.europa.eu/a4g/resource/id_2023-S-210-661197_ReviewerOrganisation_bdZjimbzCaRXbeYeBmF94j",
  "confidenceLevel": 1.0,
  "requestId": "case3-neg-tribunal",
  "canonicalEntity": 
  {
    "type": "http://www.w3.org/ns/org#Organization",
    "id": "http://data.europa.eu/a4g/resource/id_2023-S-210-661197_ReviewerOrganisation_bdZjimbzCaRXbeYeBmF94j",
    "entityData": "<SAME AS REQUEST>",
    "entityDataFormat": "text/turtle"
  }
}
```


---

## Example 4: Procedures with identical fundamental properties

This case demonstrates procedures that should match because they have the same identifier, title, and classification - representing the same procurement procedure appearing in multiple notices. [Sample data here](../notices/deduplicated_procedures/group1/).

Outcome: equivalent entities with high confidence.

**Request**:

```javascript
{
  "type": "EntityResolutionRequest",
  "entity": 
  { 
    "type": "http://data.europa.eu/a4g/ontology#Procedure",
    "id": "http://data.europa.eu/a4g/resource/id_2023-S-210-662861_Procedure_faF7Q5dyoGpXu3Ru4RGg73",
    "entityData": "<SEE BELOW>",
    "entityDataFormat": "text/turtle"
  },
  "requestId": "case4-proc-match",
  "originator": "TED SWS pipeline"
}
```

Entity data:

```javascript
epd:id_2023-S-210-662861_Procedure_faF7Q5dyoGpXu3Ru4RGg73
  rdf:type                            epo:Procedure;
  epo:hasDescription                  "Servicii de exploatare forestiera"@ro;
  epo:hasID                           epd:id_2023-S-210-662861_ProcedureIdentifier_faF7Q5dyoGpXu3Ru4RGg73;
  epo:hasLegalBasis                   <http://publications.europa.eu/resource/authority/legal-basis/32014L0024>;
  epo:hasProcedureType                <http://publications.europa.eu/resource/authority/procurement-procedure-type/neg-wo-call>;
  epo:hasProcurementScopeDividedIntoLot epd:id_2023-S-210-662861_Lot_DgNm7RuiSQ47VBTvdrHsRv;
  epo:hasPurpose                      epd:id_2023-S-210-662861_ProcedurePurpose_faF7Q5dyoGpXu3Ru4RGg73;
  epo:hasTitle                        "Servicii de exploatare forestiera Negociere 10 - 2023 dssv"@ro;
  epo:isCoveredByGPA                  false;
  epo:isSubjectToProcedureSpecificTerm epd:id_2023-S-210-662861_DirectAwardTerm_C5nS5y4XErvUqzRNMARW8r
.

epd:id_2023-S-210-662861_ProcedureIdentifier_faF7Q5dyoGpXu3Ru4RGg73
  rdf:type                epo:Identifier;
  epo:hasIdentifierValue  "10_2023" .

epd:id_2023-S-210-662861_ProcedurePurpose_faF7Q5dyoGpXu3Ru4RGg73
  rdf:type                    epo:Purpose;
  epo:hasContractNatureType   <http://publications.europa.eu/resource/authority/contract-nature/services>;
  epo:hasMainClassification   <http://data.europa.eu/cpv/cpv/77211100> .
```

**Resolution**:

High confidence match due to identical key identifiers and properties:

```javascript
{
  "type": "EntityResolution",
  "sourceEntityId": "http://data.europa.eu/a4g/resource/id_2023-S-210-662861_Procedure_faF7Q5dyoGpXu3Ru4RGg73",
  "confidenceLevel": 0.99,
  "requestId": "case4-proc-match",
  "canonicalEntity": 
  {
    "type": "http://data.europa.eu/a4g/ontology#Procedure",
    "id": "http://data.europa.eu/a4g/resource/id_2023-S-210-663131_Procedure_faF7Q5dyoGpXu3Ru4RGg73",
    "entityData": "<SEE BELOW>",
    "entityDataFormat": "text/turtle"
  }
}
```

Canonical entity data (nearly identical):

```javascript
epd:id_2023-S-210-663131_Procedure_faF7Q5dyoGpXu3Ru4RGg73
  rdf:type                            epo:Procedure;
  epo:hasDescription                  "Servicii de exploatare forestiera"@ro;
  epo:hasID                           epd:id_2023-S-210-663131_ProcedureIdentifier_faF7Q5dyoGpXu3Ru4RGg73;
  epo:hasLegalBasis                   <http://publications.europa.eu/resource/authority/legal-basis/32014L0024>;
  epo:hasProcedureType                <http://publications.europa.eu/resource/authority/procurement-procedure-type/neg-wo-call>;
  epo:hasProcurementScopeDividedIntoLot epd:id_2023-S-210-663131_Lot_DgNm7RuiSQ47VBTvdrHsRv;
  epo:hasPurpose                      epd:id_2023-S-210-663131_ProcedurePurpose_faF7Q5dyoGpXu3Ru4RGg73;
  epo:hasTitle                        "Servicii de exploatare forestiera Negociere 10 - 2023 dssv"@ro;
  epo:isCoveredByGPA                  false;
  epo:isSubjectToProcedureSpecificTerm epd:id_2023-S-210-663131_DirectAwardTerm_C5nS5y4XErvUqzRNMARW8r
.

epd:id_2023-S-210-663131_ProcedureIdentifier_faF7Q5dyoGpXu3Ru4RGg73
  rdf:type                epo:Identifier;
  epo:hasIdentifierValue  "10_2023" .

epd:id_2023-S-210-663131_ProcedurePurpose_faF7Q5dyoGpXu3Ru4RGg73
  rdf:type                    epo:Purpose;
  epo:hasContractNatureType   <http://publications.europa.eu/resource/authority/contract-nature/services>;
  epo:hasMainClassification   <http://data.europa.eu/cpv/cpv/77211100> .
```

---

## Example 5: Procedures with same title and identifier (Match case)

Two procedures with the same identifier and title match, representing the same procurement procedure (Stuttgart 21 railway project) appearing in multiple notices. [Sample data here](../notices/deduplicated_procedures/group3/).

Outcome: equivalent entities with high confidence.

**Request**:

```javascript
{
  "type": "EntityResolutionRequest",
  "entity": 
  { 
    "type": "http://data.europa.eu/a4g/ontology#Procedure",
    "id": "http://data.europa.eu/a4g/resource/id_2023-S-210-663534_Procedure_aE3iyMRsoF9Qvy4eFQRpLT",
    "entityData": "<SEE BELOW>",
    "entityDataFormat": "text/turtle"
  },
  "requestId": "case5-proc-same-project",
  "originator": "TED SWS pipeline"
}
```

Entity data:

```javascript
epd:id_2023-S-210-663534_Procedure_aE3iyMRsoF9Qvy4eFQRpLT
  rdf:type                            epo:Procedure;
  epo:foreseesContractSpecificTerm    epd:id_2023-S-210-663534_ContractTermProcedure_fqfw5hANKbaKT6uyGM9WEZ;
  epo:hasID                           epd:id_2023-S-210-663534_ProcedureIdentifier_aE3iyMRsoF9Qvy4eFQRpLT;
  epo:hasProcurementScopeDividedIntoLot epd:id_2023-S-210-663534_Lot_mtBaW8k5EC8G5zB7LwJPww;
  epo:hasPurpose                      epd:id_2023-S-210-663534_ProcedurePurpose_aE3iyMRsoF9Qvy4eFQRpLT;
  epo:hasTitle                        "S21, PA 1.7; Bahntechnik Oberbau Los A , (19FEI37404) 20FEI44393"@de;
  epo:isSubjectToProcedureSpecificTerm epd:id_2023-S-210-663534_ReviewTerm_7TwSLEC9PvaDEEAmGcz5G4
.

epd:id_2023-S-210-663534_ProcedureIdentifier_aE3iyMRsoF9Qvy4eFQRpLT
  rdf:type                epo:Identifier;
  epo:hasIdentifierValue  "2019/S 039-088890" .

epd:id_2023-S-210-663534_ProcedurePurpose_aE3iyMRsoF9Qvy4eFQRpLT
  rdf:type                    epo:Purpose;
  epo:hasMainClassification   <http://data.europa.eu/cpv/cpv/45236000> .
```

**Resolution**:

Strong match - these are indeed the same procedure (Stuttgart 21 railway project, same lot, same identifier):

```javascript
{
  "type": "EntityResolution",
  "sourceEntityId": "http://data.europa.eu/a4g/resource/id_2023-S-210-663534_Procedure_aE3iyMRsoF9Qvy4eFQRpLT",
  "confidenceLevel": 0.97,
  "requestId": "case5-proc-same-project",
  "canonicalEntity": 
  {
    "type": "http://data.europa.eu/a4g/ontology#Procedure",
    "id": "http://data.europa.eu/a4g/resource/id_2023-S-210-661039_Procedure_aE3iyMRsoF9Qvy4eFQRpLT",
    "entityData": "<SEE BELOW>",
    "entityDataFormat": "text/turtle"
  }
}
```

Canonical entity data:

```javascript
epd:id_2023-S-210-661039_Procedure_aE3iyMRsoF9Qvy4eFQRpLT
  rdf:type                            epo:Procedure;
  epo:foreseesContractSpecificTerm    epd:id_2023-S-210-661039_ContractTermProcedure_fqfw5hANKbaKT6uyGM9WEZ;
  epo:hasID                           epd:id_2023-S-210-661039_ProcedureIdentifier_aE3iyMRsoF9Qvy4eFQRpLT;
  epo:hasProcurementScopeDividedIntoLot epd:id_2023-S-210-661039_Lot_mtBaW8k5EC8G5zB7LwJPww;
  epo:hasPurpose                      epd:id_2023-S-210-661039_ProcedurePurpose_aE3iyMRsoF9Qvy4eFQRpLT;
  epo:hasTitle                        "S21, PA 1.7; Bahntechnik Oberbau Los A , (19FEI37404) 20FEI44393"@de;
  epo:isSubjectToProcedureSpecificTerm epd:id_2023-S-210-661039_ReviewTerm_7TwSLEC9PvaDEEAmGcz5G4
.

epd:id_2023-S-210-661039_ProcedureIdentifier_aE3iyMRsoF9Qvy4eFQRpLT
  rdf:type                epo:Identifier;
  epo:hasIdentifierValue  "2019/S 039-088890" .

epd:id_2023-S-210-661039_ProcedurePurpose_aE3iyMRsoF9Qvy4eFQRpLT
  rdf:type                    epo:Purpose;
  epo:hasMainClassification   <http://data.europa.eu/cpv/cpv/45236000> .
```

---

## Example 6: Procedures with different procedure numbers (Negative case)

This test validates that the ERE correctly identifies distinct procurement procedures at the same institution despite similar descriptions. The procedure number is a crucial discriminator. [Sample data here](../procedures/group4/).

Outcome: distinct entities with low confidence match.

**Request**:

```javascript
{
  "type": "EntityResolutionRequest",
  "entity": 
  { 
    "type": "http://data.europa.eu/a4g/ontology#Procedure",
    "id": "http://data.europa.eu/a4g/resource/id_2023-S-211-665742_Procedure_faF7Q5dyoGpXu3Ru4RGg73",
    "entityData": "<SEE BELOW>",
    "entityDataFormat": "text/turtle"
  },
  "requestId": "case6-neg-diff-procedures",
  "originator": "TED SWS pipeline"
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

No match found above the confidence threshold, the ERE creates a new canonical entity from the incoming entity:

```javascript
{
  "type": "EntityResolution",
  "sourceEntityId": "http://data.europa.eu/a4g/resource/id_2023-S-211-665742_Procedure_faF7Q5dyoGpXu3Ru4RGg73",
  "confidenceLevel": 1.0,
  "requestId": "case6-neg-diff-procedures",
  "canonicalEntity": 
  {
    "type": "http://data.europa.eu/a4g/ontology#Procedure",
    "id": "http://data.europa.eu/a4g/resource/id_2023-S-211-665742_Procedure_faF7Q5dyoGpXu3Ru4RGg73",
    "entityData": "<SAME AS REQUEST>",
    "entityDataFormat": "text/turtle"
  }
}
```
