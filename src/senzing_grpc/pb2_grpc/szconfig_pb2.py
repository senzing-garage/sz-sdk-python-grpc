# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: szconfig.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '',
    'szconfig.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eszconfig.proto\x12\x08szconfig\"K\n\x14\x41\x64\x64\x44\x61taSourceRequest\x12\x19\n\x11\x63onfig_definition\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_source_code\x18\x02 \x01(\t\"B\n\x15\x41\x64\x64\x44\x61taSourceResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x19\n\x11\x63onfig_definition\x18\x02 \x01(\t\"N\n\x17\x44\x65leteDataSourceRequest\x12\x19\n\x11\x63onfig_definition\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_source_code\x18\x02 \x01(\t\"E\n\x18\x44\x65leteDataSourceResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x19\n\x11\x63onfig_definition\x18\x02 \x01(\t\"2\n\x15GetDataSourcesRequest\x12\x19\n\x11\x63onfig_definition\x18\x01 \x01(\t\"(\n\x16GetDataSourcesResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"0\n\x13VerifyConfigRequest\x12\x19\n\x11\x63onfig_definition\x18\x01 \x01(\t\"&\n\x14VerifyConfigResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x32\xe3\x02\n\x08SzConfig\x12R\n\rAddDataSource\x12\x1e.szconfig.AddDataSourceRequest\x1a\x1f.szconfig.AddDataSourceResponse\"\x00\x12[\n\x10\x44\x65leteDataSource\x12!.szconfig.DeleteDataSourceRequest\x1a\".szconfig.DeleteDataSourceResponse\"\x00\x12U\n\x0eGetDataSources\x12\x1f.szconfig.GetDataSourcesRequest\x1a .szconfig.GetDataSourcesResponse\"\x00\x12O\n\x0cVerifyConfig\x12\x1d.szconfig.VerifyConfigRequest\x1a\x1e.szconfig.VerifyConfigResponse\"\x00\x42X\n\x14\x63om.senzing.sdk.grpcB\rSzConfigProtoZ1github.com/senzing-garage/sz-sdk-go-grpc/szconfigb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'szconfig_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.senzing.sdk.grpcB\rSzConfigProtoZ1github.com/senzing-garage/sz-sdk-go-grpc/szconfig'
  _globals['_ADDDATASOURCEREQUEST']._serialized_start=28
  _globals['_ADDDATASOURCEREQUEST']._serialized_end=103
  _globals['_ADDDATASOURCERESPONSE']._serialized_start=105
  _globals['_ADDDATASOURCERESPONSE']._serialized_end=171
  _globals['_DELETEDATASOURCEREQUEST']._serialized_start=173
  _globals['_DELETEDATASOURCEREQUEST']._serialized_end=251
  _globals['_DELETEDATASOURCERESPONSE']._serialized_start=253
  _globals['_DELETEDATASOURCERESPONSE']._serialized_end=322
  _globals['_GETDATASOURCESREQUEST']._serialized_start=324
  _globals['_GETDATASOURCESREQUEST']._serialized_end=374
  _globals['_GETDATASOURCESRESPONSE']._serialized_start=376
  _globals['_GETDATASOURCESRESPONSE']._serialized_end=416
  _globals['_VERIFYCONFIGREQUEST']._serialized_start=418
  _globals['_VERIFYCONFIGREQUEST']._serialized_end=466
  _globals['_VERIFYCONFIGRESPONSE']._serialized_start=468
  _globals['_VERIFYCONFIGRESPONSE']._serialized_end=506
  _globals['_SZCONFIG']._serialized_start=509
  _globals['_SZCONFIG']._serialized_end=864
# @@protoc_insertion_point(module_scope)
