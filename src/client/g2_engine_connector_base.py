from abc import ABCMeta, abstractmethod
from typing import Union, Tuple, Callable, Iterable
from datetime import datetime

class G2EngineConnectorBase(metaclass=ABCMeta):
    @abstractmethod
    def init_direct(self, 
                    module_name: str, 
                    senzing_config_json: Union[str,dict], 
                    config_id: int, 
                    verbose_logging: bool) -> None:
        pass

    @abstractmethod
    def init_with_url(self, url: str) -> None:
        pass

    @abstractmethod
    def init_direct_from_environment(self, 
                                     module_name: str, 
                                     config_id: int, 
                                     verbose_logging: bool) -> None:
        pass

    @abstractmethod
    def reinit(self, config_id: int) -> None:
        pass

    @abstractmethod
    def destroy(self) -> None:
        pass

    @abstractmethod
    def prime_engine(self) -> None:
        pass

    @abstractmethod
    def get_active_config_id(self) -> None:
        pass

    @abstractmethod
    def export_config(self) -> dict:
        pass

    @abstractmethod
    def export_config_and_config_id(self) -> Tuple[dict,int]:
        pass

    @abstractmethod
    def get_repository_last_modified_time(self) -> datetime:
        pass

    #Adding Records
    @abstractmethod
    def add_record(self,
                   datasource_code: str,
                   record_id: str,
                   data_as_json: Union[str,dict],
                   load_id: str) -> None:
        pass

    @abstractmethod
    def add_record_with_info(self,
                             datasource_code: str,
                             record_id: str,
                             data_as_json: str,
                             load_id: str,
                             flags: int) -> str:
        pass

    @abstractmethod
    def add_record_with_returned_record_id(self,
                                           datasource_code: str,
                                           data_as_json: str,
                                           load_id=None) -> str:
        pass

    @abstractmethod
    def add_record_with_info_with_returned_record_id(self,
                                                     datasource_code: str,
                                                     data_as_json: str,
                                                     load_id: str,
                                                     flags: int) -> Tuple[str,str]:
        pass

    #replace
    @abstractmethod
    def replace_record(self,
                       datasource_code: str,
                       record_id: str,
                       data_as_json: str,
                       load_id: str) -> None:
        pass


    @abstractmethod
    def replace_record_with_info(self,
                                 datasource_code: str,
                                 record_id: str,
                                 data_as_json: str,
                                 load_id: str,
                                 flags: int) -> str:
        pass

    #reevaluation
    @abstractmethod
    def reevaluate_record(self,
                          datasource_code: str,
                          record_id: str,
                          flags: bool) -> None:
        pass

    @abstractmethod
    def reevaluate_record_with_info(self,
                                    datasource_code: str,
                                    record_id: str,
                                    flags: bool) -> str:
        pass

    @abstractmethod
    def reevaluate_entity(self, entity_id: int, flags: int) -> None:
        pass

    @abstractmethod
    def reevaluate_entity_with_info(self, entity_id: int, flags: int) -> str:
        pass

    #redo processing
    @abstractmethod
    def count_redo_records(self) -> int:
        pass

    @abstractmethod
    def get_redo_record(self) -> str:
        pass

    @abstractmethod
    def process(self, redo_record: str) -> None:
        pass

    @abstractmethod
    def process_with_info(self, redo_record: str, flags: int) -> str:
        pass

    @abstractmethod
    def process_redo_record(self) -> str:
        pass

    @abstractmethod
    def process_redo_record_with_info(self, flags: int) -> Tuple[str,str]:
        pass

    #delete records
    @abstractmethod
    def delete_record(self, datasource_code: str, record_id: str, load_id: str) -> None:
        pass

    @abstractmethod
    def delete_record_with_info(self, datasource_code: str, record_id: str, load_id: str, flags) -> str:
        pass

    #get records and entities
    @abstractmethod
    def get_record(self, datasource_code: str, record_id: str, flags: int) ->str:
        pass

    @abstractmethod
    def get_entity_by_record_id(self, datasource_code: str, record_id: str, flags: int) ->str:
        pass

    @abstractmethod
    def get_entity_by_entity_id(self, entity_id: int, flags: int) ->str:
        pass

    #search for entities
    @abstractmethod
    def search_by_attributes(self, search_attributes: str, flags: int) -> str:
        pass

    #find paths
    @abstractmethod
    def find_path_by_entity_id(self,
                               start_entity_id: int,
                               end_entity_id: int,
                               max_degree: int,
                               flags: int) -> str:
        pass

    @abstractmethod
    def find_path_by_record_id(self,
                               start_datasource_code: str,
                               start_record_id: str,
                               end_datasource_code: str,
                               end_record_id: str,
                               max_degree: int,
                               flags: int) -> str:
        pass

    @abstractmethod
    def find_path_excluding_by_entity_id(self,
                                         start_entity_id: int,
                                         end_entity_id: int,
                                         max_degree: int,
                                         excluded_entities: str,
                                         flags: int) -> str:
        pass

    @abstractmethod
    def find_path_excluding_by_record_id(self, 
                                         start_datasource_code: str,
                                         start_record_id: str,
                                         end_datasource_code: str,
                                         end_record_id: str,
                                         max_degree: int,
                                         excluded_entities: str,
                                         flags: int) -> str:
        pass

    @abstractmethod
    def find_path_including_source_by_entity_id(self,
                                                start_entity_id: int,
                                                end_entity_id: int,
                                                max_degree: int,
                                                excluded_entities: str,
                                                required_datasources: str,
                                                flags) -> str:
        pass

    @abstractmethod
    def find_path_including_source_by_record_id(self,
                                                start_datasource_code: str,
                                                start_record_id: str,
                                                end_datasource_code: str,
                                                end_record_id: str,
                                                max_degree: int,
                                                excluded_entities: str,
                                                required_datasources: str,
                                                flags: int) ->str:
        pass

    #find networks
    @abstractmethod
    def find_network_by_entity_id(self,
                                  entity_list: str,
                                  max_degree: int,
                                  buildout_degree: int,
                                  max_entities: int,
                                  flags: int):
        pass

    @abstractmethod
    def find_network_by_record_id(self,
                                  record_list: str,
                                  max_degree: int,
                                  buildout_degree: int,
                                  max_entities: int,
                                  flags: int):
        pass

    #why
    @abstractmethod
    def why_entities(self,
                     entity_id_1: int,
                     entity_id_2: int,
                     flags: int) -> str:
        pass

    @abstractmethod
    def why_records(self,
                    datasource_code_1: str,
                    record_id_1: str,
                    datasource_code_2: str,
                    record_id_2: str,
                    flags: int) -> str:
        pass

    @abstractmethod
    def why_entity_by_record_id(self,
                                datasource_code_1: str,
                                record_id_1: str,
                                flags: int) -> str:
        pass

    @abstractmethod
    def why_entity_by_entity_id(self, entity_id: int, flags: int) -> str:
        pass

    @abstractmethod
    def how_entity_by_entity_id(self, entity_id: int, flags: int) -> str:
        pass

    #export
    @abstractmethod
    def export_csv_entity_report_with_callback(self,
                                               columns: str,
                                               flags: int,
                                               callback: Callable[[Union[str,dict]], None],
                                               return_as_string: bool):
        pass

    @abstractmethod
    def export_csv_entity_report_iteritems(self,
                                           columns: str,
                                           flags: int,
                                           return_as_string: bool):
        pass

    @abstractmethod
    def export_json_entity_report_with_callback(self,
                                                flags: int,
                                                callback: Callable[[Union[str,dict]], None],
                                                return_as_string: bool):
        pass

    @abstractmethod
    def export_json_entity_report_iteritems(self, flags: int, return_as_string: bool):
        pass

    #purge
    @abstractmethod
    def purge_repository(self) -> None:
        pass


