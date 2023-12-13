# Makefile extensions for linux.

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

SENZING_TOOLS_DATABASE_URL ?= sqlite3://na:na@/tmp/sqlite/G2C.db

# -----------------------------------------------------------------------------
# OS specific targets
# -----------------------------------------------------------------------------

.PHONY: clean-osarch-specific
clean-osarch-specific:
	@docker rm --force senzing-tools-serve-grpc || true
	@rm -rf $(TARGET_DIRECTORY) || true
	@rm -f $(GOPATH)/bin/$(PROGRAM_NAME) || true


.PHONY: dependencies-osarch-specific
dependencies-osarch-specific:
	python3 -m pip install --upgrade pip
	pip install psutil pytest pytest-cov pytest-schema


.PHONY: hello-world-osarch-specific
hello-world-osarch-specific:
	@echo "Hello World, from linux."


.PHONY: setup-osarch-specific
setup-osarch-specific:
	@docker run \
		--detach \
		--env SENZING_TOOLS_COMMAND=serve-grpc \
		--env SENZING_TOOLS_DATABASE_URL=sqlite3://na:na@/tmp/sqlite/G2C.db \
		--env SENZING_TOOLS_ENABLE_ALL=true \
		--name senzing-tools-serve-grpc \
		--publish 8261:8261 \
		--rm \
		senzing/senzing-tools
	@echo "senzing/senzing-tools server-grpc running in background."

.PHONY: test-osarch-specific
test-osarch-specific:
	@echo "--- Unit tests -------------------------------------------------------"
	@pytest tests/ --verbose --capture=no --cov=src/senzing --cov-report xml:coverage.xml
#	@echo "--- Test examples ----------------------------------------------------"
#	@pytest examples/ --verbose --capture=no --cov=src/senzing
	@echo "--- Test examples using unittest -------------------------------------"
	@python3 -m unittest \
		examples/g2config/*.py \
		examples/g2configmgr/*.py \
		examples/g2diagnostic/*.py \
		examples/g2engine/*.py \
		examples/g2product/*.py


.PHONY: view-sphinx-osarch-specific
view-sphinx-osarch-specific:
	@xdg-open file://$(MAKEFILE_DIRECTORY)/docs/build/html/index.html

# -----------------------------------------------------------------------------
# Makefile targets supported only by this platform.
# -----------------------------------------------------------------------------

.PHONY: only-linux
only-linux:
	@echo "Only linux has this Makefile target."
