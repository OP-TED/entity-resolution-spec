# Test Data

This directory contains test data for the Entity Resolution System, including manual deduplication of organizations and procedures from RDF tender notices.

- Organization matching normalizes company suffixes (Ltd, Corp, etc.)
- Procedure matching normalizes whitespace and removes common words like "procedure"
- Similarity threshold was set to 90%
- The title of entities in each group may differ

## Overview

The test data consists of three main directories:

### 1. `notices/` - Deduplicated RDF Tender Notices

Contains manual deduplication results for organizations and procedures from RDF tender notices. The duplication was done using fuzzy string matching with manual checking of the results.

#### Structure

```
test_data/notices/
├── deduplicated_organizations/
│   ├── group1/
│   ├── group2/
│   ├── group3/
│   └── group4/  # Renamed from previous group5; previous group4 was removed
│
└── deduplicated_procedures/
    ├── group1/
    ├── group2/
    ├── group3/
    └── group4/
```

### 2. `organizations/` - Extracted Organization Entities

Contains extracted organization RDF triples from the deduplicated notices. Each file contains only direct `org:Organization` entities and their first-level properties (no nested child entities).

#### Structure

```
test_data/organizations/
├── group1/   (3 files)
│   ├── 661238-2023.ttl
│   ├── 662860-2023.ttl
│   └── 663653-2023.ttl
├── group2/   (2 files)
├── group3/   (3 files)
├── group4/   (2 files)  # renamed from previous group5; previous group4 was removed
└── (no group5)
```

**Content**: Each file contains only:
- `org:Organization` entities with their direct properties
- Property URIs and values (identifiers, legal names, registered addresses, etc.)
- No nested entities - references to related entities are preserved but not their full data

### 3. `procedures/` - Extracted Procedure Entities

Contains extracted procedure RDF triples from the deduplicated notices. Each file contains only direct `epo:Procedure` entities and their first-level properties (no nested child entities).

#### Structure

```
test_data/procedures/
├── group1/   (3 files)
│   ├── 662861-2023.ttl
│   ├── 663131-2023.ttl
│   └── 664733-2023.ttl
├── group2/   (2 files)
├── group3/   (2 files)
└── group4/   (2 files)
```

**Content**: Each file contains only:
- `epo:Procedure` entities with their direct properties
- Property URIs and values (titles, descriptions, IDs, types, etc.)
- No nested entities - references to related entities are preserved but not their full data

## Deduplication Notes

The test data was prepared with the following methodology:

- **Organization matching**: Normalizes company suffixes (Ltd, Corp, etc.)
- **Procedure matching**: Normalizes whitespace and removes common words like "procedure"
- **Similarity threshold**: Set to 90%
- **Validation**: Manual checking of fuzzy matching results
- **Entity title variations**: The title of entities in each group may differ while referring to the same organization or procedure

## File Format

All test data files are in **Turtle (TTL)** format, which is a W3C standard for representing RDF data in a human-readable format.

### Example TTL Structure

**Organization example** - Direct properties only:

```turtle
@prefix org: <http://www.w3.org/ns/org#> .
@prefix epo: <http://data.europa.eu/a4g/ontology#> .
@prefix cccev: <http://data.europa.eu/m8g/> .

epd:OrganisationExample a org:Organization ;
    epo:hasID epd:IdExample ;
    epo:hasLegalName "Example Corporation"@en ;
    cccev:registeredAddress epd:AddressExample .
    # Note: epd:AddressExample is referenced but not defined in this file
```

**Procedure example** - Direct properties only:

```turtle
@prefix epo: <http://data.europa.eu/a4g/ontology#> .
@prefix epd: <http://data.europa.eu/a4g/resource/> .

epd:ProcedureExample a epo:Procedure ;
    epo:hasTitle "Example Procurement"@en ;
    epo:hasID epd:ProcedureIdExample ;
    epo:hasProcedureType <http://publications.europa.eu/resource/authority/procurement-procedure-type/open> ;
    epo:hasPurpose epd:PurposeExample .
    # Note: Related entities are referenced but not included
```

## Extraction Scope

The organizations and procedures folders contain **first-level entity triples only**:

- **Organizations**: Only `org:Organization` entities with their direct properties
- **Procedures**: Only `epo:Procedure` entities with their direct properties

Related entity references (like addresses, identifiers, etc.) are preserved as URIs but their detailed triples are not included. This provides a focused dataset for entity resolution tasks without the complexity of nested relationships.

## Usage

These test data files can be used to:

1. **Test entity extraction algorithms** - Verify that extraction logic correctly identifies organizations/procedures at the entity level
2. **Develop deduplication strategies** - Use grouped data to evaluate entity resolution approaches
3. **Validate RDF processing** - Test RDF parsing and entity-level filtering code
4. **Benchmark comparison algorithms** - Measure performance on focused entity data
5. **Entity linking** - Work with entity references to resolve duplicates across groups

## Data Quality Notes

- All TTL files are valid RDF/Turtle format
- Triples include namespace prefixes for standard vocabularies
- Related child entities are referenced by URI but their full triples are not included in the extracted files
- No triples have been modified from their original sources (only filtered/extracted)
