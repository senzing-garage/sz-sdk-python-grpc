import sys
import json
import warnings

import grpc

sys.path.insert(0, '/home/gadair/g2-sdk-proto/example_generated_source_code/python/g2diagnostic')
import g2diagnostic_pb2
import g2diagnostic_pb2_grpc


class G2DiagnosticGRPCConnector:
    def __init__(self):
        self.channel = None
        self.stub = None
        self.url = None

    # startup/shutdown methods
    def init_direct(self, module_name, ini_params, verbose_logging=False):
        warnings.warn('init does nothing for gRPC connections, use init_grpc_connection_with_url')

    def init_with_url(self, url):
        self.url = url
        self.channel = grpc.insecure_channel(self.url)
        self.stub = g2diagnostic_pb2_grpc.G2DiagnosticStub(self.channel)
        # add a ping here or something to ensure it connected

    def init_direct_with_config_id(self, config_id):
        warnings.warn('init_direct_with_config_id does nothing for gRPC connections')

    def reinit(self, config_id):
        warnings.warn('reinit does nothing for gRPC connections')

    def destroy(self):
        #return self.stub.Destroy(g2diagnostic_pb2.DestroyRequest())
        warnings.warn("destroy does nothing for gRPC connections ")

    # get sys into methods
    def get_physical_cores(self):
        return self.stub.GetPhysicalCores(g2diagnostic_pb2.GetPhysicalCoresRequest()).result

    def get_logical_cores(self):
        return self.stub.GetLogicalCores(g2diagnostic_pb2.GetLogicalCoresRequest()).result

    def get_available_memory(self):
        return self.stub.GetAvailableMemory(g2diagnostic_pb2.GetAvailableMemoryRequest()).result

    def get_total_system_memory(self):
        return self.stub.GetTotalSystemMemory(g2diagnostic_pb2.GetTotalSystemMemoryRequest()).result

    def check_db_perf(self, seconds_to_run, return_as_string=False):
        seconds_to_run = int(seconds_to_run)
        request = g2diagnostic_pb2.CheckDBPerfRequest(secondsToRun=seconds_to_run)
        result = self.stub.CheckDBPerf(request)
        result = result.result
        if not return_as_string:
            result = json.loads(result)
        return result

    def get_db_info(self, return_as_string=False):
        result = self.stub.GetDBInfo(g2diagnostic_pb2.GetDBInfoRequest())
        result = result.result
        if not return_as_string:
            result = json.loads(result)
        return result

    # data query methods
    def get_entity_details(self,
                           entity_id,
                           include_internal_features=False,
                           return_as_string=False):
        entity_id = int(entity_id)
        include_internal_features = int(include_internal_features)
        request = g2diagnostic_pb2.GetEntityDetailsRequest(
            entityID=entity_id,
            includeInternalFeatures=include_internal_features
            )
        result = self.stub.GetEntityDetails(request)
        result = result.result
        if not return_as_string:
            result = json.loads(result)
        return result

    def get_relationship_details(self,
                                 relationship_id,
                                 include_internal_features=False,
                                 return_as_string=False):
        relationship_id = int(relationship_id)
        include_internal_features = int(include_internal_features)
        request = g2diagnostic_pb2.GetRelationshipDetailsRequest(
            relationshipID=relationship_id,
            includeInternalFeatures=include_internal_features
            )
        result = self.stub.GetRelationshipDetails(request)
        result = result.result
        if not return_as_string:
            result = json.loads(result)
        return result

    def get_entity_resume(self, entity_id, return_as_string=False):
        entity_id = int(entity_id)
        request = g2diagnostic_pb2.GetEntityResumeRequest(entityID=entity_id)
        result = self.stub.GetEntityResume(request)
        result = result.result
        if not return_as_string:
            result = json.loads(result)
        return result

    def get_feature(self, lib_feat_id, return_as_string=False):
        lib_feat_id = int(lib_feat_id)
        request = g2diagnostic_pb2.GetFeatureRequest(libFeatID=lib_feat_id)
        result = self.stub.GetFeature(request)
        result = result.result
        if not return_as_string:
            result = json.loads(result)
        return result

    def find_entities_by_feature_ids(self, features, return_as_string=False):
        if isinstance(features, int):
            features = str(int)
        if isinstance(features, (list, tuple)) is False:
            features = [features]
        features = json.dumps(features)
        request = g2diagnostic_pb2.FindEntitiesByFeatureIDsRequest(features=features)
        items = self.stub.FindEntitiesByFeatureIDs(request)
        if not return_as_string:
            items = json.loads(items)
        return items

    def get_entity_list_by_size_request(self, entity_size):
        entity_size = int(entity_size)
        request = g2diagnostic_pb2.GetEntityListBySizeRequest(entitySize=entity_size)
        result = self.stub.GetEntityListBySize(request)
        return result.result

    def fetch_next_entity_by_size(self, handle):
        request = g2diagnostic_pb2.FetchNextEntityBySizeRequest(entityListBySizeHandle=handle)
        result = self.stub.FetchNextEntityBySize(request)
        if not result.result:
            return None
        return result.result

    def close_entity_list_by_size(self, handle):
        request = g2diagnostic_pb2.CloseEntityListBySizeRequest(entityListBySizeHandle=handle)
        return self.stub.CloseEntityListBySize(request)

    def get_entity_list_by_size_return_list(self, entity_size):
        result_set = []
        request = g2diagnostic_pb2.StreamEntityListBySizeRequest(entitySize=entity_size)
        for entity in self.stub.StreamEntityListBySize(request):
            if entity.result:
                result_set.extend(json.loads(entity.result))
        return result_set

    def get_entity_list_by_size_with_callback(self, entity_size, callback, return_as_string=False):
        request = g2diagnostic_pb2.StreamEntityListBySizeRequest(entitySize=entity_size)
        for entity in self.stub.StreamEntityListBySize(request):
            if entity.result:
                if return_as_string:
                    callback(entity.result)
                else:
                    callback(json.loads(entity.result))

    def get_entity_list_by_size_iteritems(self, entity_size, return_as_string=False):
        request = g2diagnostic_pb2.StreamEntityListBySizeRequest(entitySize=entity_size)
        for entity in self.stub.StreamEntityListBySize(request):
            if entity.result:
                if return_as_string:
                    yield entity.result
                else:
                    yield json.loads(entity.result)


    # stats methods
    def get_entity_size_breakdown(self,
                                  minimum_entity_size,
                                  include_internal_features=False,
                                  return_as_string=False):
        request = g2diagnostic_pb2.GetEntitySizeBreakdownRequest(
            minimumEntitySize=minimum_entity_size,
            includeInternalFeatures=include_internal_features
            )
        result = self.stub.GetEntitySizeBreakdown(request)
        result = result.result
        if not return_as_string:
            result = json.loads(result)
        return result

    def get_data_source_counts(self, return_as_string=False):
        result = self.stub.GetDataSourceCounts(g2diagnostic_pb2.GetDataSourceCountsRequest())
        result = result.result
        if not return_as_string:
            result = json.loads(result)
        return result

    def get_mapping_statistics(self, include_internal_features=False, return_as_string=False):
        request = g2diagnostic_pb2.GetMappingStatisticsRequest(
            includeInternalFeatures=include_internal_features
            )
        result = self.stub.GetMappingStatistics(request)
        result = result.result
        if not return_as_string:
            result = json.loads(result)
        return result

    def get_resolution_statistics(self, return_as_string=False):
        result = self.stub.GetResolutionStatistics(
            g2diagnostic_pb2.GetResolutionStatisticsRequest()
            )
        result = result.result
        if not return_as_string:
            result = json.loads(result)
        return result

    def get_generic_features(self, feature_type, maximum_estimated_count, return_as_string=False):
        request = g2diagnostic_pb2.GetGenericFeaturesRequest(
            featureType=feature_type,
            maximumEstimatedCount=maximum_estimated_count
            )
        result = self.stub.GetGenericFeatures(request)
        result = result.result
        if not return_as_string:
            result = json.loads(result)
        return result
