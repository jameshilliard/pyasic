# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bos/v1/configuration.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...bos.v1 import cooling_pb2 as bos_dot_v1_dot_cooling__pb2
from ...bos.v1 import performance_pb2 as bos_dot_v1_dot_performance__pb2
from ...bos.v1 import pool_pb2 as bos_dot_v1_dot_pool__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1a\x62os/v1/configuration.proto\x12\x0e\x62raiins.bos.v1\x1a\x14\x62os/v1/cooling.proto\x1a\x18\x62os/v1/performance.proto\x1a\x11\x62os/v1/pool.proto"\x1e\n\x1cGetMinerConfigurationRequest"\xc6\x02\n\x1dGetMinerConfigurationResponse\x12;\n\x0bpool_groups\x18\x01 \x03(\x0b\x32&.braiins.bos.v1.PoolGroupConfiguration\x12\x39\n\x0btemperature\x18\x02 \x01(\x0b\x32$.braiins.bos.v1.CoolingConfiguration\x12\x31\n\x05tuner\x18\x03 \x01(\x0b\x32".braiins.bos.v1.TunerConfiguration\x12-\n\x03\x64ps\x18\x04 \x01(\x0b\x32 .braiins.bos.v1.DPSConfiguration\x12K\n\x10hashboard_config\x18\x05 \x01(\x0b\x32\x31.braiins.bos.v1.HashboardPerformanceConfiguration"\x17\n\x15GetConstraintsRequest"\x95\x02\n\x16GetConstraintsResponse\x12;\n\x11tuner_constraints\x18\x01 \x01(\x0b\x32 .braiins.bos.v1.TunerConstraints\x12?\n\x13\x63ooling_constraints\x18\x02 \x01(\x0b\x32".braiins.bos.v1.CoolingConstraints\x12\x37\n\x0f\x64ps_constraints\x18\x03 \x01(\x0b\x32\x1e.braiins.bos.v1.DPSConstraints\x12\x44\n\x16hashboards_constraints\x18\x04 \x01(\x0b\x32$.braiins.bos.v1.HashboardConstraints2\xed\x01\n\x14\x43onfigurationService\x12t\n\x15GetMinerConfiguration\x12,.braiins.bos.v1.GetMinerConfigurationRequest\x1a-.braiins.bos.v1.GetMinerConfigurationResponse\x12_\n\x0eGetConstraints\x12%.braiins.bos.v1.GetConstraintsRequest\x1a&.braiins.bos.v1.GetConstraintsResponseb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "bos.v1.configuration_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_GETMINERCONFIGURATIONREQUEST"]._serialized_start = 113
    _globals["_GETMINERCONFIGURATIONREQUEST"]._serialized_end = 143
    _globals["_GETMINERCONFIGURATIONRESPONSE"]._serialized_start = 146
    _globals["_GETMINERCONFIGURATIONRESPONSE"]._serialized_end = 472
    _globals["_GETCONSTRAINTSREQUEST"]._serialized_start = 474
    _globals["_GETCONSTRAINTSREQUEST"]._serialized_end = 497
    _globals["_GETCONSTRAINTSRESPONSE"]._serialized_start = 500
    _globals["_GETCONSTRAINTSRESPONSE"]._serialized_end = 777
    _globals["_CONFIGURATIONSERVICE"]._serialized_start = 780
    _globals["_CONFIGURATIONSERVICE"]._serialized_end = 1017
# @@protoc_insertion_point(module_scope)