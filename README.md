# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-grpc/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                      |    Stmts |     Miss |   Cover |   Missing |
|---------------------------------------------------------- | -------: | -------: | ------: | --------: |
| src/senzing\_grpc/\_\_init\_\_.py                         |        7 |        0 |    100% |           |
| src/senzing\_grpc/pb2\_grpc/\_\_init\_\_.py               |        0 |        0 |    100% |           |
| src/senzing\_grpc/pb2\_grpc/szconfig\_pb2.py              |       28 |       16 |     43% |     33-48 |
| src/senzing\_grpc/pb2\_grpc/szconfig\_pb2\_grpc.py        |       46 |       19 |     59% |15-16, 19, 59-61, 65-67, 71-73, 77-97, 115, 142, 169 |
| src/senzing\_grpc/pb2\_grpc/szconfigmanager\_pb2.py       |       48 |       36 |     25% |     33-68 |
| src/senzing\_grpc/pb2\_grpc/szconfigmanager\_pb2\_grpc.py |       86 |       39 |     55% |15-16, 19, 84-86, 90-92, 96-98, 102-104, 108-110, 114-116, 120-122, 126-128, 132-177, 195, 222, 249, 276, 303, 330, 357, 384 |
| src/senzing\_grpc/pb2\_grpc/szdiagnostic\_pb2.py          |       36 |       24 |     33% |     33-56 |
| src/senzing\_grpc/pb2\_grpc/szdiagnostic\_pb2\_grpc.py    |       62 |       27 |     56% |15-16, 19, 69-71, 75-77, 81-83, 87-89, 93-95, 99-129, 147, 174, 201, 228, 255 |
| src/senzing\_grpc/pb2\_grpc/szengine\_pb2.py              |      148 |      136 |      8% |    33-168 |
| src/senzing\_grpc/pb2\_grpc/szengine\_pb2\_grpc.py        |      286 |      139 |     51% |15-16, 19, 209-211, 215-217, 221-223, 227-229, 233-235, 239-241, 245-247, 251-253, 257-259, 263-265, 269-271, 275-277, 281-283, 287-289, 293-295, 299-301, 305-307, 311-313, 317-319, 323-325, 329-331, 335-337, 341-343, 347-349, 353-355, 359-361, 365-367, 371-373, 377-379, 383-385, 389-391, 395-397, 401-403, 407-577, 595, 622, 649, 676, 703, 730, 757, 784, 811, 838, 865, 892, 919, 946, 973, 1000, 1027, 1054, 1081, 1108, 1135, 1162, 1189, 1216, 1243, 1270, 1297, 1324, 1351, 1378, 1405, 1432, 1459 |
| src/senzing\_grpc/pb2\_grpc/szproduct\_pb2.py             |       24 |       12 |     50% |     33-44 |
| src/senzing\_grpc/pb2\_grpc/szproduct\_pb2\_grpc.py       |       38 |       15 |     61% |15-16, 19, 54-56, 60-62, 66-81, 99, 126 |
| src/senzing\_grpc/szabstractfactory.py                    |       33 |        0 |    100% |           |
| src/senzing\_grpc/szconfig.py                             |       56 |        6 |     89% |65, 114-115, 149-151 |
| src/senzing\_grpc/szconfigmanager.py                      |       88 |        9 |     90% |104-105, 112-113, 120-121, 182-184 |
| src/senzing\_grpc/szdiagnostic.py                         |       53 |        8 |     85% |93-94, 124-127, 133-134 |
| src/senzing\_grpc/szengine.py                             |      285 |       50 |     82% |105-106, 113-114, 145-146, 154-162, 171-172, 179-185, 194-195, 318-319, 333-334, 375-376, 383-384, 428-429, 442-443, 453-454, 509-518, 556-559, 565-566 |
| src/senzing\_grpc/szhelpers.py                            |       38 |        6 |     84% |49, 53-55, 88-89 |
| src/senzing\_grpc/szproduct.py                            |       37 |        7 |     81% |84-85, 92-93, 109-111 |
|                                                 **TOTAL** | **1399** |  **549** | **61%** |           |


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