SHELL=/bin/bash -o pipefail

BUILD_PRINT = \e[1;34m
END_BUILD_PRINT = \e[0m

ICON_DONE = [✔]
ICON_ERROR = [x]
ICON_WARNING = [!]
ICON_PROGRESS = [-]

LINKML_MODEL_NAME=ers-core
LINKML_MODEL_VERSION=0.1.0
PYTHON_MODEL_NAME=ers_core

LINKML_MODEL_DIR=resources/schema
LINKML_MODEL=$(LINKML_MODEL_DIR)/$(LINKML_MODEL_NAME)_v$(LINKML_MODEL_VERSION).yaml
PYTHON_MODEL_DIR=src/models
CORE_MODEL=$(PYTHON_MODEL_DIR)/$(PYTHON_MODEL_NAME).py
JSON_SCHEMA_MODEL=$(LINKML_MODEL_DIR)/$(PYTHON_MODEL_NAME).json
DOCS_DIR=docs
MODEL_DOCS_DIR=$(DOCS_DIR)/schema

#-----------------------------------------------------------------------------
# Dev commands
#-----------------------------------------------------------------------------
install: check-uv
	@ echo "Installing dependencies using uv..."
	@ uv sync --no-dev

install-dev: check-uv
	@ echo "Installing dependencies using uv..."
	@ uv sync

check-uv:
	@ command -v uv >/dev/null 2>&1 || { \
		echo "uv not found. Installing uv..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	}

# CI should also generate the docs if a change is found in models
generate_models: $(LINKML_MODEL_DIR) $(PYTHON_MODEL_DIR)
	@ gen-pydantic $(LINKML_MODEL) > $(CORE_MODEL)
	@ gen-json-schema --indent 2 $(LINKML_MODEL) > $(JSON_SCHEMA_MODEL)

generate_markdown_docs: $(MODEL_DOCS_DIR)
# Changing default index name from index.md to README.md, since the github browser automatically shows the latter name
# when entering the MODEL_DOCS_DIR
	@ gen-doc $(LINKML_MODEL) -d $(MODEL_DOCS_DIR) --index-name README
# TODO: Probably we want PNG instead, but it doesn't work yet (https://github.com/linkml/linkml/issues/3009)
	@ gen-plantuml -d $(MODEL_DOCS_DIR) --format svg $(LINKML_MODEL)
	
# (Brandizi) I've played with it, but the result isn't great (single-class diagrams in each 
# class file)
# @ gen-doc -d $(MODEL_DOCS_DIR) --diagram-type plantuml_class_diagram $(LINKML_MODEL)
  
	
clean_docs:
	@ echo "Cleaning up generated documentation..."
	@ rm -rf $(MODEL_DOCS_DIR)/*.md

clean: clean_docs
