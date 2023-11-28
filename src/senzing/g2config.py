#! /usr/bin/env python3

"""
TODO: g2config_grpc.py
"""

# Import from standard library. https://docs.python.org/3/library/

from typing import Any, Dict, Union

import grpc

from .g2helpers import as_str
from .pb2_grpc import g2config_pb2, g2config_pb2_grpc
from .tmp.g2config_abstract import G2ConfigAbstract

# import pb2_grpc.g2config_pb2 as g2config_pb2
# import pb2_grpc.g2config_pb2_grpc as g2config_pb2_grpc


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
        grpc_url: str = "",
        **kwargs: Any,
    ) -> None:
        """
        Constructor

        For return value of -> None, see https://peps.python.org/pep-0484/#the-meaning-of-annotations
        """

        self.channel = grpc.insecure_channel(grpc_url)
        self.stub = g2config_pb2_grpc.G2ConfigStub(
            self.channel
        )  # mypy: disallow-untyped-calls
        self.url = grpc_url

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
        request = g2config_pb2.AddDataSourceRequest(
            configHandle=config_handle, inputJson=as_str(input_json)
        )
        result = self.stub.AddDataSource(request)
        return str(result.result)

    def close(self, config_handle: int, *args: Any, **kwargs: Any) -> None:
        request = g2config_pb2.CloseRequest(configHandle=config_handle)
        self.stub.Close(request)

    def create(self, *args: Any, **kwargs: Any) -> int:
        request = g2config_pb2.CreateRequest()
        result = self.stub.Create(request)
        return int(result.result)

    def delete_data_source(
        self,
        config_handle: int,
        input_json: Union[str, Dict[Any, Any]],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        request = g2config_pb2.DeleteDataSourceRequest(
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
        request = g2config_pb2.ListDataSourcesRequest(configHandle=config_handle)
        result = self.stub.ListDataSources(request)
        return str(result.result)

    def load(
        self, json_config: Union[str, Dict[Any, Any]], *args: Any, **kwargs: Any
    ) -> int:
        request = g2config_pb2.LoadRequest(jsonConfig=as_str(json_config))
        result = self.stub.Load(request)
        return int(result.result)

    def save(self, config_handle: int, *args: Any, **kwargs: Any) -> str:
        request = g2config_pb2.SaveRequest(configHandle=config_handle)
        result = self.stub.Save(request)
        return str(result.result)
