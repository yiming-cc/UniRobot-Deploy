# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/GraspPoint.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'depth'
# Member 'width'
# Member 'score'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GraspPoint(type):
    """Metaclass of message 'GraspPoint'."""

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
                'genie_msgs.msg.GraspPoint')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__grasp_point
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__grasp_point
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__grasp_point
            cls._TYPE_SUPPORT = module.type_support_msg__msg__grasp_point
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__grasp_point

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


class GraspPoint(metaclass=Metaclass_GraspPoint):
    """Message class 'GraspPoint'."""

    __slots__ = [
        '_pos',
        '_direction',
        '_in_plane_rotation',
        '_depth',
        '_width',
        '_score',
    ]

    _fields_and_field_types = {
        'pos': 'sequence<genie_msgs/Point3D>',
        'direction': 'sequence<genie_msgs/Point3D>',
        'in_plane_rotation': 'sequence<genie_msgs/Point3D>',
        'depth': 'sequence<float>',
        'width': 'sequence<float>',
        'score': 'sequence<float>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.pos = kwargs.get('pos', [])
        self.direction = kwargs.get('direction', [])
        self.in_plane_rotation = kwargs.get('in_plane_rotation', [])
        self.depth = array.array('f', kwargs.get('depth', []))
        self.width = array.array('f', kwargs.get('width', []))
        self.score = array.array('f', kwargs.get('score', []))

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
        if self.direction != other.direction:
            return False
        if self.in_plane_rotation != other.in_plane_rotation:
            return False
        if self.depth != other.depth:
            return False
        if self.width != other.width:
            return False
        if self.score != other.score:
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
    def direction(self):
        """Message field 'direction'."""
        return self._direction

    @direction.setter
    def direction(self, value):
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
                "The 'direction' field must be a set or sequence and each value of type 'Point3D'"
        self._direction = value

    @builtins.property
    def in_plane_rotation(self):
        """Message field 'in_plane_rotation'."""
        return self._in_plane_rotation

    @in_plane_rotation.setter
    def in_plane_rotation(self, value):
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
                "The 'in_plane_rotation' field must be a set or sequence and each value of type 'Point3D'"
        self._in_plane_rotation = value

    @builtins.property
    def depth(self):
        """Message field 'depth'."""
        return self._depth

    @depth.setter
    def depth(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'depth' array.array() must have the type code of 'f'"
            self._depth = value
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
                "The 'depth' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._depth = array.array('f', value)

    @builtins.property
    def width(self):
        """Message field 'width'."""
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'width' array.array() must have the type code of 'f'"
            self._width = value
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
                "The 'width' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._width = array.array('f', value)

    @builtins.property
    def score(self):
        """Message field 'score'."""
        return self._score

    @score.setter
    def score(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'score' array.array() must have the type code of 'f'"
            self._score = value
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
                "The 'score' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._score = array.array('f', value)
