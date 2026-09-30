# Analysing the ERS examples


## Select basic info about an organisation

Use `?org a org:Organization` to find organisation URIs.

```sql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX org: <http://www.w3.org/ns/org#>
prefix epd: <http://data.europa.eu/a4g/resource/>

SELECT * WHERE {
  bind ( epd:id_2023-S-210-661197_ContractorOrganisation_WFzZGbdirSo5EBhCMeQqCo AS ?myorg )
  ?myorg ?p ?o

} LIMIT 1000
```


## Drill down an organisation

```sql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX org: <http://www.w3.org/ns/org#>
prefix epd: <http://data.europa.eu/a4g/resource/>
PREFIX cccev: <http://data.europa.eu/m8g/>

CONSTRUCT {
  ?myorg ?p ?o.
  ?o ?p1 ?o1.
  ?o1 ?p2 ?o2
}
WHERE {
  # If you remove it, the next line will yied info about all organisations
  #
  bind ( epd:id_2023-S-210-661197_ContractorOrganisation_WFzZGbdirSo5EBhCMeQqCo AS ?myorg )

  ?myorg a org:Organization.
  ?myorg ?p ?o.

  # Add this to find couple of orgs both in the test dataset
  # ?myorg owl:sameAs ?org2.
  # ?org2 a org:Organization.


  OPTIONAL { 
    ?o ?p1 ?o1. 
    OPTIONAL { ?o1 ?p2 ?o2. }
  }
} LIMIT 1000
```

## Organisation results

```turtle
epd:id_2023-S-210-661197_ContractorOrganisationAddress_WFzZGbdirSo5EBhCMeQqCo
        rdf:type            locn:Address;
        epo:hasCountryCode  <http://publications.europa.eu/resource/authority/country/USA>;
        locn:postName       "New York" .

epd:id_2023-S-210-661197_ContractorOrganisation_WFzZGbdirSo5EBhCMeQqCo
        rdf:type                 org:Organization;
        epo:hasLegalName         "s&P Global Market Intelligence LLC"@fr;
        cccev:registeredAddress  epd:id_2023-S-210-661197_ContractorOrganisationAddress_WFzZGbdirSo5EBhCMeQqCo;
        owl:sameAs               epd:id_2023-S-210-661197_ContractorOrganisation_WFzZGbdirSo5EBhCMeQqCo .
```


## Equivalent entities having different names

```sql
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX org: <http://www.w3.org/ns/org#>
prefix epd: <http://data.europa.eu/a4g/resource/>
PREFIX cccev: <http://data.europa.eu/m8g/>
PREFIX epo:   <http://data.europa.eu/a4g/ontology#>

SELECT DISTINCT ?type ?ent1 ?ent2 ?name1 ?name2
WHERE {
  
  # BIND ( org:Organization AS ?type ) # Uncomment if you want a specific type

  ?ent2 owl:sameAs ?ent2.

  ?ent1 a ?type.
  ?ent2 a ?type.

  ?ent1 epo:hasLegalName ?name1.
  ?ent2 epo:hasLegalName ?name2.
  
  FILTER ( ?name1 != ?name2 ) 
}
ORDER BY ?type
```

## All the types in sameAs relations

```sql
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX org: <http://www.w3.org/ns/org#>
prefix epd: <http://data.europa.eu/a4g/resource/>

SELECT DISTINCT ?type
WHERE {
  ?e1 owl:sameAs ?e2.

  { ?e1 a ?type. } 
  UNION { ?e2 a ?type. }
} LIMIT 1000
```