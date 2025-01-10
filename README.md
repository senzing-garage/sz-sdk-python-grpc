# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-grpc/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                      |    Stmts |     Miss |   Cover |   Missing |
|---------------------------------------------------------- | -------: | -------: | ------: | --------: |
| src/senzing\_grpc/\_\_init\_\_.py                         |        7 |        0 |    100% |           |
| src/senzing\_grpc/pb2\_grpc/\_\_init\_\_.py               |        0 |        0 |    100% |           |
| src/senzing\_grpc/pb2\_grpc/szconfig\_pb2.py              |       42 |       32 |     24% |     23-54 |
| src/senzing\_grpc/pb2\_grpc/szconfig\_pb2\_grpc.py        |       78 |       35 |     55% |15-16, 19, 79-81, 85-87, 91-93, 97-99, 103-105, 109-111, 115-117, 121-161, 179, 206, 233, 260, 287, 314, 341 |
| src/senzing\_grpc/pb2\_grpc/szconfigmanager\_pb2.py       |       38 |       28 |     26% |     23-50 |
| src/senzing\_grpc/pb2\_grpc/szconfigmanager\_pb2\_grpc.py |       70 |       31 |     56% |15-16, 19, 74-76, 80-82, 86-88, 92-94, 98-100, 104-106, 110-145, 163, 190, 217, 244, 271, 298 |
| src/senzing\_grpc/pb2\_grpc/szdiagnostic\_pb2.py          |       34 |       24 |     29% |     23-46 |
| src/senzing\_grpc/pb2\_grpc/szdiagnostic\_pb2\_grpc.py    |       62 |       27 |     56% |15-16, 19, 69-71, 75-77, 81-83, 87-89, 93-95, 99-129, 147, 174, 201, 228, 255 |
| src/senzing\_grpc/pb2\_grpc/szengine\_pb2.py              |      146 |      136 |      7% |    23-158 |
| src/senzing\_grpc/pb2\_grpc/szengine\_pb2\_grpc.py        |      286 |      139 |     51% |15-16, 19, 209-211, 215-217, 221-223, 227-229, 233-235, 239-241, 245-247, 251-253, 257-259, 263-265, 269-271, 275-277, 281-283, 287-289, 293-295, 299-301, 305-307, 311-313, 317-319, 323-325, 329-331, 335-337, 341-343, 347-349, 353-355, 359-361, 365-367, 371-373, 377-379, 383-385, 389-391, 395-397, 401-403, 407-577, 595, 622, 649, 676, 703, 730, 757, 784, 811, 838, 865, 892, 919, 946, 973, 1000, 1027, 1054, 1081, 1108, 1135, 1162, 1189, 1216, 1243, 1270, 1297, 1324, 1351, 1378, 1405, 1432, 1459 |
| src/senzing\_grpc/pb2\_grpc/szproduct\_pb2.py             |       22 |       12 |     45% |     23-34 |
| src/senzing\_grpc/pb2\_grpc/szproduct\_pb2\_grpc.py       |       38 |       15 |     61% |15-16, 19, 54-56, 60-62, 66-81, 99, 126 |
| src/senzing\_grpc/szabstractfactory.py                    |       36 |        0 |    100% |           |
| src/senzing\_grpc/szconfig.py                             |       70 |        5 |     93% |100-101, 136-138 |
| src/senzing\_grpc/szconfigmanager.py                      |       63 |        7 |     89% |107-108, 115-116, 125-127 |
| src/senzing\_grpc/szdiagnostic.py                         |       53 |        8 |     85% |92-93, 113-116, 125-126 |
| src/senzing\_grpc/szengine.py                             |      286 |       50 |     83% |102-103, 110-111, 145-146, 154-162, 171-172, 179-185, 194-195, 318-319, 333-334, 375-376, 383-384, 424-427, 441-442, 455-456, 466-467, 485-486, 529-538 |
| src/senzing\_grpc/szhelpers.py                            |       36 |        6 |     83% |50, 54-56, 77-78 |
| src/senzing\_grpc/szproduct.py                            |       37 |        7 |     81% |85-87, 94-95, 102-103 |
|                                                 **TOTAL** | **1404** |  **562** | **60%** |           |


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