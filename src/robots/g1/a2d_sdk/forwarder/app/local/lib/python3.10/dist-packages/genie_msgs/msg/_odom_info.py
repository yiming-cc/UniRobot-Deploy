# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/OdomInfo.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'velocity'
# Member 'velocity_body'
# Member 'acceleration'
# Member 'ang_vel'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

# Member 'covariance'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_OdomInfo(type):
    """Metaclass of message 'OdomInfo'."""

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
                'genie_msgs.msg.OdomInfo')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__odom_info
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__odom_info
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__odom_info
            cls._TYPE_SUPPORT = module.type_support_msg__msg__odom_info
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__odom_info

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

            from geometry_msgs.msg import Point
            if Point.__class__._TYPE_SUPPORT is None:
                Point.__class__.__import_type_support__()

            from geometry_msgs.msg import Quaternion
            if Quaternion.__class__._TYPE_SUPPORT is None:
                Quaternion.__class__.__import_type_support__()

            from geometry_msgs.msg import Vector3
            if Vector3.__class__._TYPE_SUPPORT is None:
                Vector3.__class__.__import_type_support__()

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


class OdomInfo(metaclass=Metaclass_OdomInfo):
    """Message class 'OdomInfo'."""

    __slots__ = [
        '_header',
        '_measuring_ts',
        '_publish_ts',
        '_frame_id',
        '_child_frame_id',
        '_velocity',
        '_velocity_body',
        '_acceleration',
        '_ang_vel',
        '_is_slipping',
        '_position',
        '_orientation_quat',
        '_orientation_euler',
        '_covariance',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'measuring_ts': 'builtin_interfaces/Time',
        'publish_ts': 'builtin_interfaces/Time',
        'frame_id': 'string',
        'child_frame_id': 'string',
        'velocity': 'sequence<float>',
        'velocity_body': 'sequence<float>',
        'acceleration': 'sequence<float>',
        'ang_vel': 'sequence<float>',
        'is_slipping': 'boolean',
        'position': 'geometry_msgs/Point',
        'orientation_quat': 'geometry_msgs/Quaternion',
        'orientation_euler': 'geometry_msgs/Vector3',
        'covariance': 'float[36]',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Quaternion'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Vector3'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 36),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        from builtin_interfaces.msg import Time
        self.measuring_ts = kwargs.get('measuring_ts', Time())
        from builtin_interfaces.msg import Time
        self.publish_ts = kwargs.get('publish_ts', Time())
        self.frame_id = kwargs.get('frame_id', str())
        self.child_frame_id = kwargs.get('child_frame_id', str())
        self.velocity = array.array('f', kwargs.get('velocity', []))
        self.velocity_body = array.array('f', kwargs.get('velocity_body', []))
        self.acceleration = array.array('f', kwargs.get('acceleration', []))
        self.ang_vel = array.array('f', kwargs.get('ang_vel', []))
        self.is_slipping = kwargs.get('is_slipping', bool())
        from geometry_msgs.msg import Point
        self.position = kwargs.get('position', Point())
        from geometry_msgs.msg import Quaternion
        self.orientation_quat = kwargs.get('orientation_quat', Quaternion())
        from geometry_msgs.msg import Vector3
        self.orientation_euler = kwargs.get('orientation_euler', Vector3())
        if 'covariance' not in kwargs:
            self.covariance = numpy.zeros(36, dtype=numpy.float32)
        else:
            self.covariance = numpy.array(kwargs.get('covariance'), dtype=numpy.float32)
            assert self.covariance.shape == (36, )

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
        if self.measuring_ts != other.measuring_ts:
            return False
        if self.publish_ts != other.publish_ts:
            return False
        if self.frame_id != other.frame_id:
            return False
        if self.child_frame_id != other.child_frame_id:
            return False
        if self.velocity != other.velocity:
            return False
        if self.velocity_body != other.velocity_body:
            return False
        if self.acceleration != other.acceleration:
            return False
        if self.ang_vel != other.ang_vel:
            return False
        if self.is_slipping != other.is_slipping:
            return False
        if self.position != other.position:
            return False
        if self.orientation_quat != other.orientation_quat:
            return False
        if self.orientation_euler != other.orientation_euler:
            return False
        if all(self.covariance != other.covariance):
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
    def measuring_ts(self):
        """Message field 'measuring_ts'."""
        return self._measuring_ts

    @measuring_ts.setter
    def measuring_ts(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'measuring_ts' field must be a sub message of type 'Time'"
        self._measuring_ts = value

    @builtins.property
    def publish_ts(self):
        """Message field 'publish_ts'."""
        return self._publish_ts

    @publish_ts.setter
    def publish_ts(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'publish_ts' field must be a sub message of type 'Time'"
        self._publish_ts = value

    @builtins.property
    def frame_id(self):
        """Message field 'frame_id'."""
        return self._frame_id

    @frame_id.setter
    def frame_id(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'frame_id' field must be of type 'str'"
        self._frame_id = value

    @builtins.property
    def child_frame_id(self):
        """Message field 'child_frame_id'."""
        return self._child_frame_id

    @child_frame_id.setter
    def child_frame_id(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'child_frame_id' field must be of type 'str'"
        self._child_frame_id = value

    @builtins.property
    def velocity(self):
        """Message field 'velocity'."""
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'velocity' array.array() must have the type code of 'f'"
            self._velocity = value
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
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'velocity' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._velocity = array.array('f', value)

    @builtins.property
    def velocity_body(self):
        """Message field 'velocity_body'."""
        return self._velocity_body

    @velocity_body.setter
    def velocity_body(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'velocity_body' array.array() must have the type code of 'f'"
            self._velocity_body = value
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
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'velocity_body' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._velocity_body = array.array('f', value)

    @builtins.property
    def acceleration(self):
        """Message field 'acceleration'."""
        return self._acceleration

    @acceleration.setter
    def acceleration(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'acceleration' array.array() must have the type code of 'f'"
            self._acceleration = value
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
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'acceleration' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._acceleration = array.array('f', value)

    @builtins.property
    def ang_vel(self):
        """Message field 'ang_vel'."""
        return self._ang_vel

    @ang_vel.setter
    def ang_vel(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'ang_vel' array.array() must have the type code of 'f'"
            self._ang_vel = value
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
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'ang_vel' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._ang_vel = array.array('f', value)

    @builtins.property
    def is_slipping(self):
        """Message field 'is_slipping'."""
        return self._is_slipping

    @is_slipping.setter
    def is_slipping(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_slipping' field must be of type 'bool'"
        self._is_slipping = value

    @builtins.property
    def position(self):
        """Message field 'position'."""
        return self._position

    @position.setter
    def position(self, value):
        if __debug__:
            from geometry_msgs.msg import Point
            assert \
                isinstance(value, Point), \
                "The 'position' field must be a sub message of type 'Point'"
        self._position = value

    @builtins.property
    def orientation_quat(self):
        """Message field 'orientation_quat'."""
        return self._orientation_quat

    @orientation_quat.setter
    def orientation_quat(self, value):
        if __debug__:
            from geometry_msgs.msg import Quaternion
            assert \
                isinstance(value, Quaternion), \
                "The 'orientation_quat' field must be a sub message of type 'Quaternion'"
        self._orientation_quat = value

    @builtins.property
    def orientation_euler(self):
        """Message field 'orientation_euler'."""
        return self._orientation_euler

    @orientation_euler.setter
    def orientation_euler(self, value):
        if __debug__:
            from geometry_msgs.msg import Vector3
            assert \
                isinstance(value, Vector3), \
                "The 'orientation_euler' field must be a sub message of type 'Vector3'"
        self._orientation_euler = value

    @builtins.property
    def covariance(self):
        """Message field 'covariance'."""
        return self._covariance

    @covariance.setter
    def covariance(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'covariance' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 36, \
                "The 'covariance' numpy.ndarray() must have a size of 36"
            self._covariance = value
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
                 len(value) == 36 and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'covariance' field must be a set or sequence with length 36 and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._covariance = numpy.array(value, dtype=numpy.float32)
