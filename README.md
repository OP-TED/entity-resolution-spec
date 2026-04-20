# Entity Resolution Specifications

Formal software contract, shared data models, sample messages, and compliance tests required for integrating new Entity Resolution Engines (EREs) into Entity Resolution System.


## Requirements

- UNIX-compatible environment (Linux/macOS/WSL2)
- Make
- Python 3.12+
- [Poetry](https://python-poetry.org/) (for dependency management)

## Quick Start

```bash
make install      # install dependencies via Poetry
make all          # generate all models, schemas, and documentation
```

## Make targets overview

- `install`: install dependencies via Poetry
- `all`: generate all models, schemas, and documentation
- `generate-models`: regenerate Pydantic models and JSON Schema from LinkML
- `generate-docs`: regenerate documentation
- `lint`: run ruff linter on source code
- `lint-schema`: run LinkML linter on YAML schemas
- `clean`: remove all generated artifacts

## Installation

To get started, you need a UNIX-compatible environment (Mac/Linux/WSL2) with Make, Python and [Poetry](https://python-poetry.org/). You can then use the following command to setup your environment:

```bash
make install
```

This will install the necessary user dependencies in a Poetry-managed virtual environment.


## Development

This project uses principles of model-driven development (MDD) and domain-driven design (DDD). The core models are defined in the `src/resources/schemas` directory using [LinkML](https://linkml.io/), and the Python (Pydantic) models are generated from these specifications.

Generated Python models are in `src/erspec/models`. Regenerate them with:

```bash
make all
```

This regenerates both the LinkML-based models (Python, JSONSchema) and the navigable documentation. See the Makefile for more granular targets.


## Gherkin Specification

This repository contains Gherkin feature files under `test/features/` that serve as a formal specification of the expected behaviour of the ERE. They describe the observable contract between ERS and ERE at specification level — independent of any particular ERE implementation — and may serve as the basis for implementing acceptance tests for a conformant ERE.


## Test data

### Deduplicated notices

This repository contains manual deduplication for organizations and procedures from RDF tender notices. The duplication was done using fuzzy string matching with manual checking of the results.

[Details here](./test/test_data/README.md)

## Documentation Overview

Documentation resources for understanding the model, architecture, and interfaces:

### Model Schema Docs
See [docs/schema/README.md](docs/schema/README.md) — canonical data model and service schema documentation generated from the ERS–ERE definitions.

### Architectural Diagrams
See [docs/architecture/diagrams/README.md](docs/architecture/diagrams/README.md) — prescribed architectural diagrams illustrating system structure and components.

### Sequence Diagrams (Mermaid)
See [docs/architecture/sequence_diagrams/README.md](docs/architecture/sequence_diagrams/README.md) — Mermaid-format sequence diagrams describing key system interactions.

### Informative Interface Sequence
See [docs/ere-interface-seq-diag.md](docs/ere-interface-seq-diag.md) — informative sequence overview for ERS–ERE interactions.
Note: the ERS–ERE contract is the normative specification; this file is provided for additional context.

