# entity-resolution-spec
Formal software contract, shared data models, sample messages, and compliance tests required for integrating new Entity Resolution Engines (EREs) into the system.

## Installation

To get started, you need a UNIX-compatible environment (Mac/Linux/WSL2) with Make, Python and [Poetry](https://python-poetry.org/). You can then use the following command to setup your environment:

```bash
make install
```

This will install the necessary user dependencies in a Poetry-managed virtual environment.


## Development

This project uses principles of model-driven development (MDD) and domain-driven design (DDD). The core model is defined in the `resources/linkml` directory, and the Python (Pydantic) models (pluralized to refer to all the classes as is the practice in the programming community) are generated using the [LinkML](https://linkml.io/) framework.

The generated Python models can be found in the `src/models` directory. 
You can regenerate both the LinkML-based models (Python, JSONSchema) and the navigable documentation, by running:

```bash
make all
```

*the Makefile has more granular targets, see its content for details*.


## Running and Testing

TODO: this will be added in future. Right now, this repository contains
specifications only and does not have runnable unit tests.


## Test data

### Deduplicated notices

This repository contains manual deduplication for organizations and procedures from RDF tender notices. The duplication was done using fuzzy string matching with manual checking of the results.

[Details here](./test/test_data/README.md)
