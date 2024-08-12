#! /usr/bin/env python3

"""
TODO: szdiagnostic_grpc.py
"""

# pylint: disable=E1101

from types import TracebackType
from typing import Any, Dict, Optional, Type, Union

import grpc
from senzing_abstract import SzDiagnosticAbstract

from .pb2_grpc import szdiagnostic_pb2, szdiagnostic_pb2_grpc
from .szhelpers import new_exception

# Metadata

__all__ = ["SzDiagnostic"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-11-27"
__updated__ = "2024-07-30"

SENZING_PRODUCT_ID = "5052"  # See https://github.com/senzing-garage/knowledge-base/blob/main/lists/senzing-component-ids.md

# -----------------------------------------------------------------------------
# SzDiagnostic class
# -----------------------------------------------------------------------------


class SzDiagnostic(SzDiagnosticAbstract):
    """
    SzDiagnostic module access library over gRPC.
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
        self.stub = szdiagnostic_pb2_grpc.SzDiagnosticStub(self.channel)

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
    # SzDiagnostic methods
    # -------------------------------------------------------------------------

    def check_datastore_performance(self, seconds_to_run: int, **kwargs: Any) -> str:
        _ = kwargs
        try:
            request = szdiagnostic_pb2.CheckDatastorePerformanceRequest(secondsToRun=seconds_to_run)  # type: ignore[unused-ignore]
            response = self.stub.CheckDatastorePerformance(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def destroy(self, **kwargs: Any) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""
        _ = kwargs

    def get_datastore_info(self, **kwargs: Any) -> str:
        _ = kwargs
        try:
            request = szdiagnostic_pb2.GetDatastoreInfoRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetDatastoreInfo(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_feature(self, feature_id: int, **kwargs: Any) -> str:
        """TODO: Add get_feature()"""
        _ = feature_id
        _ = kwargs
        return ""

    def initialize(
        self,
        instance_name: str,
        settings: Union[str, Dict[Any, Any]],
        config_id: Optional[int] = None,
        verbose_logging: int = 0,
        **kwargs: Any
    ) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""
        _ = instance_name
        _ = settings
        _ = config_id
        _ = verbose_logging
        _ = kwargs

    def purge_repository(self, **kwargs: Any) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""
        _ = kwargs

    def reinitialize(self, config_id: int, **kwargs: Any) -> None:
        _ = kwargs
        try:
            request = szdiagnostic_pb2.ReinitializeRequest(configId=config_id)  # type: ignore[unused-ignore]
            self.stub.Reinitialize(request)
        except Exception as err:
            raise new_exception(err) from err
