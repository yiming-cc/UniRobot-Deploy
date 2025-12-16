# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/FimRemote.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FimRemote(type):
    """Metaclass of message 'FimRemote'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('genie_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'genie_msgs.msg.FimRemote')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__fim_remote
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__fim_remote
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__fim_remote
            cls._TYPE_SUPPORT = module.type_support_msg__msg__fim_remote
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__fim_remote

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class FimRemote(metaclass=Metaclass_FimRemote):
    """Message class 'FimRemote'."""

    __slots__ = [
        '_header',
        '_fim_vr',
        '_vr_err_code',
        '_fim_mocap',
        '_mocap_err_code',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'fim_vr': 'uint8',
        'vr_err_code': 'uint16',
        'fim_mocap': 'uint8',
        'mocap_err_code': 'uint16',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.fim_vr = kwargs.get('fim_vr', int())
        self.vr_err_code = kwargs.get('vr_err_code', int())
        self.fim_mocap = kwargs.get('fim_mocap', int())
        self.mocap_err_code = kwargs.get('mocap_err_code', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.fim_vr != other.fim_vr:
            return False
        if self.vr_err_code != other.vr_err_code:
            return False
        if self.fim_mocap != other.fim_mocap:
            return False
        if self.mocap_err_code != other.mocap_err_code:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def fim_vr(self):
        """Message field 'fim_vr'."""
        return self._fim_vr

    @fim_vr.setter
    def fim_vr(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'fim_vr' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'fim_vr' field must be an unsigned integer in [0, 255]"
        self._fim_vr = value

    @builtins.property
    def vr_err_code(self):
        """Message field 'vr_err_code'."""
        return self._vr_err_code

    @vr_err_code.setter
    def vr_err_code(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'vr_err_code' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'vr_err_code' field must be an unsigned integer in [0, 65535]"
        self._vr_err_code = value

    @builtins.property
    def fim_mocap(self):
        """Message field 'fim_mocap'."""
        return self._fim_mocap

    @fim_mocap.setter
    def fim_mocap(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'fim_mocap' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'fim_mocap' field must be an unsigned integer in [0, 255]"
        self._fim_mocap = value

    @builtins.property
    def mocap_err_code(self):
        """Message field 'mocap_err_code'."""
        return self._mocap_err_code

    @mocap_err_code.setter
    def mocap_err_code(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'mocap_err_code' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'mocap_err_code' field must be an unsigned integer in [0, 65535]"
        self._mocap_err_code = value
