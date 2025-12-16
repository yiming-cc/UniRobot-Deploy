# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/PeriStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_PeriStatus(type):
    """Metaclass of message 'PeriStatus'."""

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
                'genie_msgs.msg.PeriStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__peri_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__peri_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__peri_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__peri_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__peri_status

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


class PeriStatus(metaclass=Metaclass_PeriStatus):
    """Message class 'PeriStatus'."""

    __slots__ = [
        '_header',
        '_shut_down_compute_center_request',
        '_soft_emergency_stop_feedback',
        '_pedal_emergency_stop',
        '_button_emergency_stop',
        '_hub1_reset_request_feedback',
        '_hub2_reset_request_feedback',
        '_left_arm_reset_request_feedback',
        '_right_arm_reset_request_feedback',
        '_left_end_reset_request_feedback',
        '_right_end_reset_request_feedback',
        '_waist_pitch_motor_reset_request_feedback',
        '_lift_motor_reset_request_feedback',
        '_head_yaw_motor_reset_request_feedback',
        '_head_pitch_motor_reset_request_feedback',
        '_agv_reset_request_feedback',
        '_power_pcb_work_mode',
        '_feature_status',
        '_left_arm_power_ctrl_req_feedback',
        '_right_arm_power_ctrl_req_feedback',
        '_left_end_power_ctrl_req_feedback',
        '_right_end_power_ctrl_req_feedback',
        '_waist_pitch_motor_power_ctrl_req_feedback',
        '_lift_motor_power_ctrl_req_feedback',
        '_head_yaw_motor_power_ctrl_req_feedback',
        '_head_pitch_motor_power_ctrl_req_feedback',
        '_agv_power_ctrl_req_feedback',
        '_power_ctrl_req_failreason',
        '_left_end_current',
        '_right_end_current',
        '_waist_pitch_motor_current',
        '_lift_motor_current',
        '_head_yaw_motor_current',
        '_head_pitch_motor_current',
        '_agv_current',
        '_left_end_voltage',
        '_right_end_voltage',
        '_waist_pitch_motor_voltage',
        '_lift_motor_voltage',
        '_head_yaw_motor_voltage',
        '_head_pitch_motor_voltage',
        '_agv_voltage',
        '_emergency_stop_err_fedback',
        '_power_board_software_version',
        '_power_board_hardware_version',
        '_power_board_serial_number',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'shut_down_compute_center_request': 'uint8',
        'soft_emergency_stop_feedback': 'uint8',
        'pedal_emergency_stop': 'uint8',
        'button_emergency_stop': 'uint8',
        'hub1_reset_request_feedback': 'uint8',
        'hub2_reset_request_feedback': 'uint8',
        'left_arm_reset_request_feedback': 'uint8',
        'right_arm_reset_request_feedback': 'uint8',
        'left_end_reset_request_feedback': 'uint8',
        'right_end_reset_request_feedback': 'uint8',
        'waist_pitch_motor_reset_request_feedback': 'uint8',
        'lift_motor_reset_request_feedback': 'uint8',
        'head_yaw_motor_reset_request_feedback': 'uint8',
        'head_pitch_motor_reset_request_feedback': 'uint8',
        'agv_reset_request_feedback': 'uint8',
        'power_pcb_work_mode': 'uint8',
        'feature_status': 'uint8',
        'left_arm_power_ctrl_req_feedback': 'uint8',
        'right_arm_power_ctrl_req_feedback': 'uint8',
        'left_end_power_ctrl_req_feedback': 'uint8',
        'right_end_power_ctrl_req_feedback': 'uint8',
        'waist_pitch_motor_power_ctrl_req_feedback': 'uint8',
        'lift_motor_power_ctrl_req_feedback': 'uint8',
        'head_yaw_motor_power_ctrl_req_feedback': 'uint8',
        'head_pitch_motor_power_ctrl_req_feedback': 'uint8',
        'agv_power_ctrl_req_feedback': 'uint8',
        'power_ctrl_req_failreason': 'uint8',
        'left_end_current': 'float',
        'right_end_current': 'float',
        'waist_pitch_motor_current': 'float',
        'lift_motor_current': 'float',
        'head_yaw_motor_current': 'float',
        'head_pitch_motor_current': 'float',
        'agv_current': 'float',
        'left_end_voltage': 'float',
        'right_end_voltage': 'float',
        'waist_pitch_motor_voltage': 'float',
        'lift_motor_voltage': 'float',
        'head_yaw_motor_voltage': 'float',
        'head_pitch_motor_voltage': 'float',
        'agv_voltage': 'float',
        'emergency_stop_err_fedback': 'uint8',
        'power_board_software_version': 'string',
        'power_board_hardware_version': 'string',
        'power_board_serial_number': 'string',
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
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.shut_down_compute_center_request = kwargs.get('shut_down_compute_center_request', int())
        self.soft_emergency_stop_feedback = kwargs.get('soft_emergency_stop_feedback', int())
        self.pedal_emergency_stop = kwargs.get('pedal_emergency_stop', int())
        self.button_emergency_stop = kwargs.get('button_emergency_stop', int())
        self.hub1_reset_request_feedback = kwargs.get('hub1_reset_request_feedback', int())
        self.hub2_reset_request_feedback = kwargs.get('hub2_reset_request_feedback', int())
        self.left_arm_reset_request_feedback = kwargs.get('left_arm_reset_request_feedback', int())
        self.right_arm_reset_request_feedback = kwargs.get('right_arm_reset_request_feedback', int())
        self.left_end_reset_request_feedback = kwargs.get('left_end_reset_request_feedback', int())
        self.right_end_reset_request_feedback = kwargs.get('right_end_reset_request_feedback', int())
        self.waist_pitch_motor_reset_request_feedback = kwargs.get('waist_pitch_motor_reset_request_feedback', int())
        self.lift_motor_reset_request_feedback = kwargs.get('lift_motor_reset_request_feedback', int())
        self.head_yaw_motor_reset_request_feedback = kwargs.get('head_yaw_motor_reset_request_feedback', int())
        self.head_pitch_motor_reset_request_feedback = kwargs.get('head_pitch_motor_reset_request_feedback', int())
        self.agv_reset_request_feedback = kwargs.get('agv_reset_request_feedback', int())
        self.power_pcb_work_mode = kwargs.get('power_pcb_work_mode', int())
        self.feature_status = kwargs.get('feature_status', int())
        self.left_arm_power_ctrl_req_feedback = kwargs.get('left_arm_power_ctrl_req_feedback', int())
        self.right_arm_power_ctrl_req_feedback = kwargs.get('right_arm_power_ctrl_req_feedback', int())
        self.left_end_power_ctrl_req_feedback = kwargs.get('left_end_power_ctrl_req_feedback', int())
        self.right_end_power_ctrl_req_feedback = kwargs.get('right_end_power_ctrl_req_feedback', int())
        self.waist_pitch_motor_power_ctrl_req_feedback = kwargs.get('waist_pitch_motor_power_ctrl_req_feedback', int())
        self.lift_motor_power_ctrl_req_feedback = kwargs.get('lift_motor_power_ctrl_req_feedback', int())
        self.head_yaw_motor_power_ctrl_req_feedback = kwargs.get('head_yaw_motor_power_ctrl_req_feedback', int())
        self.head_pitch_motor_power_ctrl_req_feedback = kwargs.get('head_pitch_motor_power_ctrl_req_feedback', int())
        self.agv_power_ctrl_req_feedback = kwargs.get('agv_power_ctrl_req_feedback', int())
        self.power_ctrl_req_failreason = kwargs.get('power_ctrl_req_failreason', int())
        self.left_end_current = kwargs.get('left_end_current', float())
        self.right_end_current = kwargs.get('right_end_current', float())
        self.waist_pitch_motor_current = kwargs.get('waist_pitch_motor_current', float())
        self.lift_motor_current = kwargs.get('lift_motor_current', float())
        self.head_yaw_motor_current = kwargs.get('head_yaw_motor_current', float())
        self.head_pitch_motor_current = kwargs.get('head_pitch_motor_current', float())
        self.agv_current = kwargs.get('agv_current', float())
        self.left_end_voltage = kwargs.get('left_end_voltage', float())
        self.right_end_voltage = kwargs.get('right_end_voltage', float())
        self.waist_pitch_motor_voltage = kwargs.get('waist_pitch_motor_voltage', float())
        self.lift_motor_voltage = kwargs.get('lift_motor_voltage', float())
        self.head_yaw_motor_voltage = kwargs.get('head_yaw_motor_voltage', float())
        self.head_pitch_motor_voltage = kwargs.get('head_pitch_motor_voltage', float())
        self.agv_voltage = kwargs.get('agv_voltage', float())
        self.emergency_stop_err_fedback = kwargs.get('emergency_stop_err_fedback', int())
        self.power_board_software_version = kwargs.get('power_board_software_version', str())
        self.power_board_hardware_version = kwargs.get('power_board_hardware_version', str())
        self.power_board_serial_number = kwargs.get('power_board_serial_number', str())

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
        if self.shut_down_compute_center_request != other.shut_down_compute_center_request:
            return False
        if self.soft_emergency_stop_feedback != other.soft_emergency_stop_feedback:
            return False
        if self.pedal_emergency_stop != other.pedal_emergency_stop:
            return False
        if self.button_emergency_stop != other.button_emergency_stop:
            return False
        if self.hub1_reset_request_feedback != other.hub1_reset_request_feedback:
            return False
        if self.hub2_reset_request_feedback != other.hub2_reset_request_feedback:
            return False
        if self.left_arm_reset_request_feedback != other.left_arm_reset_request_feedback:
            return False
        if self.right_arm_reset_request_feedback != other.right_arm_reset_request_feedback:
            return False
        if self.left_end_reset_request_feedback != other.left_end_reset_request_feedback:
            return False
        if self.right_end_reset_request_feedback != other.right_end_reset_request_feedback:
            return False
        if self.waist_pitch_motor_reset_request_feedback != other.waist_pitch_motor_reset_request_feedback:
            return False
        if self.lift_motor_reset_request_feedback != other.lift_motor_reset_request_feedback:
            return False
        if self.head_yaw_motor_reset_request_feedback != other.head_yaw_motor_reset_request_feedback:
            return False
        if self.head_pitch_motor_reset_request_feedback != other.head_pitch_motor_reset_request_feedback:
            return False
        if self.agv_reset_request_feedback != other.agv_reset_request_feedback:
            return False
        if self.power_pcb_work_mode != other.power_pcb_work_mode:
            return False
        if self.feature_status != other.feature_status:
            return False
        if self.left_arm_power_ctrl_req_feedback != other.left_arm_power_ctrl_req_feedback:
            return False
        if self.right_arm_power_ctrl_req_feedback != other.right_arm_power_ctrl_req_feedback:
            return False
        if self.left_end_power_ctrl_req_feedback != other.left_end_power_ctrl_req_feedback:
            return False
        if self.right_end_power_ctrl_req_feedback != other.right_end_power_ctrl_req_feedback:
            return False
        if self.waist_pitch_motor_power_ctrl_req_feedback != other.waist_pitch_motor_power_ctrl_req_feedback:
            return False
        if self.lift_motor_power_ctrl_req_feedback != other.lift_motor_power_ctrl_req_feedback:
            return False
        if self.head_yaw_motor_power_ctrl_req_feedback != other.head_yaw_motor_power_ctrl_req_feedback:
            return False
        if self.head_pitch_motor_power_ctrl_req_feedback != other.head_pitch_motor_power_ctrl_req_feedback:
            return False
        if self.agv_power_ctrl_req_feedback != other.agv_power_ctrl_req_feedback:
            return False
        if self.power_ctrl_req_failreason != other.power_ctrl_req_failreason:
            return False
        if self.left_end_current != other.left_end_current:
            return False
        if self.right_end_current != other.right_end_current:
            return False
        if self.waist_pitch_motor_current != other.waist_pitch_motor_current:
            return False
        if self.lift_motor_current != other.lift_motor_current:
            return False
        if self.head_yaw_motor_current != other.head_yaw_motor_current:
            return False
        if self.head_pitch_motor_current != other.head_pitch_motor_current:
            return False
        if self.agv_current != other.agv_current:
            return False
        if self.left_end_voltage != other.left_end_voltage:
            return False
        if self.right_end_voltage != other.right_end_voltage:
            return False
        if self.waist_pitch_motor_voltage != other.waist_pitch_motor_voltage:
            return False
        if self.lift_motor_voltage != other.lift_motor_voltage:
            return False
        if self.head_yaw_motor_voltage != other.head_yaw_motor_voltage:
            return False
        if self.head_pitch_motor_voltage != other.head_pitch_motor_voltage:
            return False
        if self.agv_voltage != other.agv_voltage:
            return False
        if self.emergency_stop_err_fedback != other.emergency_stop_err_fedback:
            return False
        if self.power_board_software_version != other.power_board_software_version:
            return False
        if self.power_board_hardware_version != other.power_board_hardware_version:
            return False
        if self.power_board_serial_number != other.power_board_serial_number:
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
    def shut_down_compute_center_request(self):
        """Message field 'shut_down_compute_center_request'."""
        return self._shut_down_compute_center_request

    @shut_down_compute_center_request.setter
    def shut_down_compute_center_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'shut_down_compute_center_request' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'shut_down_compute_center_request' field must be an unsigned integer in [0, 255]"
        self._shut_down_compute_center_request = value

    @builtins.property
    def soft_emergency_stop_feedback(self):
        """Message field 'soft_emergency_stop_feedback'."""
        return self._soft_emergency_stop_feedback

    @soft_emergency_stop_feedback.setter
    def soft_emergency_stop_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'soft_emergency_stop_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'soft_emergency_stop_feedback' field must be an unsigned integer in [0, 255]"
        self._soft_emergency_stop_feedback = value

    @builtins.property
    def pedal_emergency_stop(self):
        """Message field 'pedal_emergency_stop'."""
        return self._pedal_emergency_stop

    @pedal_emergency_stop.setter
    def pedal_emergency_stop(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'pedal_emergency_stop' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'pedal_emergency_stop' field must be an unsigned integer in [0, 255]"
        self._pedal_emergency_stop = value

    @builtins.property
    def button_emergency_stop(self):
        """Message field 'button_emergency_stop'."""
        return self._button_emergency_stop

    @button_emergency_stop.setter
    def button_emergency_stop(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'button_emergency_stop' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'button_emergency_stop' field must be an unsigned integer in [0, 255]"
        self._button_emergency_stop = value

    @builtins.property
    def hub1_reset_request_feedback(self):
        """Message field 'hub1_reset_request_feedback'."""
        return self._hub1_reset_request_feedback

    @hub1_reset_request_feedback.setter
    def hub1_reset_request_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'hub1_reset_request_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'hub1_reset_request_feedback' field must be an unsigned integer in [0, 255]"
        self._hub1_reset_request_feedback = value

    @builtins.property
    def hub2_reset_request_feedback(self):
        """Message field 'hub2_reset_request_feedback'."""
        return self._hub2_reset_request_feedback

    @hub2_reset_request_feedback.setter
    def hub2_reset_request_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'hub2_reset_request_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'hub2_reset_request_feedback' field must be an unsigned integer in [0, 255]"
        self._hub2_reset_request_feedback = value

    @builtins.property
    def left_arm_reset_request_feedback(self):
        """Message field 'left_arm_reset_request_feedback'."""
        return self._left_arm_reset_request_feedback

    @left_arm_reset_request_feedback.setter
    def left_arm_reset_request_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'left_arm_reset_request_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'left_arm_reset_request_feedback' field must be an unsigned integer in [0, 255]"
        self._left_arm_reset_request_feedback = value

    @builtins.property
    def right_arm_reset_request_feedback(self):
        """Message field 'right_arm_reset_request_feedback'."""
        return self._right_arm_reset_request_feedback

    @right_arm_reset_request_feedback.setter
    def right_arm_reset_request_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'right_arm_reset_request_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'right_arm_reset_request_feedback' field must be an unsigned integer in [0, 255]"
        self._right_arm_reset_request_feedback = value

    @builtins.property
    def left_end_reset_request_feedback(self):
        """Message field 'left_end_reset_request_feedback'."""
        return self._left_end_reset_request_feedback

    @left_end_reset_request_feedback.setter
    def left_end_reset_request_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'left_end_reset_request_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'left_end_reset_request_feedback' field must be an unsigned integer in [0, 255]"
        self._left_end_reset_request_feedback = value

    @builtins.property
    def right_end_reset_request_feedback(self):
        """Message field 'right_end_reset_request_feedback'."""
        return self._right_end_reset_request_feedback

    @right_end_reset_request_feedback.setter
    def right_end_reset_request_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'right_end_reset_request_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'right_end_reset_request_feedback' field must be an unsigned integer in [0, 255]"
        self._right_end_reset_request_feedback = value

    @builtins.property
    def waist_pitch_motor_reset_request_feedback(self):
        """Message field 'waist_pitch_motor_reset_request_feedback'."""
        return self._waist_pitch_motor_reset_request_feedback

    @waist_pitch_motor_reset_request_feedback.setter
    def waist_pitch_motor_reset_request_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'waist_pitch_motor_reset_request_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'waist_pitch_motor_reset_request_feedback' field must be an unsigned integer in [0, 255]"
        self._waist_pitch_motor_reset_request_feedback = value

    @builtins.property
    def lift_motor_reset_request_feedback(self):
        """Message field 'lift_motor_reset_request_feedback'."""
        return self._lift_motor_reset_request_feedback

    @lift_motor_reset_request_feedback.setter
    def lift_motor_reset_request_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'lift_motor_reset_request_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'lift_motor_reset_request_feedback' field must be an unsigned integer in [0, 255]"
        self._lift_motor_reset_request_feedback = value

    @builtins.property
    def head_yaw_motor_reset_request_feedback(self):
        """Message field 'head_yaw_motor_reset_request_feedback'."""
        return self._head_yaw_motor_reset_request_feedback

    @head_yaw_motor_reset_request_feedback.setter
    def head_yaw_motor_reset_request_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'head_yaw_motor_reset_request_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'head_yaw_motor_reset_request_feedback' field must be an unsigned integer in [0, 255]"
        self._head_yaw_motor_reset_request_feedback = value

    @builtins.property
    def head_pitch_motor_reset_request_feedback(self):
        """Message field 'head_pitch_motor_reset_request_feedback'."""
        return self._head_pitch_motor_reset_request_feedback

    @head_pitch_motor_reset_request_feedback.setter
    def head_pitch_motor_reset_request_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'head_pitch_motor_reset_request_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'head_pitch_motor_reset_request_feedback' field must be an unsigned integer in [0, 255]"
        self._head_pitch_motor_reset_request_feedback = value

    @builtins.property
    def agv_reset_request_feedback(self):
        """Message field 'agv_reset_request_feedback'."""
        return self._agv_reset_request_feedback

    @agv_reset_request_feedback.setter
    def agv_reset_request_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'agv_reset_request_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'agv_reset_request_feedback' field must be an unsigned integer in [0, 255]"
        self._agv_reset_request_feedback = value

    @builtins.property
    def power_pcb_work_mode(self):
        """Message field 'power_pcb_work_mode'."""
        return self._power_pcb_work_mode

    @power_pcb_work_mode.setter
    def power_pcb_work_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'power_pcb_work_mode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'power_pcb_work_mode' field must be an unsigned integer in [0, 255]"
        self._power_pcb_work_mode = value

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
    def left_arm_power_ctrl_req_feedback(self):
        """Message field 'left_arm_power_ctrl_req_feedback'."""
        return self._left_arm_power_ctrl_req_feedback

    @left_arm_power_ctrl_req_feedback.setter
    def left_arm_power_ctrl_req_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'left_arm_power_ctrl_req_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'left_arm_power_ctrl_req_feedback' field must be an unsigned integer in [0, 255]"
        self._left_arm_power_ctrl_req_feedback = value

    @builtins.property
    def right_arm_power_ctrl_req_feedback(self):
        """Message field 'right_arm_power_ctrl_req_feedback'."""
        return self._right_arm_power_ctrl_req_feedback

    @right_arm_power_ctrl_req_feedback.setter
    def right_arm_power_ctrl_req_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'right_arm_power_ctrl_req_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'right_arm_power_ctrl_req_feedback' field must be an unsigned integer in [0, 255]"
        self._right_arm_power_ctrl_req_feedback = value

    @builtins.property
    def left_end_power_ctrl_req_feedback(self):
        """Message field 'left_end_power_ctrl_req_feedback'."""
        return self._left_end_power_ctrl_req_feedback

    @left_end_power_ctrl_req_feedback.setter
    def left_end_power_ctrl_req_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'left_end_power_ctrl_req_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'left_end_power_ctrl_req_feedback' field must be an unsigned integer in [0, 255]"
        self._left_end_power_ctrl_req_feedback = value

    @builtins.property
    def right_end_power_ctrl_req_feedback(self):
        """Message field 'right_end_power_ctrl_req_feedback'."""
        return self._right_end_power_ctrl_req_feedback

    @right_end_power_ctrl_req_feedback.setter
    def right_end_power_ctrl_req_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'right_end_power_ctrl_req_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'right_end_power_ctrl_req_feedback' field must be an unsigned integer in [0, 255]"
        self._right_end_power_ctrl_req_feedback = value

    @builtins.property
    def waist_pitch_motor_power_ctrl_req_feedback(self):
        """Message field 'waist_pitch_motor_power_ctrl_req_feedback'."""
        return self._waist_pitch_motor_power_ctrl_req_feedback

    @waist_pitch_motor_power_ctrl_req_feedback.setter
    def waist_pitch_motor_power_ctrl_req_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'waist_pitch_motor_power_ctrl_req_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'waist_pitch_motor_power_ctrl_req_feedback' field must be an unsigned integer in [0, 255]"
        self._waist_pitch_motor_power_ctrl_req_feedback = value

    @builtins.property
    def lift_motor_power_ctrl_req_feedback(self):
        """Message field 'lift_motor_power_ctrl_req_feedback'."""
        return self._lift_motor_power_ctrl_req_feedback

    @lift_motor_power_ctrl_req_feedback.setter
    def lift_motor_power_ctrl_req_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'lift_motor_power_ctrl_req_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'lift_motor_power_ctrl_req_feedback' field must be an unsigned integer in [0, 255]"
        self._lift_motor_power_ctrl_req_feedback = value

    @builtins.property
    def head_yaw_motor_power_ctrl_req_feedback(self):
        """Message field 'head_yaw_motor_power_ctrl_req_feedback'."""
        return self._head_yaw_motor_power_ctrl_req_feedback

    @head_yaw_motor_power_ctrl_req_feedback.setter
    def head_yaw_motor_power_ctrl_req_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'head_yaw_motor_power_ctrl_req_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'head_yaw_motor_power_ctrl_req_feedback' field must be an unsigned integer in [0, 255]"
        self._head_yaw_motor_power_ctrl_req_feedback = value

    @builtins.property
    def head_pitch_motor_power_ctrl_req_feedback(self):
        """Message field 'head_pitch_motor_power_ctrl_req_feedback'."""
        return self._head_pitch_motor_power_ctrl_req_feedback

    @head_pitch_motor_power_ctrl_req_feedback.setter
    def head_pitch_motor_power_ctrl_req_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'head_pitch_motor_power_ctrl_req_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'head_pitch_motor_power_ctrl_req_feedback' field must be an unsigned integer in [0, 255]"
        self._head_pitch_motor_power_ctrl_req_feedback = value

    @builtins.property
    def agv_power_ctrl_req_feedback(self):
        """Message field 'agv_power_ctrl_req_feedback'."""
        return self._agv_power_ctrl_req_feedback

    @agv_power_ctrl_req_feedback.setter
    def agv_power_ctrl_req_feedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'agv_power_ctrl_req_feedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'agv_power_ctrl_req_feedback' field must be an unsigned integer in [0, 255]"
        self._agv_power_ctrl_req_feedback = value

    @builtins.property
    def power_ctrl_req_failreason(self):
        """Message field 'power_ctrl_req_failreason'."""
        return self._power_ctrl_req_failreason

    @power_ctrl_req_failreason.setter
    def power_ctrl_req_failreason(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'power_ctrl_req_failreason' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'power_ctrl_req_failreason' field must be an unsigned integer in [0, 255]"
        self._power_ctrl_req_failreason = value

    @builtins.property
    def left_end_current(self):
        """Message field 'left_end_current'."""
        return self._left_end_current

    @left_end_current.setter
    def left_end_current(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'left_end_current' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'left_end_current' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._left_end_current = value

    @builtins.property
    def right_end_current(self):
        """Message field 'right_end_current'."""
        return self._right_end_current

    @right_end_current.setter
    def right_end_current(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'right_end_current' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'right_end_current' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._right_end_current = value

    @builtins.property
    def waist_pitch_motor_current(self):
        """Message field 'waist_pitch_motor_current'."""
        return self._waist_pitch_motor_current

    @waist_pitch_motor_current.setter
    def waist_pitch_motor_current(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'waist_pitch_motor_current' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'waist_pitch_motor_current' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._waist_pitch_motor_current = value

    @builtins.property
    def lift_motor_current(self):
        """Message field 'lift_motor_current'."""
        return self._lift_motor_current

    @lift_motor_current.setter
    def lift_motor_current(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lift_motor_current' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'lift_motor_current' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._lift_motor_current = value

    @builtins.property
    def head_yaw_motor_current(self):
        """Message field 'head_yaw_motor_current'."""
        return self._head_yaw_motor_current

    @head_yaw_motor_current.setter
    def head_yaw_motor_current(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'head_yaw_motor_current' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'head_yaw_motor_current' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._head_yaw_motor_current = value

    @builtins.property
    def head_pitch_motor_current(self):
        """Message field 'head_pitch_motor_current'."""
        return self._head_pitch_motor_current

    @head_pitch_motor_current.setter
    def head_pitch_motor_current(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'head_pitch_motor_current' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'head_pitch_motor_current' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._head_pitch_motor_current = value

    @builtins.property
    def agv_current(self):
        """Message field 'agv_current'."""
        return self._agv_current

    @agv_current.setter
    def agv_current(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'agv_current' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'agv_current' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._agv_current = value

    @builtins.property
    def left_end_voltage(self):
        """Message field 'left_end_voltage'."""
        return self._left_end_voltage

    @left_end_voltage.setter
    def left_end_voltage(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'left_end_voltage' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'left_end_voltage' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._left_end_voltage = value

    @builtins.property
    def right_end_voltage(self):
        """Message field 'right_end_voltage'."""
        return self._right_end_voltage

    @right_end_voltage.setter
    def right_end_voltage(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'right_end_voltage' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'right_end_voltage' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._right_end_voltage = value

    @builtins.property
    def waist_pitch_motor_voltage(self):
        """Message field 'waist_pitch_motor_voltage'."""
        return self._waist_pitch_motor_voltage

    @waist_pitch_motor_voltage.setter
    def waist_pitch_motor_voltage(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'waist_pitch_motor_voltage' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'waist_pitch_motor_voltage' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._waist_pitch_motor_voltage = value

    @builtins.property
    def lift_motor_voltage(self):
        """Message field 'lift_motor_voltage'."""
        return self._lift_motor_voltage

    @lift_motor_voltage.setter
    def lift_motor_voltage(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lift_motor_voltage' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'lift_motor_voltage' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._lift_motor_voltage = value

    @builtins.property
    def head_yaw_motor_voltage(self):
        """Message field 'head_yaw_motor_voltage'."""
        return self._head_yaw_motor_voltage

    @head_yaw_motor_voltage.setter
    def head_yaw_motor_voltage(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'head_yaw_motor_voltage' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'head_yaw_motor_voltage' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._head_yaw_motor_voltage = value

    @builtins.property
    def head_pitch_motor_voltage(self):
        """Message field 'head_pitch_motor_voltage'."""
        return self._head_pitch_motor_voltage

    @head_pitch_motor_voltage.setter
    def head_pitch_motor_voltage(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'head_pitch_motor_voltage' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'head_pitch_motor_voltage' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._head_pitch_motor_voltage = value

    @builtins.property
    def agv_voltage(self):
        """Message field 'agv_voltage'."""
        return self._agv_voltage

    @agv_voltage.setter
    def agv_voltage(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'agv_voltage' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'agv_voltage' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._agv_voltage = value

    @builtins.property
    def emergency_stop_err_fedback(self):
        """Message field 'emergency_stop_err_fedback'."""
        return self._emergency_stop_err_fedback

    @emergency_stop_err_fedback.setter
    def emergency_stop_err_fedback(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'emergency_stop_err_fedback' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'emergency_stop_err_fedback' field must be an unsigned integer in [0, 255]"
        self._emergency_stop_err_fedback = value

    @builtins.property
    def power_board_software_version(self):
        """Message field 'power_board_software_version'."""
        return self._power_board_software_version

    @power_board_software_version.setter
    def power_board_software_version(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'power_board_software_version' field must be of type 'str'"
        self._power_board_software_version = value

    @builtins.property
    def power_board_hardware_version(self):
        """Message field 'power_board_hardware_version'."""
        return self._power_board_hardware_version

    @power_board_hardware_version.setter
    def power_board_hardware_version(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'power_board_hardware_version' field must be of type 'str'"
        self._power_board_hardware_version = value

    @builtins.property
    def power_board_serial_number(self):
        """Message field 'power_board_serial_number'."""
        return self._power_board_serial_number

    @power_board_serial_number.setter
    def power_board_serial_number(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'power_board_serial_number' field must be of type 'str'"
        self._power_board_serial_number = value
