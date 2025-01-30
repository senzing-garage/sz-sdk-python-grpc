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

The Senzing `sz-sdk-python-grpc` package provides a [Python] Software Development Kit
adhering to the abstract classes of [sz-sdk-python]
that communicates with a [Senzing gRPC server].

[![Python 3.11 Badge]][Python 3.11]
[![PEP8 Badge]][PEP8]
[![PyPI version Badge]][PyPi version]
[![Downloads Badge]][Downloads]
[![License Badge]][License]
[![Coverage Badge]][Coverage]

## Overview

The Senzing `sz-sdk-python-grpc` packages enable Python programs to call Senzing library functions
across a network to a [Senzing gRPC server].

The `sz-sdk-python-grpc` package implements the following [sz-sdk-python] interfaces:

1. [SzConfig]
1. [SzConfigMgr]
1. [SzDiagnostic]
1. [SzEngine]
1. [SzProduct]

Other implementations of the [sz-sdk-python] interface include:

- [sz-sdk-python-core] - for calling Senzing SDK APIs natively

## Use

The following example shows how to start a Senzing gRPC server Docker container
and access it using the `senzing_grpc` Python package.

1. Run a Senzing gRPC service using Docker.

    ```console
    docker run -it --name senzing-serve-grpc -p 8261:8261 --pull always --read-only --rm senzing/serve-grpc
    ```

1. In a separate window, install the `senzing-grpc` Python package.

    ```console
    python3 -m pip install --upgrade senzing-grpc
    ```

1. Start an interactive Python session.

    ```console
    python3
    ```

1. Paste the following into the interactive Python session.

    ```python
    import grpc
    from senzing_grpc import SzAbstractFactoryGrpc
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel=grpc.insecure_channel("localhost:8261"))
    sz_product = sz_abstract_factory.create_product()
    print(sz_product.get_version())
    ```

More can be seen in [Examples].

## References

1. [Development]
1. [Errors]
1. [Examples]
1. Related artifacts:
    1. [DockerHub]
1. [sz-sdk-python package reference]

[Coverage badge]: https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fsenzing-garage%2Fsz-sdk-python%2Fpython-coverage-comment-action-data%2Fendpoint.json
[Coverage]: https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-grpc/blob/python-coverage-comment-action-data/htmlcov/index.html
[Development]: docs/development.md
[DockerHub]: https://hub.docker.com/r/senzing/sz-sdk-python-grpc
[Downloads Badge]: https://static.pepy.tech/badge/senzing-grpc
[Downloads]: https://pepy.tech/project/senzing-grpc
[Errors]: docs/errors.md
[Examples]: docs/examples.md
[License Badge]: https://img.shields.io/badge/License-Apache2-brightgreen.svg
[License]: https://github.com/senzing-garage/sz-sdk-python-grpc/blob/main/LICENSE
[PEP8 Badge]: https://img.shields.io/badge/code%20style-pep8-orange.svg
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[PyPI version Badge]: https://badge.fury.io/py/senzing-grpc.svg
[PyPi version]: https://badge.fury.io/py/senzing-grpc
[Python 3.11 Badge]: https://img.shields.io/badge/python-3.11-blue.svg
[Python 3.11]: https://www.python.org/downloads/release/python-3110/
[Python]: https://www.python.org/
[Senzing Garage]: https://github.com/senzing-garage
[Senzing gRPC server]: https://github.com/senzing-garage/serve-grpc
[Senzing Quick Start guides]: https://docs.senzing.com/quickstart/
[Senzing]: https://senzing.com/
[sz-sdk-python package reference]: https://hub.senzing.com/sz-sdk-python/
[sz-sdk-python-core]: https://github.com/senzing-garage/sz-sdk-python-core
[sz-sdk-python]: https://github.com/senzing-garage/sz-sdk-python/tree/main/src/senzing
[SzConfig]: https://github.com/senzing-garage/sz-sdk-python/blob/main/src/senzing/szconfig.py
[SzConfigMgr]: https://github.com/senzing-garage/sz-sdk-python/blob/main/src/senzing/szconfigmanager.py
[SzDiagnostic]: https://github.com/senzing-garage/sz-sdk-python/blob/main/src/senzing/szdiagnostic.py
[SzEngine]: https://github.com/senzing-garage/sz-sdk-python/blob/main/src/senzing/szengine.py
[SzProduct]: https://github.com/senzing-garage/sz-sdk-python/blob/main/src/senzing/szproduct.py
