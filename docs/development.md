# g2-sdk-python-grpc development

The following instructions are used when modifying and building the Docker image.

## Prerequisites for development

:thinking: The following tasks need to be complete before proceeding.
These are "one-time tasks" which may already have been completed.

1. The following software programs need to be installed:
    1. [git](https://github.com/Senzing/knowledge-base/blob/main/WHATIS/git.md)
    1. [make](https://github.com/Senzing/knowledge-base/blob/main/WHATIS/make.md)
    1. [docker](https://github.com/Senzing/knowledge-base/blob/main/WHATIS/docker.md)

## Clone repository

For more information on environment variables,
see [Environment Variables](https://github.com/Senzing/knowledge-base/blob/main/lists/environment-variables.md).

1. Set these environment variable values:

    ```console
    export GIT_ACCOUNT=senzing
    export GIT_REPOSITORY=g2-sdk-python-grpc
    export GIT_ACCOUNT_DIR=~/${GIT_ACCOUNT}.git
    export GIT_REPOSITORY_DIR="${GIT_ACCOUNT_DIR}/${GIT_REPOSITORY}"
    ```

1. Using the environment variables values just set, follow steps in [clone-repository](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/clone-repository.md) to install the Git repository.

## Working with Python wheel file

1. xxx

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make package
    ```

1. xxx

    ```console
    python3 -m pip freeze | grep senzing_grpc
    ```

1. xxx

    ```console
    python3 -m pip install ${GIT_REPOSITORY_DIR}/dist/*.whl
    ```

1. xxx

    ```console
    python3 -m pip
    ```
