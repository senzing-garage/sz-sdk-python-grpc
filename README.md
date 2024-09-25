# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-grpc/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                      |    Stmts |     Miss |   Cover |   Missing |
|---------------------------------------------------------- | -------: | -------: | ------: | --------: |
| src/senzing\_grpc/\_\_init\_\_.py                         |        8 |        0 |    100% |           |
| src/senzing\_grpc/pb2\_grpc/\_\_init\_\_.py               |        0 |        0 |    100% |           |
| src/senzing\_grpc/pb2\_grpc/szconfig\_pb2.py              |       42 |       32 |     24% |     24-57 |
| src/senzing\_grpc/pb2\_grpc/szconfig\_pb2\_grpc.py        |       66 |       31 |     53% |59-61, 65-67, 71-73, 77-79, 83-85, 89-91, 95-97, 101-140, 158, 175, 192, 209, 226, 243, 260 |
| src/senzing\_grpc/pb2\_grpc/szconfigmanager\_pb2.py       |       38 |       28 |     26% |     24-53 |
| src/senzing\_grpc/pb2\_grpc/szconfigmanager\_pb2\_grpc.py |       58 |       27 |     53% |54-56, 60-62, 66-68, 72-74, 78-80, 84-86, 90-124, 142, 159, 176, 193, 210, 227 |
| src/senzing\_grpc/pb2\_grpc/szdiagnostic\_pb2.py          |       34 |       24 |     29% |     24-49 |
| src/senzing\_grpc/pb2\_grpc/szdiagnostic\_pb2\_grpc.py    |       50 |       23 |     54% |49-51, 55-57, 61-63, 67-69, 73-75, 79-108, 126, 143, 160, 177, 194 |
| src/senzing\_grpc/pb2\_grpc/szengine\_pb2.py              |      142 |      132 |      7% |    24-157 |
| src/senzing\_grpc/pb2\_grpc/szengine\_pb2\_grpc.py        |      266 |      131 |     51% |184-186, 190-192, 196-198, 202-204, 208-210, 214-216, 220-222, 226-228, 232-234, 238-240, 244-246, 250-252, 256-258, 262-264, 268-270, 274-276, 280-282, 286-288, 292-294, 298-300, 304-306, 310-312, 316-318, 322-324, 328-330, 334-336, 340-342, 346-348, 352-354, 358-360, 364-366, 370-372, 376-540, 558, 575, 592, 609, 626, 643, 660, 677, 694, 711, 728, 745, 762, 779, 796, 813, 830, 847, 864, 881, 898, 915, 932, 949, 966, 983, 1000, 1017, 1034, 1051, 1068, 1085 |
| src/senzing\_grpc/pb2\_grpc/szproduct\_pb2.py             |       22 |       12 |     45% |     24-37 |
| src/senzing\_grpc/pb2\_grpc/szproduct\_pb2\_grpc.py       |       26 |       11 |     58% |34-36, 40-42, 46-60, 78, 95 |
| src/senzing\_grpc/szabstractfactory.py                    |       29 |        0 |    100% |           |
| src/senzing\_grpc/szconfig.py                             |       79 |        2 |     97% |   106-107 |
| src/senzing\_grpc/szconfigmanager.py                      |       70 |        4 |     94% |111-112, 120-121 |
| src/senzing\_grpc/szdiagnostic.py                         |       55 |       12 |     78% |95-96, 100-102, 121, 124-129 |
| src/senzing\_grpc/szengine.py                             |      310 |       36 |     88% |105-106, 114-115, 154-155, 165, 174-175, 187-188, 204-205, 215-216, 363-364, 380-381, 427-428, 436-437, 501-502, 513-514, 536-537, 585-595 |
| src/senzing\_grpc/szhelpers.py                            |       36 |        6 |     83% |50, 54-56, 77-78 |
| src/senzing\_grpc/szproduct.py                            |       41 |        4 |     90% |98-99, 107-108 |
|                                                 **TOTAL** | **1372** |  **515** | **62%** |           |


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