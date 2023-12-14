#! /usr/bin/env python3

"""
TODO: g2product_grpc.py
"""

# pylint: disable=E1101

from types import TracebackType
from typing import Any, Dict, Type, Union

import grpc

from .g2abstract.g2product_abstract import G2ProductAbstract
from .g2helpers import new_exception
from .pb2_grpc import g2product_pb2, g2product_pb2_grpc

# Metadata

__all__ = ["G2ProductGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-11-27"
__updated__ = "2023-11-27"

SENZING_PRODUCT_ID = "5056"  # See https://github.com/Senzing/knowledge-base/blob/main/lists/senzing-component-ids.md

# -----------------------------------------------------------------------------
# G2ProductGrpc class
# -----------------------------------------------------------------------------


class G2ProductGrpc(G2ProductAbstract):
    """
    G2 product module access library over gRPC.
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
        self.stub = g2product_pb2_grpc.G2ProductStub(self.channel)

    def __enter__(
        self,
    ) -> (
        Any
    ):  # TODO: Replace "Any" with "Self" once python 3.11 is lowest supported python version.
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
    # G2Product methods
    # -------------------------------------------------------------------------

    def destroy(self, *args: Any, **kwargs: Any) -> None:
        """Null function"""

    def init(
        self,
        module_name: str,
        ini_params: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """Null function"""

    def license(self, *args: Any, **kwargs: Any) -> str:
        try:
            request = g2product_pb2.LicenseRequest()  # type: ignore[unused-ignore]
            response = self.stub.License(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def version(self, *args: Any, **kwargs: Any) -> str:
        try:
            request = g2product_pb2.VersionRequest()  # type: ignore[unused-ignore]
            response = self.stub.Version(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err
