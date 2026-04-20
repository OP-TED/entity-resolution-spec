SHELL=/bin/bash -o pipefail

# Forwarding wrapper — all targets are delegated to src/Makefile.
# Run `make -C src help` to see available targets.
.PHONY: $(MAKECMDGOALS) _forward
.DEFAULT_GOAL := _forward

$(MAKECMDGOALS):
	@$(MAKE) -C src $@

_forward:
	@$(MAKE) -C src
