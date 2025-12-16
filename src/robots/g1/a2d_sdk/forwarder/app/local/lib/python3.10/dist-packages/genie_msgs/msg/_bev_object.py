# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/BevObject.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_BevObject(type):
    """Metaclass of message 'BevObject'."""

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
                'genie_msgs.msg.BevObject')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__bev_object
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__bev_object
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__bev_object
            cls._TYPE_SUPPORT = module.type_support_msg__msg__bev_object
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__bev_object

            from genie_msgs.msg import Point3D
            if Point3D.__class__._TYPE_SUPPORT is None:
                Point3D.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class BevObject(metaclass=Metaclass_BevObject):
    """Message class 'BevObject'."""

    __slots__ = [
        '_pos',
        '_size',
        '_polygon',
        '_velocity',
        '_acceleration',
        '_euler_angle',
        '_euler_angle_rate',
        '_confidence',
    ]

    _fields_and_field_types = {
        'pos': 'sequence<genie_msgs/Point3D>',
        'size': 'sequence<genie_msgs/Point3D>',
        'polygon': 'sequence<genie_msgs/Point3D>',
        'velocity': 'sequence<genie_msgs/Point3D>',
        'acceleration': 'sequence<genie_msgs/Point3D>',
        'euler_angle': 'sequence<genie_msgs/Point3D>',
        'euler_angle_rate': 'sequence<genie_msgs/Point3D>',
        'confidence': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.pos = kwargs.get('pos', [])
        self.size = kwargs.get('size', [])
        self.polygon = kwargs.get('polygon', [])
        self.velocity = kwargs.get('velocity', [])
        self.acceleration = kwargs.get('acceleration', [])
        self.euler_angle = kwargs.get('euler_angle', [])
        self.euler_angle_rate = kwargs.get('euler_angle_rate', [])
        self.confidence = kwargs.get('confidence', float())

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
        if self.pos != other.pos:
            return False
        if self.size != other.size:
            return False
        if self.polygon != other.polygon:
            return False
        if self.velocity != other.velocity:
            return False
        if self.acceleration != other.acceleration:
            return False
        if self.euler_angle != other.euler_angle:
            return False
        if self.euler_angle_rate != other.euler_angle_rate:
            return False
        if self.confidence != other.confidence:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def pos(self):
        """Message field 'pos'."""
        return self._pos

    @pos.setter
    def pos(self, value):
        if __debug__:
            from genie_msgs.msg import Point3D
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
                 all(isinstance(v, Point3D) for v in value) and
                 True), \
                "The 'pos' field must be a set or sequence and each value of type 'Point3D'"
        self._pos = value

    @builtins.property
    def size(self):
        """Message field 'size'."""
        return self._size

    @size.setter
    def size(self, value):
        if __debug__:
            from genie_msgs.msg import Point3D
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
                 all(isinstance(v, Point3D) for v in value) and
                 True), \
                "The 'size' field must be a set or sequence and each value of type 'Point3D'"
        self._size = value

    @builtins.property
    def polygon(self):
        """Message field 'polygon'."""
        return self._polygon

    @polygon.setter
    def polygon(self, value):
        if __debug__:
            from genie_msgs.msg import Point3D
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
                 all(isinstance(v, Point3D) for v in value) and
                 True), \
                "The 'polygon' field must be a set or sequence and each value of type 'Point3D'"
        self._polygon = value

    @builtins.property
    def velocity(self):
        """Message field 'velocity'."""
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if __debug__:
            from genie_msgs.msg import Point3D
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
                 all(isinstance(v, Point3D) for v in value) and
                 True), \
                "The 'velocity' field must be a set or sequence and each value of type 'Point3D'"
        self._velocity = value

    @builtins.property
    def acceleration(self):
        """Message field 'acceleration'."""
        return self._acceleration

    @acceleration.setter
    def acceleration(self, value):
        if __debug__:
            from genie_msgs.msg import Point3D
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
                 all(isinstance(v, Point3D) for v in value) and
                 True), \
                "The 'acceleration' field must be a set or sequence and each value of type 'Point3D'"
        self._acceleration = value

    @builtins.property
    def euler_angle(self):
        """Message field 'euler_angle'."""
        return self._euler_angle

    @euler_angle.setter
    def euler_angle(self, value):
        if __debug__:
            from genie_msgs.msg import Point3D
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
                 all(isinstance(v, Point3D) for v in value) and
                 True), \
                "The 'euler_angle' field must be a set or sequence and each value of type 'Point3D'"
        self._euler_angle = value

    @builtins.property
    def euler_angle_rate(self):
        """Message field 'euler_angle_rate'."""
        return self._euler_angle_rate

    @euler_angle_rate.setter
    def euler_angle_rate(self, value):
        if __debug__:
            from genie_msgs.msg import Point3D
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
                 all(isinstance(v, Point3D) for v in value) and
                 True), \
                "The 'euler_angle_rate' field must be a set or sequence and each value of type 'Point3D'"
        self._euler_angle_rate = value

    @builtins.property
    def confidence(self):
        """Message field 'confidence'."""
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'confidence' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'confidence' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._confidence = value
