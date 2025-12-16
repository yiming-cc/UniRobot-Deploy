# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/VRControllerAction.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_VRControllerAction(type):
    """Metaclass of message 'VRControllerAction'."""

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
                'genie_msgs.msg.VRControllerAction')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__vr_controller_action
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__vr_controller_action
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__vr_controller_action
            cls._TYPE_SUPPORT = module.type_support_msg__msg__vr_controller_action
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__vr_controller_action

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


class VRControllerAction(metaclass=Metaclass_VRControllerAction):
    """Message class 'VRControllerAction'."""

    __slots__ = [
        '_header',
        '_left_amplitude',
        '_right_amplitude',
        '_left_duration_ms',
        '_right_duration_ms',
        '_left_frequency_hz',
        '_right_frequency_hz',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'left_amplitude': 'float',
        'right_amplitude': 'float',
        'left_duration_ms': 'int32',
        'right_duration_ms': 'int32',
        'left_frequency_hz': 'int32',
        'right_frequency_hz': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.left_amplitude = kwargs.get('left_amplitude', float())
        self.right_amplitude = kwargs.get('right_amplitude', float())
        self.left_duration_ms = kwargs.get('left_duration_ms', int())
        self.right_duration_ms = kwargs.get('right_duration_ms', int())
        self.left_frequency_hz = kwargs.get('left_frequency_hz', int())
        self.right_frequency_hz = kwargs.get('right_frequency_hz', int())

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
        if self.left_amplitude != other.left_amplitude:
            return False
        if self.right_amplitude != other.right_amplitude:
            return False
        if self.left_duration_ms != other.left_duration_ms:
            return False
        if self.right_duration_ms != other.right_duration_ms:
            return False
        if self.left_frequency_hz != other.left_frequency_hz:
            return False
        if self.right_frequency_hz != other.right_frequency_hz:
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
    def left_amplitude(self):
        """Message field 'left_amplitude'."""
        return self._left_amplitude

    @left_amplitude.setter
    def left_amplitude(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'left_amplitude' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'left_amplitude' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._left_amplitude = value

    @builtins.property
    def right_amplitude(self):
        """Message field 'right_amplitude'."""
        return self._right_amplitude

    @right_amplitude.setter
    def right_amplitude(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'right_amplitude' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'right_amplitude' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._right_amplitude = value

    @builtins.property
    def left_duration_ms(self):
        """Message field 'left_duration_ms'."""
        return self._left_duration_ms

    @left_duration_ms.setter
    def left_duration_ms(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'left_duration_ms' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'left_duration_ms' field must be an integer in [-2147483648, 2147483647]"
        self._left_duration_ms = value

    @builtins.property
    def right_duration_ms(self):
        """Message field 'right_duration_ms'."""
        return self._right_duration_ms

    @right_duration_ms.setter
    def right_duration_ms(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'right_duration_ms' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'right_duration_ms' field must be an integer in [-2147483648, 2147483647]"
        self._right_duration_ms = value

    @builtins.property
    def left_frequency_hz(self):
        """Message field 'left_frequency_hz'."""
        return self._left_frequency_hz

    @left_frequency_hz.setter
    def left_frequency_hz(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'left_frequency_hz' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'left_frequency_hz' field must be an integer in [-2147483648, 2147483647]"
        self._left_frequency_hz = value

    @builtins.property
    def right_frequency_hz(self):
        """Message field 'right_frequency_hz'."""
        return self._right_frequency_hz

    @right_frequency_hz.setter
    def right_frequency_hz(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'right_frequency_hz' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'right_frequency_hz' field must be an integer in [-2147483648, 2147483647]"
        self._right_frequency_hz = value
