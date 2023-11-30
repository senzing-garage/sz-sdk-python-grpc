#! /usr/bin/env python3

"""
TODO: g2engine_grpc.py
"""

# pylint: disable=E1101

from typing import Any, Tuple

import grpc  # type: ignore

from .g2helpers import as_str, new_exception
from .localcopy.g2engine_abstract import G2EngineAbstract
from .localcopy.g2engineflags import G2EngineFlags
from .pb2_grpc import g2engine_pb2, g2engine_pb2_grpc

# Metadata

__all__ = ["G2EngineGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-11-27"
__updated__ = "2023-11-27"

SENZING_PRODUCT_ID = "5053"  # See https://github.com/Senzing/knowledge-base/blob/main/lists/senzing-component-ids.md

# -----------------------------------------------------------------------------
# G2EngineGrpc class
# -----------------------------------------------------------------------------


class G2EngineGrpc(G2EngineAbstract):
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

    def __enter__(self):
        """Context Manager method."""
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
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
        json_data: str,  # TODO: Fix typing to accept dict
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
        json_data: str,
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
            )
            response = self.stub.AddRecordWithInfo(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def close_export(self, response_handle: int, **kwargs: Any) -> None:
        self.fake_g2engine(response_handle)

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
        self.fake_g2engine(data_source_code, record_id, load_id)

    def delete_record_with_info(
        self,
        data_source_code: str,
        record_id: str,
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(data_source_code, record_id, load_id, flags)
        return "string"

    def destroy(self, **kwargs: Any) -> None:
        """No-op"""

    def export_config(self, **kwargs: Any) -> str:
        self.fake_g2engine()
        return "string"

    def export_config_and_config_id(self, **kwargs: Any) -> Tuple[str, int]:
        self.fake_g2engine()
        return "string", 0

    def export_csv_entity_report(
        self,
        csv_column_list: str,
        flags: int = G2EngineFlags.G2_EXPORT_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> int:
        self.fake_g2engine(csv_column_list, flags)
        return 0

    def export_json_entity_report(
        self, flags: int = G2EngineFlags.G2_EXPORT_DEFAULT_FLAGS, **kwargs: Any
    ) -> int:
        self.fake_g2engine(flags)
        return 0

    def fetch_next(self, response_handle: int, **kwargs: Any) -> str:
        self.fake_g2engine(response_handle)
        return "string"

    def find_interesting_entities_by_entity_id(
        self, entity_id: int, flags: int = 0, **kwargs: Any
    ) -> str:
        self.fake_g2engine(entity_id, flags)
        return "string"

    def find_interesting_entities_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(data_source_code, record_id, flags)
        return "string"

    def find_network_by_entity_id_v2(
        self,
        entity_list: str,
        max_degree: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(
            entity_list, max_degree, build_out_degree, max_entities, flags
        )
        return "string"

    def find_network_by_entity_id(
        self,
        entity_list: str,
        max_degree: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(entity_list, max_degree, build_out_degree, max_entities)
        return "string"

    def find_network_by_record_id_v2(
        self,
        record_list: str,
        max_degree: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(
            record_list, max_degree, build_out_degree, max_entities, flags
        )
        return "string"

    def find_network_by_record_id(
        self,
        record_list: str,
        max_degree: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(record_list, max_degree, build_out_degree, max_entities)
        return "string"

    def find_path_by_entity_id_v2(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(entity_id_1, entity_id_2, max_degree, flags)
        return "string"

    def find_path_by_entity_id(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(entity_id_1, entity_id_2, max_degree)
        return "string"

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
        self.fake_g2engine(
            data_source_code_1,
            record_id_1,
            data_source_code_2,
            record_id_2,
            max_degree,
            flags,
        )
        return "string"

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
        self.fake_g2engine(
            data_source_code_1, record_id_1, data_source_code_2, record_id_2, max_degree
        )
        return "string"

    def find_path_excluding_by_entity_id_v2(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        excluded_entities: str,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(
            entity_id_1, entity_id_2, max_degree, excluded_entities, flags
        )
        return "string"

    def find_path_excluding_by_entity_id(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        excluded_entities: str,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(entity_id_1, entity_id_2, max_degree, excluded_entities)
        return "string"

    def find_path_excluding_by_record_id_v2(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        excluded_records: str,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(
            data_source_code_1,
            record_id_1,
            data_source_code_2,
            record_id_2,
            max_degree,
            excluded_records,
            flags,
        )
        return "string"

    def find_path_excluding_by_record_id(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        excluded_records: str,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(
            data_source_code_1,
            record_id_1,
            data_source_code_2,
            record_id_2,
            max_degree,
            excluded_records,
        )
        return "string"

    def find_path_including_source_by_entity_id_v2(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        excluded_entities: str,
        required_dsrcs: str,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(
            entity_id_1,
            entity_id_2,
            max_degree,
            excluded_entities,
            required_dsrcs,
            flags,
        )
        return "string"

    def find_path_including_source_by_entity_id(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        excluded_entities: str,
        required_dsrcs: str,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(
            entity_id_1, entity_id_2, max_degree, excluded_entities, required_dsrcs
        )
        return "string"

    def find_path_including_source_by_record_id_v2(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        excluded_records: str,
        required_dsrcs: str,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(
            data_source_code_1,
            record_id_1,
            data_source_code_2,
            record_id_2,
            max_degree,
            excluded_records,
            required_dsrcs,
            flags,
        )
        return "string"

    def find_path_including_source_by_record_id(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        excluded_records: str,
        required_dsrcs: str,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(
            data_source_code_1,
            record_id_1,
            data_source_code_2,
            record_id_2,
            max_degree,
            excluded_records,
            required_dsrcs,
        )
        return "string"

    def get_active_config_id(self, **kwargs: Any) -> int:
        self.fake_g2engine()
        return 0

    def get_entity_by_entity_id_v2(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(entity_id, flags)
        return "string"

    def get_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(entity_id)
        return "string"

    def get_entity_by_record_id_v2(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(data_source_code, record_id, flags)
        return "string"

    def get_entity_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(data_source_code, record_id)
        return "string"

    def get_record_v2(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_RECORD_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(data_source_code, record_id, flags)
        return "string"

    def get_record(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_RECORD_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(data_source_code, record_id)
        return "string"

    def get_redo_record(self, **kwargs: Any) -> str:
        self.fake_g2engine()
        return "string"

    def get_repository_last_modified_time(self, **kwargs: Any) -> int:
        self.fake_g2engine()
        return 0

    def get_virtual_entity_by_record_id_v2(
        self,
        record_list: str,
        flags: int = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(record_list, flags)
        return "string"

    def get_virtual_entity_by_record_id(
        self,
        record_list: str,
        flags: int = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(record_list)
        return "string"

    def how_entity_by_entity_id_v2(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(entity_id, flags)
        return "string"

    def how_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(entity_id)
        return "string"

    def init(
        self, module_name: str, ini_params: str, verbose_logging: int = 0, **kwargs: Any
    ) -> None:
        """No-op"""

    def init_with_config_id(
        self,
        module_name: str,
        ini_params: str,
        init_config_id: int,
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """No-op"""

    def prime_engine(self, **kwargs: Any) -> None:
        """No-op"""

    def process(self, record: str, **kwargs: Any) -> None:
        self.fake_g2engine(record)

    def process_with_info(self, record: str, flags: int, **kwargs: Any) -> str:
        self.fake_g2engine(record, flags)
        return "string"

    def purge_repository(self, **kwargs: Any) -> None:
        self.fake_g2engine()

    def reevaluate_entity(self, entity_id: int, flags: int = 0, **kwargs: Any) -> None:
        self.fake_g2engine(entity_id, flags)

    def reevaluate_entity_with_info(
        self, entity_id: int, flags: int = 0, **kwargs: Any
    ) -> str:
        self.fake_g2engine(entity_id, flags)
        return "string"

    def reevaluate_record(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> None:
        self.fake_g2engine(data_source_code, record_id, flags)

    def reevaluate_record_with_info(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(data_source_code, record_id, flags)
        return "string"

    def reinit(self, init_config_id: int, **kwargs: Any) -> None:
        """No-op"""

    def replace_record(
        self,
        data_source_code: str,
        record_id: str,
        json_data: str,
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        **kwargs: Any,
    ) -> None:
        self.fake_g2engine(data_source_code, record_id, json_data, load_id)

    def replace_record_with_info(
        self,
        data_source_code: str,
        record_id: str,
        json_data: str,
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(data_source_code, record_id, json_data, load_id, flags)
        return "string"

    def search_by_attributes_v2(
        self,
        json_data: str,
        flags: int = G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(json_data, flags, flags)
        return "string"

    def search_by_attributes_v3(
        self,
        json_data: str,
        search_profile: str,
        flags: int = G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(json_data, search_profile, flags)
        return "string"

    def search_by_attributes(
        self,
        json_data: str,
        flags: int = G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(json_data)
        return "string"

    def stats(self, **kwargs: Any) -> str:
        self.fake_g2engine()
        return "string"

    def why_entities_v2(
        self,
        entity_id_1: int,
        entity_id_2: int,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(entity_id_1, entity_id_2, flags)
        return "string"

    def why_entities(
        self,
        entity_id_1: int,
        entity_id_2: int,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(entity_id_1, entity_id_2)
        return "string"

    def why_entity_by_entity_id_v2(
        self,
        entity_id: str,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(entity_id, flags)
        return "string"

    def why_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(entity_id)
        return "string"

    def why_entity_by_record_id_v2(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(data_source_code, record_id, flags)
        return "string"

    def why_entity_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(data_source_code, record_id)
        return "string"

    def why_records_v2(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        self.fake_g2engine(
            data_source_code_1, record_id_1, data_source_code_2, record_id_2, flags
        )
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
        self.fake_g2engine(
            data_source_code_1, record_id_1, data_source_code_2, record_id_2
        )
        return "string"
