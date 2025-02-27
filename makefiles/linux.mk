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
coverage-osarch-specific: export SENZING_LOG_LEVEL=TRACE
coverage-osarch-specific:
	@$(activate-venv); pytest --cov=src --cov-report=xml --ignore=src/senzing_grpc/pb2_grpc/  $(shell git ls-files '*.py' ':!:src/senzing_grpc/pb2_grpc/*')
	@$(activate-venv); coverage html --omit=src/senzing_grpc/pb2_grpc/*
	@xdg-open $(MAKEFILE_DIRECTORY)/htmlcov/index.html 1>/dev/null 2>&1


.PHONY: dependencies-for-development-osarch-specific
dependencies-for-development-osarch-specific:


.PHONY: dependencies-for-documentation-osarch-specific
dependencies-for-documentation-osarch-specific:


.PHONY: documentation-osarch-specific
documentation-osarch-specific:
	@$(activate-venv); cd docs; rm -rf build; make html
	@xdg-open file://$(MAKEFILE_DIRECTORY)/docs/build/html/index.html  1>/dev/null 2>&1


.PHONY: hello-world-osarch-specific
hello-world-osarch-specific:
	$(info Hello World, from linux.)


.PHONY: package-osarch-specific
package-osarch-specific:
	@$(activate-venv); python3 -m build


.PHONY: setup-osarch-specific
setup-osarch-specific:
	docker run \
		--detach \
		--env SENZING_TOOLS_DATABASE_URL="sqlite3://na:na@nowhere/tmp/sqlite/G2C.db?mode=memory&cache=shared" \
		--env SENZING_TOOLS_ENABLE_ALL=true \
		--name senzing-serve-grpc \
		--publish 8261:8261 \
		--rm \
		senzing/serve-grpc
	$(info "senzing/serve-grpc running in background.")


.PHONY: test-osarch-specific
test-osarch-specific:
	$(info --- Unit tests -------------------------------------------------------)
	@$(activate-venv); pytest tests/ --verbose --capture=no --cov=src --cov-report xml:coverage.xml
	$(info --- Test examples using pytest -------------------------------------)
	@$(activate-venv); pytest \
		examples/misc/ \
		examples/extras/ \
		examples/szabstractfactory/ \
		examples/szconfig/ \
		examples/szconfigmanager/ \
		examples/szdiagnostic/ \
		examples/szengine/ \
		examples/szproduct/ \
		--capture=no \
		-o python_files=*.py \
		--verbose; \
		pytest_exit_code="$$?"; \
		if [ "$$pytest_exit_code" -eq 5 ]; then \
			printf '\nExit code from pytest was %s, this is expected testing the examples if there were no Python errors\n' "$$pytest_exit_code"; \
			exit 0; \
		else \
			exit "$$pytest_exit_code"; \
		fi

.PHONY: test-server-side-tls-osarch-specific
test-server-side-tls-osarch-specific: export SENZING_TOOLS_CA_CERTIFICATE_PATH=$(MAKEFILE_DIRECTORY)/testdata/certificates/certificate-authority/certificate.pem
test-server-side-tls-osarch-specific:
	$(info --- Unit tests -------------------------------------------------------)
	@$(activate-venv); pytest tests/ --verbose --capture=no --cov=src --cov-report xml:coverage.xml
	$(info --- Test examples using pytest -------------------------------------)
	@$(activate-venv); pytest \
		examples/misc/ \
		examples/extras/ \
		examples/szabstractfactory/ \
		examples/szconfig/ \
		examples/szconfigmanager/ \
		examples/szdiagnostic/ \
		examples/szengine/ \
		examples/szproduct/ \
		--capture=no \
		-o python_files=*.py \
		--verbose; \
		pytest_exit_code="$$?"; \
		if [ "$$pytest_exit_code" -eq 5 ]; then \
			printf '\nExit code from pytest was %s, this is expected testing the examples if there were no Python errors\n' "$$pytest_exit_code"; \
			exit 0; \
		else \
			exit "$$pytest_exit_code"; \
		fi

.PHONY: test-osarch-specific-2
test-osarch-specific-2:
	$(info --- Unit tests -------------------------------------------------------)
	@$(activate-venv); pytest tests/ --verbose --capture=no --cov=src/senzing_grpc --cov-report xml:coverage.xml
	$(info --- Test examples using unittest -------------------------------------)
	@$(activate-venv); python3 -m unittest \
		examples/szconfig/*.py \
		examples/szconfigmanager/*.py \
		examples/szdiagnostic/*.py \
		examples/szengine/*.py \
		examples/szproduct/*.py


.PHONY: test-examples-2
test-examples-2:
	$(info --- Test examples using unittest -------------------------------------)
	@$(activate-venv); python3 -m unittest \
		examples/misc/add_truthset_datasources.py \
		examples/misc/add_truthset_data.py


.PHONY: venv-osarch-specific
venv-osarch-specific:
	@python3 -m venv .venv

# -----------------------------------------------------------------------------
# Makefile targets supported only by this platform.
# -----------------------------------------------------------------------------

.PHONY: only-linux
only-linux:
	$(info Only linux has this Makefile target.)
