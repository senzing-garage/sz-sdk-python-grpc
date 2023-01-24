import grpc
import sys
import json
import warnings

sys.path.insert(0, '/home/gadair/servegrpc/protobuf/g2diagnostic')

import g2diagnostic_pb2_grpc
import g2diagnostic_pb2

class G2DiagnosticGRPCConnector:
    def __init__(self):
        self.channel = None
        self.stub = None

    # startup/shutdown methods

    #GGANOTE: depricate when server configs itself
    def init(self, url, moduleName, iniParams, verboseLogging=False):
        self.channel = grpc.insecure_channel(url)
        self.stub = g2diagnostic_pb2_grpc.G2DiagnosticStub(self.channel)

        if isinstance(iniParams,dict):
            iniParams = json.dumps(iniParams)

        req = g2diagnostic_pb2.InitRequest(moduleName=moduleName, iniParams=iniParams, verboseLogging=verboseLogging)
        return self.stub.Init(req)

    def init_with_url(self, url):
        self.channel = grpc.insecure_channel(url)
        self.stub = g2diagnostic_pb2_grpc.G2DiagnosticStub(self.channel)
        # add a ping here or something to ensure it connected

    def init_direct_with_config_id(self, configId):
        warnings.warn('init_direct_with_config_id does nothing for gRPC connections')
        return

    def reinit(self, configId):
        warnings.warn('reinit does nothing for gRPC connections')
        return

    def destroy(self):
        return self.stub.Destroy(g2diagnostic_pb2.DestroyRequest())
#        warnings.warn("destroy does nothing for gRPC connections ")
#        return 

    # get sys into methods
    def get_physical_cores(self):
        return self.stub.GetPhysicalCores(g2diagnostic_pb2.GetPhysicalCoresRequest()).result

    def get_logical_cores(self):
        return self.stub.GetLogicalCores(g2diagnostic_pb2.GetLogicalCoresRequest()).result

    def get_available_memory(self):
        return self.stub.GetAvailableMemory(g2diagnostic_pb2.GetAvailableMemoryRequest()).result

    def get_total_system_memory(self):
        return self.stub.GetTotalSystemMemory(g2diagnostic_pb2.GetTotalSystemMemoryRequest()).result

    def check_db_perf(self, secondsToRun, returnAsString=False):
        secondsToRun = int(secondsToRun)
        result = self.stub.CheckDBPerf(g2diagnostic_pb2.CheckDBPerfRequest(secondsToRun=secondsToRun))
        result = result.result
        if not returnAsString:
            result = json.loads(result)
        return result

    def get_db_info(self, returnAsString=False):
        result = self.stub.GetDBInfo(g2diagnostic_pb2.GetDBInfoRequest())
        result = result.result
        if not returnAsString:
            result = json.loads(result)
        return result

    # data query methods
    def get_entity_details(self, entityID, includeInternalFeatures=False, returnAsString=False):
        entityID = int(entityID)
        includeInternalFeatures = int(includeInternalFeatures)
        result = self.stub.GetEntityDetails(g2diagnostic_pb2.GetEntityDetailsRequest(entityID=entityID, includeInternalFeatures=includeInternalFeatures))
        result = result.result
        if not returnAsString:
            result = json.loads(result)
        return result

    def get_relationship_details(self, relationshipID, includeInternalFeatures=False, returnAsString=False):
        relationshipID = int(relationshipID)
        includeInternalFeatures = int(includeInternalFeatures)
        result = self.stub.GetRelationshipDetails(g2diagnostic_pb2.GetRelationshipDetailsRequest(relationshipID=relationshipID, includeInternalFeatures=includeInternalFeatures))
        result = result.result
        if not returnAsString:
            result = json.loads(result)
        return result

    def get_entity_resume(self, entityID, returnAsString=False):
        entityID = int(entityID)
        result = self.stub.GetEntityResume(g2diagnostic_pb2.GetEntityResumeRequest(entityID=entityID))
        result = result.result
        if not returnAsString:
            result = json.loads(result)
        return result

    def get_feature(self, libFeatID, returnAsString=False):
        libFeatID = int(libFeatID)
        result = self.stub.GetFeature(g2diagnostic_pb2.GetFeatureRequest(libFeatID=libFeatID))
        result = result.result
        if not returnAsString:
            result = json.loads(result)
        return result

    def find_entities_by_feature_ids(self, features, returnAsString=False):
        if isinstance(features, int):
            features = str(int)
        if isinstance(features, (list, tuple)) == False:
            features = [features]
        features = json.dumps(features)
        return self.stub.FindEntitiesByFeatureIDs(g2diagnostic_pb2.FindEntitiesByFeatureIDsRequest(features=features))

    def get_entity_list_by_size_request(self, entitySize):
        entitySize = int(entitySize)
        result = self.stub.GetEntityListBySize(g2diagnostic_pb2.GetEntityListBySizeRequest(entitySize=entitySize))
        return result.result

    def fetch_next_entity_by_size(self, handle):
        result = self.stub.FetchNextEntityBySize(g2diagnostic_pb2.FetchNextEntityBySizeRequest(entityListBySizeHandle=handle))
        print(result)
        if not result.result:
            return None
        return result.result

    def close_entity_list_by_size(self, handle):
        return self.stub.CloseEntityListBySize(g2diagnostic_pb2.CloseEntityListBySizeRequest(entityListBySizeHandle=handle))

    def get_entity_list_by_size_return_list(self, entitySize):
        result_set = []
        handle = self.get_entity_list_by_size_request(entitySize=entitySize)

        while True:
            queried_entity = self.fetch_next_entity_by_size(handle=handle)
            print(queried_entity)
            if not queried_entity:
                break
            result_set.append(queried_entity)

        self.close_entity_list_by_size(handle=handle)
        return result_set

    def get_entity_list_by_size_with_callback(self, entitySize, callback):
        result_set = []
        handle = self.get_entity_list_by_size_request(entitySize=entitySize)

        while True:
            queried_entity = self.fetch_next_entity_by_size(handle=handle)
            if not queried_entity:
                break
            callback(queried_entity)

        self.close_entity_list_by_size(handle=handle)

    # stats methods
    def get_entity_size_breakdown(self, minimumEntitySize, includeInternalFeatures=False, returnAsString=False):
        result = self.stub.GetEntitySizeBreakdown(g2diagnostic_pb2.GetEntitySizeBreakdownRequest(minimumEntitySize=minimumEntitySize, includeInternalFeatures=includeInternalFeatures))
        result = result.result
        if not returnAsString:
            result = json.loads(result)
        return result

    def get_data_source_counts(self, returnAsString=False):
        result = self.stub.GetDataSourceCounts(g2diagnostic_pb2.GetDataSourceCountsRequest())
        result = result.result
        if not returnAsString:
            result = json.loads(result)
        return result

    def get_mapping_statistics(self, includeInternalFeatures=False, returnAsString=False):
        result = self.stub.GetMappingStatistics(g2diagnostic_pb2.GetMappingStatisticsRequest(includeInternalFeatures=includeInternalFeatures))
        result = result.result
        if not returnAsString:
            result = json.loads(result)
        return result

    def get_resolution_statistics(self, returnAsString=False):
        result = self.stub.GetResolutionStatistics(g2diagnostic_pb2.GetResolutionStatisticsRequest())
        result = result.result
        if not returnAsString:
            result = json.loads(result)
        return result

    def get_generic_features(self, featureType, maximumEstimatedCount, returnAsString=False):
        result = self.stub.GetGenericFeatures(g2diagnostic_pb2.GetGenericFeaturesRequest(featureType=featureType, maximumEstimatedCount=maximumEstimatedCount))
        result = result.result
        if not returnAsString:
            result = json.loads(result)
        return result
