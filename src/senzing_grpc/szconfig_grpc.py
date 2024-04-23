#! /usr/bin/env python3

"""
TODO: g2config_grpc.py
"""

# pylint: disable=E1101

from types import TracebackType
from typing import Any, Dict, Type, Union

import grpc
from senzing_abstract import SzConfigAbstract

# from .g2abstract.g2config_abstract import G2ConfigAbstract
from .g2helpers import as_str, new_exception
from .pb2_grpc import g2config_pb2, g2config_pb2_grpc

# Metadata

__all__ = ["SzConfigGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-11-27"
__updated__ = "2023-12-16"

SENZING_PRODUCT_ID = "5050"  # See https://github.com/senzing-garage/knowledge-base/blob/main/lists/senzing-component-ids.md

# -----------------------------------------------------------------------------
# G2ConfigGrpc class
# -----------------------------------------------------------------------------


class SzConfigGrpc(SzConfigAbstract):  # type: ignore
    """
    G2 config module access library over gRPC.
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
        self.stub = g2config_pb2_grpc.G2ConfigStub(self.channel)

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
    # G2Config methods
    # -------------------------------------------------------------------------

    def add_data_source(
        self,
        config_handle: int,
        input_json: Union[str, Dict[Any, Any]],
        *args: Any,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2config_pb2.AddDataSourceRequest(  # type: ignore[unused-ignore]
                configHandle=config_handle, inputJson=as_str(input_json)
            )
            response = self.stub.AddDataSource(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def close(self, config_handle: int, *args: Any, **kwargs: Any) -> None:
        try:
            request = g2config_pb2.CloseRequest(configHandle=config_handle)  # type: ignore[unused-ignore]
            self.stub.Close(request)
        except Exception as err:
            raise new_exception(err) from err

    def create(self, *args: Any, **kwargs: Any) -> int:
        try:
            request = g2config_pb2.CreateRequest()  # type: ignore[unused-ignore]
            response = self.stub.Create(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def delete_data_source(
        self,
        config_handle: int,
        input_json: Union[str, Dict[Any, Any]],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        try:
            request = g2config_pb2.DeleteDataSourceRequest(  # type: ignore[unused-ignore]
                configHandle=config_handle, inputJson=as_str(input_json)
            )
            self.stub.DeleteDataSource(request)
        except Exception as err:
            raise new_exception(err) from err

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

    def list_data_sources(self, config_handle: int, *args: Any, **kwargs: Any) -> str:
        try:
            request = g2config_pb2.ListDataSourcesRequest(configHandle=config_handle)  # type: ignore[unused-ignore]
            response = self.stub.ListDataSources(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def load(
        self, json_config: Union[str, Dict[Any, Any]], *args: Any, **kwargs: Any
    ) -> int:
        try:
            request = g2config_pb2.LoadRequest(jsonConfig=as_str(json_config))  # type: ignore[unused-ignore]
            response = self.stub.Load(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def save(self, config_handle: int, *args: Any, **kwargs: Any) -> str:
        try:
            request = g2config_pb2.SaveRequest(configHandle=config_handle)  # type: ignore[unused-ignore]
            response = self.stub.Save(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err
