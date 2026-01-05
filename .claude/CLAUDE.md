# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `sz-sdk-python-grpc`, a Python SDK that provides gRPC-based access to Senzing entity resolution services. It implements the abstract interfaces from `sz-sdk-python` and communicates with a Senzing gRPC server (Docker container `senzing/serve-grpc`).

**Status**: Work-in-progress (Semantic Version 0.n.x) - part of Senzing Garage (experimental projects).

## Common Commands

```bash
# Install development dependencies (one-time setup)
make dependencies-for-development

# Run all linters (pylint, mypy, bandit, black, flake8, isort)
make lint

# Run tests (starts Docker gRPC server, runs pytest)
make clean setup test

# Run a single test file
.venv/bin/pytest tests/szengine_test.py -v

# Run a specific test
.venv/bin/pytest tests/szengine_test.py::test_add_record -v

# Generate coverage report with HTML
make clean setup coverage

# TLS test variants
make clean setup-server-side-tls test-server-side-tls
make clean setup-mutual-tls test-mutual-tls

# Build wheel package
make package

# Build Sphinx documentation
make documentation
```

## Architecture

```console
Python Application
    ↓
SzAbstractFactoryGrpc (creates all interface instances)
    ├── SzConfigGrpc        - Configuration schema management
    ├── SzConfigManagerGrpc - Config lifecycle (CRUD, default config)
    ├── SzDiagnosticGrpc    - System diagnostics, repository info
    ├── SzEngineGrpc        - Entity resolution (add/get/delete records, search, export)
    └── SzProductGrpc       - Product metadata (version, license)
    ↓
gRPC Channel (insecure or TLS)
    ↓
senzing/serve-grpc Docker container
```

**Source structure**: `src/senzing_grpc/` contains all implementation files.

**Key pattern**: All SDK methods use the `@catch_sdk_exceptions` decorator from `szhelpers.py` which converts gRPC errors to Senzing SDK exceptions (SzError subclasses).

**Proto definitions**: Uses `senzing_grpc_protobuf` package - request/response objects like `szengine_pb2.AddRecordRequest()`.

## Testing Requirements

- Tests require a running gRPC server: `make setup` starts `senzing/serve-grpc` Docker container on port 8261
- Test files are in `tests/` directory
- Examples in `examples/` are also run as tests
- Linters exclude `docs/source/*` and `src/senzing_grpc/pb2_grpc/*`

## Code Style

- Line length: 120 characters
- Type checking: mypy strict mode enabled
- Formatting: black, isort (profile=black)
- Python: >=3.10

## Senzing Claude Commands

Reference `/senzing` for available commands: `changelog-update`, `code-review`, `github-issue-fix-proposal`.
