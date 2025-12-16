# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/VRControllerState.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_VRControllerState(type):
    """Metaclass of message 'VRControllerState'."""

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
                'genie_msgs.msg.VRControllerState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__vr_controller_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__vr_controller_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__vr_controller_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__vr_controller_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__vr_controller_state

            from geometry_msgs.msg import Quaternion
            if Quaternion.__class__._TYPE_SUPPORT is None:
                Quaternion.__class__.__import_type_support__()

            from geometry_msgs.msg import Vector3
            if Vector3.__class__._TYPE_SUPPORT is None:
                Vector3.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class VRControllerState(metaclass=Metaclass_VRControllerState):
    """Message class 'VRControllerState'."""

    __slots__ = [
        '_name',
        '_id',
        '_key_one',
        '_key_two',
        '_hand_trig',
        '_index_trig',
        '_axis_x',
        '_axis_y',
        '_axis_click',
        '_position',
        '_orientation',
    ]

    _fields_and_field_types = {
        'name': 'string',
        'id': 'uint32',
        'key_one': 'boolean',
        'key_two': 'boolean',
        'hand_trig': 'double',
        'index_trig': 'double',
        'axis_x': 'double',
        'axis_y': 'double',
        'axis_click': 'boolean',
        'position': 'geometry_msgs/Vector3',
        'orientation': 'geometry_msgs/Quaternion',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Vector3'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Quaternion'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.name = kwargs.get('name', str())
        self.id = kwargs.get('id', int())
        self.key_one = kwargs.get('key_one', bool())
        self.key_two = kwargs.get('key_two', bool())
        self.hand_trig = kwargs.get('hand_trig', float())
        self.index_trig = kwargs.get('index_trig', float())
        self.axis_x = kwargs.get('axis_x', float())
        self.axis_y = kwargs.get('axis_y', float())
        self.axis_click = kwargs.get('axis_click', bool())
        from geometry_msgs.msg import Vector3
        self.position = kwargs.get('position', Vector3())
        from geometry_msgs.msg import Quaternion
        self.orientation = kwargs.get('orientation', Quaternion())

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
        if self.name != other.name:
            return False
        if self.id != other.id:
            return False
        if self.key_one != other.key_one:
            return False
        if self.key_two != other.key_two:
            return False
        if self.hand_trig != other.hand_trig:
            return False
        if self.index_trig != other.index_trig:
            return False
        if self.axis_x != other.axis_x:
            return False
        if self.axis_y != other.axis_y:
            return False
        if self.axis_click != other.axis_click:
            return False
        if self.position != other.position:
            return False
        if self.orientation != other.orientation:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def name(self):
        """Message field 'name'."""
        return self._name

    @name.setter
    def name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'name' field must be of type 'str'"
        self._name = value

    @builtins.property  # noqa: A003
    def id(self):  # noqa: A003
        """Message field 'id'."""
        return self._id

    @id.setter  # noqa: A003
    def id(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'id' field must be an unsigned integer in [0, 4294967295]"
        self._id = value

    @builtins.property
    def key_one(self):
        """Message field 'key_one'."""
        return self._key_one

    @key_one.setter
    def key_one(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'key_one' field must be of type 'bool'"
        self._key_one = value

    @builtins.property
    def key_two(self):
        """Message field 'key_two'."""
        return self._key_two

    @key_two.setter
    def key_two(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'key_two' field must be of type 'bool'"
        self._key_two = value

    @builtins.property
    def hand_trig(self):
        """Message field 'hand_trig'."""
        return self._hand_trig

    @hand_trig.setter
    def hand_trig(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'hand_trig' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'hand_trig' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._hand_trig = value

    @builtins.property
    def index_trig(self):
        """Message field 'index_trig'."""
        return self._index_trig

    @index_trig.setter
    def index_trig(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'index_trig' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'index_trig' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._index_trig = value

    @builtins.property
    def axis_x(self):
        """Message field 'axis_x'."""
        return self._axis_x

    @axis_x.setter
    def axis_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'axis_x' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'axis_x' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._axis_x = value

    @builtins.property
    def axis_y(self):
        """Message field 'axis_y'."""
        return self._axis_y

    @axis_y.setter
    def axis_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'axis_y' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'axis_y' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._axis_y = value

    @builtins.property
    def axis_click(self):
        """Message field 'axis_click'."""
        return self._axis_click

    @axis_click.setter
    def axis_click(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'axis_click' field must be of type 'bool'"
        self._axis_click = value

    @builtins.property
    def position(self):
        """Message field 'position'."""
        return self._position

    @position.setter
    def position(self, value):
        if __debug__:
            from geometry_msgs.msg import Vector3
            assert \
                isinstance(value, Vector3), \
                "The 'position' field must be a sub message of type 'Vector3'"
        self._position = value

    @builtins.property
    def orientation(self):
        """Message field 'orientation'."""
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        if __debug__:
            from geometry_msgs.msg import Quaternion
            assert \
                isinstance(value, Quaternion), \
                "The 'orientation' field must be a sub message of type 'Quaternion'"
        self._orientation = value
