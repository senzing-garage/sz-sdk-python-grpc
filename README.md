# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-grpc/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                   |    Stmts |     Miss |   Cover |   Missing |
|--------------------------------------- | -------: | -------: | ------: | --------: |
| src/senzing\_grpc/\_\_init\_\_.py      |        7 |        0 |    100% |           |
| src/senzing\_grpc/szabstractfactory.py |       35 |        0 |    100% |           |
| src/senzing\_grpc/szconfig.py          |       63 |        6 |     90% |65, 117-118, 152-154 |
| src/senzing\_grpc/szconfigmanager.py   |      101 |        9 |     91% |110-111, 119-120, 128-129, 194-196 |
| src/senzing\_grpc/szdiagnostic.py      |       56 |        8 |     86% |95-96, 127-130, 136-137 |
| src/senzing\_grpc/szengine.py          |      325 |       44 |     86% |107-108, 116-117, 150-151, 160-168, 178-179, 187-193, 203-204, 341-342, 357-358, 402-403, 411-412, 475-476, 487-488, 599-600, 617-620, 626-627 |
| src/senzing\_grpc/szhelpers.py         |       72 |        9 |     88% |56, 60-62, 90, 97-98, 117, 155 |
| src/senzing\_grpc/szproduct.py         |       39 |        7 |     82% |85-86, 94-95, 111-113 |
|                              **TOTAL** |  **698** |   **83** | **88%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-grpc/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-grpc/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fsenzing-garage%2Fsz-sdk-python-grpc%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-grpc/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.