# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-grpc/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                      |    Stmts |     Miss |   Cover |   Missing |
|---------------------------------------------------------- | -------: | -------: | ------: | --------: |
| src/senzing\_grpc/\_\_init\_\_.py                         |        7 |        0 |    100% |           |
| src/senzing\_grpc/pb2\_grpc/\_\_init\_\_.py               |        0 |        0 |    100% |           |
| src/senzing\_grpc/pb2\_grpc/szconfig\_pb2.py              |       32 |       20 |     38% |     33-52 |
| src/senzing\_grpc/pb2\_grpc/szconfig\_pb2\_grpc.py        |       54 |       23 |     57% |16-17, 20, 69-71, 75-77, 81-83, 87-89, 93-117, 137, 167, 197, 227 |
| src/senzing\_grpc/pb2\_grpc/szconfigmanager\_pb2.py       |       48 |       36 |     25% |     33-68 |
| src/senzing\_grpc/pb2\_grpc/szconfigmanager\_pb2\_grpc.py |       86 |       39 |     55% |16-17, 20, 93-95, 99-101, 105-107, 111-113, 117-119, 123-125, 129-131, 135-137, 141-185, 205, 235, 265, 295, 325, 355, 385, 415 |
| src/senzing\_grpc/pb2\_grpc/szdiagnostic\_pb2.py          |       36 |       24 |     33% |     33-56 |
| src/senzing\_grpc/pb2\_grpc/szdiagnostic\_pb2\_grpc.py    |       62 |       27 |     56% |16-17, 20, 75-77, 81-83, 87-89, 93-95, 99-101, 105-134, 154, 184, 214, 244, 274 |
| src/senzing\_grpc/pb2\_grpc/szengine\_pb2.py              |      152 |      140 |      8% |    33-172 |
| src/senzing\_grpc/pb2\_grpc/szengine\_pb2\_grpc.py        |      294 |      143 |     51% |16-17, 20, 249-251, 255-257, 261-263, 267-269, 273-275, 279-281, 285-287, 291-293, 297-299, 303-305, 309-311, 315-317, 321-323, 327-329, 333-335, 339-341, 345-347, 351-353, 357-359, 363-365, 369-371, 375-377, 381-383, 387-389, 393-395, 399-401, 405-407, 411-413, 417-419, 423-425, 429-431, 435-437, 441-443, 447-449, 453-627, 647, 677, 707, 737, 767, 797, 827, 857, 887, 917, 947, 977, 1007, 1037, 1067, 1097, 1127, 1157, 1187, 1217, 1247, 1277, 1307, 1337, 1367, 1397, 1427, 1457, 1487, 1517, 1547, 1577, 1607, 1637 |
| src/senzing\_grpc/pb2\_grpc/szproduct\_pb2.py             |       24 |       12 |     50% |     33-44 |
| src/senzing\_grpc/pb2\_grpc/szproduct\_pb2\_grpc.py       |       38 |       15 |     61% |16-17, 20, 57-59, 63-65, 69-83, 103, 133 |
| src/senzing\_grpc/szabstractfactory.py                    |       33 |        0 |    100% |           |
| src/senzing\_grpc/szconfig.py                             |       60 |        6 |     90% |65, 114-115, 149-151 |
| src/senzing\_grpc/szconfigmanager.py                      |       92 |        9 |     90% |107-108, 115-116, 123-124, 185-187 |
| src/senzing\_grpc/szdiagnostic.py                         |       53 |        8 |     85% |93-94, 124-127, 133-134 |
| src/senzing\_grpc/szengine.py                             |      292 |       52 |     82% |105-106, 113-114, 145-146, 154-162, 171-172, 179-185, 194-195, 325-326, 340-341, 382-383, 390-391, 435-436, 449-450, 460-461, 518-527, 566-567, 584-587, 593-594 |
| src/senzing\_grpc/szhelpers.py                            |       46 |        8 |     83% |49, 53-55, 81, 88-89, 108 |
| src/senzing\_grpc/szproduct.py                            |       37 |        7 |     81% |84-85, 92-93, 109-111 |
|                                                 **TOTAL** | **1446** |  **569** | **61%** |           |


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