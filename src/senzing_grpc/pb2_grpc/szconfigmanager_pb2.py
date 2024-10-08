# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: szconfigmanager.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15szconfigmanager.proto\x12\x0fszconfigmanager\"C\n\x10\x41\x64\x64\x43onfigRequest\x12\x18\n\x10\x63onfigDefinition\x18\x01 \x01(\t\x12\x15\n\rconfigComment\x18\x02 \x01(\t\"#\n\x11\x41\x64\x64\x43onfigResponse\x12\x0e\n\x06result\x18\x01 \x01(\x03\"$\n\x10GetConfigRequest\x12\x10\n\x08\x63onfigId\x18\x01 \x01(\x03\"#\n\x11GetConfigResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x13\n\x11GetConfigsRequest\"$\n\x12GetConfigsResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x1b\n\x19GetDefaultConfigIdRequest\",\n\x1aGetDefaultConfigIdResponse\x12\x0e\n\x06result\x18\x01 \x01(\x03\"[\n\x1dReplaceDefaultConfigIdRequest\x12\x1e\n\x16\x63urrentDefaultConfigId\x18\x01 \x01(\x03\x12\x1a\n\x12newDefaultConfigId\x18\x02 \x01(\x03\" \n\x1eReplaceDefaultConfigIdResponse\"-\n\x19SetDefaultConfigIdRequest\x12\x10\n\x08\x63onfigId\x18\x01 \x01(\x03\"\x1c\n\x1aSetDefaultConfigIdResponse2\xf5\x04\n\x0fSzConfigManager\x12T\n\tAddConfig\x12!.szconfigmanager.AddConfigRequest\x1a\".szconfigmanager.AddConfigResponse\"\x00\x12T\n\tGetConfig\x12!.szconfigmanager.GetConfigRequest\x1a\".szconfigmanager.GetConfigResponse\"\x00\x12W\n\nGetConfigs\x12\".szconfigmanager.GetConfigsRequest\x1a#.szconfigmanager.GetConfigsResponse\"\x00\x12o\n\x12GetDefaultConfigId\x12*.szconfigmanager.GetDefaultConfigIdRequest\x1a+.szconfigmanager.GetDefaultConfigIdResponse\"\x00\x12{\n\x16ReplaceDefaultConfigId\x12..szconfigmanager.ReplaceDefaultConfigIdRequest\x1a/.szconfigmanager.ReplaceDefaultConfigIdResponse\"\x00\x12o\n\x12SetDefaultConfigId\x12*.szconfigmanager.SetDefaultConfigIdRequest\x1a+.szconfigmanager.SetDefaultConfigIdResponse\"\x00\x42|\n*com.senzing.sz.engine.grpc.SzConfigManagerB\x14SzConfigManagerProtoZ8github.com/senzing-garage/sz-sdk-go-grpc/szconfigmanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'szconfigmanager_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.senzing.sz.engine.grpc.SzConfigManagerB\024SzConfigManagerProtoZ8github.com/senzing-garage/sz-sdk-go-grpc/szconfigmanager'
  _globals['_ADDCONFIGREQUEST']._serialized_start=42
  _globals['_ADDCONFIGREQUEST']._serialized_end=109
  _globals['_ADDCONFIGRESPONSE']._serialized_start=111
  _globals['_ADDCONFIGRESPONSE']._serialized_end=146
  _globals['_GETCONFIGREQUEST']._serialized_start=148
  _globals['_GETCONFIGREQUEST']._serialized_end=184
  _globals['_GETCONFIGRESPONSE']._serialized_start=186
  _globals['_GETCONFIGRESPONSE']._serialized_end=221
  _globals['_GETCONFIGSREQUEST']._serialized_start=223
  _globals['_GETCONFIGSREQUEST']._serialized_end=242
  _globals['_GETCONFIGSRESPONSE']._serialized_start=244
  _globals['_GETCONFIGSRESPONSE']._serialized_end=280
  _globals['_GETDEFAULTCONFIGIDREQUEST']._serialized_start=282
  _globals['_GETDEFAULTCONFIGIDREQUEST']._serialized_end=309
  _globals['_GETDEFAULTCONFIGIDRESPONSE']._serialized_start=311
  _globals['_GETDEFAULTCONFIGIDRESPONSE']._serialized_end=355
  _globals['_REPLACEDEFAULTCONFIGIDREQUEST']._serialized_start=357
  _globals['_REPLACEDEFAULTCONFIGIDREQUEST']._serialized_end=448
  _globals['_REPLACEDEFAULTCONFIGIDRESPONSE']._serialized_start=450
  _globals['_REPLACEDEFAULTCONFIGIDRESPONSE']._serialized_end=482
  _globals['_SETDEFAULTCONFIGIDREQUEST']._serialized_start=484
  _globals['_SETDEFAULTCONFIGIDREQUEST']._serialized_end=529
  _globals['_SETDEFAULTCONFIGIDRESPONSE']._serialized_start=531
  _globals['_SETDEFAULTCONFIGIDRESPONSE']._serialized_end=559
  _globals['_SZCONFIGMANAGER']._serialized_start=562
  _globals['_SZCONFIGMANAGER']._serialized_end=1191
# @@protoc_insertion_point(module_scope)
