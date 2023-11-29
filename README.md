# g2-sdk-python-grpc

## :warning: WARNING: g2-sdk-python-grpc is still in development :warning: _

At the moment, this is "work-in-progress" with Semantic Versions of `0.n.x`.
Although it can be reviewed and commented on,
the recommendation is not to use it yet.

## Synopsis

The Senzing `g2-sdk-python-grpc` package provides a Python Software Development Kit
adhering to the abstract classes of
[g2-sdk-python-next](https://github.com/Senzing/g2-sdk-python-next/tree/main/src/senzing)
that communicates with a
[Senzing gRPC server](https://github.com/Senzing/servegrpc).

## Overview

The Senzing `g2-sdk-python-grpc` packages enable Python programs to call Senzing library functions
across a network to a
[Senzing gRPC server](https://github.com/Senzing/servegrpc).

The `g2-sdk-python-grpc` package implement thes following
[g2-sdk-python](https://github.com/Senzing/fixme)
interfaces:

1. [G2config](https://github.com/Senzing/g2-sdk-python-next/blob/main/src/senzing/g2config_abstract.py)
1. [G2configmgr](https://github.com/Senzing/g2-sdk-python-next/blob/main/src/senzing/g2configmgr_abstract.py)
1. [G2diagnostic](https://github.com/Senzing/g2-sdk-python-next/blob/main/src/senzing/g2diagnostic_abstract.py)
1. [G2engine](https://github.com/Senzing/g2-sdk-python-next/blob/main/src/senzing/g2engine_abstract.py)
1. [G2product](https://github.com/Senzing/g2-sdk-python-next/blob/main/src/senzing/g2product_abstract.py)

Other implementations of the
[g2-sdk-python](https://github.com/Senzing/fixme)
interface include:

- [g2-sdk-python-next](https://github.com/Senzing/g2-sdk-python-next) - for
  calling Senzing SDK APIs natively

## Use

(TODO:)

## References

1. [Development](docs/development.md)
1. [Errors](docs/errors.md)
1. [Examples](docs/examples.md)
1. [g2-sdk-python-next package reference](https://hub.senzing.com/g2-sdk-python-next/)
