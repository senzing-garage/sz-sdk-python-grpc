# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: szengine.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0eszengine.proto\x12\x08szengine"e\n\x10\x41\x64\x64RecordRequest\x12\x16\n\x0e\x64\x61taSourceCode\x18\x01 \x01(\t\x12\x10\n\x08recordId\x18\x02 \x01(\t\x12\x18\n\x10recordDefinition\x18\x03 \x01(\t\x12\r\n\x05\x66lags\x18\x04 \x01(\x03"#\n\x11\x41\x64\x64RecordResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"*\n\x12\x43loseExportRequest\x12\x14\n\x0c\x65xportHandle\x18\x01 \x01(\x03"\x15\n\x13\x43loseExportResponse"\x19\n\x17\x43ountRedoRecordsRequest"*\n\x18\x43ountRedoRecordsResponse\x12\x0e\n\x06result\x18\x01 \x01(\x03"N\n\x13\x44\x65leteRecordRequest\x12\x16\n\x0e\x64\x61taSourceCode\x18\x01 \x01(\t\x12\x10\n\x08recordId\x18\x02 \x01(\t\x12\r\n\x05\x66lags\x18\x03 \x01(\x03"&\n\x14\x44\x65leteRecordResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"D\n\x1c\x45xportCsvEntityReportRequest\x12\x15\n\rcsvColumnList\x18\x01 \x01(\t\x12\r\n\x05\x66lags\x18\x02 \x01(\x03"/\n\x1d\x45xportCsvEntityReportResponse\x12\x0e\n\x06result\x18\x01 \x01(\x03".\n\x1d\x45xportJsonEntityReportRequest\x12\r\n\x05\x66lags\x18\x01 \x01(\x03"0\n\x1e\x45xportJsonEntityReportResponse\x12\x0e\n\x06result\x18\x01 \x01(\x03"(\n\x10\x46\x65tchNextRequest\x12\x14\n\x0c\x65xportHandle\x18\x01 \x01(\x03"#\n\x11\x46\x65tchNextResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"K\n(FindInterestingEntitiesByEntityIdRequest\x12\x10\n\x08\x65ntityId\x18\x01 \x01(\x03\x12\r\n\x05\x66lags\x18\x02 \x01(\x03";\n)FindInterestingEntitiesByEntityIdResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"c\n(FindInterestingEntitiesByRecordIdRequest\x12\x16\n\x0e\x64\x61taSourceCode\x18\x01 \x01(\t\x12\x10\n\x08recordId\x18\x02 \x01(\t\x12\r\n\x05\x66lags\x18\x03 \x01(\x03";\n)FindInterestingEntitiesByRecordIdResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\x89\x01\n\x1c\x46indNetworkByEntityIdRequest\x12\x11\n\tentityIds\x18\x01 \x01(\t\x12\x12\n\nmaxDegrees\x18\x02 \x01(\x03\x12\x16\n\x0e\x62uildOutDegree\x18\x03 \x01(\x03\x12\x1b\n\x13\x62uildOutMaxEntities\x18\x04 \x01(\x03\x12\r\n\x05\x66lags\x18\x05 \x01(\x03"/\n\x1d\x46indNetworkByEntityIdResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\x8a\x01\n\x1c\x46indNetworkByRecordIdRequest\x12\x12\n\nrecordKeys\x18\x01 \x01(\t\x12\x12\n\nmaxDegrees\x18\x02 \x01(\x03\x12\x16\n\x0e\x62uildOutDegree\x18\x03 \x01(\x03\x12\x1b\n\x13\x62uildOutMaxEntities\x18\x04 \x01(\x03\x12\r\n\x05\x66lags\x18\x05 \x01(\x03"/\n\x1d\x46indNetworkByRecordIdResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\x9f\x01\n\x19\x46indPathByEntityIdRequest\x12\x15\n\rstartEntityId\x18\x01 \x01(\x03\x12\x13\n\x0b\x65ndEntityId\x18\x02 \x01(\x03\x12\x12\n\nmaxDegrees\x18\x03 \x01(\x03\x12\x16\n\x0e\x61voidEntityIds\x18\x04 \x01(\t\x12\x1b\n\x13requiredDataSources\x18\x05 \x01(\t\x12\r\n\x05\x66lags\x18\x06 \x01(\x03",\n\x1a\x46indPathByEntityIdResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\xd8\x01\n\x19\x46indPathByRecordIdRequest\x12\x1b\n\x13startDataSourceCode\x18\x01 \x01(\t\x12\x15\n\rstartRecordId\x18\x02 \x01(\t\x12\x19\n\x11\x65ndDataSourceCode\x18\x03 \x01(\t\x12\x13\n\x0b\x65ndRecordId\x18\x04 \x01(\t\x12\x12\n\nmaxDegrees\x18\x05 \x01(\x03\x12\x17\n\x0f\x61voidRecordKeys\x18\x06 \x01(\t\x12\x1b\n\x13requiredDataSources\x18\x07 \x01(\t\x12\r\n\x05\x66lags\x18\x08 \x01(\x03",\n\x1a\x46indPathByRecordIdResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\x1a\n\x18GetActiveConfigIdRequest"+\n\x19GetActiveConfigIdResponse\x12\x0e\n\x06result\x18\x01 \x01(\x03"=\n\x1aGetEntityByEntityIdRequest\x12\x10\n\x08\x65ntityId\x18\x01 \x01(\x03\x12\r\n\x05\x66lags\x18\x02 \x01(\x03"-\n\x1bGetEntityByEntityIdResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"U\n\x1aGetEntityByRecordIdRequest\x12\x16\n\x0e\x64\x61taSourceCode\x18\x01 \x01(\t\x12\x10\n\x08recordId\x18\x02 \x01(\t\x12\r\n\x05\x66lags\x18\x03 \x01(\x03"-\n\x1bGetEntityByRecordIdResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"K\n\x10GetRecordRequest\x12\x16\n\x0e\x64\x61taSourceCode\x18\x01 \x01(\t\x12\x10\n\x08recordId\x18\x02 \x01(\t\x12\r\n\x05\x66lags\x18\x03 \x01(\x03"#\n\x11GetRecordResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\x16\n\x14GetRedoRecordRequest"\'\n\x15GetRedoRecordResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\x11\n\x0fGetStatsRequest""\n\x10GetStatsResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"F\n!GetVirtualEntityByRecordIdRequest\x12\x12\n\nrecordKeys\x18\x01 \x01(\t\x12\r\n\x05\x66lags\x18\x02 \x01(\x03"4\n"GetVirtualEntityByRecordIdResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"=\n\x1aHowEntityByEntityIdRequest\x12\x10\n\x08\x65ntityId\x18\x01 \x01(\x03\x12\r\n\x05\x66lags\x18\x02 \x01(\x03"-\n\x1bHowEntityByEntityIdResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\x14\n\x12PrimeEngineRequest"\x15\n\x13PrimeEngineResponse"=\n\x18ProcessRedoRecordRequest\x12\x12\n\nredoRecord\x18\x01 \x01(\t\x12\r\n\x05\x66lags\x18\x02 \x01(\x03"+\n\x19ProcessRedoRecordResponse\x12\x0e\n\x06result\x18\x01 \x01(\t":\n\x17ReevaluateEntityRequest\x12\x10\n\x08\x65ntityId\x18\x01 \x01(\x03\x12\r\n\x05\x66lags\x18\x02 \x01(\x03"*\n\x18ReevaluateEntityResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"R\n\x17ReevaluateRecordRequest\x12\x16\n\x0e\x64\x61taSourceCode\x18\x01 \x01(\t\x12\x10\n\x08recordId\x18\x02 \x01(\t\x12\r\n\x05\x66lags\x18\x03 \x01(\x03"*\n\x18ReevaluateRecordResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\'\n\x13ReinitializeRequest\x12\x10\n\x08\x63onfigId\x18\x01 \x01(\x03"\x16\n\x14ReinitializeResponse"U\n\x19SearchByAttributesRequest\x12\x12\n\nattributes\x18\x01 \x01(\t\x12\x15\n\rsearchProfile\x18\x02 \x01(\t\x12\r\n\x05\x66lags\x18\x03 \x01(\x03",\n\x1aSearchByAttributesResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"J\n"StreamExportCsvEntityReportRequest\x12\x15\n\rcsvColumnList\x18\x01 \x01(\t\x12\r\n\x05\x66lags\x18\x02 \x01(\x03"5\n#StreamExportCsvEntityReportResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"4\n#StreamExportJsonEntityReportRequest\x12\r\n\x05\x66lags\x18\x01 \x01(\x03"6\n$StreamExportJsonEntityReportResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"I\n\x12WhyEntitiesRequest\x12\x11\n\tentityId1\x18\x01 \x01(\x03\x12\x11\n\tentityId2\x18\x02 \x01(\x03\x12\r\n\x05\x66lags\x18\x03 \x01(\x03"%\n\x13WhyEntitiesResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"S\n\x18WhyRecordInEntityRequest\x12\x16\n\x0e\x64\x61taSourceCode\x18\x01 \x01(\t\x12\x10\n\x08recordId\x18\x02 \x01(\t\x12\r\n\x05\x66lags\x18\x03 \x01(\x03"+\n\x19WhyRecordInEntityResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"z\n\x11WhyRecordsRequest\x12\x17\n\x0f\x64\x61taSourceCode1\x18\x01 \x01(\t\x12\x11\n\trecordId1\x18\x02 \x01(\t\x12\x17\n\x0f\x64\x61taSourceCode2\x18\x03 \x01(\t\x12\x11\n\trecordId2\x18\x04 \x01(\t\x12\r\n\x05\x66lags\x18\x05 \x01(\x03"$\n\x12WhyRecordsResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2\xb8\x18\n\x08SzEngine\x12\x46\n\tAddRecord\x12\x1a.szengine.AddRecordRequest\x1a\x1b.szengine.AddRecordResponse"\x00\x12L\n\x0b\x43loseExport\x12\x1c.szengine.CloseExportRequest\x1a\x1d.szengine.CloseExportResponse"\x00\x12[\n\x10\x43ountRedoRecords\x12!.szengine.CountRedoRecordsRequest\x1a".szengine.CountRedoRecordsResponse"\x00\x12O\n\x0c\x44\x65leteRecord\x12\x1d.szengine.DeleteRecordRequest\x1a\x1e.szengine.DeleteRecordResponse"\x00\x12j\n\x15\x45xportCsvEntityReport\x12&.szengine.ExportCsvEntityReportRequest\x1a\'.szengine.ExportCsvEntityReportResponse"\x00\x12m\n\x16\x45xportJsonEntityReport\x12\'.szengine.ExportJsonEntityReportRequest\x1a(.szengine.ExportJsonEntityReportResponse"\x00\x12\x46\n\tFetchNext\x12\x1a.szengine.FetchNextRequest\x1a\x1b.szengine.FetchNextResponse"\x00\x12\x8e\x01\n!FindInterestingEntitiesByEntityId\x12\x32.szengine.FindInterestingEntitiesByEntityIdRequest\x1a\x33.szengine.FindInterestingEntitiesByEntityIdResponse"\x00\x12\x8e\x01\n!FindInterestingEntitiesByRecordId\x12\x32.szengine.FindInterestingEntitiesByRecordIdRequest\x1a\x33.szengine.FindInterestingEntitiesByRecordIdResponse"\x00\x12j\n\x15\x46indNetworkByEntityId\x12&.szengine.FindNetworkByEntityIdRequest\x1a\'.szengine.FindNetworkByEntityIdResponse"\x00\x12j\n\x15\x46indNetworkByRecordId\x12&.szengine.FindNetworkByRecordIdRequest\x1a\'.szengine.FindNetworkByRecordIdResponse"\x00\x12\x61\n\x12\x46indPathByEntityId\x12#.szengine.FindPathByEntityIdRequest\x1a$.szengine.FindPathByEntityIdResponse"\x00\x12\x61\n\x12\x46indPathByRecordId\x12#.szengine.FindPathByRecordIdRequest\x1a$.szengine.FindPathByRecordIdResponse"\x00\x12^\n\x11GetActiveConfigId\x12".szengine.GetActiveConfigIdRequest\x1a#.szengine.GetActiveConfigIdResponse"\x00\x12\x64\n\x13GetEntityByEntityId\x12$.szengine.GetEntityByEntityIdRequest\x1a%.szengine.GetEntityByEntityIdResponse"\x00\x12\x64\n\x13GetEntityByRecordId\x12$.szengine.GetEntityByRecordIdRequest\x1a%.szengine.GetEntityByRecordIdResponse"\x00\x12\x46\n\tGetRecord\x12\x1a.szengine.GetRecordRequest\x1a\x1b.szengine.GetRecordResponse"\x00\x12R\n\rGetRedoRecord\x12\x1e.szengine.GetRedoRecordRequest\x1a\x1f.szengine.GetRedoRecordResponse"\x00\x12\x43\n\x08GetStats\x12\x19.szengine.GetStatsRequest\x1a\x1a.szengine.GetStatsResponse"\x00\x12y\n\x1aGetVirtualEntityByRecordId\x12+.szengine.GetVirtualEntityByRecordIdRequest\x1a,.szengine.GetVirtualEntityByRecordIdResponse"\x00\x12\x64\n\x13HowEntityByEntityId\x12$.szengine.HowEntityByEntityIdRequest\x1a%.szengine.HowEntityByEntityIdResponse"\x00\x12L\n\x0bPrimeEngine\x12\x1c.szengine.PrimeEngineRequest\x1a\x1d.szengine.PrimeEngineResponse"\x00\x12^\n\x11ProcessRedoRecord\x12".szengine.ProcessRedoRecordRequest\x1a#.szengine.ProcessRedoRecordResponse"\x00\x12[\n\x10ReevaluateEntity\x12!.szengine.ReevaluateEntityRequest\x1a".szengine.ReevaluateEntityResponse"\x00\x12[\n\x10ReevaluateRecord\x12!.szengine.ReevaluateRecordRequest\x1a".szengine.ReevaluateRecordResponse"\x00\x12O\n\x0cReinitialize\x12\x1d.szengine.ReinitializeRequest\x1a\x1e.szengine.ReinitializeResponse"\x00\x12\x61\n\x12SearchByAttributes\x12#.szengine.SearchByAttributesRequest\x1a$.szengine.SearchByAttributesResponse"\x00\x12~\n\x1bStreamExportCsvEntityReport\x12,.szengine.StreamExportCsvEntityReportRequest\x1a-.szengine.StreamExportCsvEntityReportResponse"\x00\x30\x01\x12\x81\x01\n\x1cStreamExportJsonEntityReport\x12-.szengine.StreamExportJsonEntityReportRequest\x1a..szengine.StreamExportJsonEntityReportResponse"\x00\x30\x01\x12L\n\x0bWhyEntities\x12\x1c.szengine.WhyEntitiesRequest\x1a\x1d.szengine.WhyEntitiesResponse"\x00\x12^\n\x11WhyRecordInEntity\x12".szengine.WhyRecordInEntityRequest\x1a#.szengine.WhyRecordInEntityResponse"\x00\x12I\n\nWhyRecords\x12\x1b.szengine.WhyRecordsRequest\x1a\x1c.szengine.WhyRecordsResponse"\x00\x42g\n#com.senzing.sz.engine.grpc.SzEngineB\rSzEngineProtoZ1github.com/senzing-garage/sz-sdk-go-grpc/szengineb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "szengine_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"\n#com.senzing.sz.engine.grpc.SzEngineB\rSzEngineProtoZ1github.com/senzing-garage/sz-sdk-go-grpc/szengine"
    )
    _globals["_ADDRECORDREQUEST"]._serialized_start = 28
    _globals["_ADDRECORDREQUEST"]._serialized_end = 129
    _globals["_ADDRECORDRESPONSE"]._serialized_start = 131
    _globals["_ADDRECORDRESPONSE"]._serialized_end = 166
    _globals["_CLOSEEXPORTREQUEST"]._serialized_start = 168
    _globals["_CLOSEEXPORTREQUEST"]._serialized_end = 210
    _globals["_CLOSEEXPORTRESPONSE"]._serialized_start = 212
    _globals["_CLOSEEXPORTRESPONSE"]._serialized_end = 233
    _globals["_COUNTREDORECORDSREQUEST"]._serialized_start = 235
    _globals["_COUNTREDORECORDSREQUEST"]._serialized_end = 260
    _globals["_COUNTREDORECORDSRESPONSE"]._serialized_start = 262
    _globals["_COUNTREDORECORDSRESPONSE"]._serialized_end = 304
    _globals["_DELETERECORDREQUEST"]._serialized_start = 306
    _globals["_DELETERECORDREQUEST"]._serialized_end = 384
    _globals["_DELETERECORDRESPONSE"]._serialized_start = 386
    _globals["_DELETERECORDRESPONSE"]._serialized_end = 424
    _globals["_EXPORTCSVENTITYREPORTREQUEST"]._serialized_start = 426
    _globals["_EXPORTCSVENTITYREPORTREQUEST"]._serialized_end = 494
    _globals["_EXPORTCSVENTITYREPORTRESPONSE"]._serialized_start = 496
    _globals["_EXPORTCSVENTITYREPORTRESPONSE"]._serialized_end = 543
    _globals["_EXPORTJSONENTITYREPORTREQUEST"]._serialized_start = 545
    _globals["_EXPORTJSONENTITYREPORTREQUEST"]._serialized_end = 591
    _globals["_EXPORTJSONENTITYREPORTRESPONSE"]._serialized_start = 593
    _globals["_EXPORTJSONENTITYREPORTRESPONSE"]._serialized_end = 641
    _globals["_FETCHNEXTREQUEST"]._serialized_start = 643
    _globals["_FETCHNEXTREQUEST"]._serialized_end = 683
    _globals["_FETCHNEXTRESPONSE"]._serialized_start = 685
    _globals["_FETCHNEXTRESPONSE"]._serialized_end = 720
    _globals["_FINDINTERESTINGENTITIESBYENTITYIDREQUEST"]._serialized_start = 722
    _globals["_FINDINTERESTINGENTITIESBYENTITYIDREQUEST"]._serialized_end = 797
    _globals["_FINDINTERESTINGENTITIESBYENTITYIDRESPONSE"]._serialized_start = 799
    _globals["_FINDINTERESTINGENTITIESBYENTITYIDRESPONSE"]._serialized_end = 858
    _globals["_FINDINTERESTINGENTITIESBYRECORDIDREQUEST"]._serialized_start = 860
    _globals["_FINDINTERESTINGENTITIESBYRECORDIDREQUEST"]._serialized_end = 959
    _globals["_FINDINTERESTINGENTITIESBYRECORDIDRESPONSE"]._serialized_start = 961
    _globals["_FINDINTERESTINGENTITIESBYRECORDIDRESPONSE"]._serialized_end = 1020
    _globals["_FINDNETWORKBYENTITYIDREQUEST"]._serialized_start = 1023
    _globals["_FINDNETWORKBYENTITYIDREQUEST"]._serialized_end = 1160
    _globals["_FINDNETWORKBYENTITYIDRESPONSE"]._serialized_start = 1162
    _globals["_FINDNETWORKBYENTITYIDRESPONSE"]._serialized_end = 1209
    _globals["_FINDNETWORKBYRECORDIDREQUEST"]._serialized_start = 1212
    _globals["_FINDNETWORKBYRECORDIDREQUEST"]._serialized_end = 1350
    _globals["_FINDNETWORKBYRECORDIDRESPONSE"]._serialized_start = 1352
    _globals["_FINDNETWORKBYRECORDIDRESPONSE"]._serialized_end = 1399
    _globals["_FINDPATHBYENTITYIDREQUEST"]._serialized_start = 1402
    _globals["_FINDPATHBYENTITYIDREQUEST"]._serialized_end = 1561
    _globals["_FINDPATHBYENTITYIDRESPONSE"]._serialized_start = 1563
    _globals["_FINDPATHBYENTITYIDRESPONSE"]._serialized_end = 1607
    _globals["_FINDPATHBYRECORDIDREQUEST"]._serialized_start = 1610
    _globals["_FINDPATHBYRECORDIDREQUEST"]._serialized_end = 1826
    _globals["_FINDPATHBYRECORDIDRESPONSE"]._serialized_start = 1828
    _globals["_FINDPATHBYRECORDIDRESPONSE"]._serialized_end = 1872
    _globals["_GETACTIVECONFIGIDREQUEST"]._serialized_start = 1874
    _globals["_GETACTIVECONFIGIDREQUEST"]._serialized_end = 1900
    _globals["_GETACTIVECONFIGIDRESPONSE"]._serialized_start = 1902
    _globals["_GETACTIVECONFIGIDRESPONSE"]._serialized_end = 1945
    _globals["_GETENTITYBYENTITYIDREQUEST"]._serialized_start = 1947
    _globals["_GETENTITYBYENTITYIDREQUEST"]._serialized_end = 2008
    _globals["_GETENTITYBYENTITYIDRESPONSE"]._serialized_start = 2010
    _globals["_GETENTITYBYENTITYIDRESPONSE"]._serialized_end = 2055
    _globals["_GETENTITYBYRECORDIDREQUEST"]._serialized_start = 2057
    _globals["_GETENTITYBYRECORDIDREQUEST"]._serialized_end = 2142
    _globals["_GETENTITYBYRECORDIDRESPONSE"]._serialized_start = 2144
    _globals["_GETENTITYBYRECORDIDRESPONSE"]._serialized_end = 2189
    _globals["_GETRECORDREQUEST"]._serialized_start = 2191
    _globals["_GETRECORDREQUEST"]._serialized_end = 2266
    _globals["_GETRECORDRESPONSE"]._serialized_start = 2268
    _globals["_GETRECORDRESPONSE"]._serialized_end = 2303
    _globals["_GETREDORECORDREQUEST"]._serialized_start = 2305
    _globals["_GETREDORECORDREQUEST"]._serialized_end = 2327
    _globals["_GETREDORECORDRESPONSE"]._serialized_start = 2329
    _globals["_GETREDORECORDRESPONSE"]._serialized_end = 2368
    _globals["_GETSTATSREQUEST"]._serialized_start = 2370
    _globals["_GETSTATSREQUEST"]._serialized_end = 2387
    _globals["_GETSTATSRESPONSE"]._serialized_start = 2389
    _globals["_GETSTATSRESPONSE"]._serialized_end = 2423
    _globals["_GETVIRTUALENTITYBYRECORDIDREQUEST"]._serialized_start = 2425
    _globals["_GETVIRTUALENTITYBYRECORDIDREQUEST"]._serialized_end = 2495
    _globals["_GETVIRTUALENTITYBYRECORDIDRESPONSE"]._serialized_start = 2497
    _globals["_GETVIRTUALENTITYBYRECORDIDRESPONSE"]._serialized_end = 2549
    _globals["_HOWENTITYBYENTITYIDREQUEST"]._serialized_start = 2551
    _globals["_HOWENTITYBYENTITYIDREQUEST"]._serialized_end = 2612
    _globals["_HOWENTITYBYENTITYIDRESPONSE"]._serialized_start = 2614
    _globals["_HOWENTITYBYENTITYIDRESPONSE"]._serialized_end = 2659
    _globals["_PRIMEENGINEREQUEST"]._serialized_start = 2661
    _globals["_PRIMEENGINEREQUEST"]._serialized_end = 2681
    _globals["_PRIMEENGINERESPONSE"]._serialized_start = 2683
    _globals["_PRIMEENGINERESPONSE"]._serialized_end = 2704
    _globals["_PROCESSREDORECORDREQUEST"]._serialized_start = 2706
    _globals["_PROCESSREDORECORDREQUEST"]._serialized_end = 2767
    _globals["_PROCESSREDORECORDRESPONSE"]._serialized_start = 2769
    _globals["_PROCESSREDORECORDRESPONSE"]._serialized_end = 2812
    _globals["_REEVALUATEENTITYREQUEST"]._serialized_start = 2814
    _globals["_REEVALUATEENTITYREQUEST"]._serialized_end = 2872
    _globals["_REEVALUATEENTITYRESPONSE"]._serialized_start = 2874
    _globals["_REEVALUATEENTITYRESPONSE"]._serialized_end = 2916
    _globals["_REEVALUATERECORDREQUEST"]._serialized_start = 2918
    _globals["_REEVALUATERECORDREQUEST"]._serialized_end = 3000
    _globals["_REEVALUATERECORDRESPONSE"]._serialized_start = 3002
    _globals["_REEVALUATERECORDRESPONSE"]._serialized_end = 3044
    _globals["_REINITIALIZEREQUEST"]._serialized_start = 3046
    _globals["_REINITIALIZEREQUEST"]._serialized_end = 3085
    _globals["_REINITIALIZERESPONSE"]._serialized_start = 3087
    _globals["_REINITIALIZERESPONSE"]._serialized_end = 3109
    _globals["_SEARCHBYATTRIBUTESREQUEST"]._serialized_start = 3111
    _globals["_SEARCHBYATTRIBUTESREQUEST"]._serialized_end = 3196
    _globals["_SEARCHBYATTRIBUTESRESPONSE"]._serialized_start = 3198
    _globals["_SEARCHBYATTRIBUTESRESPONSE"]._serialized_end = 3242
    _globals["_STREAMEXPORTCSVENTITYREPORTREQUEST"]._serialized_start = 3244
    _globals["_STREAMEXPORTCSVENTITYREPORTREQUEST"]._serialized_end = 3318
    _globals["_STREAMEXPORTCSVENTITYREPORTRESPONSE"]._serialized_start = 3320
    _globals["_STREAMEXPORTCSVENTITYREPORTRESPONSE"]._serialized_end = 3373
    _globals["_STREAMEXPORTJSONENTITYREPORTREQUEST"]._serialized_start = 3375
    _globals["_STREAMEXPORTJSONENTITYREPORTREQUEST"]._serialized_end = 3427
    _globals["_STREAMEXPORTJSONENTITYREPORTRESPONSE"]._serialized_start = 3429
    _globals["_STREAMEXPORTJSONENTITYREPORTRESPONSE"]._serialized_end = 3483
    _globals["_WHYENTITIESREQUEST"]._serialized_start = 3485
    _globals["_WHYENTITIESREQUEST"]._serialized_end = 3558
    _globals["_WHYENTITIESRESPONSE"]._serialized_start = 3560
    _globals["_WHYENTITIESRESPONSE"]._serialized_end = 3597
    _globals["_WHYRECORDINENTITYREQUEST"]._serialized_start = 3599
    _globals["_WHYRECORDINENTITYREQUEST"]._serialized_end = 3682
    _globals["_WHYRECORDINENTITYRESPONSE"]._serialized_start = 3684
    _globals["_WHYRECORDINENTITYRESPONSE"]._serialized_end = 3727
    _globals["_WHYRECORDSREQUEST"]._serialized_start = 3729
    _globals["_WHYRECORDSREQUEST"]._serialized_end = 3851
    _globals["_WHYRECORDSRESPONSE"]._serialized_start = 3853
    _globals["_WHYRECORDSRESPONSE"]._serialized_end = 3889
    _globals["_SZENGINE"]._serialized_start = 3892
    _globals["_SZENGINE"]._serialized_end = 7020
# @@protoc_insertion_point(module_scope)
