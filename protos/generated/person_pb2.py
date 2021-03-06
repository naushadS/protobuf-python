# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generated/person.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="generated/person.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x16generated/person.proto"I\n\x06Person\x12\x11\n\tfirstName\x18\x01 \x01(\t\x12\x10\n\x08lastName\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\r\n\x05\x65mail\x18\x04 \x01(\t"#\n\x07Persons\x12\x18\n\x07persons\x18\x01 \x03(\x0b\x32\x07.Personb\x06proto3',
)


_PERSON = _descriptor.Descriptor(
    name="Person",
    full_name="Person",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="firstName",
            full_name="Person.firstName",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="lastName",
            full_name="Person.lastName",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="age",
            full_name="Person.age",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="email",
            full_name="Person.email",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=26,
    serialized_end=99,
)


_PERSONS = _descriptor.Descriptor(
    name="Persons",
    full_name="Persons",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="persons",
            full_name="Persons.persons",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=101,
    serialized_end=136,
)

_PERSONS.fields_by_name["persons"].message_type = _PERSON
DESCRIPTOR.message_types_by_name["Person"] = _PERSON
DESCRIPTOR.message_types_by_name["Persons"] = _PERSONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType(
    "Person",
    (_message.Message,),
    {
        "DESCRIPTOR": _PERSON,
        "__module__": "generated.person_pb2"
        # @@protoc_insertion_point(class_scope:Person)
    },
)
_sym_db.RegisterMessage(Person)

Persons = _reflection.GeneratedProtocolMessageType(
    "Persons",
    (_message.Message,),
    {
        "DESCRIPTOR": _PERSONS,
        "__module__": "generated.person_pb2"
        # @@protoc_insertion_point(class_scope:Persons)
    },
)
_sym_db.RegisterMessage(Persons)


# @@protoc_insertion_point(module_scope)
