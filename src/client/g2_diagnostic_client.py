import pprint

import grpc
import sys
import json


import g2diagnostic_pb2
import g2diagnostic_pb2_grpc


class G2DiagnosticClient:
    def __init__(self):
        self.type = None
        self.connector = None

    #internal methods
    def legacy_init_grpc_connector(self, url, moduleName, iniParams):
        import g2_diagnostic_grpc_connector
        self.type = 'GRPC'
        self.connector = g2_diagnostic_grpc_connector.G2DiagnosticGRPCConnector()
        return self.connector.init(url, moduleName, iniParams)

    def __init_grpc_connector(self):
        import g2_diagnostic_grpc_connector
        self.type = 'GRPC'
        self.connector = g2_diagnostic_grpc_connector.G2DiagnosticGRPCConnector()

    def __init_direct_connector(self):
        self.type = 'DIRECT'
        raise Exception('unimplemented')

    #startup/shutdown methods
    def init_grpc_connection_with_url(self, url):
        import g2_diagnostic_grpc_connector
        self.__init_grpc_connector()
        self.connector.init_with_url(url)

    def init_direct(self, moduleName, iniParams, verboseLogging=False):
        import g2_diagnostic_direct_connector
        self.__init_direct_connector()
        if isinstance(iniParams, dict):
            iniParams = json.dumps(iniParams)

        return self.connector.init(moduleName=moduleName, iniParams=iniParams, verboseLogging=verboseLogging)

    def init_direct_from_environment(self, moduleName, verboseLogging=False):
        import g2_diagnostic_direct_connector
        self.type = 'DIRECT'
        self.connector = g2_diagnostic_direct_connector.G2DiagnosticDirectConnector()
        return self.connector.init_direct_from_environment(moduleName, verboseLogging)

    def init_with_config_id(self, configId):
        self.__init_direct_connector()
        configId = int(configId)
        return self.connector.init_with_config_id(configId=configId)

    def reinit(self, configId):
        configId = int(configId)
        return self.connector.reinit(configId=configId)

    def destroy(self):
        return self.connector.destroy()

    #get sys into methods
    def get_physical_cores(self):
        return self.connector.get_physical_cores()

    def get_logical_cores(self):
        return self.connector.get_logical_cores()
    
    def get_available_memory(self):
        return self.connector.get_available_memory()

    def get_total_system_memory(self):
        return self.connector.get_total_system_memory()

    def check_db_perf(self, secondsToRun):
        return self.connector.check_db_perf(secondsToRun=secondsToRun)

    def get_db_info(self, returnAsString=False):
        return self.connector.get_db_info()

    #data query methods
    def get_entity_details(self, entityID, includeInternalFeatures=False, returnAsString=False):
        entityID = int(entityID)
        includeInternalFeatures = int(includeInternalFeatures)
        return self.connector.get_entity_details(entityID=entityID, includeInternalFeatures=includeInternalFeatures)

    def get_relationship_details(self, relationshipID, includeInternalFeatures=False, returnAsString=False):
        relationshipID=int(relationshipID)
        includeInternalFeatures = int(includeInternalFeatures)
        return self.connector.get_relationship_details(relationshipID=relationshipID, includeInternalFeatures=includeInternalFeatures, returnAsString=returnAsString)

    def get_entity_resume(self, entityID, returnAsString=False):
        entityID = int(entityID)
        return self.connector.get_entity_resume(entityID=entityID, returnAsString=returnAsString)

    def get_feature(self, libFeatID, returnAsString=False):
        libFeatID = int(libFeatID)
        return self.connector.get_feature(libFeatID=libFeatID, returnAsString=returnAsString)

    def find_entities_by_feature_ids(self, features, returnAsString=False):
        if isinstance(features, int):
            features = str(features)
        if isinstance(features, (list,tuple)) == False:
            features = [features]
        features = json.dumps(features)
        return self.connector.find_entities_by_feature_ids(features=features)

    def get_entity_list_by_size_request(self, entitySize):
        entitySize = int(entitySize)
        return self.connector.get_entity_list_by_size(entitySize=entitySize)
    
    def fetch_next_entity_by_size(self, handle):
        return self.connector.fetch_next_entity_by_size(handle)

    def close_entity_list_by_size(self, handle):
        return self.connector.close_entity_list_by_size(handle)

    def get_entity_list_by_size_return_list(self, entity_size):
        return self.connector.get_entity_list_by_size_return_list(entity_size)

    def get_entity_list_by_size_with_callback(self, entitySize, callback):
        return self.connector.get_entity_list_by_size_with_callback(entitySize=entitySize, callback=callback)

    #stats methods
    def get_enity_size_breakdown(self, minimumEntitySize, includeInternalFeatures=False, returnAsString=False):
        return self.connector.get_entity_size_breakdown(minimumEntitySize=minimumEntitySize, includeInternalFeatures=includeInternalFeatures, returnAsString=returnAsString)

    def get_data_source_counts(self, returnAsString=False):
        return self.connector.get_data_source_counts(returnAsString=returnAsString)

    def get_mapping_statistics(self, includeInternalFeatures=False, returnAsString=False):
        return self.connector.get_mapping_statistics(includeInternalFeatures=includeInternalFeatures, returnAsString=returnAsString)

    def get_resolution_statistics(self, returnAsString=False):
        return self.connector.get_resolution_statistics()

    def get_generic_features(self, featureType, maximumEstimatedCount, returnAsString=False):
        return self.connector.get_generic_features(featureType=featureType, maximumEstimatedCount=maximumEstimatedCount)


