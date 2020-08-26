# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GamayunResult.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GamayunResult.proto',
  package='gamayun',
  syntax='proto3',
  serialized_options=b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13GamayunResult.proto\x12\x07gamayun\",\n\nTaskResult\x12\r\n\x05jobId\x18\x01 \x01(\t\x12\x0f\n\x07results\x18\x02 \x03(\t\"\x0f\n\rEmptyResponse2G\n\x06Result\x12=\n\x0cReportResult\x12\x13.gamayun.TaskResult\x1a\x16.gamayun.EmptyResponse\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3'
)




_TASKRESULT = _descriptor.Descriptor(
  name='TaskResult',
  full_name='gamayun.TaskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobId', full_name='gamayun.TaskResult.jobId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='gamayun.TaskResult.results', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=76,
)


_EMPTYRESPONSE = _descriptor.Descriptor(
  name='EmptyResponse',
  full_name='gamayun.EmptyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['TaskResult'] = _TASKRESULT
DESCRIPTOR.message_types_by_name['EmptyResponse'] = _EMPTYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskResult = _reflection.GeneratedProtocolMessageType('TaskResult', (_message.Message,), {
  'DESCRIPTOR' : _TASKRESULT,
  '__module__' : 'GamayunResult_pb2'
  # @@protoc_insertion_point(class_scope:gamayun.TaskResult)
  })
_sym_db.RegisterMessage(TaskResult)

EmptyResponse = _reflection.GeneratedProtocolMessageType('EmptyResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYRESPONSE,
  '__module__' : 'GamayunResult_pb2'
  # @@protoc_insertion_point(class_scope:gamayun.EmptyResponse)
  })
_sym_db.RegisterMessage(EmptyResponse)


DESCRIPTOR._options = None

_RESULT = _descriptor.ServiceDescriptor(
  name='Result',
  full_name='gamayun.Result',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=95,
  serialized_end=166,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReportResult',
    full_name='gamayun.Result.ReportResult',
    index=0,
    containing_service=None,
    input_type=_TASKRESULT,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RESULT)

DESCRIPTOR.services_by_name['Result'] = _RESULT

# @@protoc_insertion_point(module_scope)
