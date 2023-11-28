#! /usr/bin/env python3

"""
TODO: g2config_grpc.py
"""

# pylint: disable=E1101

from typing import Any, Dict, Union

import grpc  # type: ignore

from .g2helpers import as_str
from .pb2_grpc import g2config_pb2, g2config_pb2_grpc
from .tmp.g2config_abstract import G2ConfigAbstract

# Metadata

__all__ = ["G2ConfigGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-11-27"
__updated__ = "2023-11-27"

SENZING_PRODUCT_ID = "5050"  # See https://github.com/Senzing/knowledge-base/blob/main/lists/senzing-component-ids.md

# -----------------------------------------------------------------------------
# G2ConfigGrpc class
# -----------------------------------------------------------------------------


class G2ConfigGrpc(G2ConfigAbstract):
    """
    G2 config module access library
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
        self.stub = g2config_pb2_grpc.G2ConfigStub(self.channel)  # type: ignore[no-untyped-call]

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
        request = g2config_pb2.AddDataSourceRequest(  # type: ignore[attr-defined]
            configHandle=config_handle, inputJson=as_str(input_json)
        )
        result = self.stub.AddDataSource(request)
        return str(result.result)

    def close(self, config_handle: int, *args: Any, **kwargs: Any) -> None:
        request = g2config_pb2.CloseRequest(configHandle=config_handle)  # type: ignore[attr-defined]
        self.stub.Close(request)

    def create(self, *args: Any, **kwargs: Any) -> int:
        request = g2config_pb2.CreateRequest()  # type: ignore[attr-defined]
        result = self.stub.Create(request)
        return int(result.result)

    def delete_data_source(
        self,
        config_handle: int,
        input_json: Union[str, Dict[Any, Any]],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        request = g2config_pb2.DeleteDataSourceRequest(  # type: ignore[attr-defined]
            configHandle=config_handle, inputJson=as_str(input_json)
        )
        self.stub.DeleteDataSource(request)

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

    def list_data_sources(self, config_handle: int, *args: Any, **kwargs: Any) -> str:
        request = g2config_pb2.ListDataSourcesRequest(configHandle=config_handle)  # type: ignore[attr-defined]
        result = self.stub.ListDataSources(request)
        return str(result.result)

    def load(
        self, json_config: Union[str, Dict[Any, Any]], *args: Any, **kwargs: Any
    ) -> int:
        request = g2config_pb2.LoadRequest(jsonConfig=as_str(json_config))  # type: ignore[attr-defined]
        result = self.stub.Load(request)
        return int(result.result)

    def save(self, config_handle: int, *args: Any, **kwargs: Any) -> str:
        request = g2config_pb2.SaveRequest(configHandle=config_handle)  # type: ignore[attr-defined]
        result = self.stub.Save(request)
        return str(result.result)
