# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/Position.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Position(type):
    """Metaclass of message 'Position'."""

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
                'genie_msgs.msg.Position')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__position
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__position
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__position
            cls._TYPE_SUPPORT = module.type_support_msg__msg__position
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__position

            from genie_msgs.msg import MotorState
            if MotorState.__class__._TYPE_SUPPORT is None:
                MotorState.__class__.__import_type_support__()

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


class Position(metaclass=Metaclass_Position):
    """Message class 'Position'."""

    __slots__ = [
        '_header',
        '_agv_status',
        '_position_conf',
        '_agv_pos_x',
        '_agv_pos_y',
        '_agv_pos_z',
        '_agv_angle',
        '_odom_x',
        '_odom_y',
        '_odom_z',
        '_odom_angle',
        '_linear_speed',
        '_angular_speed',
        '_acc_x',
        '_acc_y',
        '_acc_z',
        '_gyro_x',
        '_gyro_y',
        '_gyro_z',
        '_roll',
        '_pitch',
        '_yaw',
        '_map_id',
        '_chassis_error',
        '_motor_states',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'agv_status': 'int32',
        'position_conf': 'float',
        'agv_pos_x': 'float',
        'agv_pos_y': 'float',
        'agv_pos_z': 'float',
        'agv_angle': 'float',
        'odom_x': 'float',
        'odom_y': 'float',
        'odom_z': 'float',
        'odom_angle': 'float',
        'linear_speed': 'float',
        'angular_speed': 'float',
        'acc_x': 'float',
        'acc_y': 'float',
        'acc_z': 'float',
        'gyro_x': 'float',
        'gyro_y': 'float',
        'gyro_z': 'float',
        'roll': 'float',
        'pitch': 'float',
        'yaw': 'float',
        'map_id': 'int32',
        'chassis_error': 'int32',
        'motor_states': 'sequence<genie_msgs/MotorState>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
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
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'MotorState')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.agv_status = kwargs.get('agv_status', int())
        self.position_conf = kwargs.get('position_conf', float())
        self.agv_pos_x = kwargs.get('agv_pos_x', float())
        self.agv_pos_y = kwargs.get('agv_pos_y', float())
        self.agv_pos_z = kwargs.get('agv_pos_z', float())
        self.agv_angle = kwargs.get('agv_angle', float())
        self.odom_x = kwargs.get('odom_x', float())
        self.odom_y = kwargs.get('odom_y', float())
        self.odom_z = kwargs.get('odom_z', float())
        self.odom_angle = kwargs.get('odom_angle', float())
        self.linear_speed = kwargs.get('linear_speed', float())
        self.angular_speed = kwargs.get('angular_speed', float())
        self.acc_x = kwargs.get('acc_x', float())
        self.acc_y = kwargs.get('acc_y', float())
        self.acc_z = kwargs.get('acc_z', float())
        self.gyro_x = kwargs.get('gyro_x', float())
        self.gyro_y = kwargs.get('gyro_y', float())
        self.gyro_z = kwargs.get('gyro_z', float())
        self.roll = kwargs.get('roll', float())
        self.pitch = kwargs.get('pitch', float())
        self.yaw = kwargs.get('yaw', float())
        self.map_id = kwargs.get('map_id', int())
        self.chassis_error = kwargs.get('chassis_error', int())
        self.motor_states = kwargs.get('motor_states', [])

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
        if self.agv_status != other.agv_status:
            return False
        if self.position_conf != other.position_conf:
            return False
        if self.agv_pos_x != other.agv_pos_x:
            return False
        if self.agv_pos_y != other.agv_pos_y:
            return False
        if self.agv_pos_z != other.agv_pos_z:
            return False
        if self.agv_angle != other.agv_angle:
            return False
        if self.odom_x != other.odom_x:
            return False
        if self.odom_y != other.odom_y:
            return False
        if self.odom_z != other.odom_z:
            return False
        if self.odom_angle != other.odom_angle:
            return False
        if self.linear_speed != other.linear_speed:
            return False
        if self.angular_speed != other.angular_speed:
            return False
        if self.acc_x != other.acc_x:
            return False
        if self.acc_y != other.acc_y:
            return False
        if self.acc_z != other.acc_z:
            return False
        if self.gyro_x != other.gyro_x:
            return False
        if self.gyro_y != other.gyro_y:
            return False
        if self.gyro_z != other.gyro_z:
            return False
        if self.roll != other.roll:
            return False
        if self.pitch != other.pitch:
            return False
        if self.yaw != other.yaw:
            return False
        if self.map_id != other.map_id:
            return False
        if self.chassis_error != other.chassis_error:
            return False
        if self.motor_states != other.motor_states:
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
    def agv_status(self):
        """Message field 'agv_status'."""
        return self._agv_status

    @agv_status.setter
    def agv_status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'agv_status' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'agv_status' field must be an integer in [-2147483648, 2147483647]"
        self._agv_status = value

    @builtins.property
    def position_conf(self):
        """Message field 'position_conf'."""
        return self._position_conf

    @position_conf.setter
    def position_conf(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'position_conf' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'position_conf' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._position_conf = value

    @builtins.property
    def agv_pos_x(self):
        """Message field 'agv_pos_x'."""
        return self._agv_pos_x

    @agv_pos_x.setter
    def agv_pos_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'agv_pos_x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'agv_pos_x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._agv_pos_x = value

    @builtins.property
    def agv_pos_y(self):
        """Message field 'agv_pos_y'."""
        return self._agv_pos_y

    @agv_pos_y.setter
    def agv_pos_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'agv_pos_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'agv_pos_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._agv_pos_y = value

    @builtins.property
    def agv_pos_z(self):
        """Message field 'agv_pos_z'."""
        return self._agv_pos_z

    @agv_pos_z.setter
    def agv_pos_z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'agv_pos_z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'agv_pos_z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._agv_pos_z = value

    @builtins.property
    def agv_angle(self):
        """Message field 'agv_angle'."""
        return self._agv_angle

    @agv_angle.setter
    def agv_angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'agv_angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'agv_angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._agv_angle = value

    @builtins.property
    def odom_x(self):
        """Message field 'odom_x'."""
        return self._odom_x

    @odom_x.setter
    def odom_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'odom_x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'odom_x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._odom_x = value

    @builtins.property
    def odom_y(self):
        """Message field 'odom_y'."""
        return self._odom_y

    @odom_y.setter
    def odom_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'odom_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'odom_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._odom_y = value

    @builtins.property
    def odom_z(self):
        """Message field 'odom_z'."""
        return self._odom_z

    @odom_z.setter
    def odom_z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'odom_z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'odom_z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._odom_z = value

    @builtins.property
    def odom_angle(self):
        """Message field 'odom_angle'."""
        return self._odom_angle

    @odom_angle.setter
    def odom_angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'odom_angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'odom_angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._odom_angle = value

    @builtins.property
    def linear_speed(self):
        """Message field 'linear_speed'."""
        return self._linear_speed

    @linear_speed.setter
    def linear_speed(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'linear_speed' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'linear_speed' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._linear_speed = value

    @builtins.property
    def angular_speed(self):
        """Message field 'angular_speed'."""
        return self._angular_speed

    @angular_speed.setter
    def angular_speed(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'angular_speed' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'angular_speed' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._angular_speed = value

    @builtins.property
    def acc_x(self):
        """Message field 'acc_x'."""
        return self._acc_x

    @acc_x.setter
    def acc_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'acc_x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'acc_x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._acc_x = value

    @builtins.property
    def acc_y(self):
        """Message field 'acc_y'."""
        return self._acc_y

    @acc_y.setter
    def acc_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'acc_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'acc_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._acc_y = value

    @builtins.property
    def acc_z(self):
        """Message field 'acc_z'."""
        return self._acc_z

    @acc_z.setter
    def acc_z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'acc_z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'acc_z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._acc_z = value

    @builtins.property
    def gyro_x(self):
        """Message field 'gyro_x'."""
        return self._gyro_x

    @gyro_x.setter
    def gyro_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'gyro_x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'gyro_x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._gyro_x = value

    @builtins.property
    def gyro_y(self):
        """Message field 'gyro_y'."""
        return self._gyro_y

    @gyro_y.setter
    def gyro_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'gyro_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'gyro_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._gyro_y = value

    @builtins.property
    def gyro_z(self):
        """Message field 'gyro_z'."""
        return self._gyro_z

    @gyro_z.setter
    def gyro_z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'gyro_z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'gyro_z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._gyro_z = value

    @builtins.property
    def roll(self):
        """Message field 'roll'."""
        return self._roll

    @roll.setter
    def roll(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'roll' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'roll' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._roll = value

    @builtins.property
    def pitch(self):
        """Message field 'pitch'."""
        return self._pitch

    @pitch.setter
    def pitch(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pitch' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pitch' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pitch = value

    @builtins.property
    def yaw(self):
        """Message field 'yaw'."""
        return self._yaw

    @yaw.setter
    def yaw(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'yaw' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'yaw' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._yaw = value

    @builtins.property
    def map_id(self):
        """Message field 'map_id'."""
        return self._map_id

    @map_id.setter
    def map_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'map_id' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'map_id' field must be an integer in [-2147483648, 2147483647]"
        self._map_id = value

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
            assert value >= -2147483648 and value < 2147483648, \
                "The 'chassis_error' field must be an integer in [-2147483648, 2147483647]"
        self._chassis_error = value

    @builtins.property
    def motor_states(self):
        """Message field 'motor_states'."""
        return self._motor_states

    @motor_states.setter
    def motor_states(self, value):
        if __debug__:
            from genie_msgs.msg import MotorState
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
                 all(isinstance(v, MotorState) for v in value) and
                 True), \
                "The 'motor_states' field must be a set or sequence and each value of type 'MotorState'"
        self._motor_states = value
