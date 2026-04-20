SHELL=/bin/bash -o pipefail

# ─── Formatting ──────────────────────────────────────────────────────────────────

BUILD_PRINT  = \e[1;34m
END_PRINT    = \e[0m

ICON_DONE     = $(BUILD_PRINT)$(END_PRINT) [✔]
ICON_ERROR    = $(BUILD_PRINT)$(END_PRINT) [✗]
ICON_PROGRESS = $(BUILD_PRINT)$(END_PRINT) [-]

define log_progress
	@printf "$(ICON_PROGRESS) $(BUILD_PRINT)$(1)$(END_PRINT)\n"
endef

define log_done
	@printf "$(ICON_DONE) $(BUILD_PRINT)$(1)$(END_PRINT)\n"
endef

# ─── Paths & Naming ─────────────────────────────────────────────────────────────
# Root-relative paths — used by Make for dependency tracking only.
# Recipes use src/-relative paths via `cd src &&`.

SCHEMAS_DIR    = src/resources/schemas
SCRIPTS_DIR    = src/resources/scripts
TEMPLATES_DIR  = src/resources/templates
MODELS_DIR     = src/erspec/models

ERE_SCHEMA_NAME  = ere-service-schema
CORE_SCHEMA_NAME = core-schema
JSON_SCHEMA_NAME = er-schema

ERE_SCHEMA_PATH    = $(SCHEMAS_DIR)/$(ERE_SCHEMA_NAME).yaml
CORE_SCHEMA_PATH   = $(SCHEMAS_DIR)/$(CORE_SCHEMA_NAME).yaml
ALL_SCHEMA_SOURCES = $(ERE_SCHEMA_PATH) $(CORE_SCHEMA_PATH)

PYTHON_ERE_MODEL  = $(MODELS_DIR)/ere.py
PYTHON_CORE_MODEL = $(MODELS_DIR)/core.py
JSON_SCHEMA_PATH  = $(SCHEMAS_DIR)/$(JSON_SCHEMA_NAME).json

MODEL_DOCS_DIR    = docs/schema
MODEL_DOCS_README = $(MODEL_DOCS_DIR)/README.md

# ─── Help ────────────────────────────────────────────────────────────────────────

.PHONY: help
help:
	@echo ""
	@echo "Usage:"
	@echo "  make <target>"
	@echo ""
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*##"; printf ""} \
		/^[a-zA-Z0-9_-]+:.*##/ { \
			printf "  \033[1;34m%-20s\033[0m %s\n", $$1, $$2 \
		}' $(MAKEFILE_LIST)

# ─── Setup ───────────────────────────────────────────────────────────────────────

.PHONY: install
install: ## Install dependencies using Poetry
	$(call log_progress,Installing dependencies using Poetry...)
	@cd src && poetry sync
	$(call log_done,Dependencies installed.)

# ─── Quality ─────────────────────────────────────────────────────────────────────

.PHONY: lint
lint: ## Run ruff linter on source code
	$(call log_progress,Running ruff checks...)
	@cd src && poetry run ruff check erspec/
	$(call log_done,Ruff checks completed.)

.PHONY: lint-schema
lint-schema: ## Run LinkML linter on YAML schemas
	$(call log_progress,Linting LinkML schemas...)
	@cd src && poetry run linkml lint --ignore-warnings resources/schemas/$(ERE_SCHEMA_NAME).yaml
	@cd src && poetry run linkml lint --ignore-warnings resources/schemas/$(CORE_SCHEMA_NAME).yaml
	$(call log_done,LinkML schema lint completed.)

# ─── Aggregate targets ──────────────────────────────────────────────────────────

.PHONY: all
all: generate-models generate-doc ## Generate all artefacts (models + docs)
	$(call log_done,All artefacts generated.)

.PHONY: generate-models
generate-models: $(PYTHON_ERE_MODEL) $(JSON_SCHEMA_PATH) ## Generate Python models and JSON Schema
	$(call log_done,All models generated.)

.PHONY: generate-doc
generate-doc: $(MODEL_DOCS_README) ## Generate schema documentation and diagrams
	$(call log_done,Documentation generated.)

# ─── Python Pydantic models ──────────────────────────────────────────────────────

$(PYTHON_ERE_MODEL) $(PYTHON_CORE_MODEL) &: $(ALL_SCHEMA_SOURCES)
	$(call log_progress,Generating Python models...)
	@mkdir -p $(MODELS_DIR)
	@cd src && poetry run python resources/scripts/generate_models.py \
		--schema resources/schemas/$(ERE_SCHEMA_NAME).yaml \
		--output erspec/models/ere.py \
		--template-dir resources/templates \
		--schemas-dir resources/schemas
	@cd src && poetry run ruff check --fix erspec/models/
	$(call log_done,Python models generated.)

# ─── JSON Schema ─────────────────────────────────────────────────────────────────

$(JSON_SCHEMA_PATH): $(ALL_SCHEMA_SOURCES)
	$(call log_progress,Generating JSON Schema...)
	@mkdir -p $(dir $(JSON_SCHEMA_PATH))
	@cd src && poetry run linkml generate json-schema --indent 2 \
		resources/schemas/$(ERE_SCHEMA_NAME).yaml > resources/schemas/$(JSON_SCHEMA_NAME).json
	$(call log_done,JSON Schema generated -> $(JSON_SCHEMA_PATH))

# ─── Documentation & PlantUML diagrams ──────────────────────────────────────────

$(MODEL_DOCS_README): $(ALL_SCHEMA_SOURCES)
	$(call log_progress,Generating schema documentation...)
	@mkdir -p $(MODEL_DOCS_DIR)
	@cd src && poetry run linkml generate doc resources/schemas/$(ERE_SCHEMA_NAME).yaml \
		-d ../docs/schema --index-name README
	@cd src && poetry run linkml generate plantuml \
		-d ../docs/schema --format svg resources/schemas/$(ERE_SCHEMA_NAME).yaml
	$(call log_done,Documentation generated -> $(MODEL_DOCS_DIR))

# ─── Clean ───────────────────────────────────────────────────────────────────────

.PHONY: clean-models
clean-models: ## Remove all generated models
	$(call log_progress,Cleaning generated models...)
	@rm -f $(PYTHON_ERE_MODEL) $(PYTHON_CORE_MODEL) $(JSON_SCHEMA_PATH)
	$(call log_done,Generated models cleaned.)

.PHONY: clean-doc
clean-doc: ## Remove generated docs and diagrams
	$(call log_progress,Cleaning generated documentation...)
	@rm -rf $(MODEL_DOCS_DIR)/*.md $(MODEL_DOCS_DIR)/*.svg
	$(call log_done,Generated documentation cleaned.)

.PHONY: clean
clean: clean-models clean-doc ## Remove all generated files
	$(call log_done,All generated files cleaned.)
