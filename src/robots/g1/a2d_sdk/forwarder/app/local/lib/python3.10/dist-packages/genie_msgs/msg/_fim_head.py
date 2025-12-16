# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/FimHead.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'fim_neck'
# Member 'neck_err_code'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FimHead(type):
    """Metaclass of message 'FimHead'."""

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
                'genie_msgs.msg.FimHead')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__fim_head
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__fim_head
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__fim_head
            cls._TYPE_SUPPORT = module.type_support_msg__msg__fim_head
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__fim_head

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


class FimHead(metaclass=Metaclass_FimHead):
    """Message class 'FimHead'."""

    __slots__ = [
        '_header',
        '_fim_neck',
        '_neck_err_code',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'fim_neck': 'sequence<uint8>',
        'neck_err_code': 'sequence<uint16>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('uint8')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('uint16')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.fim_neck = array.array('B', kwargs.get('fim_neck', []))
        self.neck_err_code = array.array('H', kwargs.get('neck_err_code', []))

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
        if self.fim_neck != other.fim_neck:
            return False
        if self.neck_err_code != other.neck_err_code:
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
    def fim_neck(self):
        """Message field 'fim_neck'."""
        return self._fim_neck

    @fim_neck.setter
    def fim_neck(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'B', \
                "The 'fim_neck' array.array() must have the type code of 'B'"
            self._fim_neck = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= 0 and val < 256 for val in value)), \
                "The 'fim_neck' field must be a set or sequence and each value of type 'int' and each unsigned integer in [0, 255]"
        self._fim_neck = array.array('B', value)

    @builtins.property
    def neck_err_code(self):
        """Message field 'neck_err_code'."""
        return self._neck_err_code

    @neck_err_code.setter
    def neck_err_code(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'H', \
                "The 'neck_err_code' array.array() must have the type code of 'H'"
            self._neck_err_code = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= 0 and val < 65536 for val in value)), \
                "The 'neck_err_code' field must be a set or sequence and each value of type 'int' and each unsigned integer in [0, 65535]"
        self._neck_err_code = array.array('H', value)
