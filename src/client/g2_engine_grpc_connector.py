import sys
import warnings
import grpc
import json
from datetime import datetime

from g2_flags import G2Flags

sys.path.insert(0, '/home/gadair/g2-sdk-proto/example_generated_source_code/python/g2engine')
import g2engine_pb2
import g2engine_pb2_grpc


class G2EngineGRPCConnector:
    def __init__(self):
        self.channel = None
        self.stub = None
        self.url = None

    # startup/shutdown methods
    def init(self, url, module_name, ini_params, verbose_logging=False):
        warnings.warn('init does nothing for gRPC connections, use init_grpc_connection_with_url')

    def init_with_url(self, url):
        self.url = url
        self.channel = grpc.insecure_channel(self.url)
        self.stub = g2engine_pb2_grpc.G2EngineStub(self.channel)
        # add a ping here or something to ensure it connected

    def init_direct_with_config_id(self, config_id):
        warnings.warn('init_direct_with_config_id does nothing for gRPC connections')

    def reinit(self, config_id):
        warnings.warn('reinit does nothing for gRPC connections')

    def destroy(self):
        #return self.stub.Destroy(g2diagnostic_pb2.DestroyRequest())
        warnings.warn("destroy does nothing for gRPC connections ")

    def prime_engine(self):
        self.stub.PrimeEngine(g2engine_pb2.PrimeEngineRequest())

    def get_active_config_id(self):
        return self.stub.GetActiveConfigID(g2engine_pb2.GetActiveConfigIDRequest()).result

    def export_config(self):
        response = self.stub.ExportConfig(g2engine_pb2.ExportConfigRequest())
        config = json.loads(response.result)
        return config

    def export_config_and_config_id(self):
        response = self.stub.ExportConfigAndConfigID(g2engine_pb2.ExportConfigAndConfigIDRequest())
        config = json.loads(response.config)
        config_id = response.configID
        return (config,config_id)

    def get_repository_last_modified_time(self):
        last_modified_unixtime = self.stub.GetRepositoryLastModifiedTime(g2engine_pb2.GetRepositoryLastModifiedTimeRequest()).result
        last_modified_unixtime /= 1000
        last_modified_datetime = datetime.fromtimestamp(last_modified_unixtime)
        return last_modified_datetime

    #Adding Records
    def add_record(self, datasource_code, record_id, data_as_json, load_id):
        request = g2engine_pb2.AddRecordRequest(dataSourceCode=datasource_code, 
                                                recordID=record_id,
                                                jsonData=data_as_json,
                                                loadID=load_id)
        self.stub.AddRecord(request)

    def add_record_with_info(self, datasource_code, record_id, data_as_json, load_id, flags, return_as_string):
        if isinstance(flags, G2Flags):
            flags = flags.get_flags()
        if flags is None:
            flags = 0
        request = g2engine_pb2.AddRecordWithInfoRequest(
            dataSourceCode=datasource_code,
            recordID=record_id,
            jsonData=data_as_json,
            loadID=load_id,
            flags=flags)
        result = self.stub.AddRecordWithInfo(request).result
        if return_as_string:
            return result
        return json.loads(result)

    def add_record_with_returned_record_id(self, datasource_code, data_as_json, load_id=None):
        request = g2engine_pb2.AddRecordWithReturnedRecordIDRequest(
            dataSourceCode=datasource_code,
            jsonData=data_as_json,
            loadID=load_id)
        result = self.stub.AddRecordWithReturnedRecordID(request).result
        return result

    def add_record_with_info_with_returned_record_id(self, datasource_code, data_as_json, load_id, flags, return_as_string):
        if isinstance(flags, G2Flags):
            flags = flags.get_flags()
        if flags is None:
            flags = 0
        request = g2engine_pb2.AddRecordWithInfoWithReturnedRecordIDRequest(
            dataSourceCode=datasource_code,
            jsonData=data_as_json,
            loadID=load_id,
            flags=flags)
        response = self.stub.AddRecordWithInfoWithReturnedRecordID(request)
        if return_as_string:
            return (response.withInfo, response.recordID)
        return (json.loads(response.withInfo), response.recordID)

    def replace_record(self, datasource_code, record_id, data_as_json, load_id):
        request = g2engine_pb2.ReplaceRecordRequest(dataSourceCode=datasource_code, 
                                                recordID=record_id,
                                                jsonData=data_as_json,
                                                loadID=load_id)
        self.stub.ReplaceRecord(request)


    def replace_record_with_info(self, datasource_code, record_id, data_as_json, load_id, flags, return_as_string):
        if isinstance(flags, G2Flags):
            flags = flags.get_flags()
        if flags is None:
            flags = 0
        request = g2engine_pb2.ReplaceRecordWithInfoRequest(
            dataSourceCode=datasource_code,
            recordID=record_id,
            jsonData=data_as_json,
            loadID=load_id,
            flags=flags)
        result = self.stub.ReplaceRecordWithInfo(request).result
        if return_as_string:
            return result
        return json.loads(result)

    def reevaluate_record(self, datasource_code, record_id, flags=None):
        request = g2engine_pb2.ReevaluateRecordRequest(dataSourceCode=datasource_code, recordID=record_id)
        self.stub.ReevaluateRecord(request)

    def reevaluate_record_with_info(self, datasource_code, record_id, flags=None):
        request = g2engine_pb2.ReevaluateRecordWithInfoRequest(dataSourceCode=datasource_code, recordID=record_id, flags=flags)
        result = self.stub.ReevaluateRecordWithInfo(request).result
        return result

    def reevaluate_entity(self, entity_id, flags=None):
        request = g2engine_pb2.ReevaluateEntityRequest(entityID=entity_id, flags=flags)
        self.stub.ReevaluateEntity(request)

    def reevaluate_entity_with_info(self, entity_id, flags=None):
        request = g2engine_pb2.ReevaluateEntityRequestWithInfo(entityID=entity_id, flags=flags)
        result = self.stub.ReevaluateEntityWithInfo(request).result
        return result

    def count_redo_records(self):
        request = g2engine_pb2.CountRedoRecordsRequest()
        return self.stub.CountRedoRecords(request)

    def get_redo_record(self):
        request = g2engine_pb2.GetRedoRecordRequest()
        return self.stub.GetRedoRecord(request).result

    def process(self, redo_record):
        request = g2engine_pb2.ProcessRequest(redo_record)
        self.stub.Process(request)

    def process_with_info(self, redo_record, flags):
        request = g2engine_pb2.ProcessWithInfoRequest(redo_record, flags.get_flags())
        return self.stub.ProcessWithInfo(request).result

    def process_redo_record(self):
        request = g2engine_pb2.ProcessRedoRecordRequest()
        return self.stub.ProcessRedoRecord(request).result

    def process_redo_record_with_info(self, flags=None):
        request = g2engine_pb2.ProcessRedoRecordWithInfoRequest(flags=flags)
        response = self.stub.ProcessRedoRecordWithInfo(request)
        return (response.result, response.info)

    def delete_record(self, datasource_code, record_id, load_id):
        request = g2engine_pb2.DeleteRecordRequest(dataSourceCode=datasource_code, recordID=record_id, loadID=load_id)
        self.stub.DeleteRecord(request)

    def delete_record_with_info(self, datasource_code, record_id, load_id, flags):
        request = g2engine_pb2.DeleteRecordWithInfoRequest(dataSourceCode=datasource_code, recordID=record_id, loadID=load_id, flags=flags)
        response = self.stub.DeleteRecordWithInfo(request)
        return response.result

    def get_record(self, datasource_code, record_id, flags):
        request = g2engine_pb2.GetRecordRequest(dataSourceCode=datasource_code, recordID=record_id, flags=flags)
        response = self.stub.GetRecord(request)
        return response.result

    def get_entity_by_record_id(self, datasource_code, record_id, flags):
        request = g2engine_pb2.GetEntityByRecordID_V2Request(dataSourceCode=datasource_code, recordID=record_id, flags=flags)
        response = self.stub.GetEntityByRecordID_V2(request)
        return response.result

    def get_entity_by_entity_id(self, entity_id, flags):
        request = g2engine_pb2.GetEntityByEntityID_V2Request(
            entity_id=entity_id, 
            flags=flags)
        response = self.stub.GetEntityByEntityID_V2(request)
        return response.result

    def search_by_attributes(self, search_attributes, flags):
        request = g2engine_pb2.SearchByAttributes_V2Request(
            search_attributes, 
            flags)
        response = self.stub.SearchByAttributes_V2(request)
        return response.result

    def find_path_by_entity_id(self, start_entity_id, end_entity_id, max_degree, flags):
        request = g2engine_pb2.FindPathByEntityID_V2Request(
            entityID1=start_entity_id,
            entityID2=end_entity_id,
            maxDegree=max_degree,
            flags=flags)
        response = self.stub.FindPathByEntityID_V2(request)
        return response.result

    def find_path_by_record_id(self, start_datasource_code, start_record_id, end_datasource_code, end_record_id, max_degree, flags):
        request = g2engine_pb2.FindPathByRecordID_V2Request(
            dataSourceCode1=start_datasource_code,
            recordID1=start_record_id,
            dataSourceCode2=end_datasource_code,
            recordID2=end_record_id,
            maxDegree=max_degree,
            flags=flags)
        response = self.stub.FindPathByRecordID_V2(request)
        return response.result

    def find_path_excluding_by_entity_id(self, 
                                         start_entity_id, 
                                         end_entity_id, 
                                         max_degree, 
                                         excluded_entities, 
                                         flags):
        request = g2engine_pb2.FindPathExcludingByEntityID_V2Request(
            entityID1=start_entity_id,
            entityID2=end_entity_id,
            maxDegree=max_degree,
            excludedEntities=excluded_entities,
            flags=flags)
        response = self.stub.FindPathExcludingByEntityID_V2(request)
        return response.result

    def find_path_excluding_by_record_id(self, 
                                         start_datasource_code,
                                         start_record_id,
                                         end_datasource_code,
                                         end_record_id,
                                         max_degree,
                                         excluded_entities,
                                         flags):
        request = g2engine_pb2.FindPathExcludingByRecordID_V2Request(
            dataSourceCode1=start_datasource_code,
            recordID1=start_record_id,
            dataSourceCode2=end_datasource_code,
            recordID2=end_record_id,
            maxDegree=max_degree,
            excludedEntity=excluded_entities, 
            flags=flags)
        response = self.stub.FindPathExcludingByRecordID_V2(request)
        return response.result

    def find_path_including_source_by_entity_id(self,
                                                start_entity_id,
                                                end_entity_id,
                                                max_degree,
                                                excluded_entities,
                                                required_datasources,
                                                flags):
        request = g2engine_pb2.FindPathIncludingSourceByEntityID_V2Request(
            entityID1=start_entity_id,
            entityID2=end_entity_id,
            maxDegree=max_degree,
            excludedEntities=excluded_entities,
            requiredDsrcs=required_datasources,
            flags=flags)
        response = self.stub.FindPathIncludingSourceByEntityID(request)
        return response.result

    def find_path_including_source_by_record_id(self,
                                                start_datasource_code,
                                                start_record_id,
                                                end_datasource_code,
                                                end_record_id,
                                                max_degree,
                                                excluded_entities,
                                                required_datasources,
                                                flags):
        request = g2engine_pb2.FindPathIncludingSourceByEntityID_V2Request(
            dataSourceCode1=start_datasource_code,
            recordID1=start_record_id,
            dataSourceCode2=end_datasource_code,
            recordID2=end_record_id,
            maxDegree=max_degree,
            excludedEntities=excluded_entities,
            requiredDsrcs=required_datasources,
            flags=flags)
        response = self.stub.FindPathIncludingSourceByEntityID(request)
        return response.result

    def find_network_by_entity_id(self,
                                  entity_list,
                                  max_degree,
                                  buildout_degree,
                                  max_entities,
                                  flags):
        request = g2engine_pb2.FindNetworkByEntityID_V2Request(
            entityList=entity_list,
            maxDegree = max_degree,
            buildOutDegree=buildout_degree,
            maxEntities=max_entities,
            flags=flags)
        response = self.stub.FindNetworkByEntityID_V2(request)
        return response.result

    def find_network_by_record_id(self,
                                  record_list,
                                  max_degree,
                                  buildout_degree,
                                  max_entities,
                                  flags):
        request = g2engine_pb2.FindNetworkByRecordID_V2Request(
            recordList=record_list,
            maxDegree=max_degree,
            buildOutDegree=buildout_degree,
            maxEntities=max_entities,
            flags=flags)
        response = self.stub.FindNetworkByRecordID_V2(request)
        return response.result

    def why_entities(self, entity_id_1, entity_id_2, flags):
        request = g2engine_pb2.WhyEntities_V2Request(
            entityID1=entity_id_1,
            entityID2=entity_id_2,
            flags=flags)
        response = self.stub.WhyEntities(request)
        return response.result

    def why_records(self, 
                    datasource_code_1, 
                    record_id_1, 
                    datasource_code_2, 
                    record_id_2, 
                    flags):
        request = g2engine_pb2.WhyRecords_V2Request(
            dataSourceCode1=datasource_code_1,
            recordID1=record_id_1,
            dataSourceCode2=datasource_code_2,
            recordID2=record_id_2,
            flags=flags
        )
        response = self.stub.WhyRecords(request)
        return response.result

    def why_entity_by_record_id(self,
                                datasource_code_1,
                                record_id_1,
                                flags):
        request = g2engine_pb2.WhyRecords_V2Request(
            dataSourceCode=datasource_code_1,
            recordID=record_id_1,
            flags=flags
        )
        response = self.stub.WhyEntityByRecordID(request)
        return response.result

    def how_entity_by_entity_id(self, entity_id, flags):
        request = g2engine_pb2.HowEntityByEntityID_V2Request(
            entityID=entity_id, 
            flags=flags
        )
        response = self.stub.HowEntityByEntityID_V2(request)
        return response.result

    def export_csv_entity_report_with_callback(self, columns, flags, callback, return_as_string):
        for item in self.export_csv_entity_report_iteritems(columns=columns, flags=flags, return_as_string=return_as_string):
            callback(item)

    def export_csv_entity_report_iteritems(self, columns, flags, return_as_string):
        request = g2engine_pb2.StreamExportCSVEntityReportRequest(csvColumnList=columns, flags=flags)
        for item in self.stub.StreamExportCSVEntityReport(request):
            if item.result:
                if return_as_string:
                    yield item.result
                else:
                    #return list instead -- maybe dict?
                    yield item.result

    def export_json_entity_report_with_callback(self, flags, callback, return_as_string):
        for item in self.export_json_entity_report_iteritems(flags=flags, return_as_string=return_as_string):
            callback(item)

    def export_json_entity_report_iteritems(self, flags, return_as_string):
        request = g2engine_pb2.StreamExportJSONEntityReportRequest(flags=flags)
        for item in self.stub.StreamExportJSONEntityReport(request):
            if item.result:
                if return_as_string:
                    yield item.result
                else:
                    yield json.loads(item.result)

    def purge_repository(self):
        request = g2engine_pb2.PurgeRepositoryRequest()
        self.stub.PurgeRepository(request)


