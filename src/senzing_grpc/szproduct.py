#! /usr/bin/env python3

"""
``senzing_grpc.szproduct.SzProductGrpc`` is a `gRPC`_ implementation
of the `senzing.szproduct.SzProduct`_ interface.

.. _gRPC: https://grpc.io
.. _senzing.szproduct.SzProduct: https://garage.senzing.com/sz-sdk-python/senzing.html#module-senzing.szproduct
"""

# pylint: disable=E1101

from types import TracebackType
from typing import Any, Dict, Type, Union

import grpc
from senzing import SzProduct
from senzing_grpc_protobuf import szproduct_pb2, szproduct_pb2_grpc

from .szhelpers import new_exception

# Metadata

__all__ = ["SzProductGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2025-01-10"
__updated__ = "2025-01-16"

SENZING_PRODUCT_ID = (
    "5056"  # See https://github.com/senzing-garage/knowledge-base/blob/main/lists/senzing-component-ids.md
)

# -----------------------------------------------------------------------------
# SzProductGrpc class
# -----------------------------------------------------------------------------


class SzProductGrpc(SzProduct):
    """
    SzProduct module access library over gRPC.
    """

    # -------------------------------------------------------------------------
    # Python dunder/magic methods
    # -------------------------------------------------------------------------

    def __init__(
        self,
        grpc_channel: grpc.Channel,
    ) -> None:
        """
        Constructor

        For return value of -> None, see https://peps.python.org/pep-0484/#the-meaning-of-annotations
        """
        # pylint: disable=W0613

        self.channel = grpc_channel
        self.stub = szproduct_pb2_grpc.SzProductStub(self.channel)

    def __enter__(
        self,
    ) -> Any:  # TODO: Replace "Any" with "Self" once python 3.11 is lowest supported python version.
        """Context Manager method."""
        return self

    def __exit__(
        self,
        exc_type: Union[Type[BaseException], None],
        exc_val: Union[BaseException, None],
        exc_tb: Union[TracebackType, None],
    ) -> None:
        """Context Manager method."""

    # -------------------------------------------------------------------------
    # SzProduct methods
    # -------------------------------------------------------------------------

    def get_license(self) -> str:
        try:
            request = szproduct_pb2.GetLicenseRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetLicense(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_version(self) -> str:
        try:
            request = szproduct_pb2.GetVersionRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetVersion(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    # -------------------------------------------------------------------------
    # Non-public SzProductCore methods
    # -------------------------------------------------------------------------

    def _destroy(self) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""

    def initialize(
        self,
        instance_name: str,
        settings: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
    ) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""
        _ = instance_name
        _ = settings
        _ = verbose_logging
