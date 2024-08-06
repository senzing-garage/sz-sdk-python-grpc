# Makefile for Python project

# Detect the operating system and architecture.

include makefiles/osdetect.mk

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

# "Simple expanded" variables (':=')

# PROGRAM_NAME is the name of the GIT repository.
PROGRAM_NAME := $(shell basename `git rev-parse --show-toplevel`)
MAKEFILE_PATH := $(abspath $(firstword $(MAKEFILE_LIST)))
MAKEFILE_DIRECTORY := $(shell dirname $(MAKEFILE_PATH))
TARGET_DIRECTORY := $(MAKEFILE_DIRECTORY)/target
DIST_DIRECTORY := $(MAKEFILE_DIRECTORY)/dist
BUILD_TAG := $(shell git describe --always --tags --abbrev=0  | sed 's/v//')
BUILD_ITERATION := $(shell git log $(BUILD_TAG)..HEAD --oneline | wc -l | sed 's/^ *//')
BUILD_VERSION := $(shell git describe --always --tags --abbrev=0 --dirty  | sed 's/v//')
DOCKER_CONTAINER_NAME := $(PROGRAM_NAME)
DOCKER_IMAGE_NAME := senzing/$(PROGRAM_NAME)
DOCKER_BUILD_IMAGE_NAME := $(DOCKER_IMAGE_NAME)-build
GIT_REMOTE_URL := $(shell git config --get remote.origin.url)
GIT_REPOSITORY_NAME := $(shell basename `git rev-parse --show-toplevel`)
GIT_VERSION := $(shell git describe --always --tags --long --dirty | sed -e 's/\-0//' -e 's/\-g.......//')
PATH := $(MAKEFILE_DIRECTORY)/bin:$(PATH)

# Conditional assignment. ('?=')
# Can be overridden with "export"
# Example: "export LD_LIBRARY_PATH=/path/to/my/senzing/g2/lib"

LD_LIBRARY_PATH ?= /opt/senzing/g2/lib
PYTHONPATH ?= $(MAKEFILE_DIRECTORY)/src

# Export environment variables.

.EXPORT_ALL_VARIABLES:

# -----------------------------------------------------------------------------
# The first "make" target runs as default.
# -----------------------------------------------------------------------------

.PHONY: default
default: help

# -----------------------------------------------------------------------------
# Operating System / Architecture targets
# -----------------------------------------------------------------------------

-include makefiles/$(OSTYPE).mk
-include makefiles/$(OSTYPE)_$(OSARCH).mk


.PHONY: hello-world
hello-world: hello-world-osarch-specific

# -----------------------------------------------------------------------------
# Dependency management
# -----------------------------------------------------------------------------

.PHONY: dependencies-for-development
dependencies-for-development:
	@python3 -m pip install --upgrade pip
	@python3 -m pip install --requirement development-requirements.txt


.PHONY: dependencies
dependencies:
	@python3 -m pip install --requirement requirements.txt

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

.PHONY: setup
setup: setup-osarch-specific

# -----------------------------------------------------------------------------
# Lint
# -----------------------------------------------------------------------------

.PHONY: lint
lint: pylint mypy bandit black flake8 isort

# -----------------------------------------------------------------------------
# Build
# -----------------------------------------------------------------------------

.PHONY: docker-build
docker-build: docker-build-osarch-specific

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Test
# -----------------------------------------------------------------------------

.PHONY: test
test: test-tests test-examples


.PHONY: test-tests
test-tests:
	$(info --- Unit tests -----------------------------------------------------------------)
	@pytest tests --verbose --capture=no --cov=src --cov-report xml:coverage.xml


.PHONY: test-examples
test-examples:
	$(info --- Test examples --------------------------------------------------------------)
	@python3 -m unittest \
		examples/szconfig/*.py \
		examples/szconfigmanager/*.py \
		examples/szdiagnostic/*.py \
		examples/szengine/*.py \
		examples/szproduct/*.py


.PHONY: docker-test
docker-test:
	@docker-compose -f docker-compose.test.yml up

# -----------------------------------------------------------------------------
# Coverage
# -----------------------------------------------------------------------------

.PHONY: coverage
coverage: coverage-osarch-specific

# -----------------------------------------------------------------------------
# Documentation
# -----------------------------------------------------------------------------

.PHONY: documentation
documentation: documentation-osarch-specific

# -----------------------------------------------------------------------------
# Package
# -----------------------------------------------------------------------------

.PHONY: package
package: clean
	@python3 -m build

# -----------------------------------------------------------------------------
# Publish
# -----------------------------------------------------------------------------

.PHONY: publish-test
publish-test: package
	python3 -m twine upload --repository testpypi dist/*

# -----------------------------------------------------------------------------
# Clean
# -----------------------------------------------------------------------------

.PHONY: clean
clean: clean-osarch-specific

# -----------------------------------------------------------------------------
# Utility targets
# -----------------------------------------------------------------------------

.PHONY: help
help:
	$(info Build $(PROGRAM_NAME) version $(BUILD_VERSION)-$(BUILD_ITERATION))
	$(info Makefile targets:)
	@$(MAKE) -pRrq -f $(firstword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs


.PHONY: print-make-variables
print-make-variables:
	@$(foreach V,$(sort $(.VARIABLES)), \
		$(if $(filter-out environment% default automatic, \
		$(origin $V)),$(warning $V=$($V) ($(value $V)))))

# -----------------------------------------------------------------------------
# Specific programs
# -----------------------------------------------------------------------------

.PHONY: bandit
bandit:
	$(info --- bandit ---------------------------------------------------------------------)
	@bandit $(shell git ls-files '*.py' ':!:tests/*' ':!:docs/source/*' ':!:src/senzing_grpc/pb2_grpc/*')


.PHONY: black
black:
	$(info --- black ----------------------------------------------------------------------)
	@black $(shell git ls-files '*.py' ':!:docs/source/*' ':!:src/senzing_grpc/pb2_grpc/*')


.PHONY: flake8
flake8:
	$(info --- flake8 ---------------------------------------------------------------------)
	@flake8 $(shell git ls-files '*.py' ':!:docs/source/*' ':!:src/senzing_grpc/pb2_grpc/*')


.PHONY: isort
isort:
	$(info --- isort ----------------------------------------------------------------------)
	@isort $(shell git ls-files '*.py' ':!:docs/source/*' ':!:src/senzing_grpc/pb2_grpc/*')


.PHONY: mypy
mypy:
	$(info --- mypy -----------------------------------------------------------------------)
	@mypy --strict $(shell git ls-files '*.py' ':!:docs/source/*' ':!:src/senzing_grpc/pb2_grpc/*')


.PHONY: pydoc
pydoc:
	$(info --- pydoc ----------------------------------------------------------------------)
	@python3 -m pydoc


.PHONY: pydoc-web
pydoc-web:
	$(info --- pydoc-web ------------------------------------------------------------------)
	@python3 -m pydoc -p 8885


.PHONY: pylint
pylint:
	$(info --- pylint ---------------------------------------------------------------------)
	@pylint $(shell git ls-files '*.py' ':!:docs/source/*' ':!:src/senzing_grpc/pb2_grpc/*')


.PHONY: pytest
pytest:
	$(info --- pytest ---------------------------------------------------------------------)
	@pytest $(shell git ls-files '*.py' ':!:docs/source/*' ':!:src/senzing_grpc/pb2_grpc/*')


.PHONY: sphinx
sphinx: sphinx-osarch-specific
	$(info --- sphinx ---------------------------------------------------------------------)


.PHONY: view-sphinx
view-sphinx: view-sphinx-osarch-specific
	$(info --- view-sphinx ----------------------------------------------------------------)
