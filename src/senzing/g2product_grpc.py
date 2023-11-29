#! /usr/bin/env python3

"""
TODO: g2product_grpc.py
"""

# pylint: disable=E1101

from typing import Any, Dict, Union

import grpc  # type: ignore

from .pb2_grpc import g2product_pb2, g2product_pb2_grpc
from .tmp.g2product_abstract import G2ProductAbstract

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
    G2 product module access library
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

    # -------------------------------------------------------------------------
    # G2Product methods
    # -------------------------------------------------------------------------

    def destroy(self, *args: Any, **kwargs: Any) -> None:
        """No-op"""

    def init(
        self,
        module_name: str,
        ini_params: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """No-op"""

    def license(self, *args: Any, **kwargs: Any) -> str:
        request = g2product_pb2.LicenseRequest()
        response = self.stub.License(request)
        return str(response.result)

    def version(self, *args: Any, **kwargs: Any) -> str:
        request = g2product_pb2.VersionRequest()
        response = self.stub.Version(request)
        return str(response.result)
