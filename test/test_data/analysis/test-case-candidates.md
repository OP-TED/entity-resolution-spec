## Organsiations

### Case 1, Minor variations

* `epd:id_2023-S-210-661238_ReviewerOrganisation_LLhJHMi9mby8ixbkfyGoWj`
* `epd:id_2023-S-210-662860_ReviewerOrganisation_LLhJHMi9mby8ixbkfyGoWj`

* Same legal name
* Same address
* Same contact point

* **Result**: they should be considered equivalent, high confidence.


### Case 2, Organisations with case-different names

* `http://data.europa.eu/a4g/resource/id_2023-S-210-661039_ContractorOrganisation_KoxN6kkynnWenCXubDp4jC, http://data.europa.eu/a4g/resource/id_2023-S-210-661039_ContractorOrganisationModification_4jxq5KuyAaGTzG5CNj9Ycp`


* Names differ by case only
* Same address

* **Result**: they should be considered equivalent, high confidence.


### Case 3, Organisations with different names, different addresses

* `<http://data.europa.eu/a4g/resource/id_2023-S-210-661197_ReviewerOrganisation_bdZjimbzCaRXbeYeBmF94j>`
* `<http://data.europa.eu/a4g/resource/id_2023-S-210-663952_ReviewProcedureInformationProviderOrganisation_eP5uWDhd4iYABCZbaj8dzQ>`

* Names are similar
* Addresses are similar

* **Result**: They shouldn't match, since "Greffe de Tribunal" is a department of "Tribunal" 


### Case 4, Procedures with fundamental fields matching

* `epd:id_2023-S-210-662861_Procedure_faF7Q5dyoGpXu3Ru4RGg73`
* `epd:id_2023-S-210-663131_Procedure_faF7Q5dyoGpXu3Ru4RGg73`

* Same identifier value
* Same title
* Same description
* Same classification

* **Result**: they should be considered equivalent, high confidence.


### Case 5, Procedures with same title

* `epd:id_2023-S-210-663534_Procedure_aE3iyMRsoF9Qvy4eFQRpLT`
* `epd:id_2023-S-210-661039_Procedure_aE3iyMRsoF9Qvy4eFQRpLT`

* Other properties/paths that might be used for similarity:

* `epo:hasProcurementScopeDividedIntoLot/*` 
  * Lots have identical titles, identical ID values
	* `epo:isFundedBy` points to funds with identical titles

* **Result**: they should be considered equivalent, high/moderate confidence.


### Case 6, Negative match between procedures

* `epd:id_2023-S-211-665742_Procedure_faF7Q5dyoGpXu3Ru4RGg73` 
* `epd:id_2023-S-211-665798_Procedure_faF7Q5dyoGpXu3Ru4RGg73`

* Titles are: "Procedimento n.º 239X000350", "Procedimento n.º 239X000323". 
* They're likely different procedures

* **Result**: they shouldn't match.
