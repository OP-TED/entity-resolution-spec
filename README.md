# Entity Resolution Specifications
Formal software contract, shared data models, sample messages, and compliance tests required for integrating new Entity Resolution Engines (EREs) into the system.

> Note: Active development continues in the OP-TED repository: https://github.com/OP-TED/entity-resolution-spec

## Requirements

- UNIX-compatible environment (Linux/macOS/WSL2)
- Make
- Python (managed via [uv](https://docs.astral.sh/uv/getting-started/installation/))

## Quick Start

```bash
make             # installs user dependencies via uv
make install-dev # installs development tooling (tests, lint, codegen)
make generate_models
make generate_docs
```

## Make targets overview

- install: user dependencies
- install-dev: dev dependencies (tests, lint, LinkML codegen)
- generate_models: regenerate Pydantic models from LinkML
- generate_docs: regenerate documentation

## Installation

To get started, you need a UNIX-compatible environment (Mac/Linux/WSL2) with Make. You can then use the following command:

```bash
make
```

This will run the first and default Make target `make install`, which installs the necessary _user_ dependencies with the [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager.

To install the development dependencies, you can run:

```bash
make install-dev
```

This will install the additional dependencies required for development, such as testing and linting tools, including LinkML for codegen (see below).

## Development

This project uses model-driven development (MDD) and domain-driven design (DDD). The core model is defined in `resources/linkml`, and Python (Pydantic) models are generated using the [LinkML](https://linkml.io/) framework.

Generated Python models are in `src/models`. Regenerate them with:

```bash
make generate_models
```

Regenerate documentation with:

```bash
make generate_docs
```

## Running and Testing

TODO: this will be added in future. Right now, this repository contains
specifications only and does not have runnable unit tests.


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

