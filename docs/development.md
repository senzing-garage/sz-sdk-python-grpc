# g2-sdk-python-grpc development

The following instructions are used when modifying and building the Docker image.

## Prerequisites for development

:thinking: The following tasks need to be complete before proceeding.
These are "one-time tasks" which may already have been completed.

1. The following software programs need to be installed:
    1. [git](https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/git.md)
    1. [make](https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/make.md)
    1. [docker](https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/docker.md)

## Clone repository

For more information on environment variables,
see [Environment Variables](https://github.com/senzing-garage/knowledge-base/blob/main/lists/environment-variables.md).

1. Set these environment variable values:

    ```console
    export GIT_ACCOUNT=senzing-garage
    export GIT_REPOSITORY=g2-sdk-python-grpc
    export GIT_ACCOUNT_DIR=~/${GIT_ACCOUNT}.git
    export GIT_REPOSITORY_DIR="${GIT_ACCOUNT_DIR}/${GIT_REPOSITORY}"
    ```

1. Using the environment variables values just set, follow steps in [clone-repository](https://github.com/senzing-garage/knowledge-base/blob/main/HOWTO/clone-repository.md) to install the Git repository.

## Working with Python wheel file

1. Build the `wheel` file for distribution.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make package
    ```

1. Verify that `senzing-grpc` is not installed.
   Example:

    ```console
    python3 -m pip freeze | grep senzing_grpc
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
    python3 -m pip freeze | grep senzing_grpc
    ```

    Example return:
    > senzing-grpc @ file:///home/senzing/senzing-garage.git/g2-sdk-python-grpc/dist/senzing_grpc-0.0.1-py3-none-any.whl#sha256=2a4e5218d66d5be60ee31bfad5943e6611fc921f28a4326d9594ceceae7e0ac1

1. Uninstall the `senzing-grpc` python package.
   Example:

    ```console
    python3 -m pip uninstall senzing-grpc
    ```
