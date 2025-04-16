# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/senzing-garage/sz-sdk-python-grpc/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                      |    Stmts |     Miss |   Cover |   Missing |
|---------------------------------------------------------- | -------: | -------: | ------: | --------: |
| src/senzing\_grpc/\_\_init\_\_.py                         |        7 |        0 |    100% |           |
| src/senzing\_grpc/pb2\_grpc/\_\_init\_\_.py               |        0 |        0 |    100% |           |
| src/senzing\_grpc/pb2\_grpc/szconfig\_pb2.py              |       32 |       20 |     38% |     33-52 |
| src/senzing\_grpc/pb2\_grpc/szconfig\_pb2\_grpc.py        |       54 |       23 |     57% |15-16, 19, 64-66, 70-72, 76-78, 82-84, 88-113, 131, 158, 185, 212 |
| src/senzing\_grpc/pb2\_grpc/szconfigmanager\_pb2.py       |       48 |       36 |     25% |     33-68 |
| src/senzing\_grpc/pb2\_grpc/szconfigmanager\_pb2\_grpc.py |       86 |       39 |     55% |15-16, 19, 84-86, 90-92, 96-98, 102-104, 108-110, 114-116, 120-122, 126-128, 132-177, 195, 222, 249, 276, 303, 330, 357, 384 |
| src/senzing\_grpc/pb2\_grpc/szdiagnostic\_pb2.py          |       36 |       24 |     33% |     33-56 |
| src/senzing\_grpc/pb2\_grpc/szdiagnostic\_pb2\_grpc.py    |       62 |       27 |     56% |15-16, 19, 69-71, 75-77, 81-83, 87-89, 93-95, 99-129, 147, 174, 201, 228, 255 |
| src/senzing\_grpc/pb2\_grpc/szengine\_pb2.py              |      152 |      140 |      8% |    33-172 |
| src/senzing\_grpc/pb2\_grpc/szengine\_pb2\_grpc.py        |      294 |      143 |     51% |15-16, 19, 214-216, 220-222, 226-228, 232-234, 238-240, 244-246, 250-252, 256-258, 262-264, 268-270, 274-276, 280-282, 286-288, 292-294, 298-300, 304-306, 310-312, 316-318, 322-324, 328-330, 334-336, 340-342, 346-348, 352-354, 358-360, 364-366, 370-372, 376-378, 382-384, 388-390, 394-396, 400-402, 406-408, 412-414, 418-593, 611, 638, 665, 692, 719, 746, 773, 800, 827, 854, 881, 908, 935, 962, 989, 1016, 1043, 1070, 1097, 1124, 1151, 1178, 1205, 1232, 1259, 1286, 1313, 1340, 1367, 1394, 1421, 1448, 1475, 1502 |
| src/senzing\_grpc/pb2\_grpc/szproduct\_pb2.py             |       24 |       12 |     50% |     33-44 |
| src/senzing\_grpc/pb2\_grpc/szproduct\_pb2\_grpc.py       |       38 |       15 |     61% |15-16, 19, 54-56, 60-62, 66-81, 99, 126 |
| src/senzing\_grpc/szabstractfactory.py                    |       33 |        0 |    100% |           |
| src/senzing\_grpc/szconfig.py                             |       60 |        6 |     90% |65, 114-115, 149-151 |
| src/senzing\_grpc/szconfigmanager.py                      |       92 |        9 |     90% |107-108, 115-116, 123-124, 185-187 |
| src/senzing\_grpc/szdiagnostic.py                         |       53 |        8 |     85% |93-94, 124-127, 133-134 |
| src/senzing\_grpc/szengine.py                             |      292 |       52 |     82% |105-106, 113-114, 145-146, 154-162, 171-172, 179-185, 194-195, 318-319, 333-334, 375-376, 383-384, 428-429, 442-443, 453-454, 509-518, 557-558, 575-578, 584-585 |
| src/senzing\_grpc/szhelpers.py                            |       38 |        6 |     84% |49, 53-55, 88-89 |
| src/senzing\_grpc/szproduct.py                            |       37 |        7 |     81% |84-85, 92-93, 109-111 |
|                                                 **TOTAL** | **1438** |  **567** | **61%** |           |


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