.DEFAULT_GOAL := help
SHELL := /bin/bash

MOCHI_ROOT := $(abspath ../..)
RUNNER := $(MOCHI_ROOT)/cmd/leetcode-runner

.PHONY: run build range test clean help run-rkt run-hs

run: ## Run a problem. Usage: make run ID=<n>
@if [ -z "$(ID)" ]; then echo "❌ Usage: make run ID=<n>"; exit 1; fi
@go run $(RUNNER) run $(ID)

build: ## Build and run one problem in language. Usage: make build ID=<n> LANG=go
@if [ -z "$(ID)" ]; then echo "❌ Usage: make build ID=<n> LANG=<lang>"; exit 1; fi
@go run $(RUNNER) build --id $(ID) $(if $(LANG),--lang $(LANG)) --run

run-java: ## Execute the compiled Java solution for problem n. Usage: make run-java ID=<n>
@if [ -z "$(ID)" ]; then echo "❌ Usage: make run-java ID=<n>"; exit 1; fi
@go run $(RUNNER) build --id $(ID) --lang java --run

run-rkt: ## Execute the compiled Racket solution for problem n. Usage: make run-rkt ID=<n>
@if [ -z "$(ID)" ]; then echo "❌ Usage: make run-rkt ID=<n>"; exit 1; fi
@go run $(RUNNER) build --id $(ID) --lang rkt --run

run-hs: ## Execute the compiled Haskell solution for problem n. Usage: make run-hs ID=<n>
@if [ -z "$(ID)" ]; then echo "❌ Usage: make run-hs ID=<n>"; exit 1; fi
@go run $(RUNNER) build --id $(ID) --lang hs --run

range: ## Build problems in range. Usage: make range FROM=1 TO=100 LANG=go
@go run $(RUNNER) build --from $(FROM) --to $(TO) $(if $(LANG),--lang $(LANG)) --run

test: ## Run tests for all problems
@go run $(RUNNER) test

clean:
@rm -rf ../leetcode-out
@echo "🧹 Cleaned build outputs"

help:
@echo ""
@echo "📦 \033[1mMochi LeetCode Makefile\033[0m"
@echo "Usage: make [target] [VAR=val]"
@echo ""
@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'

