# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/PeriCmd.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_PeriCmd(type):
    """Metaclass of message 'PeriCmd'."""

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
                'genie_msgs.msg.PeriCmd')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__peri_cmd
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__peri_cmd
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__peri_cmd
            cls._TYPE_SUPPORT = module.type_support_msg__msg__peri_cmd
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__peri_cmd

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


class PeriCmd(metaclass=Metaclass_PeriCmd):
    """Message class 'PeriCmd'."""

    __slots__ = [
        '_header',
        '_compute_center_ready_shut_down',
        '_soft_emergency_stop',
        '_hub1_reset_request',
        '_hub2_reset_request',
        '_left_arm_reset_request',
        '_right_arm_reset_request',
        '_left_end_reset_request',
        '_right_end_reset_request',
        '_waist_pitch_motor_reset_request',
        '_lift_motor_reset_request',
        '_head_yaw_motor_reset_request',
        '_head_pitch_motor_reset_request',
        '_agv_reset_request',
        '_work_mode',
        '_feature_status',
        '_left_arm_power_ctrl_req',
        '_right_arm_power_ctrl_req',
        '_left_end_power_ctrl_req',
        '_right_end_power_ctrl_req',
        '_waist_pitch_motor_power_ctrl_req',
        '_lift_motor_power_ctrl_req',
        '_head_yaw_motor_power_ctrl_req',
        '_head_pitch_motor_power_ctrl_req',
        '_agv_power_ctrl_req',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'compute_center_ready_shut_down': 'uint8',
        'soft_emergency_stop': 'uint8',
        'hub1_reset_request': 'uint8',
        'hub2_reset_request': 'uint8',
        'left_arm_reset_request': 'uint8',
        'right_arm_reset_request': 'uint8',
        'left_end_reset_request': 'uint8',
        'right_end_reset_request': 'uint8',
        'waist_pitch_motor_reset_request': 'uint8',
        'lift_motor_reset_request': 'uint8',
        'head_yaw_motor_reset_request': 'uint8',
        'head_pitch_motor_reset_request': 'uint8',
        'agv_reset_request': 'uint8',
        'work_mode': 'uint8',
        'feature_status': 'uint8',
        'left_arm_power_ctrl_req': 'uint8',
        'right_arm_power_ctrl_req': 'uint8',
        'left_end_power_ctrl_req': 'uint8',
        'right_end_power_ctrl_req': 'uint8',
        'waist_pitch_motor_power_ctrl_req': 'uint8',
        'lift_motor_power_ctrl_req': 'uint8',
        'head_yaw_motor_power_ctrl_req': 'uint8',
        'head_pitch_motor_power_ctrl_req': 'uint8',
        'agv_power_ctrl_req': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.compute_center_ready_shut_down = kwargs.get('compute_center_ready_shut_down', int())
        self.soft_emergency_stop = kwargs.get('soft_emergency_stop', int())
        self.hub1_reset_request = kwargs.get('hub1_reset_request', int())
        self.hub2_reset_request = kwargs.get('hub2_reset_request', int())
        self.left_arm_reset_request = kwargs.get('left_arm_reset_request', int())
        self.right_arm_reset_request = kwargs.get('right_arm_reset_request', int())
        self.left_end_reset_request = kwargs.get('left_end_reset_request', int())
        self.right_end_reset_request = kwargs.get('right_end_reset_request', int())
        self.waist_pitch_motor_reset_request = kwargs.get('waist_pitch_motor_reset_request', int())
        self.lift_motor_reset_request = kwargs.get('lift_motor_reset_request', int())
        self.head_yaw_motor_reset_request = kwargs.get('head_yaw_motor_reset_request', int())
        self.head_pitch_motor_reset_request = kwargs.get('head_pitch_motor_reset_request', int())
        self.agv_reset_request = kwargs.get('agv_reset_request', int())
        self.work_mode = kwargs.get('work_mode', int())
        self.feature_status = kwargs.get('feature_status', int())
        self.left_arm_power_ctrl_req = kwargs.get('left_arm_power_ctrl_req', int())
        self.right_arm_power_ctrl_req = kwargs.get('right_arm_power_ctrl_req', int())
        self.left_end_power_ctrl_req = kwargs.get('left_end_power_ctrl_req', int())
        self.right_end_power_ctrl_req = kwargs.get('right_end_power_ctrl_req', int())
        self.waist_pitch_motor_power_ctrl_req = kwargs.get('waist_pitch_motor_power_ctrl_req', int())
        self.lift_motor_power_ctrl_req = kwargs.get('lift_motor_power_ctrl_req', int())
        self.head_yaw_motor_power_ctrl_req = kwargs.get('head_yaw_motor_power_ctrl_req', int())
        self.head_pitch_motor_power_ctrl_req = kwargs.get('head_pitch_motor_power_ctrl_req', int())
        self.agv_power_ctrl_req = kwargs.get('agv_power_ctrl_req', int())

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
        if self.compute_center_ready_shut_down != other.compute_center_ready_shut_down:
            return False
        if self.soft_emergency_stop != other.soft_emergency_stop:
            return False
        if self.hub1_reset_request != other.hub1_reset_request:
            return False
        if self.hub2_reset_request != other.hub2_reset_request:
            return False
        if self.left_arm_reset_request != other.left_arm_reset_request:
            return False
        if self.right_arm_reset_request != other.right_arm_reset_request:
            return False
        if self.left_end_reset_request != other.left_end_reset_request:
            return False
        if self.right_end_reset_request != other.right_end_reset_request:
            return False
        if self.waist_pitch_motor_reset_request != other.waist_pitch_motor_reset_request:
            return False
        if self.lift_motor_reset_request != other.lift_motor_reset_request:
            return False
        if self.head_yaw_motor_reset_request != other.head_yaw_motor_reset_request:
            return False
        if self.head_pitch_motor_reset_request != other.head_pitch_motor_reset_request:
            return False
        if self.agv_reset_request != other.agv_reset_request:
            return False
        if self.work_mode != other.work_mode:
            return False
        if self.feature_status != other.feature_status:
            return False
        if self.left_arm_power_ctrl_req != other.left_arm_power_ctrl_req:
            return False
        if self.right_arm_power_ctrl_req != other.right_arm_power_ctrl_req:
            return False
        if self.left_end_power_ctrl_req != other.left_end_power_ctrl_req:
            return False
        if self.right_end_power_ctrl_req != other.right_end_power_ctrl_req:
            return False
        if self.waist_pitch_motor_power_ctrl_req != other.waist_pitch_motor_power_ctrl_req:
            return False
        if self.lift_motor_power_ctrl_req != other.lift_motor_power_ctrl_req:
            return False
        if self.head_yaw_motor_power_ctrl_req != other.head_yaw_motor_power_ctrl_req:
            return False
        if self.head_pitch_motor_power_ctrl_req != other.head_pitch_motor_power_ctrl_req:
            return False
        if self.agv_power_ctrl_req != other.agv_power_ctrl_req:
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
    def compute_center_ready_shut_down(self):
        """Message field 'compute_center_ready_shut_down'."""
        return self._compute_center_ready_shut_down

    @compute_center_ready_shut_down.setter
    def compute_center_ready_shut_down(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'compute_center_ready_shut_down' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'compute_center_ready_shut_down' field must be an unsigned integer in [0, 255]"
        self._compute_center_ready_shut_down = value

    @builtins.property
    def soft_emergency_stop(self):
        """Message field 'soft_emergency_stop'."""
        return self._soft_emergency_stop

    @soft_emergency_stop.setter
    def soft_emergency_stop(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'soft_emergency_stop' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'soft_emergency_stop' field must be an unsigned integer in [0, 255]"
        self._soft_emergency_stop = value

    @builtins.property
    def hub1_reset_request(self):
        """Message field 'hub1_reset_request'."""
        return self._hub1_reset_request

    @hub1_reset_request.setter
    def hub1_reset_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'hub1_reset_request' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'hub1_reset_request' field must be an unsigned integer in [0, 255]"
        self._hub1_reset_request = value

    @builtins.property
    def hub2_reset_request(self):
        """Message field 'hub2_reset_request'."""
        return self._hub2_reset_request

    @hub2_reset_request.setter
    def hub2_reset_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'hub2_reset_request' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'hub2_reset_request' field must be an unsigned integer in [0, 255]"
        self._hub2_reset_request = value

    @builtins.property
    def left_arm_reset_request(self):
        """Message field 'left_arm_reset_request'."""
        return self._left_arm_reset_request

    @left_arm_reset_request.setter
    def left_arm_reset_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'left_arm_reset_request' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'left_arm_reset_request' field must be an unsigned integer in [0, 255]"
        self._left_arm_reset_request = value

    @builtins.property
    def right_arm_reset_request(self):
        """Message field 'right_arm_reset_request'."""
        return self._right_arm_reset_request

    @right_arm_reset_request.setter
    def right_arm_reset_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'right_arm_reset_request' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'right_arm_reset_request' field must be an unsigned integer in [0, 255]"
        self._right_arm_reset_request = value

    @builtins.property
    def left_end_reset_request(self):
        """Message field 'left_end_reset_request'."""
        return self._left_end_reset_request

    @left_end_reset_request.setter
    def left_end_reset_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'left_end_reset_request' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'left_end_reset_request' field must be an unsigned integer in [0, 255]"
        self._left_end_reset_request = value

    @builtins.property
    def right_end_reset_request(self):
        """Message field 'right_end_reset_request'."""
        return self._right_end_reset_request

    @right_end_reset_request.setter
    def right_end_reset_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'right_end_reset_request' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'right_end_reset_request' field must be an unsigned integer in [0, 255]"
        self._right_end_reset_request = value

    @builtins.property
    def waist_pitch_motor_reset_request(self):
        """Message field 'waist_pitch_motor_reset_request'."""
        return self._waist_pitch_motor_reset_request

    @waist_pitch_motor_reset_request.setter
    def waist_pitch_motor_reset_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'waist_pitch_motor_reset_request' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'waist_pitch_motor_reset_request' field must be an unsigned integer in [0, 255]"
        self._waist_pitch_motor_reset_request = value

    @builtins.property
    def lift_motor_reset_request(self):
        """Message field 'lift_motor_reset_request'."""
        return self._lift_motor_reset_request

    @lift_motor_reset_request.setter
    def lift_motor_reset_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'lift_motor_reset_request' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'lift_motor_reset_request' field must be an unsigned integer in [0, 255]"
        self._lift_motor_reset_request = value

    @builtins.property
    def head_yaw_motor_reset_request(self):
        """Message field 'head_yaw_motor_reset_request'."""
        return self._head_yaw_motor_reset_request

    @head_yaw_motor_reset_request.setter
    def head_yaw_motor_reset_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'head_yaw_motor_reset_request' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'head_yaw_motor_reset_request' field must be an unsigned integer in [0, 255]"
        self._head_yaw_motor_reset_request = value

    @builtins.property
    def head_pitch_motor_reset_request(self):
        """Message field 'head_pitch_motor_reset_request'."""
        return self._head_pitch_motor_reset_request

    @head_pitch_motor_reset_request.setter
    def head_pitch_motor_reset_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'head_pitch_motor_reset_request' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'head_pitch_motor_reset_request' field must be an unsigned integer in [0, 255]"
        self._head_pitch_motor_reset_request = value

    @builtins.property
    def agv_reset_request(self):
        """Message field 'agv_reset_request'."""
        return self._agv_reset_request

    @agv_reset_request.setter
    def agv_reset_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'agv_reset_request' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'agv_reset_request' field must be an unsigned integer in [0, 255]"
        self._agv_reset_request = value

    @builtins.property
    def work_mode(self):
        """Message field 'work_mode'."""
        return self._work_mode

    @work_mode.setter
    def work_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'work_mode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'work_mode' field must be an unsigned integer in [0, 255]"
        self._work_mode = value

    @builtins.property
    def feature_status(self):
        """Message field 'feature_status'."""
        return self._feature_status

    @feature_status.setter
    def feature_status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'feature_status' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'feature_status' field must be an unsigned integer in [0, 255]"
        self._feature_status = value

    @builtins.property
    def left_arm_power_ctrl_req(self):
        """Message field 'left_arm_power_ctrl_req'."""
        return self._left_arm_power_ctrl_req

    @left_arm_power_ctrl_req.setter
    def left_arm_power_ctrl_req(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'left_arm_power_ctrl_req' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'left_arm_power_ctrl_req' field must be an unsigned integer in [0, 255]"
        self._left_arm_power_ctrl_req = value

    @builtins.property
    def right_arm_power_ctrl_req(self):
        """Message field 'right_arm_power_ctrl_req'."""
        return self._right_arm_power_ctrl_req

    @right_arm_power_ctrl_req.setter
    def right_arm_power_ctrl_req(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'right_arm_power_ctrl_req' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'right_arm_power_ctrl_req' field must be an unsigned integer in [0, 255]"
        self._right_arm_power_ctrl_req = value

    @builtins.property
    def left_end_power_ctrl_req(self):
        """Message field 'left_end_power_ctrl_req'."""
        return self._left_end_power_ctrl_req

    @left_end_power_ctrl_req.setter
    def left_end_power_ctrl_req(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'left_end_power_ctrl_req' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'left_end_power_ctrl_req' field must be an unsigned integer in [0, 255]"
        self._left_end_power_ctrl_req = value

    @builtins.property
    def right_end_power_ctrl_req(self):
        """Message field 'right_end_power_ctrl_req'."""
        return self._right_end_power_ctrl_req

    @right_end_power_ctrl_req.setter
    def right_end_power_ctrl_req(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'right_end_power_ctrl_req' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'right_end_power_ctrl_req' field must be an unsigned integer in [0, 255]"
        self._right_end_power_ctrl_req = value

    @builtins.property
    def waist_pitch_motor_power_ctrl_req(self):
        """Message field 'waist_pitch_motor_power_ctrl_req'."""
        return self._waist_pitch_motor_power_ctrl_req

    @waist_pitch_motor_power_ctrl_req.setter
    def waist_pitch_motor_power_ctrl_req(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'waist_pitch_motor_power_ctrl_req' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'waist_pitch_motor_power_ctrl_req' field must be an unsigned integer in [0, 255]"
        self._waist_pitch_motor_power_ctrl_req = value

    @builtins.property
    def lift_motor_power_ctrl_req(self):
        """Message field 'lift_motor_power_ctrl_req'."""
        return self._lift_motor_power_ctrl_req

    @lift_motor_power_ctrl_req.setter
    def lift_motor_power_ctrl_req(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'lift_motor_power_ctrl_req' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'lift_motor_power_ctrl_req' field must be an unsigned integer in [0, 255]"
        self._lift_motor_power_ctrl_req = value

    @builtins.property
    def head_yaw_motor_power_ctrl_req(self):
        """Message field 'head_yaw_motor_power_ctrl_req'."""
        return self._head_yaw_motor_power_ctrl_req

    @head_yaw_motor_power_ctrl_req.setter
    def head_yaw_motor_power_ctrl_req(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'head_yaw_motor_power_ctrl_req' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'head_yaw_motor_power_ctrl_req' field must be an unsigned integer in [0, 255]"
        self._head_yaw_motor_power_ctrl_req = value

    @builtins.property
    def head_pitch_motor_power_ctrl_req(self):
        """Message field 'head_pitch_motor_power_ctrl_req'."""
        return self._head_pitch_motor_power_ctrl_req

    @head_pitch_motor_power_ctrl_req.setter
    def head_pitch_motor_power_ctrl_req(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'head_pitch_motor_power_ctrl_req' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'head_pitch_motor_power_ctrl_req' field must be an unsigned integer in [0, 255]"
        self._head_pitch_motor_power_ctrl_req = value

    @builtins.property
    def agv_power_ctrl_req(self):
        """Message field 'agv_power_ctrl_req'."""
        return self._agv_power_ctrl_req

    @agv_power_ctrl_req.setter
    def agv_power_ctrl_req(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'agv_power_ctrl_req' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'agv_power_ctrl_req' field must be an unsigned integer in [0, 255]"
        self._agv_power_ctrl_req = value
