# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/CameraObject.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CameraObject(type):
    """Metaclass of message 'CameraObject'."""

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
                'genie_msgs.msg.CameraObject')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__camera_object
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__camera_object
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__camera_object
            cls._TYPE_SUPPORT = module.type_support_msg__msg__camera_object
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__camera_object

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


class CameraObject(metaclass=Metaclass_CameraObject):
    """Message class 'CameraObject'."""

    __slots__ = [
        '_camera_id',
        '_pos',
        '_corner',
        '_size',
        '_mask',
        '_instance_id',
        '_ground_point',
        '_confidence',
        '_class_type',
        '_sub_type',
    ]

    _fields_and_field_types = {
        'camera_id': 'sequence<string>',
        'pos': 'sequence<genie_msgs/Point3D>',
        'corner': 'sequence<genie_msgs/Point3D>',
        'size': 'sequence<genie_msgs/Point3D>',
        'mask': 'sequence<genie_msgs/Point3D>',
        'instance_id': 'int32',
        'ground_point': 'genie_msgs/Point3D',
        'confidence': 'float',
        'class_type': 'int32',
        'sub_type': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D')),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'Point3D'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.camera_id = kwargs.get('camera_id', [])
        self.pos = kwargs.get('pos', [])
        self.corner = kwargs.get('corner', [])
        self.size = kwargs.get('size', [])
        self.mask = kwargs.get('mask', [])
        self.instance_id = kwargs.get('instance_id', int())
        from genie_msgs.msg import Point3D
        self.ground_point = kwargs.get('ground_point', Point3D())
        self.confidence = kwargs.get('confidence', float())
        self.class_type = kwargs.get('class_type', int())
        self.sub_type = kwargs.get('sub_type', int())

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
        if self.camera_id != other.camera_id:
            return False
        if self.pos != other.pos:
            return False
        if self.corner != other.corner:
            return False
        if self.size != other.size:
            return False
        if self.mask != other.mask:
            return False
        if self.instance_id != other.instance_id:
            return False
        if self.ground_point != other.ground_point:
            return False
        if self.confidence != other.confidence:
            return False
        if self.class_type != other.class_type:
            return False
        if self.sub_type != other.sub_type:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def camera_id(self):
        """Message field 'camera_id'."""
        return self._camera_id

    @camera_id.setter
    def camera_id(self, value):
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
                 all(isinstance(v, str) for v in value) and
                 True), \
                "The 'camera_id' field must be a set or sequence and each value of type 'str'"
        self._camera_id = value

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
    def corner(self):
        """Message field 'corner'."""
        return self._corner

    @corner.setter
    def corner(self, value):
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
                "The 'corner' field must be a set or sequence and each value of type 'Point3D'"
        self._corner = value

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
    def mask(self):
        """Message field 'mask'."""
        return self._mask

    @mask.setter
    def mask(self, value):
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
                "The 'mask' field must be a set or sequence and each value of type 'Point3D'"
        self._mask = value

    @builtins.property
    def instance_id(self):
        """Message field 'instance_id'."""
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'instance_id' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'instance_id' field must be an integer in [-2147483648, 2147483647]"
        self._instance_id = value

    @builtins.property
    def ground_point(self):
        """Message field 'ground_point'."""
        return self._ground_point

    @ground_point.setter
    def ground_point(self, value):
        if __debug__:
            from genie_msgs.msg import Point3D
            assert \
                isinstance(value, Point3D), \
                "The 'ground_point' field must be a sub message of type 'Point3D'"
        self._ground_point = value

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

    @builtins.property
    def class_type(self):
        """Message field 'class_type'."""
        return self._class_type

    @class_type.setter
    def class_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'class_type' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'class_type' field must be an integer in [-2147483648, 2147483647]"
        self._class_type = value

    @builtins.property
    def sub_type(self):
        """Message field 'sub_type'."""
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'sub_type' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'sub_type' field must be an integer in [-2147483648, 2147483647]"
        self._sub_type = value
