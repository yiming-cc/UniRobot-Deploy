# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/SetControlMode.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SetControlMode(type):
    """Metaclass of message 'SetControlMode'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'INPUT_VR': 51,
        'INPUT_MOCAP': 52,
        'INPUT_HMI': 53,
        'INPUT_GDK': 54,
        'MODE_STOP': 0,
        'MODE_SERVO': 1,
        'MODE_PLANNING': 2,
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
                'genie_msgs.msg.SetControlMode')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__set_control_mode
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__set_control_mode
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__set_control_mode
            cls._TYPE_SUPPORT = module.type_support_msg__msg__set_control_mode
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__set_control_mode

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'INPUT_VR': cls.__constants['INPUT_VR'],
            'INPUT_MOCAP': cls.__constants['INPUT_MOCAP'],
            'INPUT_HMI': cls.__constants['INPUT_HMI'],
            'INPUT_GDK': cls.__constants['INPUT_GDK'],
            'MODE_STOP': cls.__constants['MODE_STOP'],
            'MODE_SERVO': cls.__constants['MODE_SERVO'],
            'MODE_PLANNING': cls.__constants['MODE_PLANNING'],
        }

    @property
    def INPUT_VR(self):
        """Message constant 'INPUT_VR'."""
        return Metaclass_SetControlMode.__constants['INPUT_VR']

    @property
    def INPUT_MOCAP(self):
        """Message constant 'INPUT_MOCAP'."""
        return Metaclass_SetControlMode.__constants['INPUT_MOCAP']

    @property
    def INPUT_HMI(self):
        """Message constant 'INPUT_HMI'."""
        return Metaclass_SetControlMode.__constants['INPUT_HMI']

    @property
    def INPUT_GDK(self):
        """Message constant 'INPUT_GDK'."""
        return Metaclass_SetControlMode.__constants['INPUT_GDK']

    @property
    def MODE_STOP(self):
        """Message constant 'MODE_STOP'."""
        return Metaclass_SetControlMode.__constants['MODE_STOP']

    @property
    def MODE_SERVO(self):
        """Message constant 'MODE_SERVO'."""
        return Metaclass_SetControlMode.__constants['MODE_SERVO']

    @property
    def MODE_PLANNING(self):
        """Message constant 'MODE_PLANNING'."""
        return Metaclass_SetControlMode.__constants['MODE_PLANNING']


class SetControlMode(metaclass=Metaclass_SetControlMode):
    """
    Message class 'SetControlMode'.

    Constants:
      INPUT_VR
      INPUT_MOCAP
      INPUT_HMI
      INPUT_GDK
      MODE_STOP
      MODE_SERVO
      MODE_PLANNING
    """

    __slots__ = [
        '_header',
        '_input_type',
        '_control_mode',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'input_type': 'uint8',
        'control_mode': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.input_type = kwargs.get('input_type', int())
        self.control_mode = kwargs.get('control_mode', int())

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
        if self.input_type != other.input_type:
            return False
        if self.control_mode != other.control_mode:
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
    def input_type(self):
        """Message field 'input_type'."""
        return self._input_type

    @input_type.setter
    def input_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'input_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'input_type' field must be an unsigned integer in [0, 255]"
        self._input_type = value

    @builtins.property
    def control_mode(self):
        """Message field 'control_mode'."""
        return self._control_mode

    @control_mode.setter
    def control_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'control_mode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'control_mode' field must be an unsigned integer in [0, 255]"
        self._control_mode = value
