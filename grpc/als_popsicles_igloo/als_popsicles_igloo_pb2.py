# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: als_popsicles_igloo/als_popsicles_igloo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from openconfig import ywrapper_pb2 as github_dot_com_dot_openconfig_dot_ygot_dot_proto_dot_ywrapper_dot_ywrapper__pb2
from openconfig import yext_pb2 as github_dot_com_dot_openconfig_dot_ygot_dot_proto_dot_yext_dot_yext__pb2
from enums import enums_pb2 as enums_dot_enums__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='als_popsicles_igloo/als_popsicles_igloo.proto',
  package='protos.als_popsicles_igloo',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-als_popsicles_igloo/als_popsicles_igloo.proto\x12\x1aprotos.als_popsicles_igloo\x1a\x38github.com/openconfig/ygot/proto/ywrapper/ywrapper.proto\x1a\x30github.com/openconfig/ygot/proto/yext/yext.proto\x1a\x11\x65nums/enums.proto\"\xe1\x01\n\x04Menu\x12\x43\n\x0b\x64\x65scription\x18\xc5\xa0\x87\x15 \x01(\x0b\x32\x15.ywrapper.StringValueB\x14\x82\x41\x11/menu/description\x12;\n\x05price\x18\xcc\xc4\xcf\x8f\x01 \x01(\x0b\x32\x18.ywrapper.Decimal64ValueB\x0e\x82\x41\x0b/menu/price\x12W\n\x04type\x18\x91\xe9\xee/ \x01(\x0e\x32\x37.als_popsicle_igloo.enums.AlsPopsiclesIglooPopsicleTypeB\r\x82\x41\n/menu/type\"\xd2\x02\n\x08Purchase\x12N\n\rpayment_total\x18\xe6\xc7\xce| \x01(\x0b\x32\x18.ywrapper.Decimal64ValueB\x1a\x82\x41\x17/purchase/payment_total\x12`\n\tpopsicles\x18\xcb\x8f\xb9\xd3\x01 \x03(\x0b\x32\x31.protos.als_popsicles_igloo.Purchase.PopsiclesKeyB\x16\x82\x41\x13/purchase/popsicles\x1a\x0b\n\tPopsicles\x1a\x86\x01\n\x0cPopsiclesKey\x12\x33\n\tmenu_item\x18\x01 \x01(\tB \x82\x41\x1d/purchase/popsicles/menu_item\x12\x41\n\tpopsicles\x18\x02 \x01(\x0b\x32..protos.als_popsicles_igloo.Purchase.Popsicles2b\n\x0bMenuRequest\x12S\n\x0brequestMenu\x12 .protos.als_popsicles_igloo.Menu\x1a .protos.als_popsicles_igloo.Menu\"\x00\x62\x06proto3')
  ,
  dependencies=[github_dot_com_dot_openconfig_dot_ygot_dot_proto_dot_ywrapper_dot_ywrapper__pb2.DESCRIPTOR,github_dot_com_dot_openconfig_dot_ygot_dot_proto_dot_yext_dot_yext__pb2.DESCRIPTOR,enums_dot_enums__pb2.DESCRIPTOR,])




_MENU = _descriptor.Descriptor(
  name='Menu',
  full_name='protos.als_popsicles_igloo.Menu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='protos.als_popsicles_igloo.Menu.description', index=0,
      number=44159045, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202A\021/menu/description'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='protos.als_popsicles_igloo.Menu.price', index=1,
      number=301195852, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202A\013/menu/price'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='protos.als_popsicles_igloo.Menu.type', index=2,
      number=100381841, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202A\n/menu/type'), file=DESCRIPTOR),
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
  serialized_start=205,
  serialized_end=430,
)


_PURCHASE_POPSICLES = _descriptor.Descriptor(
  name='Popsicles',
  full_name='protos.als_popsicles_igloo.Purchase.Popsicles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=623,
  serialized_end=634,
)

_PURCHASE_POPSICLESKEY = _descriptor.Descriptor(
  name='PopsiclesKey',
  full_name='protos.als_popsicles_igloo.Purchase.PopsiclesKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='menu_item', full_name='protos.als_popsicles_igloo.Purchase.PopsiclesKey.menu_item', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202A\035/purchase/popsicles/menu_item'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='popsicles', full_name='protos.als_popsicles_igloo.Purchase.PopsiclesKey.popsicles', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=637,
  serialized_end=771,
)

_PURCHASE = _descriptor.Descriptor(
  name='Purchase',
  full_name='protos.als_popsicles_igloo.Purchase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payment_total', full_name='protos.als_popsicles_igloo.Purchase.payment_total', index=0,
      number=261333990, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202A\027/purchase/payment_total'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='popsicles', full_name='protos.als_popsicles_igloo.Purchase.popsicles', index=1,
      number=443434955, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202A\023/purchase/popsicles'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PURCHASE_POPSICLES, _PURCHASE_POPSICLESKEY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=433,
  serialized_end=771,
)

_MENU.fields_by_name['description'].message_type = github_dot_com_dot_openconfig_dot_ygot_dot_proto_dot_ywrapper_dot_ywrapper__pb2._STRINGVALUE
_MENU.fields_by_name['price'].message_type = github_dot_com_dot_openconfig_dot_ygot_dot_proto_dot_ywrapper_dot_ywrapper__pb2._DECIMAL64VALUE
_MENU.fields_by_name['type'].enum_type = enums_dot_enums__pb2._ALSPOPSICLESIGLOOPOPSICLETYPE
_PURCHASE_POPSICLES.containing_type = _PURCHASE
_PURCHASE_POPSICLESKEY.fields_by_name['popsicles'].message_type = _PURCHASE_POPSICLES
_PURCHASE_POPSICLESKEY.containing_type = _PURCHASE
_PURCHASE.fields_by_name['payment_total'].message_type = github_dot_com_dot_openconfig_dot_ygot_dot_proto_dot_ywrapper_dot_ywrapper__pb2._DECIMAL64VALUE
_PURCHASE.fields_by_name['popsicles'].message_type = _PURCHASE_POPSICLESKEY
DESCRIPTOR.message_types_by_name['Menu'] = _MENU
DESCRIPTOR.message_types_by_name['Purchase'] = _PURCHASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Menu = _reflection.GeneratedProtocolMessageType('Menu', (_message.Message,), dict(
  DESCRIPTOR = _MENU,
  __module__ = 'als_popsicles_igloo.als_popsicles_igloo_pb2'
  # @@protoc_insertion_point(class_scope:protos.als_popsicles_igloo.Menu)
  ))
_sym_db.RegisterMessage(Menu)

Purchase = _reflection.GeneratedProtocolMessageType('Purchase', (_message.Message,), dict(

  Popsicles = _reflection.GeneratedProtocolMessageType('Popsicles', (_message.Message,), dict(
    DESCRIPTOR = _PURCHASE_POPSICLES,
    __module__ = 'als_popsicles_igloo.als_popsicles_igloo_pb2'
    # @@protoc_insertion_point(class_scope:protos.als_popsicles_igloo.Purchase.Popsicles)
    ))
  ,

  PopsiclesKey = _reflection.GeneratedProtocolMessageType('PopsiclesKey', (_message.Message,), dict(
    DESCRIPTOR = _PURCHASE_POPSICLESKEY,
    __module__ = 'als_popsicles_igloo.als_popsicles_igloo_pb2'
    # @@protoc_insertion_point(class_scope:protos.als_popsicles_igloo.Purchase.PopsiclesKey)
    ))
  ,
  DESCRIPTOR = _PURCHASE,
  __module__ = 'als_popsicles_igloo.als_popsicles_igloo_pb2'
  # @@protoc_insertion_point(class_scope:protos.als_popsicles_igloo.Purchase)
  ))
_sym_db.RegisterMessage(Purchase)
_sym_db.RegisterMessage(Purchase.Popsicles)
_sym_db.RegisterMessage(Purchase.PopsiclesKey)


_MENU.fields_by_name['description']._options = None
_MENU.fields_by_name['price']._options = None
_MENU.fields_by_name['type']._options = None
_PURCHASE_POPSICLESKEY.fields_by_name['menu_item']._options = None
_PURCHASE.fields_by_name['payment_total']._options = None
_PURCHASE.fields_by_name['popsicles']._options = None

_MENUREQUEST = _descriptor.ServiceDescriptor(
  name='MenuRequest',
  full_name='protos.als_popsicles_igloo.MenuRequest',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=773,
  serialized_end=871,
  methods=[
  _descriptor.MethodDescriptor(
    name='requestMenu',
    full_name='protos.als_popsicles_igloo.MenuRequest.requestMenu',
    index=0,
    containing_service=None,
    input_type=_MENU,
    output_type=_MENU,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MENUREQUEST)

DESCRIPTOR.services_by_name['MenuRequest'] = _MENUREQUEST

# @@protoc_insertion_point(module_scope)
