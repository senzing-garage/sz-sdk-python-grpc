# sz-sdk-python-grpc

If you are beginning your journey with [Senzing],
please start with [Senzing Quick Start guides].

You are in the [Senzing Garage] where projects are "tinkered" on.
Although this GitHub repository may help you understand an approach to using Senzing,
it's not considered to be "production ready" and is not considered to be part of the Senzing product.
Heck, it may not even be appropriate for your application of Senzing!

## :warning: WARNING: sz-sdk-python-grpc is still in development :warning: _

At the moment, this is "work-in-progress" with Semantic Versions of `0.n.x`.
Although it can be reviewed and commented on,
the recommendation is not to use it yet.

## Synopsis

The Senzing `sz-sdk-python-grpc` package provides a Python Software Development Kit
adhering to the abstract classes of [sz-sdk-python-abstract]
that communicates with a [Senzing gRPC server].

[![Python 3.11 Badge]][Python 3.11]
[![PEP8 Badge]][PEP8]
[![PyPI version Badge]][PyPi version]
[![Downloads Badge]][Downloads]

## Overview

The Senzing `sz-sdk-python-grpc` packages enable Python programs to call Senzing library functions
across a network to a [Senzing gRPC server].

The `sz-sdk-python-grpc` package implements the following [sz-sdk-python-abstract] interfaces:

1. [SzConfigAbstract]
1. [SzConfigMgrAbstract]
1. [SzDiagnosticAbstract]
1. [SzEngineAbstract]
1. [SzProductAbstract]

Other implementations of the [sz-sdk-python-abstract] interface include:

- [sz-sdk-python] - for calling Senzing SDK APIs natively

## Use

The following example shows how to start a Senzing gRPC server Docker container
and access it using the `senzing_grpc` Python package.

1. Install the `senzing-grpc` Python package.
   Example:

    ```console
    python3 -m pip install --upgrade senzing-grpc
    ```

1. Run a Senzing gRPC service using Docker.
   Example:

    ```console
    docker run \
      --env SENZING_TOOLS_COMMAND=serve-grpc \
      --env SENZING_TOOLS_DATABASE_URL=sqlite3://na:na@nowhere/tmp/sqlite/G2C.db \
      --env SENZING_TOOLS_ENABLE_ALL=true \
      --name senzing-tools-serve-grpc \
      --publish 8261:8261 \
      --pull always \
      --rm \
      senzing/senzing-tools
    ```

   **Note:** In this example, `SENZING_TOOLS_DATABASE_URL` specifies a file *inside* the container.
   Thus the database is temporal and will be deleted when the container is killed.

1. In a separate window, start an interactive Python session.
   Example:

    ```console
    python3
    ```

1. Paste the following into the interactive Python session.
   Example:

    ```python
    import grpc
    from senzing_grpc import SzAbstractFactory
    sz_abstract_factory = SzAbstractFactory(grpc_channel=grpc.insecure_channel("localhost:8261"))
    sz_product = sz_abstract_factory.create_sz_product()
    print(sz_product.get_version())

    ```

More can be seen in [Examples].

## References

1. [Development]
1. [Errors]
1. [Examples]
1. Related artifacts:
    1. [DockerHub]
1. [sz-sdk-python-abstract package reference]

[Development]: docs/development.md
[DockerHub]: https://hub.docker.com/r/senzing/template-python
[Downloads Badge]: https://static.pepy.tech/badge/senzing-grpc
[Downloads]: https://pepy.tech/project/senzing-grpc
[Errors]: docs/errors.md
[Examples]: docs/examples.md
[PEP8 Badge]: https://img.shields.io/badge/code%20style-pep8-orange.svg
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[PyPI version Badge]: https://badge.fury.io/py/senzing-grpc.svg
[PyPi version]: https://badge.fury.io/py/senzing-grpc
[Python 3.11 Badge]: https://img.shields.io/badge/python-3.11-blue.svg
[Python 3.11]: https://www.python.org/downloads/release/python-3110/
[Senzing Garage]: https://github.com/senzing-garage
[Senzing gRPC server]: https://github.com/senzing-garage/servegrpc
[Senzing Quick Start guides]: https://docs.senzing.com/quickstart/
[Senzing]: https://senzing.com/
[sz-sdk-python-abstract package reference]: https://hub.senzing.com/sz-sdk-python-abstract/
[sz-sdk-python-abstract]: https://github.com/senzing-garage/sz-sdk-python-abstract/tree/main/src/senzing_abstract
[sz-sdk-python]: https://github.com/senzing-garage/sz-sdk-python
[SzConfigAbstract]: https://github.com/senzing-garage/sz-sdk-python-abstract/blob/main/src/senzing_abstract/szconfig_abstract.py
[SzConfigMgrAbstract]: https://github.com/senzing-garage/sz-sdk-python-abstract/blob/main/src/senzing_abstract/szconfigmanager_abstract.py
[SzDiagnosticAbstract]: https://github.com/senzing-garage/sz-sdk-python-abstract/blob/main/src/senzing_abstract/szdiagnostic_abstract.py
[SzEngineAbstract]: https://github.com/senzing-garage/sz-sdk-python-abstract/blob/main/src/senzing_abstract/szengine_abstract.py
[SzProductAbstract]: https://github.com/senzing-garage/sz-sdk-python-abstract/blob/main/src/senzing_abstract/szproduct_abstract.py
