# g2-sdk-python-grpc

If you are beginning your journey with
[Senzing](https://senzing.com/),
please start with
[Senzing Quick Start guides](https://docs.senzing.com/quickstart/).

You are in the
[Senzing Garage](https://github.com/senzing-garage)
where projects are "tinkered" on.
Although this GitHub repository may help you understand an approach to using Senzing,
it's not considered to be "production ready" and is not considered to be part of the Senzing product.
Heck, it may not even be appropriate for your application of Senzing!

## :warning: WARNING: g2-sdk-python-grpc is still in development :warning: _

At the moment, this is "work-in-progress" with Semantic Versions of `0.n.x`.
Although it can be reviewed and commented on,
the recommendation is not to use it yet.

## Synopsis

The Senzing `g2-sdk-python-grpc` package provides a Python Software Development Kit
adhering to the abstract classes of
[g2-sdk-python-abstract](https://github.com/senzing-garage/g2-sdk-python-abstract/tree/main/src/senzing_abstract)
that communicates with a
[Senzing gRPC server](https://github.com/senzing-garage/servegrpc).

## Overview

The Senzing `g2-sdk-python-grpc` packages enable Python programs to call Senzing library functions
across a network to a
[Senzing gRPC server](https://github.com/senzing-garage/servegrpc).

The `g2-sdk-python-grpc` package implements the following
[g2-sdk-python-abstract](https://github.com/senzing-garage/g2-sdk-python-abstract/tree/main/src/senzing_abstract)
interfaces:

1. [G2ConfigAbstract](https://github.com/senzing-garage/g2-sdk-python-abstract/blob/main/src/senzing_abstract/g2config_abstract.py)
1. [G2ConfigMgrAbstract](https://github.com/senzing-garage/g2-sdk-python-abstract/blob/main/src/senzing_abstract/g2configmgr_abstract.py)
1. [G2DiagnosticAbstract](https://github.com/senzing-garage/g2-sdk-python-abstract/blob/main/src/senzing_abstract/g2diagnostic_abstract.py)
1. [G2EngineAbstract](https://github.com/senzing-garage/g2-sdk-python-abstract/blob/main/src/senzing_abstract/g2engine_abstract.py)
1. [G2ProductAbstract](https://github.com/senzing-garage/g2-sdk-python-abstract/blob/main/src/senzing_abstract/g2product_abstract.py)

Other implementations of the
[g2-sdk-python-abstract](https://github.com/senzing-garage/g2-sdk-python-abstract/tree/main/src/senzing_abstract)
interface include:

- [g2-sdk-python-next](https://github.com/senzing-garage/g2-sdk-python-next) - for
  calling Senzing SDK APIs natively

## Use

The following example shows how to start a Senzing gRPC server Docker container
and access it using the `senzing_grpc` Python package.

1. Install the `senzing-grpc` Python package.
   If the `senzing-grpc` Python package is already installed,
   this step is not necessary.
   Example:

    ```console
    python3 -m pip install --upgrade senzing-grpc
    ```

1. Run a Senzing gRPC service using Docker.
   Example:

    ```console
    docker run \
      --env SENZING_TOOLS_COMMAND=serve-grpc \
      --env SENZING_TOOLS_DATABASE_URL=sqlite3://na:na@/tmp/sqlite/G2C.db \
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
    from senzing_grpc import G2ProductGrpc
    g2_product = G2ProductGrpc(grpc_channel=grpc.insecure_channel("localhost:8261"))
    print(g2_product.version())
    ```

More can be seen in
[Examples](docs/examples.md).

## References

1. [Development](docs/development.md)
1. [Errors](docs/errors.md)
1. [Examples](docs/examples.md)
1. [g2-sdk-python-abstract package reference](http://hub.senzing.com/g2-sdk-python-abstract/)
