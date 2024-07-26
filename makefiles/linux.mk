# Makefile extensions for linux.

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

PATH := $(MAKEFILE_DIRECTORY)/bin:$(PATH)

# -----------------------------------------------------------------------------
# OS specific targets
# -----------------------------------------------------------------------------

.PHONY: clean-osarch-specific
clean-osarch-specific:
	@docker rm  --force senzing-serve-grpc 2> /dev/null || true
	@rm -f  $(MAKEFILE_DIRECTORY)/.coverage || true
	@rm -f  $(MAKEFILE_DIRECTORY)/coverage.xml || true
	@rm -fr $(DIST_DIRECTORY) || true
	@rm -fr $(MAKEFILE_DIRECTORY)/.mypy_cache || true
	@rm -fr $(MAKEFILE_DIRECTORY)/.pytest_cache || true
	@rm -fr $(MAKEFILE_DIRECTORY)/dist || true
	@rm -fr $(MAKEFILE_DIRECTORY)/docs/build || true
	@rm -fr $(MAKEFILE_DIRECTORY)/htmlcov || true
	@rm -fr $(TARGET_DIRECTORY) || true
	@find . | grep -E "(/__pycache__$$|\.pyc$$|\.pyo$$)" | xargs rm -rf


.PHONY: coverage-osarch-specific
coverage-osarch-specific:
	@pytest --cov=src --cov-report=xml  $(shell git ls-files '*.py'   )
	@coverage html
	@xdg-open $(MAKEFILE_DIRECTORY)/htmlcov/index.html


.PHONY: hello-world-osarch-specific
hello-world-osarch-specific:
	$(info "Hello World, from linux.")


.PHONY: setup-osarch-specific
setup-osarch-specific:
	@docker run \
		--detach \
		--env SENZING_TOOLS_DATABASE_URL=sqlite3://na:na@/tmp/sqlite/G2C.db \
		--env SENZING_TOOLS_ENABLE_ALL=true \
		--name senzing-serve-grpc \
		--publish 8261:8261 \
		--rm \
		--user root \
		senzing/serve-grpc
	$(info "senzing/serve-grpc running in background.")


.PHONY: test-osarch-specific-2
test-osarch-specific-2:
	@echo "--- Unit tests -------------------------------------------------------"
	@pytest tests/ --verbose --capture=no --cov=src/senzing_grpc --cov-report xml:coverage.xml
	# @echo "--- Test examples ----------------------------------------------------"
	# @pytest examples/ --verbose --capture=no --cov=src/senzing_grpc
	@echo "--- Test examples using unittest -------------------------------------"
	@python3 -m unittest \
		examples/szconfig/*.py \
		examples/szconfigmanager/*.py \
		examples/szdiagnostic/*.py \
		examples/szengine/*.py \
		examples/szproduct/*.py


.PHONY: test-examples-2
test-examples-2:
	@echo "--- Test examples using unittest -------------------------------------"
	@python3 -m unittest \
		examples/misc/add_truthset_datasources.py \
		examples/misc/add_truthset_data.py


.PHONY: sphinx-osarch-specific
sphinx-osarch-specific:
	@cd docs; rm -rf build; make html


.PHONY: view-sphinx-osarch-specific
view-sphinx-osarch-specific:
	@xdg-open file://$(MAKEFILE_DIRECTORY)/docs/build/html/index.html

# -----------------------------------------------------------------------------
# Makefile targets supported only by this platform.
# -----------------------------------------------------------------------------

.PHONY: only-linux
only-linux:
	$(info "Only linux has this Makefile target.")
