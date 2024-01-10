#! /usr/bin/env python3

"""
TODO: g2engine_grpc.py
"""

# pylint: disable=E1101,C0302

from types import TracebackType
from typing import Any, Dict, Iterable, Tuple, Type, Union

import grpc
from senzing_abstract import G2EngineAbstract, G2EngineFlags

from .g2helpers import as_str, new_exception
from .pb2_grpc import g2engine_pb2, g2engine_pb2_grpc

# Metadata

__all__ = ["G2EngineGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-11-27"
__updated__ = "2024-01-10"

SENZING_PRODUCT_ID = "5053"  # See https://github.com/senzing-garage/knowledge-base/blob/main/lists/senzing-component-ids.md

# -----------------------------------------------------------------------------
# G2EngineGrpc class
# -----------------------------------------------------------------------------


class G2EngineGrpc(G2EngineAbstract):  # type: ignore
    """
    G2 engine module access library over gRPC.
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
        self.stub = g2engine_pb2_grpc.G2EngineStub(self.channel)
        self.noop = ""

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
    # Development methods - to be removed after initial development
    # -------------------------------------------------------------------------

    def fake_g2engine(self, *args: Any, **kwargs: Any) -> None:
        """TODO: Remove once SDK methods have been implemented."""
        if len(args) + len(kwargs) > 2000:
            print(self.noop)

    # -------------------------------------------------------------------------
    # G2Engine methods
    # -------------------------------------------------------------------------

    def add_record(
        self,
        data_source_code: str,
        record_id: str,
        json_data: Union[str, Dict[Any, Any]],
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        flags: int = 0,  # pylint: disable=W0613
        **kwargs: Any,
    ) -> None:
        try:
            request = g2engine_pb2.AddRecordRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                jsonData=as_str(json_data),
                loadID=load_id,
            )
            self.stub.AddRecord(request)
        except Exception as err:
            raise new_exception(err) from err

    def add_record_with_info(
        self,
        data_source_code: str,
        record_id: str,
        json_data: Union[str, Dict[Any, Any]],
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.AddRecordWithInfoRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                jsonData=as_str(json_data),
                loadID=load_id,
                flags=flags,
            )
            response = self.stub.AddRecordWithInfo(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def close_export(self, response_handle: int, **kwargs: Any) -> None:
        try:
            request = g2engine_pb2.CloseExportRequest(  # type: ignore[unused-ignore]
                responseHandle=response_handle,
            )
            self.stub.CloseExport(request)
        except Exception as err:
            raise new_exception(err) from err

    def count_redo_records(self, **kwargs: Any) -> int:
        try:
            request = g2engine_pb2.CountRedoRecordsRequest()  # type: ignore[unused-ignore]
            response = self.stub.CountRedoRecords(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def delete_record(
        self,
        data_source_code: str,
        record_id: str,
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        **kwargs: Any,
    ) -> None:
        try:
            request = g2engine_pb2.DeleteRecordRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                loadID=load_id,
            )
            self.stub.DeleteRecord(request)
        except Exception as err:
            raise new_exception(err) from err

    def delete_record_with_info(
        self,
        data_source_code: str,
        record_id: str,
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.DeleteRecordWithInfoRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                loadID=load_id,
                flags=flags,
            )
            response = self.stub.DeleteRecordWithInfo(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def destroy(self, **kwargs: Any) -> None:
        """Null function"""

    def export_config(self, **kwargs: Any) -> str:
        try:
            request = g2engine_pb2.ExportConfigRequest()  # type: ignore[unused-ignore]
            response = self.stub.ExportConfig(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def export_config_and_config_id(self, **kwargs: Any) -> Tuple[str, int]:
        try:
            request = g2engine_pb2.ExportConfigAndConfigIDRequest()  # type: ignore[unused-ignore]
            response = self.stub.ExportConfigAndConfigID(request)
            return str(response.config), response.configID
        except Exception as err:
            raise new_exception(err) from err

    def export_csv_entity_report(
        self,
        csv_column_list: str,
        flags: int = G2EngineFlags.G2_EXPORT_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> int:
        try:
            request = g2engine_pb2.ExportCSVEntityReportRequest(  # type: ignore[unused-ignore]
                csvColumnList=csv_column_list,
                flags=flags,
            )
            response = self.stub.ExportCSVEntityReport(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def export_csv_entity_report_iterator(
        self,
        flags: int = G2EngineFlags.G2_EXPORT_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> Iterable[str]:
        if len(kwargs) > 0:
            pass  # TODO: To disable pylint W0613
        try:
            request = g2engine_pb2.StreamExportCSVEntityReportRequest(  # type: ignore[unused-ignore]
                flags=flags
            )
            for item in self.stub.StreamExportCSVEntityReport(request):
                if item.result:
                    yield item.result
        except Exception as err:
            raise new_exception(err) from err

    def export_json_entity_report(
        self, flags: int = G2EngineFlags.G2_EXPORT_DEFAULT_FLAGS, **kwargs: Any
    ) -> int:
        try:
            request = g2engine_pb2.ExportJSONEntityReportRequest(  # type: ignore[unused-ignore]
                flags=flags,
            )
            response = self.stub.ExportJSONEntityReport(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def export_json_entity_report_iterator(
        self,
        flags: int = G2EngineFlags.G2_EXPORT_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> Iterable[str]:
        if len(kwargs) > 0:
            pass  # TODO: To disable pylint W0613
        try:
            request = g2engine_pb2.StreamExportJSONEntityReportRequest(  # type: ignore[unused-ignore]
                flags=flags
            )
            for item in self.stub.StreamExportJSONEntityReport(request):
                if item.result:
                    yield item.result
        except Exception as err:
            raise new_exception(err) from err

    def fetch_next(self, response_handle: int, **kwargs: Any) -> str:
        try:
            request = g2engine_pb2.FetchNextRequest(  # type: ignore[unused-ignore]
                responseHandle=response_handle,
            )
            response = self.stub.FetchNext(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_interesting_entities_by_entity_id(
        self, entity_id: int, flags: int = 0, **kwargs: Any
    ) -> str:
        try:
            request = g2engine_pb2.FindInterestingEntitiesByEntityIDRequest(  # type: ignore[unused-ignore]
                entityID=entity_id,
                flags=flags,
            )
            response = self.stub.FindInterestingEntitiesByEntityID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_interesting_entities_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindInterestingEntitiesByRecordIDRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                flags=flags,
            )
            response = self.stub.FindInterestingEntitiesByRecordID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_network_by_entity_id(
        self,
        entity_list: Union[str, Dict[Any, Any]],
        max_degree: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindNetworkByEntityIDRequest(  # type: ignore[unused-ignore]
                entityList=as_str(entity_list),
                maxDegree=max_degree,
                buildOutDegree=build_out_degree,
                maxEntities=max_entities,
            )
            response = self.stub.FindNetworkByEntityID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_network_by_entity_id_v2(
        self,
        entity_list: Union[str, Dict[Any, Any]],
        max_degree: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindNetworkByEntityID_V2Request(  # type: ignore[unused-ignore]
                entityList=as_str(entity_list),
                maxDegree=max_degree,
                buildOutDegree=build_out_degree,
                maxEntities=max_entities,
                flags=flags,
            )
            response = self.stub.FindNetworkByEntityID_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_network_by_record_id(
        self,
        record_list: Union[str, Dict[Any, Any]],
        max_degree: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindNetworkByRecordIDRequest(  # type: ignore[unused-ignore]
                recordList=as_str(record_list),
                maxDegree=max_degree,
                buildOutDegree=build_out_degree,
                maxEntities=max_entities,
            )
            response = self.stub.FindNetworkByRecordID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_network_by_record_id_v2(
        self,
        record_list: Union[str, Dict[Any, Any]],
        max_degree: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindNetworkByRecordID_V2Request(  # type: ignore[unused-ignore]
                recordList=as_str(record_list),
                maxDegree=max_degree,
                buildOutDegree=build_out_degree,
                maxEntities=max_entities,
                flags=flags,
            )
            response = self.stub.FindNetworkByRecordID_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_by_entity_id(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindPathByEntityIDRequest(  # type: ignore[unused-ignore]
                entityID1=entity_id_1,
                entityID2=entity_id_2,
                maxDegree=max_degree,
            )
            response = self.stub.FindPathByEntityID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_by_entity_id_v2(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindPathByEntityID_V2Request(  # type: ignore[unused-ignore]
                entityID1=entity_id_1,
                entityID2=entity_id_2,
                maxDegree=max_degree,
                flags=flags,
            )
            response = self.stub.FindPathByEntityID_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_by_record_id(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindPathByRecordIDRequest(  # type: ignore[unused-ignore]
                dataSourceCode1=data_source_code_1,
                recordID1=record_id_1,
                dataSourceCode2=data_source_code_2,
                recordID2=record_id_2,
                maxDegree=max_degree,
            )
            response = self.stub.FindPathByRecordID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_by_record_id_v2(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindPathByRecordID_V2Request(  # type: ignore[unused-ignore]
                dataSourceCode1=data_source_code_1,
                recordID1=record_id_1,
                dataSourceCode2=data_source_code_2,
                recordID2=record_id_2,
                maxDegree=max_degree,
                flags=flags,
            )
            response = self.stub.FindPathByRecordID_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_excluding_by_entity_id(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        excluded_entities: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindPathExcludingByEntityIDRequest(  # type: ignore[unused-ignore]
                entityID1=entity_id_1,
                entityID2=entity_id_2,
                maxDegree=max_degree,
                excludedEntities=as_str(excluded_entities),
            )
            response = self.stub.FindPathExcludingByEntityID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_excluding_by_entity_id_v2(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        excluded_entities: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindPathExcludingByEntityID_V2Request(  # type: ignore[unused-ignore]
                entityID1=entity_id_1,
                entityID2=entity_id_2,
                maxDegree=max_degree,
                excludedEntities=as_str(excluded_entities),
                flags=flags,
            )
            response = self.stub.FindPathExcludingByEntityID_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_excluding_by_record_id(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        excluded_records: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindPathExcludingByRecordIDRequest(  # type: ignore[unused-ignore]
                dataSourceCode1=data_source_code_1,
                recordID1=record_id_1,
                dataSourceCode2=data_source_code_2,
                recordID2=record_id_2,
                maxDegree=max_degree,
                excludedRecords=as_str(excluded_records),
            )
            response = self.stub.FindPathExcludingByRecordID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_excluding_by_record_id_v2(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        excluded_records: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindPathExcludingByRecordID_V2Request(  # type: ignore[unused-ignore]
                dataSourceCode1=data_source_code_1,
                recordID1=record_id_1,
                dataSourceCode2=data_source_code_2,
                recordID2=record_id_2,
                maxDegree=max_degree,
                excludedRecords=as_str(excluded_records),
                flags=flags,
            )
            response = self.stub.FindPathExcludingByRecordID_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_including_source_by_entity_id(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        excluded_entities: Union[str, Dict[Any, Any]],
        required_dsrcs: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindPathIncludingSourceByEntityIDRequest(  # type: ignore[unused-ignore]
                entityID1=entity_id_1,
                entityID2=entity_id_2,
                maxDegree=max_degree,
                excludedEntities=as_str(excluded_entities),
                requiredDsrcs=as_str(required_dsrcs),
            )
            response = self.stub.FindPathIncludingSourceByEntityID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_including_source_by_entity_id_v2(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        excluded_entities: Union[str, Dict[Any, Any]],
        required_dsrcs: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindPathIncludingSourceByEntityID_V2Request(  # type: ignore[unused-ignore]
                entityID1=entity_id_1,
                entityID2=entity_id_2,
                maxDegree=max_degree,
                excludedEntities=as_str(excluded_entities),
                requiredDsrcs=as_str(required_dsrcs),
                flags=flags,
            )
            response = self.stub.FindPathIncludingSourceByEntityID_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_including_source_by_record_id(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        excluded_records: Union[str, Dict[Any, Any]],
        required_dsrcs: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindPathIncludingSourceByRecordIDRequest(  # type: ignore[unused-ignore]
                dataSourceCode1=data_source_code_1,
                recordID1=record_id_1,
                dataSourceCode2=data_source_code_2,
                recordID2=record_id_2,
                maxDegree=max_degree,
                excludedRecords=as_str(excluded_records),
                requiredDsrcs=as_str(required_dsrcs),
            )
            response = self.stub.FindPathIncludingSourceByRecordID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_including_source_by_record_id_v2(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        excluded_records: Union[str, Dict[Any, Any]],
        required_dsrcs: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.FindPathIncludingSourceByRecordID_V2Request(  # type: ignore[unused-ignore]
                dataSourceCode1=data_source_code_1,
                recordID1=record_id_1,
                dataSourceCode2=data_source_code_2,
                recordID2=record_id_2,
                maxDegree=max_degree,
                excludedRecords=as_str(excluded_records),
                requiredDsrcs=as_str(required_dsrcs),
                flags=flags,
            )
            response = self.stub.FindPathIncludingSourceByRecordID_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_active_config_id(self, **kwargs: Any) -> int:
        try:
            request = g2engine_pb2.GetActiveConfigIDRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetActiveConfigID(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.GetEntityByEntityIDRequest(  # type: ignore[unused-ignore]
                entityID=entity_id,
            )
            response = self.stub.GetEntityByEntityID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_entity_by_entity_id_v2(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.GetEntityByEntityID_V2Request(  # type: ignore[unused-ignore]
                entityID=entity_id,
                flags=flags,
            )
            response = self.stub.GetEntityByEntityID_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_entity_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.GetEntityByRecordIDRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
            )
            response = self.stub.GetEntityByRecordID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_entity_by_record_id_v2(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.GetEntityByRecordID_V2Request(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                flags=flags,
            )
            response = self.stub.GetEntityByRecordID_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_record(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_RECORD_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.GetRecord_V2Request(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                flags=flags,
            )
            response = self.stub.GetRecord_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_record_v2(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_RECORD_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.GetRecord_V2Request(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                flags=flags,
            )
            response = self.stub.GetRecord_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_redo_record(self, **kwargs: Any) -> str:
        try:
            request = g2engine_pb2.GetRedoRecordRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetRedoRecord(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_repository_last_modified_time(self, **kwargs: Any) -> int:
        try:
            request = g2engine_pb2.GetRepositoryLastModifiedTimeResponse()  # type: ignore[unused-ignore]
            response = self.stub.GetRepositoryLastModifiedTime(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_virtual_entity_by_record_id(
        self,
        record_list: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.GetVirtualEntityByRecordIDRequest(  # type: ignore[unused-ignore]
                recordList=as_str(record_list),
            )
            response = self.stub.GetVirtualEntityByRecordID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_virtual_entity_by_record_id_v2(
        self,
        record_list: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.GetVirtualEntityByRecordID_V2Request(  # type: ignore[unused-ignore]
                recordList=as_str(record_list),
                flags=flags,
            )
            response = self.stub.GetVirtualEntityByRecordID_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def how_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.HowEntityByEntityIDRequest(  # type: ignore[unused-ignore]
                entityID=entity_id,
            )
            response = self.stub.HowEntityByEntityID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def how_entity_by_entity_id_v2(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.HowEntityByEntityID_V2Request(  # type: ignore[unused-ignore]
                entityID=entity_id,
                flags=flags,
            )
            response = self.stub.HowEntityByEntityID_V2(request)
            return str(response.result)
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

    def prime_engine(self, **kwargs: Any) -> None:
        """Null function"""

    def process(self, record: Union[str, Dict[Any, Any]], **kwargs: Any) -> None:
        try:
            request = g2engine_pb2.ProcessRequest(  # type: ignore[unused-ignore]
                record=as_str(record),
            )
            self.stub.Process(request)
        except Exception as err:
            raise new_exception(err) from err

    def process_with_info(
        self, record: Union[str, Dict[Any, Any]], flags: int, **kwargs: Any
    ) -> str:
        try:
            request = g2engine_pb2.ProcessWithInfoRequest(  # type: ignore[unused-ignore]
                record=as_str(record),
                flags=flags,
            )
            response = self.stub.ProcessWithInfo(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def purge_repository(self, **kwargs: Any) -> None:
        """Null function"""

    def reevaluate_entity(self, entity_id: int, flags: int = 0, **kwargs: Any) -> None:
        try:
            request = g2engine_pb2.ReevaluateEntityRequest(  # type: ignore[unused-ignore]
                entityID=entity_id,
                flags=flags,
            )
            self.stub.ReevaluateEntity(request)
        except Exception as err:
            raise new_exception(err) from err

    def reevaluate_entity_with_info(
        self, entity_id: int, flags: int = 0, **kwargs: Any
    ) -> str:
        try:
            request = g2engine_pb2.ReevaluateEntityWithInfoRequest(  # type: ignore[unused-ignore]
                entityID=entity_id,
                flags=flags,
            )
            response = self.stub.ReevaluateEntityWithInfo(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def reevaluate_record(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> None:
        try:
            request = g2engine_pb2.ReevaluateRecordRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                flags=flags,
            )
            self.stub.ReevaluateRecord(request)
        except Exception as err:
            raise new_exception(err) from err

    def reevaluate_record_with_info(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.ReevaluateRecordWithInfoRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                flags=flags,
            )
            response = self.stub.ReevaluateRecordWithInfo(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def reinit(self, init_config_id: int, **kwargs: Any) -> None:
        try:
            request = g2engine_pb2.ReinitRequest(  # type: ignore[unused-ignore]
                initConfigID=init_config_id,
            )
            self.stub.Reinit(request)
        except Exception as err:
            raise new_exception(err) from err

    def replace_record(
        self,
        data_source_code: str,
        record_id: str,
        json_data: Union[str, Dict[Any, Any]],
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        **kwargs: Any,
    ) -> None:
        try:
            request = g2engine_pb2.ReplaceRecordRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                jsonData=as_str(json_data),
                loadID=load_id,
            )
            self.stub.ReplaceRecord(request)
        except Exception as err:
            raise new_exception(err) from err

    def replace_record_with_info(
        self,
        data_source_code: str,
        record_id: str,
        json_data: Union[str, Dict[Any, Any]],
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.ReplaceRecordWithInfoRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                jsonData=as_str(json_data),
                loadID=load_id,
                flags=flags,
            )
            response = self.stub.ReplaceRecordWithInfo(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def search_by_attributes(
        self,
        json_data: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.SearchByAttributesRequest(  # type: ignore[unused-ignore]
                jsonData=as_str(json_data),
            )
            response = self.stub.SearchByAttributes(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def search_by_attributes_v2(
        self,
        json_data: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.SearchByAttributes_V2Request(  # type: ignore[unused-ignore]
                jsonData=as_str(json_data),
                flags=flags,
            )
            response = self.stub.SearchByAttributes_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def search_by_attributes_v3(
        self,
        json_data: Union[str, Dict[Any, Any]],
        search_profile: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(json_data, search_profile, flags)
        return "{}"
        # TODO: Uncomment after V3 is published.
        # try:
        #     request = g2engine_pb2.SearchByAttributes_V3Request(  # type: ignore[unused-ignore]
        #         jsonData=as_str(json_data),
        #         searchProfile=as_str(search_profile),
        #         flags=flags,
        #     )
        #     response = self.stub.SearchByAttributes_V3(request)
        #     return str(response.result)
        # except Exception as err:
        #     raise new_exception(err) from err

    def stats(self, **kwargs: Any) -> str:
        try:
            request = g2engine_pb2.StatsRequest()  # type: ignore[unused-ignore]
            response = self.stub.Stats(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_entities(
        self,
        entity_id_1: int,
        entity_id_2: int,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.WhyEntitiesRequest(  # type: ignore[unused-ignore]
                entityID1=entity_id_1,
                entityID2=entity_id_2,
            )
            response = self.stub.WhyEntities(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_entities_v2(
        self,
        entity_id_1: int,
        entity_id_2: int,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.WhyEntities_V2Request(  # type: ignore[unused-ignore]
                entityID1=entity_id_1,
                entityID2=entity_id_2,
                flags=flags,
            )
            response = self.stub.WhyEntities_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.WhyEntityByEntityIDRequest(  # type: ignore[unused-ignore]
                entityID=entity_id,
            )
            response = self.stub.WhyEntityByEntityID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_entity_by_entity_id_v2(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.WhyEntityByEntityID_V2Request(  # type: ignore[unused-ignore]
                entityID=entity_id,
                flags=flags,
            )
            response = self.stub.WhyEntityByEntityID_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_entity_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.WhyEntityByRecordIDRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
            )
            response = self.stub.WhyEntityByRecordID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_entity_by_record_id_v2(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.WhyEntityByRecordID_V2Request(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                flags=flags,
            )
            response = self.stub.WhyEntityByRecordID_V2(request)
            return as_str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_record_in_entity(
        self,
        data_source_code: str,
        record_id: str,
        **kwargs: Any,
    ) -> str:
        # TODO: Implement after V3 is published.
        self.fake_g2engine(data_source_code, record_id)
        return "string"

    def why_record_in_entity_v2(
        self,
        data_source_code: str,
        record_id: str,
        flags: int,
        **kwargs: Any,
    ) -> str:
        # TODO: Implement after V3 is published.
        self.fake_g2engine(data_source_code, record_id, flags)
        return "string"

    def why_records(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.WhyRecordsRequest(  # type: ignore[unused-ignore]
                dataSourceCode1=data_source_code_1,
                recordID1=record_id_1,
                dataSourceCode2=data_source_code_2,
                recordID2=record_id_2,
            )
            response = self.stub.WhyRecords(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_records_v2(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = g2engine_pb2.WhyRecords_V2Request(  # type: ignore[unused-ignore]
                dataSourceCode1=data_source_code_1,
                recordID1=record_id_1,
                dataSourceCode2=data_source_code_2,
                recordID2=record_id_2,
                flags=flags,
            )
            response = self.stub.WhyRecords_V2(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err
