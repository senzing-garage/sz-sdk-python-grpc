#! /usr/bin/env python3

"""
``senzing_grpc.szconfig.SzConfigGrpc`` is a `gRPC`_ implementation
of the `senzing.szconfig.SzConfig`_ interface.

.. _gRPC: https://grpc.io
.. _senzing.szconfig.SzConfig: https://garage.senzing.com/sz-sdk-python/senzing.html#module-senzing.szconfig
"""

# pylint: disable=E1101

from types import TracebackType
from typing import Any, Dict, Type, Union

import grpc
from senzing import SzConfig

from .pb2_grpc import szconfig_pb2, szconfig_pb2_grpc
from .szhelpers import as_str, new_exception

# Metadata

__all__ = ["SzConfigGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2025-01-10"
__updated__ = "2025-01-16"

SENZING_PRODUCT_ID = (
    "5050"  # See https://github.com/senzing-garage/knowledge-base/blob/main/lists/senzing-component-ids.md
)

# -----------------------------------------------------------------------------
# SzConfigGrpc class
# -----------------------------------------------------------------------------


class SzConfigGrpc(SzConfig):
    """
    SzConfig module access library over gRPC.
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

        self.channel = grpc_channel
        self.stub = szconfig_pb2_grpc.SzConfigStub(self.channel)

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
    # SzConfig methods
    # -------------------------------------------------------------------------

    def add_data_source(
        self,
        config_handle: int,
        data_source_code: str,
    ) -> str:
        try:
            request = szconfig_pb2.AddDataSourceRequest(  # type: ignore[unused-ignore]
                config_handle=config_handle, data_source_code=data_source_code
            )
            response = self.stub.AddDataSource(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def close_config(self, config_handle: int) -> None:
        try:
            request = szconfig_pb2.CloseConfigRequest(config_handle=config_handle)  # type: ignore[unused-ignore]
            self.stub.CloseConfig(request)
        except Exception as err:
            raise new_exception(err) from err

    def create_config(self) -> int:
        try:
            request = szconfig_pb2.CreateConfigRequest()  # type: ignore[unused-ignore]
            response = self.stub.CreateConfig(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def delete_data_source(self, config_handle: int, data_source_code: str) -> None:
        try:
            request = szconfig_pb2.DeleteDataSourceRequest(config_handle=config_handle, data_source_code=data_source_code)  # type: ignore[unused-ignore]
            self.stub.DeleteDataSource(request)
        except Exception as err:
            raise new_exception(err) from err

    def _destroy(self) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""

    def export_config(self, config_handle: int) -> str:
        try:
            request = szconfig_pb2.ExportConfigRequest(config_handle=config_handle)  # type: ignore[unused-ignore]
            response = self.stub.ExportConfig(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_data_sources(self, config_handle: int) -> str:
        try:
            request = szconfig_pb2.GetDataSourcesRequest(config_handle=config_handle)  # type: ignore[unused-ignore]
            response = self.stub.GetDataSources(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def _initialize(
        self,
        instance_name: str,
        settings: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
    ) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""
        _ = instance_name
        _ = settings
        _ = verbose_logging

    def import_config(self, config_definition: str) -> int:
        try:
            request = szconfig_pb2.ImportConfigRequest(config_definition=as_str(config_definition))  # type: ignore[unused-ignore]
            response = self.stub.ImportConfig(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err
