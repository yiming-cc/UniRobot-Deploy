# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/FaultType.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FaultType(type):
    """Metaclass of message 'FaultType'."""

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
                'genie_msgs.msg.FaultType')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__fault_type
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__fault_type
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__fault_type
            cls._TYPE_SUPPORT = module.type_support_msg__msg__fault_type
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__fault_type

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class FaultType(metaclass=Metaclass_FaultType):
    """Message class 'FaultType'."""

    __slots__ = [
        '_fault_code',
        '_severity',
        '_component',
        '_description',
        '_fault_type',
        '_guide',
    ]

    _fields_and_field_types = {
        'fault_code': 'uint64',
        'severity': 'uint64',
        'component': 'string',
        'description': 'string',
        'fault_type': 'string',
        'guide': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.fault_code = kwargs.get('fault_code', int())
        self.severity = kwargs.get('severity', int())
        self.component = kwargs.get('component', str())
        self.description = kwargs.get('description', str())
        self.fault_type = kwargs.get('fault_type', str())
        self.guide = kwargs.get('guide', str())

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
        if self.fault_code != other.fault_code:
            return False
        if self.severity != other.severity:
            return False
        if self.component != other.component:
            return False
        if self.description != other.description:
            return False
        if self.fault_type != other.fault_type:
            return False
        if self.guide != other.guide:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def fault_code(self):
        """Message field 'fault_code'."""
        return self._fault_code

    @fault_code.setter
    def fault_code(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'fault_code' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'fault_code' field must be an unsigned integer in [0, 18446744073709551615]"
        self._fault_code = value

    @builtins.property
    def severity(self):
        """Message field 'severity'."""
        return self._severity

    @severity.setter
    def severity(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'severity' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'severity' field must be an unsigned integer in [0, 18446744073709551615]"
        self._severity = value

    @builtins.property
    def component(self):
        """Message field 'component'."""
        return self._component

    @component.setter
    def component(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'component' field must be of type 'str'"
        self._component = value

    @builtins.property
    def description(self):
        """Message field 'description'."""
        return self._description

    @description.setter
    def description(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'description' field must be of type 'str'"
        self._description = value

    @builtins.property
    def fault_type(self):
        """Message field 'fault_type'."""
        return self._fault_type

    @fault_type.setter
    def fault_type(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'fault_type' field must be of type 'str'"
        self._fault_type = value

    @builtins.property
    def guide(self):
        """Message field 'guide'."""
        return self._guide

    @guide.setter
    def guide(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'guide' field must be of type 'str'"
        self._guide = value
