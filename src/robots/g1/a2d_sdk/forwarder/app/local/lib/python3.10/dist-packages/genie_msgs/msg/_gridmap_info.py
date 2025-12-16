# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/GridmapInfo.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'data'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GridmapInfo(type):
    """Metaclass of message 'GridmapInfo'."""

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
                'genie_msgs.msg.GridmapInfo')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__gridmap_info
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__gridmap_info
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__gridmap_info
            cls._TYPE_SUPPORT = module.type_support_msg__msg__gridmap_info
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__gridmap_info

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

            from geometry_msgs.msg import Pose
            if Pose.__class__._TYPE_SUPPORT is None:
                Pose.__class__.__import_type_support__()

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


class GridmapInfo(metaclass=Metaclass_GridmapInfo):
    """Message class 'GridmapInfo'."""

    __slots__ = [
        '_header',
        '_measuring_ts',
        '_publish_ts',
        '_frame_id',
        '_resolution',
        '_width',
        '_height',
        '_origin',
        '_orientation_euler',
        '_data',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'measuring_ts': 'builtin_interfaces/Time',
        'publish_ts': 'builtin_interfaces/Time',
        'frame_id': 'string',
        'resolution': 'float',
        'width': 'uint32',
        'height': 'uint32',
        'origin': 'geometry_msgs/Pose',
        'orientation_euler': 'geometry_msgs/Vector3',
        'data': 'sequence<int8>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Vector3'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int8')),  # noqa: E501
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
        self.resolution = kwargs.get('resolution', float())
        self.width = kwargs.get('width', int())
        self.height = kwargs.get('height', int())
        from geometry_msgs.msg import Pose
        self.origin = kwargs.get('origin', Pose())
        from geometry_msgs.msg import Vector3
        self.orientation_euler = kwargs.get('orientation_euler', Vector3())
        self.data = array.array('b', kwargs.get('data', []))

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
        if self.resolution != other.resolution:
            return False
        if self.width != other.width:
            return False
        if self.height != other.height:
            return False
        if self.origin != other.origin:
            return False
        if self.orientation_euler != other.orientation_euler:
            return False
        if self.data != other.data:
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
    def resolution(self):
        """Message field 'resolution'."""
        return self._resolution

    @resolution.setter
    def resolution(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'resolution' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'resolution' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._resolution = value

    @builtins.property
    def width(self):
        """Message field 'width'."""
        return self._width

    @width.setter
    def width(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'width' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'width' field must be an unsigned integer in [0, 4294967295]"
        self._width = value

    @builtins.property
    def height(self):
        """Message field 'height'."""
        return self._height

    @height.setter
    def height(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'height' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'height' field must be an unsigned integer in [0, 4294967295]"
        self._height = value

    @builtins.property
    def origin(self):
        """Message field 'origin'."""
        return self._origin

    @origin.setter
    def origin(self, value):
        if __debug__:
            from geometry_msgs.msg import Pose
            assert \
                isinstance(value, Pose), \
                "The 'origin' field must be a sub message of type 'Pose'"
        self._origin = value

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
    def data(self):
        """Message field 'data'."""
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'b', \
                "The 'data' array.array() must have the type code of 'b'"
            self._data = value
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
                 all(val >= -128 and val < 128 for val in value)), \
                "The 'data' field must be a set or sequence and each value of type 'int' and each integer in [-128, 127]"
        self._data = array.array('b', value)
