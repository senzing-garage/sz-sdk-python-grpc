#! /usr/bin/env python3

"""
TODO: g2configmgr_grpc.py
"""

# pylint: disable=E1101

from types import TracebackType
from typing import Any, Dict, Type, Union

import grpc

# from .g2exception import translate_exception
from .g2helpers import as_str, new_exception
from .localcopy.g2configmgr_abstract import G2ConfigMgrAbstract
from .pb2_grpc import g2configmgr_pb2, g2configmgr_pb2_grpc

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
    G2 config-manager module access library over gRPC.
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
    # G2ConfigMgr methods
    # -------------------------------------------------------------------------

    def add_config(
        self,
        config_str: Union[str, Dict[Any, Any]],
        config_comments: str,
        *args: Any,
        **kwargs: Any,
    ) -> int:
        try:
            request = g2configmgr_pb2.AddConfigRequest(  # type: ignore[unused-ignore]
                configStr=as_str(config_str), configComments=as_str(config_comments)
            )
            response = self.stub.AddConfig(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def destroy(self, *args: Any, **kwargs: Any) -> None:
        """Null function"""

    def get_config(self, config_id: int, *args: Any, **kwargs: Any) -> str:
        try:
            request = g2configmgr_pb2.GetConfigRequest(configID=config_id)  # type: ignore[unused-ignore]
            response = self.stub.GetConfig(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_config_list(self, *args: Any, **kwargs: Any) -> str:
        try:
            request = g2configmgr_pb2.GetConfigListRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetConfigList(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_default_config_id(self, *args: Any, **kwargs: Any) -> int:
        try:
            request = g2configmgr_pb2.GetDefaultConfigIDRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetDefaultConfigID(request)
            return int(response.configID)
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

    def replace_default_config_id(
        self, old_config_id: int, new_config_id: int, *args: Any, **kwargs: Any
    ) -> None:
        try:
            request = g2configmgr_pb2.ReplaceDefaultConfigIDRequest(  # type: ignore[unused-ignore]
                oldConfigID=old_config_id,
                newConfigID=new_config_id,
            )
            self.stub.ReplaceDefaultConfigID(request)
        except Exception as err:
            raise new_exception(err) from err

    def set_default_config_id(self, config_id: int, *args: Any, **kwargs: Any) -> None:
        try:
            request = g2configmgr_pb2.SetDefaultConfigIDRequest(  # type: ignore[unused-ignore]
                configID=config_id,
            )
            self.stub.SetDefaultConfigID(request)
        except Exception as err:
            raise new_exception(err) from err
