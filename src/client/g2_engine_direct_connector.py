import sys
import warnings
import json
from datetime import datetime
from typing import Union, Tuple, Callable, Iterable

from g2_engine_connector_base import G2EngineConnectorBase

try:
    from senzing import G2Engine
except ModuleNotFoundError:
    warnings.warn('Cannot import Senzing python libraries.')
    warnings.warn('Please verify your PYTHONPATH includes the path to senzing python libs')
    warnings.warn('Environment can be setup by sourcing "setupEnv" '\
                  'from your senzing project directory')
    sys.exit(-1)


class G2EngineDirectConnector(G2EngineConnectorBase):
    def __init__(self):
        self.g2_handle = None

    # startup/shutdown methods
    def init(self,
             module_name: str,
             senzing_config_json: Union[str,dict],
             config_id: int,
             verbose_logging: bool) -> None:
        if isinstance(senzing_config_json, dict):
            senzing_config_json = json.dumps(senzing_config_json)
        self.g2_handle = G2Engine()
        if not config_id:
            self.g2_handle.init(
                engine_name_=module_name,
                ini_params_=senzing_config_json,
                debug_=verbose_logging)
        else:
            self.g2_handle.initWithConfigID(
                engine_name_=module_name,
                ini_params_=senzing_config_json,
                initConfigID_=config_id,
                debug_=verbose_logging)

    def init_with_url(self, url: str) -> None:
        warnings.warn('init_with_url is not valid for direct connections')

    def init_direct(self,
                    module_name: str,
                    senzing_config_json: Union[str,dict],
                    config_id: int,
                    verbose_logging: bool) -> None:
        self.init(
            module_name=module_name,
            senzing_config_json=senzing_config_json,
            config_id=config_id,
            verbose_logging=verbose_logging)

    def init_direct_from_environment(self,
                                     module_name: str,
                                     config_id: int,
                                     verbose_logging: bool) -> None:
        import senzing_module_config
        json_config = senzing_module_config.get_json_config()
        self.init(
            module_name=module_name,
            senzing_config_json=json_config,
            config_id=config_id,
            verbose_logging=verbose_logging)

    def reinit(self, config_id: int) -> None:
        config_id = bytes(config_id, 'utf-8')
        self.g2_handle.reinit(config_id)

    def destroy(self) -> None:
        self.g2_handle.destroy()
        self.g2_handle = None

    def prime_engine(self) -> None:
        self.g2_handle.primeEngine()

    def get_active_config_id(self) -> int:
        response = bytearray()
        self.g2_handle.getActiveConfigID(response)
        return int(response.decode())

    def export_config(self) -> dict:
        config = bytearray()
        config_id = bytearray()
        self.g2_handle.exportConfig(config, config_id)
        config = json.loads(config.decode())
        return config

    def export_config_and_config_id(self) -> Tuple[dict,int]:
        config = bytearray()
        config_id = bytearray()
        self.g2_handle.exportConfig(config, config_id)
        config = json.loads(config.decode())
        config_id = config_id.decode()
        return (config, config_id)


    def get_repository_last_modified_time(self) -> datetime:
        last_modified_time_bytearray = bytearray()
        self.g2_handle.getRepositoryLastModifiedTime(last_modified_time_bytearray)
        last_modified_unixtime = int(last_modified_time_bytearray.decode())
        last_modified_unixtime /= 1000
        last_modified_datetime = datetime.fromtimestamp(last_modified_unixtime)        
        return last_modified_datetime

    #Adding Records
    def add_record(self,
                   datasource_code: str,
                   record_id: str,
                   data_as_json: str,
                   load_id: str) -> None:
        self.g2_handle.addRecord(
            dataSourceCode=datasource_code,
            recordId=record_id,
            jsonData=data_as_json,
            load_id=load_id
        )

    def add_record_with_info(self, 
                             datasource_code: str, 
                             record_id: str, 
                             data_as_json: str, 
                             load_id: str, 
                             flags: int) -> str:
        info_bytearray = bytearray()
        self.g2_handle.addRecordWithInfo(
            dataSourceCode=datasource_code,
            recordId=record_id,
            jsonData=data_as_json,
            response=info_bytearray,
            load_id=load_id,
            flags=flags
        )
        info = info_bytearray.decode()
        return info

    def add_record_with_returned_record_id(self,
                                           datasource_code: str,
                                           data_as_json: str,
                                           load_id: bool) -> str:
        record_id = bytearray()
        self.g2_handle.addRecordWithReturnedRecordID(
            dataSourceCode=datasource_code,
            recordID=record_id,
            jsonData=data_as_json,
            load_id=load_id
        )
        record_id = record_id.decode()
        return record_id


    def add_record_with_info_with_returned_record_id(self,
                                                     datasource_code: str,
                                                     data_as_json: str,
                                                     load_id: str,
                                                     flags: int) -> str:
        info = bytearray()
        record_id = bytearray()
        self.g2_handle.addRecordWithInfoWithReturnedRecordID(
            dataSourceCode=datasource_code,
            jsonData=data_as_json,
            recordID=record_id,
            info=info,
            load_id=load_id
        )
        record_id = record_id.decode()
        info = info.decode()
        return (info, record_id)

    #replace records
    def replace_record(self,
                       datasource_code: str,
                       record_id: str,
                       data_as_json: str,
                       load_id: str) -> None:
        self.g2_handle.replaceRecord(
            dataSourceCode=datasource_code,
            recordId=record_id,
            jsonData=data_as_json,
            load_id=load_id
        )

    def replace_record_with_info(self,
                                 datasource_code: str,
                                 record_id: str,
                                 data_as_json: str,
                                 load_id: str,
                                 flags: int) -> str:
        info = bytearray()
        self.g2_handle.addRecordWithInfo(
            dataSourceCode=datasource_code,
            recordId=record_id,
            jsonData=data_as_json,
            response=info,
            load_id=load_id,
            flags=flags
        )
        info = info.decode()
        return info

    #reeval
    def reevaluate_record(self,
                          datasource_code: str,
                          record_id: str,
                          flags: int) -> None:
        self.g2_handle.reevaluateRecord(
            dataSourceCode=datasource_code,
            recordId=record_id,
            flags=flags
            )

    def reevaluate_record_with_info(self,
                                    datasource_code: str,
                                    record_id: str,
                                    flags: int) -> str:
        info = bytearray()
        self.g2_handle.reevaluateRecordWithInfo(
            dataSourceCode=datasource_code,
            recordId=record_id,
            response=info,
            flags=flags
        )
        info = info.decode()
        return info

    def reevaluate_entity(self, entity_id: int, flags: int) -> None:
        self.g2_handle.reevaluateEntity(
            entityID=entity_id,
            flags=flags
        )

    def reevaluate_entity_with_info(self, entity_id: int, flags: int) -> str:
        info = bytearray()
        self.g2_handle.reevaluateEntityWithInfo(
            entityID=entity_id,
            response=info,
            flags=flags
        )
        info = info.decode()
        return info

    #redo
    def count_redo_records(self) -> int:
        return self.g2_handle.countRedoRecords()

    def get_redo_record(self) -> str:
        record = bytearray()
        self.g2_handle.getRedoRecord(record)
        record = record.decode()
        return record

    def process(self, redo_record: str) -> None:
        self.g2_handle.process(redo_record)

    def process_with_info(self, redo_record: str, flags: int) -> str:
        info = bytearray()
        self.g2_handle.processWithInfo(
            input_umf_=redo_record,
            response=info,
            flags=flags
        )
        info = info.decode()
        info = json.loads(info)
        return info

    def process_redo_record(self) -> str:
        response = bytearray()
        self.g2_handle.processRedoRecord(
            response=response
        )
        response = response.decode()
        return response

    def process_redo_record_with_info(self, flags: int) -> Tuple[str,str]:
        response = bytearray()
        info = bytearray()
        self.g2_handle.processRedoRecordWithInfo(
            response=response,
            flags=flags,
            info=info
        )
        response = response.decode()
        info = info.decode()
        info = json.loads(info)
        return (response, info)

    #delete records 
    def delete_record(self, datasource_code: str, record_id: str, load_id: str) -> None:
        self.g2_handle.deleteRecord(
            dataSourceCode=datasource_code,
            recordId=record_id,
            load_id=load_id
        )

    def delete_record_with_info(self, datasource_code: str, record_id: str, load_id: str, flags) -> str:
        info = bytearray()
        self.g2_handle.deleteRecordWithInfo(
            dataSourceCode=datasource_code,
            recordId=record_id,
            response=info,
            load_id=load_id
        )
        info = info.decode()
        info = json.loads(info)
        return info

    #get records and entities
    def get_record(self, datasource_code: str, record_id: str, flags: int) ->str:
        record_info = bytearray()
        self.g2_handle.getRecord(
            dsrcCode=datasource_code,
            recordId=record_id,
            response=record_info,
            flags=flags
        )
        record_info = record_info.decode()
        record_info = json.loads(record_info)
        return record_info

    def get_entity_by_record_id(self, datasource_code: str, record_id: str, flags: int) ->str:
        entity_info = bytearray()
        self.g2_handle.getEntityByRecordID(
            dsrcCode=datasource_code,
            recordId=record_id,
            response=entity_info,
            flags=flags
        )
        entity_info = entity_info.decode()
        entity_info = json.loads(entity_info)
        return entity_info

    def get_entity_by_entity_id(self, entity_id: int, flags: int) ->str:
        entity_info = bytearray()
        self.g2_handle.getEntityByEntityID(
            entityID=entity_id,
            response=entity_info,
            flags=flags
        )
        entity_info = entity_info.decode()
        entity_info = json.loads(entity_info)
        return entity_info

    #search for entities
    def search_by_attributes(self, search_attributes: str, flags: int) -> str:
        response = bytearray()
        self.g2_handle.searchByAttributes(
            jsonData=search_attributes,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    #find paths
    def find_path_by_entity_id(self,
                               start_entity_id: int,
                               end_entity_id: int,
                               max_degree: int,
                               flags: int) -> str:
        response = bytearray()
        self.g2_handle.findPathByEntityID(
            startEntityID=start_entity_id,
            endEntityID=end_entity_id,
            maxDegree=max_degree,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    def find_path_by_record_id(self,
                               start_datasource_code: str,
                               start_record_id: str,
                               end_datasource_code: str,
                               end_record_id: str,
                               max_degree: int,
                               flags: int) -> str:
        response = bytearray()
        self.g2_handle.findPathByRecordID(
            startDsrcCode=start_datasource_code,
            startRecordId=start_record_id,
            endDsrcCode=end_datasource_code,
            endRecordId=end_record_id,
            maxDegree=max_degree,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    def find_path_excluding_by_entity_id(self,
                                         start_entity_id: int,
                                         end_entity_id: int,
                                         max_degree: int,
                                         excluded_entities: str,
                                         flags: int) -> str:
        response = bytearray()
        self.g2_handle.findPathExcludingByEntityID(
            startEntityID=start_entity_id,
            endEntityID=end_entity_id,
            maxDegree=max_degree,
            excluded_entities=excluded_entities,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    def find_path_excluding_by_record_id(self,
                                         start_datasource_code: str,
                                         start_record_id: str,
                                         end_datasource_code: str,
                                         end_record_id: str,
                                         max_degree: int,
                                         excluded_entities: str,
                                         flags: int) -> str:
        response = bytearray()
        self.g2_handle.findPathExcludingByRecordID(
            startDsrcCode=start_datasource_code,
            startRecordId=start_record_id,
            endDsrcCode=end_datasource_code,
            endRecordId=end_record_id,
            maxDegree=max_degree,
            excludedEntities=excluded_entities,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    def find_path_including_source_by_entity_id(self,
                                                start_entity_id: int,
                                                end_entity_id: int,
                                                max_degree: int,
                                                excluded_entities: str,
                                                required_datasources: str,
                                                flags) -> str:
        response = bytearray()
        self.g2_handle.findPathIncludingSourceByEntityID(
            startEntityID=start_entity_id,
            endEntityID=end_entity_id,
            maxDegree=max_degree,
            excludedEntities=excluded_entities,
            requiredDsrcs=required_datasources,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    def find_path_including_source_by_record_id(self,
                                                start_datasource_code: str,
                                                start_record_id: str,
                                                end_datasource_code: str,
                                                end_record_id: str,
                                                max_degree: int,
                                                excluded_entities: str,
                                                required_datasources: str,
                                                flags: int) ->str:
        response = bytearray()
        self.g2_handle.findPathIncludingSourceByEntityID(
            startDsrcCode=start_datasource_code,
            startRecordId=start_record_id,
            endDsrcCode=end_datasource_code,
            endRecordId=end_record_id,
            maxDegree=max_degree,
            excludedEntities=excluded_entities,
            requiredDsrcs=required_datasources,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    #find networks
    def find_network_by_entity_id(self,
                                  entity_list: str,
                                  max_degree: int,
                                  buildout_degree: int,
                                  max_entities: int,
                                  flags: int):
        response = bytearray()
        self.g2_handle.findNetworkByEntityID(
            entityList=entity_list,
            maxDegree=max_degree,
            buildOutDegree=buildout_degree,
            maxEntities=max_entities,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    def find_network_by_record_id(self,
                                  record_list: str,
                                  max_degree: int,
                                  buildout_degree: int,
                                  max_entities: int,
                                  flags: int):
        response = bytearray()
        self.g2_handle.findNetworkByRecordID(
            recordList=record_list,
            maxDegree=max_degree,
            buildOutDegree=buildout_degree,
            maxEntities=max_entities,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    #why
    def why_entities(self,
                     entity_id_1: int,
                     entity_id_2: int,
                     flags: int) -> str:
        response = bytearray()
        self.g2_handle.whyEntities(
            entityID1=entity_id_1,
            entityID2=entity_id_2,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    def why_records(self,
                    datasource_code_1: str,
                    record_id_1: str,
                    datasource_code_2: str,
                    record_id_2: str,
                    flags: int) -> str:
        response = bytearray()
        self.g2_handle.whyRecords(
            dataSourceCode1=datasource_code_1,
            recordID1=record_id_1,
            dataSourceCode2=datasource_code_2,
            recordID2=record_id_2,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    def why_entity_by_record_id(self,
                                datasource_code_1: str,
                                record_id_1: str,
                                flags: int) -> str:
        response = bytearray()
        self.g2_handle.whyEntityByRecordID(
            dataSourceCode=datasource_code_1,
            recordID=record_id_1,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    def why_entity_by_entity_id(self, entity_id: int, flags: int) -> str:
        response = bytearray()
        self.g2_handle.whyEntityByEntityID(
            entityID=entity_id,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    def how_entity_by_entity_id(self, entity_id: int, flags: int) -> str:
        response = bytearray()
        self.g2_handle.howEntityByEntityID(
            entityID=entity_id,
            response=response,
            flags=flags
        )
        response = response.decode()
        return response

    #export
    def export_csv_entity_report_with_callback(self,
                                               columns: str,
                                               flags: int,
                                               callback: Callable[[Union[str,dict]], None],
                                               return_as_string: bool) -> None:
        for row in self.export_csv_entity_report_iteritems(
            columns=columns,
            flags=flags,
            return_as_string=return_as_string
        ):
            callback(row)

    def export_csv_entity_report_iteritems(self,
                                           columns: str,
                                           flags: int,
                                           return_as_string: bool)\
                                           -> Iterable[Union[str,dict]]:
        handle = self.g2_handle.exportCSVEntityReport(
            headersForCSV=columns,
            flags=flags
        )

        while True:
            data_buffer = bytearray()
            row = self.g2_handle.fetchNext(
                exportHandle=handle,
                response=data_buffer
            )
            if not row:
                break
            row = row.decode()
            if return_as_string:
                yield row
            else:
                #return list or dict?
                yield row
        self.g2_handle.closeExport(exportHandle=handle)

    def export_json_entity_report_with_callback(self,
                                                flags: int,
                                                callback: Callable[[Union[str,dict]], None],
                                                return_as_string: bool) -> None:
        for row in self.export_json_entity_report_iteritems(
            flags=flags,
            return_as_string=return_as_string
        ):
            callback(row)

    def export_json_entity_report_iteritems(self,
                                            flags: int,
                                            return_as_string: bool)\
                                            -> Iterable[Union[str,dict]]:
        handle = self.g2_handle.exportJSONEntityReport(flags=flags)

        while True:
            data_buffer = bytearray()
            row = self.g2_handle.fetchNext(
                exportHandle=handle,
                response=data_buffer
            )
            if not row:
                break
            row = row.decode()
            if return_as_string:
                yield row
            else:
                yield json.loads(row)
        self.g2_handle.closeExport(exportHandle=handle)

    #purge
    def purge_repository(self) -> None:
        self.g2_handle.purgeRepository()
