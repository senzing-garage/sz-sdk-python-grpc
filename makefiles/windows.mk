# Makefile extensions for windows.

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

SENZING_TOOLS_DATABASE_URL ?= sqlite3://na:na@nowhere/C:\Temp\sqlite\G2C.db

# -----------------------------------------------------------------------------
# OS specific targets
# -----------------------------------------------------------------------------

.PHONY: clean-osarch-specific
clean-osarch-specific:
	del /F /S /Q $(DIST_DIRECTORY)
	del /F /S /Q $(MAKEFILE_DIRECTORY)/__pycache__
	del /F /S /Q $(MAKEFILE_DIRECTORY)/coverage.xml
	del /F /S /Q $(TARGET_DIRECTORY)


.PHONY: dependencies-osarch-specific
dependencies-osarch-specific:
	python3 -m pip install --upgrade pip
	pip install psutil pytest pytest-cov pytest-schema


.PHONY: hello-world-osarch-specific
hello-world-osarch-specific:
	@echo "Hello World, from windows."


.PHONY: setup-osarch-specific
setup-osarch-specific:


.PHONY: test-osarch-specific
test-osarch-specific:
	@echo "--- Unit tests -------------------------------------------------------"
	@pytest tests/ --verbose --capture=no --cov=src/senzing_grpc
	@echo "--- Test examples ----------------------------------------------------"
	@pytest examples/ --verbose --capture=no --cov=src/senzing_grpc


.PHONY: view-sphinx-osarch-specific
view-sphinx-osarch-specific:
	@xdg-open file://$(MAKEFILE_DIRECTORY)/docs/build/html/index.html

# -----------------------------------------------------------------------------
# Makefile targets supported only by this platform.
# -----------------------------------------------------------------------------

.PHONY: only-windows
only-windows:
	@echo "Only windows has this Makefile target."
