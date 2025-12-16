# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/PublicFaultMsg.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_PublicFaultMsg(type):
    """Metaclass of message 'PublicFaultMsg'."""

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
                'genie_msgs.msg.PublicFaultMsg')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__public_fault_msg
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__public_fault_msg
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__public_fault_msg
            cls._TYPE_SUPPORT = module.type_support_msg__msg__public_fault_msg
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__public_fault_msg

            from genie_msgs.msg import FaultType
            if FaultType.__class__._TYPE_SUPPORT is None:
                FaultType.__class__.__import_type_support__()

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


class PublicFaultMsg(metaclass=Metaclass_PublicFaultMsg):
    """Message class 'PublicFaultMsg'."""

    __slots__ = [
        '_header',
        '_fault_codes',
        '_publish_ptp_ts',
        '_publisher_id',
        '_counter',
        '_publish_ts',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'fault_codes': 'sequence<genie_msgs/FaultType>',
        'publish_ptp_ts': 'uint64',
        'publisher_id': 'string',
        'counter': 'uint64',
        'publish_ts': 'uint64',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'FaultType')),  # noqa: E501
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.fault_codes = kwargs.get('fault_codes', [])
        self.publish_ptp_ts = kwargs.get('publish_ptp_ts', int())
        self.publisher_id = kwargs.get('publisher_id', str())
        self.counter = kwargs.get('counter', int())
        self.publish_ts = kwargs.get('publish_ts', int())

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
        if self.fault_codes != other.fault_codes:
            return False
        if self.publish_ptp_ts != other.publish_ptp_ts:
            return False
        if self.publisher_id != other.publisher_id:
            return False
        if self.counter != other.counter:
            return False
        if self.publish_ts != other.publish_ts:
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
    def fault_codes(self):
        """Message field 'fault_codes'."""
        return self._fault_codes

    @fault_codes.setter
    def fault_codes(self, value):
        if __debug__:
            from genie_msgs.msg import FaultType
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
                 all(isinstance(v, FaultType) for v in value) and
                 True), \
                "The 'fault_codes' field must be a set or sequence and each value of type 'FaultType'"
        self._fault_codes = value

    @builtins.property
    def publish_ptp_ts(self):
        """Message field 'publish_ptp_ts'."""
        return self._publish_ptp_ts

    @publish_ptp_ts.setter
    def publish_ptp_ts(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'publish_ptp_ts' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'publish_ptp_ts' field must be an unsigned integer in [0, 18446744073709551615]"
        self._publish_ptp_ts = value

    @builtins.property
    def publisher_id(self):
        """Message field 'publisher_id'."""
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'publisher_id' field must be of type 'str'"
        self._publisher_id = value

    @builtins.property
    def counter(self):
        """Message field 'counter'."""
        return self._counter

    @counter.setter
    def counter(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'counter' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'counter' field must be an unsigned integer in [0, 18446744073709551615]"
        self._counter = value

    @builtins.property
    def publish_ts(self):
        """Message field 'publish_ts'."""
        return self._publish_ts

    @publish_ts.setter
    def publish_ts(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'publish_ts' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'publish_ts' field must be an unsigned integer in [0, 18446744073709551615]"
        self._publish_ts = value
