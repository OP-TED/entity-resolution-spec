SHELL=/bin/bash -o pipefail

# Virtual environment paths
VENV_DIR=.venv
VENV_BIN=$(VENV_DIR)/bin

BUILD_PRINT = \e[1;34m
END_BUILD_PRINT = \e[0m

ICON_DONE = [✔]
ICON_ERROR = [x]
ICON_WARNING = [!]
ICON_PROGRESS = [-]

# Directory definitions
LINKML_MODEL_DIR=resources/schema
PYTHON_MODEL_DIR=src/models
JSON_SCHEMA_DIR=specs/json-schema
DOCS_DIR=docs
MODEL_DOCS_DIR=$(DOCS_DIR)/schema

# Find all LinkML YAML models dynamically
LINKML_MODELS=$(wildcard $(LINKML_MODEL_DIR)/*.yaml)
LINKML_MODEL_NAMES=$(notdir $(LINKML_MODELS))

# Generate output file paths for each model
PYTHON_MODELS=$(patsubst $(LINKML_MODEL_DIR)/%.yaml,$(PYTHON_MODEL_DIR)/%.py,$(LINKML_MODELS))
JSON_SCHEMAS=$(patsubst $(LINKML_MODEL_DIR)/%.yaml,$(JSON_SCHEMA_DIR)/%.json,$(LINKML_MODELS))
MARKDOWN_DOCS=$(patsubst $(LINKML_MODEL_DIR)/%.yaml,$(MODEL_DOCS_DIR)/%/README.md,$(LINKML_MODELS))
PLANTUML_DIAGRAMS=$(patsubst $(LINKML_MODEL_DIR)/%.yaml,$(MODEL_DOCS_DIR)/%.svg,$(LINKML_MODELS))

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

#-----------------------------------------------------------------------------
# Pattern rules for LinkML model transformations
#-----------------------------------------------------------------------------

# Generate Python Pydantic models from LinkML YAML
$(PYTHON_MODEL_DIR)/%.py: $(LINKML_MODEL_DIR)/%.yaml | $(PYTHON_MODEL_DIR)
	@ echo "$(ICON_PROGRESS) Generating Python model from $<..."
	@ $(VENV_BIN)/gen-pydantic $< > $@
	@ echo "$(ICON_DONE) Generated: $@"

# Generate JSON Schema from LinkML YAML
$(JSON_SCHEMA_DIR)/%.json: $(LINKML_MODEL_DIR)/%.yaml | $(JSON_SCHEMA_DIR)
	@ echo "$(ICON_PROGRESS) Generating JSON Schema from $<..."
	@ $(VENV_BIN)/gen-json-schema --indent 2 $< > $@
	@ echo "$(ICON_DONE) Generated: $@"

# Generate Markdown documentation from LinkML YAML
$(MODEL_DOCS_DIR)/%/README.md: $(LINKML_MODEL_DIR)/%.yaml | $(MODEL_DOCS_DIR)
	@ echo "$(ICON_PROGRESS) Generating Markdown docs from $<..."
	@ $(VENV_BIN)/gen-doc $< -d $(MODEL_DOCS_DIR)/$* --index-name README
	@ echo "$(ICON_DONE) Generated: $@"

# Generate PlantUML diagrams from LinkML YAML
$(MODEL_DOCS_DIR)/%.svg: $(LINKML_MODEL_DIR)/%.yaml | $(MODEL_DOCS_DIR)
	@ echo "$(ICON_PROGRESS) Generating PlantUML diagram from $<..."
	@ $(VENV_BIN)/gen-plantuml -d $(MODEL_DOCS_DIR) --format svg $<
	@ echo "$(ICON_DONE) Generated: $@"

#-----------------------------------------------------------------------------
# Directory creation
#-----------------------------------------------------------------------------
$(PYTHON_MODEL_DIR) $(JSON_SCHEMA_DIR) $(MODEL_DOCS_DIR):
	@ mkdir -p $@

#-----------------------------------------------------------------------------
# Aggregated targets
#-----------------------------------------------------------------------------

# Generate all Python models
generate_python_models: $(PYTHON_MODELS)
	@ echo "$(ICON_DONE) All Python models generated"

# Generate all JSON Schemas
generate_json_schemas: $(JSON_SCHEMAS)
	@ echo "$(ICON_DONE) All JSON Schemas generated"

# Generate all documentation (Markdown + PlantUML)
generate_markdown_docs: $(MARKDOWN_DOCS) $(PLANTUML_DIAGRAMS)
	@ echo "$(ICON_DONE) All documentation generated"

# Generate all model artifacts (Python, JSON Schema, Docs, Diagrams)
generate_models: generate_python_models generate_json_schemas generate_markdown_docs
	@ echo "$(BUILD_PRINT)═══════════════════════════════════════════════════════$(END_BUILD_PRINT)"
	@ echo "$(BUILD_PRINT)✓ All LinkML models transformed successfully$(END_BUILD_PRINT)"
	@ echo "$(BUILD_PRINT)═══════════════════════════════════════════════════════$(END_BUILD_PRINT)"

#-----------------------------------------------------------------------------
# Validation targets
#-----------------------------------------------------------------------------

# Validate and lint all LinkML schemas
# Step 1: Validate YAML syntax
# Step 2: Check best practices and potential issues with linkml-lint
lint-models:
	@ echo "$(ICON_PROGRESS) [1/2] Validating LinkML schemas..."
	@ $(VENV_BIN)/linkml-lint --validate $(LINKML_MODEL_DIR)
	@ echo "$(ICON_DONE) Schema Validation complete"
	@ echo ""
	@ echo "$(ICON_PROGRESS) [2/2] Linting LinkML schemas..."
	@ $(VENV_BIN)/linkml-lint $(LINKML_MODEL_DIR)
	@ echo "$(ICON_DONE) Schema linting complete"


#-----------------------------------------------------------------------------
# Cleanup targets
#-----------------------------------------------------------------------------

clean_python_models:
	@ echo "Cleaning up generated Python models..."
	@ rm -rf $(PYTHON_MODEL_DIR)/*.py

clean_json_schemas:
	@ echo "Cleaning up generated JSON Schemas..."
	@ rm -rf $(JSON_SCHEMA_DIR)/*.json

clean_docs:
	@ echo "Cleaning up generated documentation..."
	@ rm -rf $(MODEL_DOCS_DIR)/*

clean: clean_python_models clean_json_schemas clean_docs
	@ echo "$(ICON_DONE) Cleanup complete"
