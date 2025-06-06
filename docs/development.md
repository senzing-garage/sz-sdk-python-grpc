# sz-sdk-python-grpc development

The following instructions are useful during development.

**Note:** This has been tested on Linux and Darwin/macOS.
It has not been tested on Windows.

## Prerequisites for development

:thinking: The following tasks need to be complete before proceeding.
These are "one-time tasks" which may already have been completed.

1. The following software programs need to be installed:
   1. [git]
   1. [make]
   1. [docker]
   1. [sphinx]

## Install Senzing C library

Since the Senzing library is a prerequisite, it must be installed first.

1. Verify Senzing C shared objects, configuration, and SDK header files are installed.

   1. `/opt/senzing/er/lib`
   1. `/opt/senzing/er/sdk/c`
   1. `/etc/opt/senzing`

1. If not installed, see [How to Install Senzing for Python Development].

## Install Git repository

1. Identify git repository.

   ```console
   export GIT_ACCOUNT=senzing-garage
   export GIT_REPOSITORY=sz-sdk-python-grpc
   export GIT_ACCOUNT_DIR=~/${GIT_ACCOUNT}.git
   export GIT_REPOSITORY_DIR="${GIT_ACCOUNT_DIR}/${GIT_REPOSITORY}"

   ```

1. Using the environment variables values just set, follow
   steps in [clone-repository] to install the Git repository.

## Dependencies

1. A one-time command to install dependencies needed for `make` targets.
   Example:

   ```console
   cd ${GIT_REPOSITORY_DIR}
   make dependencies-for-development

   ```

1. Install dependencies needed for [Python] code.
   Example:

   ```console
   cd ${GIT_REPOSITORY_DIR}
   make dependencies

   ```

1. Install dependencies needed for documentation.
   Example:

   ```console
   cd ${GIT_REPOSITORY_DIR}
   make dependencies-for-documentation

   ```

## Working with grpc and Protobuffer files

After copying files from [sz-sdk-proto/example_generated_source_code/python],
an `import` statement must be modified in each of:

- [szconfig_pb2_grpc.py]
- [szconfigmanager_pb2_grpc.py]
- [szdiagnostic_pb2_grpc.py]
- [szengine_pb2_grpc.py]
- [szproduct_pb2_grpc.py]

Example from [szconfig_pb2_grpc.py]:

Before:

```python
    import szconfig_pb2 as szconfig__pb2
```

After:

```python
    from . import szconfig_pb2 as szconfig__pb2
```

## Lint

1. Run linting.
   Example:

   ```console
   cd ${GIT_REPOSITORY_DIR}
   make lint

   ```

## Build

Not applicable.

## Run

Not applicable.

## Test

1. Run tests.
   Example:

   ```console
   cd ${GIT_REPOSITORY_DIR}
   make clean setup test

   ```

### Test Server-Side TLS

1. Run a gRPC server.
   Either:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make clean setup-server-side-tls test-server-side-tls
    ```

### Test Mutual TLS

1. Run a gRPC server.
   Either:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make clean setup-mutual-tls test-mutual-tls
    ```

   Or:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make clean setup-mutual-tls test-mutual-tls-encrypted-key
    ```

## Coverage

Create a code coverage map.

1. Run Go tests.
   Example:

   ```console
   cd ${GIT_REPOSITORY_DIR}
   make clean setup coverage

   ```

   A web-browser will show the results of the coverage.
   The goal is to have over 80% coverage.

## Documentation

1. View documentation.
   Example:

   ```console
   cd ${GIT_REPOSITORY_DIR}
   make clean documentation

   ```

1. If a web page doesn't appear, run the following command and paste the results into a web browser's address bar.

   ```console
   echo "file://${GIT_REPOSITORY_DIR}/docs/build/html/index.html"
   ```

## Package

1. Build the `wheel` file for distribution.
   Example:

   ```console
   cd ${GIT_REPOSITORY_DIR}
   make package

   ```

1. Activate virtual environment.

   ```console
   cd ${GIT_REPOSITORY_DIR}
   source .venv/bin/activate

   ```

1. Verify that `senzing-grpc` is not installed.
   Example:

   ```console
   python3 -m pip freeze | grep -e senzing-grpc -e senzing_grpc

   ```

   Nothing is returned.

1. Install directly from `wheel` file.
   Example:

   ```console
   python3 -m pip install ${GIT_REPOSITORY_DIR}/dist/*.whl

   ```

1. Verify that `senzing-grpc` is installed.
   Example:

   ```console
   python3 -m pip freeze | grep -e senzing-grpc -e senzing_grpc

   ```

   Example return:

   > senzing-grpc @ file:///home/senzing/senzing-garage.git/sz-sdk-python-grpc/dist/senzing_grpc-0.0.1-py3-none-any.whl#sha256=2a4e5218d66d5be60ee31bfad5943e6611fc921f28a4326d9594ceceae7e0ac1

1. Uninstall the `senzing-grpc` python package.
   Example:

   ```console
   python3 -m pip uninstall senzing-grpc

   ```

1. Deactivate virtual environment.

   ```console
   deactivate

   ```

## Test publish

:warning: This test can only be performed once per versioned release.

1. Test publishing `wheel` file to [Test PyPi].
   Example:

   ```console
   cd ${GIT_REPOSITORY_DIR}
   make publish-test

   ```

1. Visit [Test PyPi] and search for package.

## References

1. [bandit]
1. [black]
1. [coverage]
1. [flake8]
1. [isort]
1. [mypy]
1. [pylint]
1. [pytest]
1. [sphinx]

[bandit]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/bandit.md
[black]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/black.md
[clone-repository]: https://github.com/senzing-garage/knowledge-base/blob/main/HOWTO/clone-repository.md
[coverage]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/coverage.md
[docker]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/docker.md
[flake8]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/flake8.md
[git]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/git.md
[How to Install Senzing for Python Development]: https://github.com/senzing-garage/knowledge-base/blob/main/HOWTO/install-senzing-for-python-development.md
[isort]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/isort.md
[make]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/make.md
[mypy]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/mypy.md
[pylint]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/pylint.md
[pytest]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/pytest.md
[Python]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/python.md
[sphinx]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/sphinx.md
[szconfig_pb2_grpc.py]: ../src/senzing_grpc/pb2_grpc/szconfig_pb2_grpc.py
[szconfigmanager_pb2_grpc.py]: ../src/senzing_grpc/pb2_grpc/szconfigmanager_pb2_grpc.py
[szdiagnostic_pb2_grpc.py]: ../src/senzing_grpc/pb2_grpc/szdiagnostic_pb2_grpc.py
[szengine_pb2_grpc.py]: ../src/senzing_grpc/pb2_grpc/szengine_pb2_grpc.py
[szproduct_pb2_grpc.py]: ../src/senzing_grpc/pb2_grpc/szproduct_pb2_grpc.py
[sz-sdk-proto/example_generated_source_code/python]: https://github.com/senzing-garage/sz-sdk-proto/tree/main/example_generated_source_code/python
[Test PyPi]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/pypi.md#test-pypi
