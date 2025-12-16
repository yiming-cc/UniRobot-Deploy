# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/WholeBodyStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_WholeBodyStatus(type):
    """Metaclass of message 'WholeBodyStatus'."""

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
                'genie_msgs.msg.WholeBodyStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__whole_body_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__whole_body_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__whole_body_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__whole_body_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__whole_body_status

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


class WholeBodyStatus(metaclass=Metaclass_WholeBodyStatus):
    """Message class 'WholeBodyStatus'."""

    __slots__ = [
        '_header',
        '_right_arm_error',
        '_left_arm_error',
        '_right_arm_control',
        '_left_arm_control',
        '_right_arm_estop',
        '_left_arm_estop',
        '_right_end_error',
        '_left_end_error',
        '_right_end_model',
        '_left_end_model',
        '_waist_error',
        '_lift_error',
        '_neck_error',
        '_chassis_error',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'right_arm_error': 'uint32',
        'left_arm_error': 'uint32',
        'right_arm_control': 'boolean',
        'left_arm_control': 'boolean',
        'right_arm_estop': 'boolean',
        'left_arm_estop': 'boolean',
        'right_end_error': 'uint32',
        'left_end_error': 'uint32',
        'right_end_model': 'string',
        'left_end_model': 'string',
        'waist_error': 'uint32',
        'lift_error': 'uint32',
        'neck_error': 'uint32',
        'chassis_error': 'uint32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.right_arm_error = kwargs.get('right_arm_error', int())
        self.left_arm_error = kwargs.get('left_arm_error', int())
        self.right_arm_control = kwargs.get('right_arm_control', bool())
        self.left_arm_control = kwargs.get('left_arm_control', bool())
        self.right_arm_estop = kwargs.get('right_arm_estop', bool())
        self.left_arm_estop = kwargs.get('left_arm_estop', bool())
        self.right_end_error = kwargs.get('right_end_error', int())
        self.left_end_error = kwargs.get('left_end_error', int())
        self.right_end_model = kwargs.get('right_end_model', str())
        self.left_end_model = kwargs.get('left_end_model', str())
        self.waist_error = kwargs.get('waist_error', int())
        self.lift_error = kwargs.get('lift_error', int())
        self.neck_error = kwargs.get('neck_error', int())
        self.chassis_error = kwargs.get('chassis_error', int())

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
        if self.right_arm_error != other.right_arm_error:
            return False
        if self.left_arm_error != other.left_arm_error:
            return False
        if self.right_arm_control != other.right_arm_control:
            return False
        if self.left_arm_control != other.left_arm_control:
            return False
        if self.right_arm_estop != other.right_arm_estop:
            return False
        if self.left_arm_estop != other.left_arm_estop:
            return False
        if self.right_end_error != other.right_end_error:
            return False
        if self.left_end_error != other.left_end_error:
            return False
        if self.right_end_model != other.right_end_model:
            return False
        if self.left_end_model != other.left_end_model:
            return False
        if self.waist_error != other.waist_error:
            return False
        if self.lift_error != other.lift_error:
            return False
        if self.neck_error != other.neck_error:
            return False
        if self.chassis_error != other.chassis_error:
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
    def right_arm_error(self):
        """Message field 'right_arm_error'."""
        return self._right_arm_error

    @right_arm_error.setter
    def right_arm_error(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'right_arm_error' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'right_arm_error' field must be an unsigned integer in [0, 4294967295]"
        self._right_arm_error = value

    @builtins.property
    def left_arm_error(self):
        """Message field 'left_arm_error'."""
        return self._left_arm_error

    @left_arm_error.setter
    def left_arm_error(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'left_arm_error' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'left_arm_error' field must be an unsigned integer in [0, 4294967295]"
        self._left_arm_error = value

    @builtins.property
    def right_arm_control(self):
        """Message field 'right_arm_control'."""
        return self._right_arm_control

    @right_arm_control.setter
    def right_arm_control(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'right_arm_control' field must be of type 'bool'"
        self._right_arm_control = value

    @builtins.property
    def left_arm_control(self):
        """Message field 'left_arm_control'."""
        return self._left_arm_control

    @left_arm_control.setter
    def left_arm_control(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'left_arm_control' field must be of type 'bool'"
        self._left_arm_control = value

    @builtins.property
    def right_arm_estop(self):
        """Message field 'right_arm_estop'."""
        return self._right_arm_estop

    @right_arm_estop.setter
    def right_arm_estop(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'right_arm_estop' field must be of type 'bool'"
        self._right_arm_estop = value

    @builtins.property
    def left_arm_estop(self):
        """Message field 'left_arm_estop'."""
        return self._left_arm_estop

    @left_arm_estop.setter
    def left_arm_estop(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'left_arm_estop' field must be of type 'bool'"
        self._left_arm_estop = value

    @builtins.property
    def right_end_error(self):
        """Message field 'right_end_error'."""
        return self._right_end_error

    @right_end_error.setter
    def right_end_error(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'right_end_error' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'right_end_error' field must be an unsigned integer in [0, 4294967295]"
        self._right_end_error = value

    @builtins.property
    def left_end_error(self):
        """Message field 'left_end_error'."""
        return self._left_end_error

    @left_end_error.setter
    def left_end_error(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'left_end_error' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'left_end_error' field must be an unsigned integer in [0, 4294967295]"
        self._left_end_error = value

    @builtins.property
    def right_end_model(self):
        """Message field 'right_end_model'."""
        return self._right_end_model

    @right_end_model.setter
    def right_end_model(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'right_end_model' field must be of type 'str'"
        self._right_end_model = value

    @builtins.property
    def left_end_model(self):
        """Message field 'left_end_model'."""
        return self._left_end_model

    @left_end_model.setter
    def left_end_model(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'left_end_model' field must be of type 'str'"
        self._left_end_model = value

    @builtins.property
    def waist_error(self):
        """Message field 'waist_error'."""
        return self._waist_error

    @waist_error.setter
    def waist_error(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'waist_error' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'waist_error' field must be an unsigned integer in [0, 4294967295]"
        self._waist_error = value

    @builtins.property
    def lift_error(self):
        """Message field 'lift_error'."""
        return self._lift_error

    @lift_error.setter
    def lift_error(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'lift_error' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'lift_error' field must be an unsigned integer in [0, 4294967295]"
        self._lift_error = value

    @builtins.property
    def neck_error(self):
        """Message field 'neck_error'."""
        return self._neck_error

    @neck_error.setter
    def neck_error(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'neck_error' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'neck_error' field must be an unsigned integer in [0, 4294967295]"
        self._neck_error = value

    @builtins.property
    def chassis_error(self):
        """Message field 'chassis_error'."""
        return self._chassis_error

    @chassis_error.setter
    def chassis_error(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'chassis_error' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'chassis_error' field must be an unsigned integer in [0, 4294967295]"
        self._chassis_error = value
