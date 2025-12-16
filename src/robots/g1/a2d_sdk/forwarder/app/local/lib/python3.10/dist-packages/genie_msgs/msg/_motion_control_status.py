# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/MotionControlStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MotionControlStatus(type):
    """Metaclass of message 'MotionControlStatus'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'MODE_STOP': 0,
        'MODE_SERVO': 1,
        'MODE_PLANNING': 2,
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
                'genie_msgs.msg.MotionControlStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__motion_control_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__motion_control_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__motion_control_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__motion_control_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__motion_control_status

            from geometry_msgs.msg import Pose
            if Pose.__class__._TYPE_SUPPORT is None:
                Pose.__class__.__import_type_support__()

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'MODE_STOP': cls.__constants['MODE_STOP'],
            'MODE_SERVO': cls.__constants['MODE_SERVO'],
            'MODE_PLANNING': cls.__constants['MODE_PLANNING'],
        }

    @property
    def MODE_STOP(self):
        """Message constant 'MODE_STOP'."""
        return Metaclass_MotionControlStatus.__constants['MODE_STOP']

    @property
    def MODE_SERVO(self):
        """Message constant 'MODE_SERVO'."""
        return Metaclass_MotionControlStatus.__constants['MODE_SERVO']

    @property
    def MODE_PLANNING(self):
        """Message constant 'MODE_PLANNING'."""
        return Metaclass_MotionControlStatus.__constants['MODE_PLANNING']


class MotionControlStatus(metaclass=Metaclass_MotionControlStatus):
    """
    Message class 'MotionControlStatus'.

    Constants:
      MODE_STOP
      MODE_SERVO
      MODE_PLANNING
    """

    __slots__ = [
        '_header',
        '_frame_names',
        '_frame_poses',
        '_collision_pairs_1',
        '_collision_pairs_2',
        '_mode',
        '_error_code',
        '_error_msg',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'frame_names': 'sequence<string>',
        'frame_poses': 'sequence<geometry_msgs/Pose>',
        'collision_pairs_1': 'sequence<string>',
        'collision_pairs_2': 'sequence<string>',
        'mode': 'uint8',
        'error_code': 'uint8',
        'error_msg': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.frame_names = kwargs.get('frame_names', [])
        self.frame_poses = kwargs.get('frame_poses', [])
        self.collision_pairs_1 = kwargs.get('collision_pairs_1', [])
        self.collision_pairs_2 = kwargs.get('collision_pairs_2', [])
        self.mode = kwargs.get('mode', int())
        self.error_code = kwargs.get('error_code', int())
        self.error_msg = kwargs.get('error_msg', str())

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
        if self.frame_names != other.frame_names:
            return False
        if self.frame_poses != other.frame_poses:
            return False
        if self.collision_pairs_1 != other.collision_pairs_1:
            return False
        if self.collision_pairs_2 != other.collision_pairs_2:
            return False
        if self.mode != other.mode:
            return False
        if self.error_code != other.error_code:
            return False
        if self.error_msg != other.error_msg:
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
    def frame_names(self):
        """Message field 'frame_names'."""
        return self._frame_names

    @frame_names.setter
    def frame_names(self, value):
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
                "The 'frame_names' field must be a set or sequence and each value of type 'str'"
        self._frame_names = value

    @builtins.property
    def frame_poses(self):
        """Message field 'frame_poses'."""
        return self._frame_poses

    @frame_poses.setter
    def frame_poses(self, value):
        if __debug__:
            from geometry_msgs.msg import Pose
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
                 all(isinstance(v, Pose) for v in value) and
                 True), \
                "The 'frame_poses' field must be a set or sequence and each value of type 'Pose'"
        self._frame_poses = value

    @builtins.property
    def collision_pairs_1(self):
        """Message field 'collision_pairs_1'."""
        return self._collision_pairs_1

    @collision_pairs_1.setter
    def collision_pairs_1(self, value):
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
                "The 'collision_pairs_1' field must be a set or sequence and each value of type 'str'"
        self._collision_pairs_1 = value

    @builtins.property
    def collision_pairs_2(self):
        """Message field 'collision_pairs_2'."""
        return self._collision_pairs_2

    @collision_pairs_2.setter
    def collision_pairs_2(self, value):
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
                "The 'collision_pairs_2' field must be a set or sequence and each value of type 'str'"
        self._collision_pairs_2 = value

    @builtins.property
    def mode(self):
        """Message field 'mode'."""
        return self._mode

    @mode.setter
    def mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'mode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'mode' field must be an unsigned integer in [0, 255]"
        self._mode = value

    @builtins.property
    def error_code(self):
        """Message field 'error_code'."""
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'error_code' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'error_code' field must be an unsigned integer in [0, 255]"
        self._error_code = value

    @builtins.property
    def error_msg(self):
        """Message field 'error_msg'."""
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'error_msg' field must be of type 'str'"
        self._error_msg = value
