# Analysis of ERS Sample Data

This folder has some analysis/inspection we have done on the provided sample data for the ERS System, with a focus on ERE.

The folder contains:

* [ere-test-cases.md](ere-test-cases.md): test cases based on the sample data. These are a base for Gherkin and unit tests.

* [queries.md](queries.md): various SPARQL queries I made against the TDB that I loaded with all the files in [notices](../notices).

Old files:

* [same-as-entities.tsv](same-as-entities.tsv): sameAs entities having different names, with a name similarity score. We have considered these as cases where the future ERE will need to find equivalence bases on various criteria (name similarity, address, etc).

* [test-case-candidates.md](test-case-candidates.md): data that are interesting to build Gherkin and unit test cases. Initially based on queries against the whole sample dataset and in particular on the `same-as-entities.tsv` file.
