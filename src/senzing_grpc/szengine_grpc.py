#! /usr/bin/env python3

"""
TODO: g2engine_grpc.py
"""

# pylint: disable=E1101,C0302

from types import TracebackType
from typing import Any, Dict, Iterable, Type, Union

import grpc
from senzing_abstract import SzEngineAbstract, SzEngineFlags

from .pb2_grpc import szengine_pb2, szengine_pb2_grpc
from .szhelpers import as_str, new_exception

# Metadata

__all__ = ["G2EngineGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-11-27"
__updated__ = "2024-01-10"

SENZING_PRODUCT_ID = "5053"  # See https://github.com/senzing-garage/knowledge-base/blob/main/lists/senzing-component-ids.md

# -----------------------------------------------------------------------------
# G2EngineGrpc class
# -----------------------------------------------------------------------------


class G2EngineGrpc(SzEngineAbstract):  # type: ignore
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
        self.stub = szengine_pb2_grpc.SzEngineStub(self.channel)
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
        record_definition: Union[str, Dict[Any, Any]],
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.AddRecordRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                jsonData=as_str(record_definition),
                flags=flags,
            )
            self.stub.AddRecord(request)
            response = self.stub.AddRecord(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def close_export(self, export_handle: int, **kwargs: Any) -> None:
        try:
            request = szengine_pb2.CloseExportRequest(  # type: ignore[unused-ignore]
                responseHandle=export_handle,
            )
            self.stub.CloseExport(request)
        except Exception as err:
            raise new_exception(err) from err

    def count_redo_records(self, **kwargs: Any) -> int:
        try:
            request = szengine_pb2.CountRedoRecordsRequest()  # type: ignore[unused-ignore]
            response = self.stub.CountRedoRecords(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def delete_record(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.DeleteRecordRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                flags=flags,
            )
            response = self.stub.DeleteRecord(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def destroy(self, **kwargs: Any) -> None:
        """Null function"""

    def export_csv_entity_report(
        self,
        csv_column_list: str,
        flags: int = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> int:
        try:
            request = szengine_pb2.ExportCSVEntityReportRequest(  # type: ignore[unused-ignore]
                csvColumnList=csv_column_list,
                flags=flags,
            )
            response = self.stub.ExportCsvEntityReport(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def export_csv_entity_report_iterator(
        self,
        csv_column_list: str,
        flags: int = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> Iterable[str]:
        if len(kwargs) > 0:
            pass  # TODO: To disable pylint W0613
        try:
            request = szengine_pb2.StreamExportCsvEntityReportRequest(  # type: ignore[unused-ignore]
                csv_column_list=csv_column_list, flags=flags
            )
            for item in self.stub.StreamExportCsvEntityReport(request):
                if item.result:
                    yield item.result
        except Exception as err:
            raise new_exception(err) from err

    def export_json_entity_report(
        self, flags: int = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS, **kwargs: Any
    ) -> int:
        try:
            request = szengine_pb2.ExportJsonEntityReportRequest(  # type: ignore[unused-ignore]
                flags=flags,
            )
            response = self.stub.ExportJsonEntityReport(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def export_json_entity_report_iterator(
        self,
        flags: int = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> Iterable[str]:
        if len(kwargs) > 0:
            pass  # TODO: To disable pylint W0613
        try:
            request = szengine_pb2.StreamExportJsonEntityReportRequest(  # type: ignore[unused-ignore]
                flags=flags
            )
            for item in self.stub.StreamExportJsonEntityReport(request):
                if item.result:
                    yield item.result
        except Exception as err:
            raise new_exception(err) from err

    def fetch_next(self, export_handle: int, **kwargs: Any) -> str:
        try:
            request = szengine_pb2.FetchNextRequest(  # type: ignore[unused-ignore]
                responseHandle=response_handle,
            )
            response = self.stub.FetchNext(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    # def find_interesting_entities_by_entity_id(
    #     self, entity_id: int, flags: int = 0, **kwargs: Any
    # ) -> str:
    #     try:
    #         request = szengine_pb2.FindInterestingEntitiesByEntityIDRequest(  # type: ignore[unused-ignore]
    #             entityID=entity_id,
    #             flags=flags,
    #         )
    #         response = self.stub.FindInterestingEntitiesByEntityId(request)
    #         return str(response.result)
    #     except Exception as err:
    #         raise new_exception(err) from err

    # def find_interesting_entities_by_record_id(
    #     self, data_source_code: str, record_id: str, flags: int = 0, **kwargs: Any
    # ) -> str:
    #     try:
    #         request = szengine_pb2.FindInterestingEntitiesByRecordIDRequest(  # type: ignore[unused-ignore]
    #             dataSourceCode=data_source_code,
    #             recordID=record_id,
    #             flags=flags,
    #         )
    #         response = self.stub.FindInterestingEntitiesByRecordID(request)
    #         return str(response.result)
    #     except Exception as err:
    #         raise new_exception(err) from err

    def find_network_by_entity_id(
        self,
        entity_list: Union[str, Dict[str, List[Dict[str, int]]]],
        max_degrees: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.FindNetworkByEntityIDRequest(  # type: ignore[unused-ignore]
                entityList=as_str(entity_list),
                maxDegree=max_degrees,
                buildOutDegree=build_out_degree,
                maxEntities=max_entities,
            )
            response = self.stub.FindNetworkByEntityId(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_network_by_record_id(
        self,
        record_list: Union[str, Dict[str, List[Dict[str, str]]]],
        max_degrees: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.FindNetworkByRecordIDRequest(  # type: ignore[unused-ignore]
                recordList=as_str(record_list),
                maxDegree=max_degree,
                buildOutDegree=build_out_degree,
                maxEntities=max_entities,
            )
            response = self.stub.FindNetworkByRecordID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_by_entity_id(
        self,
        start_entity_id: int,
        end_entity_id: int,
        max_degrees: int,
        # TODO Should accept both entity and record IDs in V4, test
        exclusions: Union[str, Dict[Any, Any]] = "",
        required_data_sources: Union[str, Dict[Any, Any]] = "",
        flags: int = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.FindPathByEntityIDRequest(  # type: ignore[unused-ignore]
                entityID1=entity_id_1,
                entityID2=entity_id_2,
                maxDegree=max_degree,
            )
            response = self.stub.FindPathByEntityID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_by_record_id(
        self,
        start_data_source_code: str,
        start_record_id: str,
        end_data_source_code: str,
        end_record_id: str,
        max_degrees: int,
        exclusions: Union[str, Dict[Any, Any]] = "",
        required_data_sources: Union[str, Dict[Any, Any]] = "",
        flags: int = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.FindPathByRecordIDRequest(  # type: ignore[unused-ignore]
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

    def get_active_config_id(self, **kwargs: Any) -> int:
        try:
            request = szengine_pb2.GetActiveConfigIDRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetActiveConfigID(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = SzEngineFlags.SZ_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.GetEntityByEntityIDRequest(  # type: ignore[unused-ignore]
                entityID=entity_id,
            )
            response = self.stub.GetEntityByEntityID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_entity_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = SzEngineFlags.SZ_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.GetEntityByRecordIDRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
            )
            response = self.stub.GetEntityByRecordID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_record(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = SzEngineFlags.SZ_RECORD_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.GetRecord_V2Request(  # type: ignore[unused-ignore]
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
            request = szengine_pb2.GetRedoRecordRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetRedoRecord(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_repository_last_modified_time(self, **kwargs: Any) -> int:
        try:
            request = szengine_pb2.GetRepositoryLastModifiedTimeResponse()  # type: ignore[unused-ignore]
            response = self.stub.GetRepositoryLastModifiedTime(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_stats(self, **kwargs: Any) -> str:
        try:
            request = szengine_pb2.StatsRequest()  # type: ignore[unused-ignore]
            response = self.stub.Stats(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_virtual_entity_by_record_id(
        self,
        record_list: Union[str, Dict[Any, Any]],
        flags: int = SzEngineFlags.SZ_VIRTUAL_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.GetVirtualEntityByRecordIDRequest(  # type: ignore[unused-ignore]
                recordList=as_str(record_list),
            )
            response = self.stub.GetVirtualEntityByRecordID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def how_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = SzEngineFlags.SZ_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.HowEntityByEntityIDRequest(  # type: ignore[unused-ignore]
                entityID=entity_id,
            )
            response = self.stub.HowEntityByEntityID(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def initialize(
        self,
        instance_name: str,
        settings: Union[str, Dict[Any, Any]],
        config_id: Optional[int] = None,
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """Null function"""

    def prime_engine(self, **kwargs: Any) -> None:
        """Null function"""

    def process_redo_record(self, redo_record: str, flags: int, **kwargs: Any) -> str:
        try:
            request = szengine_pb2.ProcessRedoRecordRequest(  # type: ignore[unused-ignore]
                record=as_str(redo_record),
                flags=flags,
            )
            response = self.stub.ProcessRedoRecord(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def reevaluate_entity(self, entity_id: int, flags: int = 0, **kwargs: Any) -> str:
        try:
            request = szengine_pb2.ReevaluateEntityRequest(  # type: ignore[unused-ignore]
                entityID=entity_id,
                flags=flags,
            )
            response = self.stub.ReevaluateEntity(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def reevaluate_record(
        self, data_source_code: str, record_id: str, flags: int = 0, **kwargs: Any
    ) -> str:
        try:
            request = szengine_pb2.ReevaluateRecordRequest(  # type: ignore[unused-ignore]
                dataSourceCode=data_source_code,
                recordID=record_id,
                flags=flags,
            )
            response = self.stub.ReevaluateRecord(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def reinitialize(self, config_id: int, **kwargs: Any) -> None:
        """Null function"""

    def search_by_attributes(
        self,
        attributes: Union[str, Dict[Any, Any]],
        search_profile: str = "",
        flags: int = SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.SearchByAttributesRequest(  # type: ignore[unused-ignore]
                jsonData=as_str(json_data),
            )
            response = self.stub.SearchByAttributes(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_entities(
        self,
        entity_id_1: int,
        entity_id_2: int,
        flags: int = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.WhyEntitiesRequest(  # type: ignore[unused-ignore]
                entityID1=entity_id_1,
                entityID2=entity_id_2,
            )
            response = self.stub.WhyEntities(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_record_in_entity(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = SzEngineFlags.SZ_WHY_RECORDS_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        # TODO: Implement after V3 is published.
        self.fake_g2engine(data_source_code, record_id)
        return "string"

    def why_records(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        flags: int = SzEngineFlags.SZ_WHY_RECORDS_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        try:
            request = szengine_pb2.WhyRecordsRequest(  # type: ignore[unused-ignore]
                dataSourceCode1=data_source_code_1,
                recordID1=record_id_1,
                dataSourceCode2=data_source_code_2,
                recordID2=record_id_2,
            )
            response = self.stub.WhyRecords(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err
