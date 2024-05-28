# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-grpc/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                      |    Stmts |     Miss |   Cover |   Missing |
|---------------------------------------------------------- | -------: | -------: | ------: | --------: |
| src/senzing\_grpc/\_\_init\_\_.py                         |        7 |        0 |    100% |           |
| src/senzing\_grpc/pb2\_grpc/\_\_init\_\_.py               |        0 |        0 |    100% |           |
| src/senzing\_grpc/pb2\_grpc/szconfig\_pb2.py              |       42 |       32 |     24% |     24-57 |
| src/senzing\_grpc/pb2\_grpc/szconfig\_pb2\_grpc.py        |       66 |       31 |     53% |59-61, 65-67, 71-73, 77-79, 83-85, 89-91, 95-97, 101-141, 161, 190, 219, 248, 277, 306, 335 |
| src/senzing\_grpc/pb2\_grpc/szconfigmanager\_pb2.py       |       38 |       28 |     26% |     24-53 |
| src/senzing\_grpc/pb2\_grpc/szconfigmanager\_pb2\_grpc.py |       58 |       27 |     53% |54-56, 60-62, 66-68, 72-74, 78-80, 84-86, 90-125, 145, 174, 203, 232, 261, 290 |
| src/senzing\_grpc/pb2\_grpc/szdiagnostic\_pb2.py          |       30 |       20 |     33% |     24-45 |
| src/senzing\_grpc/pb2\_grpc/szdiagnostic\_pb2\_grpc.py    |       42 |       19 |     55% |44-46, 50-52, 56-58, 62-64, 68-93, 113, 142, 171, 200 |
| src/senzing\_grpc/pb2\_grpc/szengine\_pb2.py              |      138 |      128 |      7% |    24-153 |
| src/senzing\_grpc/pb2\_grpc/szengine\_pb2\_grpc.py        |      258 |      127 |     51% |179-181, 185-187, 191-193, 197-199, 203-205, 209-211, 215-217, 221-223, 227-229, 233-235, 239-241, 245-247, 251-253, 257-259, 263-265, 269-271, 275-277, 281-283, 287-289, 293-295, 299-301, 305-307, 311-313, 317-319, 323-325, 329-331, 335-337, 341-343, 347-349, 353-355, 359-361, 365-525, 545, 574, 603, 632, 661, 690, 719, 748, 777, 806, 835, 864, 893, 922, 951, 980, 1009, 1038, 1067, 1096, 1125, 1154, 1183, 1212, 1241, 1270, 1299, 1328, 1357, 1386, 1415 |
| src/senzing\_grpc/pb2\_grpc/szhasher\_pb2.py              |       33 |       33 |      0% |      5-45 |
| src/senzing\_grpc/pb2\_grpc/szhasher\_pb2\_grpc.py        |       50 |       50 |      0% |     7-249 |
| src/senzing\_grpc/pb2\_grpc/szproduct\_pb2.py             |       22 |       12 |     45% |     24-37 |
| src/senzing\_grpc/pb2\_grpc/szproduct\_pb2\_grpc.py       |       26 |       11 |     58% |34-36, 40-42, 46-61, 81, 110 |
| src/senzing\_grpc/szconfig.py                             |       79 |        2 |     97% |   106-107 |
| src/senzing\_grpc/szconfigmanager.py                      |       70 |        4 |     94% |111-112, 120-121 |
| src/senzing\_grpc/szdiagnostic.py                         |       55 |       12 |     78% |95-96, 100-102, 121, 124-129 |
| src/senzing\_grpc/szengine.py                             |      275 |       41 |     85% |104-105, 113-114, 153-154, 164, 173-174, 186-187, 203-204, 214-215, 362-363, 379-380, 426-427, 435-436, 492-501, 512-513, 535-536, 584-594 |
| src/senzing\_grpc/szhelpers.py                            |       39 |        6 |     85% |49, 53-55, 77-78 |
| src/senzing\_grpc/szproduct.py                            |       41 |        4 |     90% |98-99, 107-108 |
|                                                 **TOTAL** | **1369** |  **587** | **57%** |           |


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