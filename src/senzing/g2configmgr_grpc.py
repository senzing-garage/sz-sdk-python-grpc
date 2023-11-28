#! /usr/bin/env python3

"""
TODO: g2configmgr_grpc.py
"""

# pylint: disable=E1101

from typing import Any, Dict, Union

import grpc  # type: ignore

# from .g2exception import translate_exception
from .g2helpers import as_str
from .pb2_grpc import g2configmgr_pb2, g2configmgr_pb2_grpc
from .tmp.g2configmgr_abstract import G2ConfigMgrAbstract

# Metadata

__all__ = ["G2ConfigMgrGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-11-27"
__updated__ = "2023-11-27"

SENZING_PRODUCT_ID = "5051"  # See https://github.com/Senzing/knowledge-base/blob/main/lists/senzing-component-ids.md

# -----------------------------------------------------------------------------
# G2ConfigMgrGrpc class
# -----------------------------------------------------------------------------


class G2ConfigMgrGrpc(G2ConfigMgrAbstract):
    """
    G2 config-manager module access library
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
        self.stub = g2configmgr_pb2_grpc.G2ConfigMgrStub(self.channel)

    # -------------------------------------------------------------------------
    # G2ConfigMgr methods
    # -------------------------------------------------------------------------

    def add_config(
        self,
        config_str: Union[str, Dict[Any, Any]],
        config_comments: str,
        *args: Any,
        **kwargs: Any,
    ) -> int:
        request = g2configmgr_pb2.AddDataSourceRequest(
            configStr=config_str, configComments=as_str(config_str)
        )
        result = self.stub.AddConfig(request)
        return int(result.result)

    def destroy(self, *args: Any, **kwargs: Any) -> None:
        """No-op"""

    def get_config(self, config_id: int, *args: Any, **kwargs: Any) -> str:
        request = g2configmgr_pb2.GetConfigRequest(configID=config_id)
        result = self.stub.GetConfig(request)
        return str(result.result)

    def get_config_list(self, *args: Any, **kwargs: Any) -> str:
        request = g2configmgr_pb2.GetConfigListRequest()
        result = self.stub.GetConfigList(request)
        return str(result.result)

    def get_default_config_id(self, *args: Any, **kwargs: Any) -> int:
        request = g2configmgr_pb2.GetDefaultConfigIDRequest()
        result = self.stub.GetDefaultConfigID(request)
        return int(result.result)

    def init(
        self,
        module_name: str,
        ini_params: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """No-op"""

    def replace_default_config_id(
        self, old_config_id: int, new_config_id: int, *args: Any, **kwargs: Any
    ) -> None:
        request = g2configmgr_pb2.ReplaceDefaultConfigIDRequest(
            oldConfigID=old_config_id,
            newConfigID=new_config_id,
        )
        self.stub.ReplaceDefaultConfigID(request)

    def set_default_config_id(self, config_id: int, *args: Any, **kwargs: Any) -> None:
        request = g2configmgr_pb2.SetDefaultConfigIDRequest(
            configID=config_id,
        )
        self.stub.SetDefaultConfigID(request)
