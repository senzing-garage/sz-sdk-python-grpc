#! /usr/bin/env python3

"""
``senzing_grpc.szengine.SzEngineGrpc`` is a `gRPC`_ implementation
of the `senzing.szengine.SzEngine`_ interface.

.. _gRPC: https://grpc.io
.. _senzing.szengine.SzEngine: https://garage.senzing.com/sz-sdk-python/senzing.html#module-senzing.szengine
"""

# pylint: disable=E1101,C0302

import json
from types import TracebackType
from typing import Any, Dict, Iterable, List, Optional, Tuple, Type, Union

import grpc
from senzing import SzEngine, SzEngineFlags
from senzing_grpc_protobuf import szengine_pb2, szengine_pb2_grpc

from .szhelpers import as_str, new_exception

# Metadata

__all__ = ["SzEngineGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2025-01-10"
__updated__ = "2025-01-16"

SENZING_PRODUCT_ID = (
    "5053"  # See https://github.com/senzing-garage/knowledge-base/blob/main/lists/senzing-component-ids.md
)

# -----------------------------------------------------------------------------
# SzEngineGrpc class
# -----------------------------------------------------------------------------


class SzEngineGrpc(SzEngine):
    """
    Sz engine module access library over gRPC.
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
    # SzEngine methods
    # -------------------------------------------------------------------------

    def add_record(
        self,
        data_source_code: str,
        record_id: str,
        record_definition: str,
        flags: int = SzEngineFlags.SZ_ADD_RECORD_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.AddRecordRequest(  # type: ignore[unused-ignore]
                data_source_code=as_str(data_source_code),
                record_id=as_str(record_id),
                record_definition=as_str(record_definition),
                flags=flags,
            )
            response = self.stub.AddRecord(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def close_export_report(self, export_handle: int) -> None:
        try:
            request = szengine_pb2.CloseExportReportRequest(  # type: ignore[unused-ignore]
                export_handle=export_handle,
            )
            self.stub.CloseExportReport(request)
        except Exception as err:
            raise new_exception(err) from err

    def count_redo_records(self) -> int:
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
        flags: int = SzEngineFlags.SZ_DELETE_RECORD_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.DeleteRecordRequest(  # type: ignore[unused-ignore]
                data_source_code=as_str(data_source_code),
                record_id=as_str(record_id),
                flags=flags,
            )
            response = self.stub.DeleteRecord(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def export_csv_entity_report(
        self,
        csv_column_list: str,
        flags: int = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS,
    ) -> int:
        try:
            request = szengine_pb2.ExportCsvEntityReportRequest(  # type: ignore[unused-ignore]
                csv_column_list=as_str(csv_column_list),
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
    ) -> Iterable[str]:
        """TODO: Add method docstring to export_csv_entity_report_iterator."""
        try:
            request = szengine_pb2.StreamExportCsvEntityReportRequest(  # type: ignore[unused-ignore]
                csv_column_list=as_str(csv_column_list), flags=flags
            )
            for item in self.stub.StreamExportCsvEntityReport(request):
                if item.result:
                    yield item.result
        except Exception as err:
            raise new_exception(err) from err

    def export_json_entity_report(self, flags: int = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS) -> int:
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
    ) -> Iterable[str]:
        """TODO: Add method docstring to export_json_entity_report_iterator."""
        try:
            request = szengine_pb2.StreamExportJsonEntityReportRequest(flags=flags)  # type: ignore[unused-ignore]
            for item in self.stub.StreamExportJsonEntityReport(request):
                if item.result:
                    yield item.result
        except Exception as err:
            raise new_exception(err) from err

    def fetch_next(self, export_handle: int) -> str:
        try:
            request = szengine_pb2.FetchNextRequest(  # type: ignore[unused-ignore]
                export_handle=export_handle,
            )
            response = self.stub.FetchNext(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_interesting_entities_by_entity_id(
        self, entity_id: int, flags: int = SzEngineFlags.SZ_FIND_INTERESTING_ENTITIES_DEFAULT_FLAGS
    ) -> str:
        try:
            request = szengine_pb2.FindInterestingEntitiesByEntityIdRequest(  # type: ignore[unused-ignore]
                entity_id=entity_id,
                flags=flags,
            )
            response = self.stub.FindInterestingEntitiesByEntityId(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_interesting_entities_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = SzEngineFlags.SZ_FIND_INTERESTING_ENTITIES_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.FindInterestingEntitiesByRecordIdRequest(  # type: ignore[unused-ignore]
                data_source_code=as_str(data_source_code),
                record_id=as_str(record_id),
                flags=flags,
            )
            response = self.stub.FindInterestingEntitiesByRecordId(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_network_by_entity_id(
        self,
        entity_ids: List[int],
        max_degrees: int,
        build_out_degrees: int,
        build_out_max_entities: int,
        flags: int = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.FindNetworkByEntityIdRequest(  # type: ignore[unused-ignore]
                entity_ids=entity_ids_json(entity_ids),
                max_degrees=max_degrees,
                build_out_degrees=build_out_degrees,
                build_out_max_entities=build_out_max_entities,
                flags=flags,
            )
            response = self.stub.FindNetworkByEntityId(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_network_by_record_id(
        self,
        record_keys: List[Tuple[str, str]],
        max_degrees: int,
        build_out_degrees: int,
        build_out_max_entities: int,
        flags: int = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.FindNetworkByRecordIdRequest(  # type: ignore[unused-ignore]
                record_keys=record_keys_json(record_keys),
                max_degrees=max_degrees,
                build_out_degrees=build_out_degrees,
                build_out_max_entities=build_out_max_entities,
                flags=flags,
            )
            response = self.stub.FindNetworkByRecordId(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def find_path_by_entity_id(
        self,
        start_entity_id: int,
        end_entity_id: int,
        max_degrees: int,
        # TODO Should accept both entity and record IDs in V4, test
        avoid_entity_ids: Optional[List[int]] = None,
        required_data_sources: Optional[List[str]] = None,
        flags: int = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.FindPathByEntityIdRequest(  # type: ignore[unused-ignore]
                start_entity_id=start_entity_id,
                end_entity_id=end_entity_id,
                max_degrees=max_degrees,
                avoid_entity_ids=avoid_entity_ids_json(avoid_entity_ids),
                required_data_sources=required_data_sources_json(required_data_sources),
                flags=flags,
            )
            response = self.stub.FindPathByEntityId(request)
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
        avoid_record_keys: Optional[List[Tuple[str, str]]] = None,
        required_data_sources: Optional[List[str]] = None,
        flags: int = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.FindPathByRecordIdRequest(  # type: ignore[unused-ignore]
                start_data_source_code=as_str(start_data_source_code),
                start_record_id=as_str(start_record_id),
                end_data_source_code=as_str(end_data_source_code),
                end_record_id=as_str(end_record_id),
                max_degrees=max_degrees,
                avoid_record_keys=avoid_record_keys_json(avoid_record_keys),
                required_data_sources=required_data_sources_json(required_data_sources),
                flags=flags,
            )
            response = self.stub.FindPathByRecordId(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_active_config_id(self) -> int:
        try:
            request = szengine_pb2.GetActiveConfigIdRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetActiveConfigId(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = SzEngineFlags.SZ_ENTITY_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.GetEntityByEntityIdRequest(  # type: ignore[unused-ignore]
                entity_id=entity_id,
                flags=flags,
            )
            response = self.stub.GetEntityByEntityId(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_entity_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = SzEngineFlags.SZ_ENTITY_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.GetEntityByRecordIdRequest(  # type: ignore[unused-ignore]
                data_source_code=as_str(data_source_code),
                record_id=as_str(record_id),
                flags=flags,
            )
            response = self.stub.GetEntityByRecordId(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_record(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = SzEngineFlags.SZ_RECORD_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.GetRecordRequest(  # type: ignore[unused-ignore]
                data_source_code=as_str(data_source_code),
                record_id=as_str(record_id),
                flags=flags,
            )
            response = self.stub.GetRecord(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_redo_record(self) -> str:
        try:
            request = szengine_pb2.GetRedoRecordRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetRedoRecord(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_stats(self) -> str:
        try:
            request = szengine_pb2.GetStatsRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetStats(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_virtual_entity_by_record_id(
        self,
        record_keys: List[Tuple[str, str]],
        flags: int = SzEngineFlags.SZ_VIRTUAL_ENTITY_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.GetVirtualEntityByRecordIdRequest(  # type: ignore[unused-ignore]
                record_keys=record_keys_json(record_keys),
                flags=flags,
            )
            response = self.stub.GetVirtualEntityByRecordId(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def how_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = SzEngineFlags.SZ_HOW_ENTITY_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.HowEntityByEntityIdRequest(  # type: ignore[unused-ignore]
                entity_id=entity_id,
                flags=flags,
            )
            response = self.stub.HowEntityByEntityId(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_record_preview(
        self,
        record_definition: str,
        flags: int = SzEngineFlags.SZ_RECORD_PREVIEW_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.GetRecordPreviewRequest(  # type: ignore[unused-ignore]
                record_definition=as_str(record_definition),
                flags=flags,
            )
            response = self.stub.GetRecordPreview(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def prime_engine(self) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""

    def process_redo_record(self, redo_record: str, flags: int = 0) -> str:
        try:
            request = szengine_pb2.ProcessRedoRecordRequest(  # type: ignore[unused-ignore]
                redo_record=as_str(redo_record),
                flags=flags,
            )
            response = self.stub.ProcessRedoRecord(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def reevaluate_entity(self, entity_id: int, flags: int = SzEngineFlags.SZ_REEVALUATE_RECORD_DEFAULT_FLAGS) -> str:
        try:
            request = szengine_pb2.ReevaluateEntityRequest(  # type: ignore[unused-ignore]
                entity_id=entity_id,
                flags=flags,
            )
            response = self.stub.ReevaluateEntity(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def reevaluate_record(
        self, data_source_code: str, record_id: str, flags: int = SzEngineFlags.SZ_REEVALUATE_RECORD_DEFAULT_FLAGS
    ) -> str:
        try:
            request = szengine_pb2.ReevaluateRecordRequest(  # type: ignore[unused-ignore]
                data_source_code=as_str(data_source_code),
                record_id=as_str(record_id),
                flags=flags,
            )
            response = self.stub.ReevaluateRecord(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def search_by_attributes(
        self,
        attributes: str,
        flags: int = SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,
        search_profile: str = "",
    ) -> str:
        try:
            request = szengine_pb2.SearchByAttributesRequest(  # type: ignore[unused-ignore]
                attributes=as_str(attributes),
                search_profile=as_str(search_profile),
                flags=flags,
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
    ) -> str:
        try:
            request = szengine_pb2.WhyEntitiesRequest(  # type: ignore[unused-ignore]
                entity_id_1=entity_id_1,
                entity_id_2=entity_id_2,
                flags=flags,
            )
            response = self.stub.WhyEntities(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_record_in_entity(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = SzEngineFlags.SZ_WHY_RECORD_IN_ENTITY_DEFAULT_FLAGS,
    ) -> str:
        # TODO: Implement after V3 is published.
        try:
            request = szengine_pb2.WhyRecordInEntityRequest(  # type: ignore[unused-ignore]
                data_source_code=as_str(data_source_code),
                record_id=as_str(record_id),
                flags=flags,
            )
            response = self.stub.WhyRecordInEntity(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_records(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        flags: int = SzEngineFlags.SZ_WHY_RECORDS_DEFAULT_FLAGS,
    ) -> str:
        try:
            request = szengine_pb2.WhyRecordsRequest(  # type: ignore[unused-ignore]
                data_source_code_1=as_str(data_source_code_1),
                record_id_1=as_str(record_id_1),
                data_source_code_2=as_str(data_source_code_2),
                record_id_2=as_str(record_id_2),
                flags=flags,
            )
            response = self.stub.WhyRecords(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def why_search(
        self,
        attributes: str,
        entity_id: int,
        flags: int = SzEngineFlags.SZ_WHY_SEARCH_DEFAULT_FLAGS,
        search_profile: str = "",
    ) -> str:
        try:
            request = szengine_pb2.WhySearchRequest(  # type: ignore[unused-ignore]
                attributes=as_str(attributes),
                entity_id=entity_id,
                search_profile=as_str(search_profile),
                flags=flags,
            )
            response = self.stub.WhySearch(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    # -------------------------------------------------------------------------
    # Non-public SzEngine methods
    # -------------------------------------------------------------------------

    def _destroy(self) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""

    def initialize(
        self,
        instance_name: str,
        settings: Union[str, Dict[Any, Any]],
        config_id: Optional[int] = None,
        verbose_logging: int = 0,
    ) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""
        _ = instance_name
        _ = settings
        _ = config_id
        _ = verbose_logging

    def reinitialize(self, config_id: int) -> None:
        try:
            request = szengine_pb2.ReinitializeRequest(config_id=config_id)  # type: ignore[unused-ignore]
            self.stub.Reinitialize(request)
        except Exception as err:
            raise new_exception(err) from err


# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------


def entity_ids_json(entity_ids: List[int]) -> str:
    entity_list = []
    for entity_id in entity_ids:
        entity_list.append({"ENTITY_ID": entity_id})
    return json.dumps({"ENTITIES": entity_list})


def record_keys_json(record_keys: List[Tuple[str, str]]) -> str:
    record_key_list = []
    for record_key in record_keys:
        record_key_list.append({"DATA_SOURCE": record_key[0], "RECORD_ID": record_key[1]})
    return json.dumps({"RECORDS": record_key_list})


def avoid_entity_ids_json(avoid_entity_ids: Optional[List[int]] = None) -> str:
    result = ""
    if avoid_entity_ids:
        avoid_entity_id_list = []
        for avoid_entity_id in avoid_entity_ids:
            avoid_entity_id_list.append({"ENTITY_ID": avoid_entity_id})
        result = json.dumps({"ENTITIES": avoid_entity_id_list})
    return result


def avoid_record_keys_json(avoid_record_keys: Optional[List[Tuple[str, str]]] = None) -> str:
    result = ""
    if avoid_record_keys:
        avoid_record_keys_list = []
        for avoid_record_key in avoid_record_keys:
            avoid_record_keys_list.append(
                {
                    "DATA_SOURCE": avoid_record_key[0],
                    "RECORD_ID": avoid_record_key[1],
                }
            )
        result = json.dumps({"RECORDS": avoid_record_keys_list})
    return result


def required_data_sources_json(
    required_data_sources: Optional[List[str]] = None,
) -> str:
    result = ""
    if required_data_sources:
        required_data_sources_list = []
        for required_data_source in required_data_sources:
            required_data_sources_list.append(required_data_source)
        result = json.dumps({"DATA_SOURCES": required_data_sources_list})
    return result
