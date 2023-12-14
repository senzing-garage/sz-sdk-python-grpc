#! /usr/bin/env python3

"""
TODO: g2diagnostic_grpc.py
"""

# pylint: disable=E1101

from types import TracebackType
from typing import Any, Dict, Type, Union

import grpc

from .abstract.g2diagnostic_abstract import G2DiagnosticAbstract
from .g2helpers import new_exception
from .pb2_grpc import g2diagnostic_pb2, g2diagnostic_pb2_grpc

# Metadata

__all__ = ["G2DiagnosticGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-11-27"
__updated__ = "2023-11-27"

SENZING_PRODUCT_ID = "5052"  # See https://github.com/Senzing/knowledge-base/blob/main/lists/senzing-component-ids.md

# -----------------------------------------------------------------------------
# G2DiagnosticGrpc class
# -----------------------------------------------------------------------------


class G2DiagnosticGrpc(G2DiagnosticAbstract):
    """
    G2 diagnostic module access library over gRPC.
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
        self.stub = g2diagnostic_pb2_grpc.G2DiagnosticStub(self.channel)

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
    # G2Diagnostic methods
    # -------------------------------------------------------------------------

    def check_db_perf(self, seconds_to_run: int, *args: Any, **kwargs: Any) -> str:
        try:
            request = g2diagnostic_pb2.CheckDBPerfRequest(secondsToRun=seconds_to_run)  # type: ignore[unused-ignore]
            response = self.stub.CheckDBPerf(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def destroy(self, *args: Any, **kwargs: Any) -> None:
        """Null function"""

    def get_available_memory(self, *args: Any, **kwargs: Any) -> int:
        try:
            request = g2diagnostic_pb2.GetAvailableMemoryRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetAvailableMemory(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_db_info(self, *args: Any, **kwargs: Any) -> str:
        try:
            request = g2diagnostic_pb2.GetDBInfoRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetDBInfo(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_logical_cores(self, *args: Any, **kwargs: Any) -> int:
        try:
            request = g2diagnostic_pb2.GetLogicalCoresRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetLogicalCores(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_physical_cores(self, *args: Any, **kwargs: Any) -> int:
        try:
            request = g2diagnostic_pb2.GetPhysicalCoresRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetPhysicalCores(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_total_system_memory(self, *args: Any, **kwargs: Any) -> int:
        try:
            request = g2diagnostic_pb2.GetTotalSystemMemoryRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetTotalSystemMemory(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def init(
        self,
        module_name: str,
        ini_params: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """Null function"""

    def init_with_config_id(
        self,
        module_name: str,
        ini_params: Union[str, Dict[Any, Any]],
        init_config_id: int,
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """Null function"""

    def reinit(self, init_config_id: int, *args: Any, **kwargs: Any) -> None:
        """Null function"""
