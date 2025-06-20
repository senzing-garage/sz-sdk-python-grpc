# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-grpc/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                   |    Stmts |     Miss |   Cover |   Missing |
|--------------------------------------- | -------: | -------: | ------: | --------: |
| src/senzing\_grpc/\_\_init\_\_.py      |        7 |        0 |    100% |           |
| src/senzing\_grpc/szabstractfactory.py |       33 |        0 |    100% |           |
| src/senzing\_grpc/szconfig.py          |       60 |        6 |     90% |65, 114-115, 149-151 |
| src/senzing\_grpc/szconfigmanager.py   |       92 |        9 |     90% |107-108, 115-116, 123-124, 185-187 |
| src/senzing\_grpc/szdiagnostic.py      |       53 |        8 |     85% |93-94, 124-127, 133-134 |
| src/senzing\_grpc/szengine.py          |      292 |       52 |     82% |105-106, 113-114, 145-146, 154-162, 171-172, 179-185, 194-195, 325-326, 340-341, 382-383, 390-391, 435-436, 449-450, 460-461, 518-527, 566-567, 584-587, 593-594 |
| src/senzing\_grpc/szhelpers.py         |       46 |        8 |     83% |49, 53-55, 81, 88-89, 108 |
| src/senzing\_grpc/szproduct.py         |       37 |        7 |     81% |84-85, 92-93, 109-111 |
|                              **TOTAL** |  **620** |   **90** | **85%** |           |


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