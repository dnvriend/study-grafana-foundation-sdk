.PHONY: help
.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

up: init ## docker compose up
	@docker compose up -d

down: ## docker compose down
	@docker compose down

restart: down up ## down and up
	
logs: ## show alloy logs
	@docker compose logs grafana -f

generate: clean ## generate dashboards
	@find src -name "*.py" -exec python3 {} \;

clean: init ## clean generated dashboards
	@rm -rf build/*

init: ## initialize project
	@mkdir -p build
	@uv sync
