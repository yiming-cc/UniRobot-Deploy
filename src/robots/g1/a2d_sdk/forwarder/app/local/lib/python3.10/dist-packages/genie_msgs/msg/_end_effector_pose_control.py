# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/EndEffectorPoseControl.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_EndEffectorPoseControl(type):
    """Metaclass of message 'EndEffectorPoseControl'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'GROUP_LEFT_ARM': 4,
        'GROUP_RIGHT_ARM': 8,
        'GROUP_DUAL_ARM': 12,
        'GROUP_LEFT_ARM_WAIST_LIFT': 20,
        'GROUP_LEFT_ARM_WAIST_PITCH': 36,
        'GROUP_LEFT_ARM_WAIST': 52,
        'GROUP_RIGHT_ARM_WAIST_LIFT': 24,
        'GROUP_RIGHT_ARM_WAIST_PITCH': 40,
        'GROUP_RIGHT_ARM_WAIST': 56,
        'GROUP_DUAL_ARM_WAIST_LIFT': 28,
        'GROUP_DUAL_ARM_WAIST_PITCH': 44,
        'GROUP_DUAL_ARM_WAIST': 60,
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
                'genie_msgs.msg.EndEffectorPoseControl')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__end_effector_pose_control
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__end_effector_pose_control
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__end_effector_pose_control
            cls._TYPE_SUPPORT = module.type_support_msg__msg__end_effector_pose_control
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__end_effector_pose_control

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
            'GROUP_LEFT_ARM': cls.__constants['GROUP_LEFT_ARM'],
            'GROUP_RIGHT_ARM': cls.__constants['GROUP_RIGHT_ARM'],
            'GROUP_DUAL_ARM': cls.__constants['GROUP_DUAL_ARM'],
            'GROUP_LEFT_ARM_WAIST_LIFT': cls.__constants['GROUP_LEFT_ARM_WAIST_LIFT'],
            'GROUP_LEFT_ARM_WAIST_PITCH': cls.__constants['GROUP_LEFT_ARM_WAIST_PITCH'],
            'GROUP_LEFT_ARM_WAIST': cls.__constants['GROUP_LEFT_ARM_WAIST'],
            'GROUP_RIGHT_ARM_WAIST_LIFT': cls.__constants['GROUP_RIGHT_ARM_WAIST_LIFT'],
            'GROUP_RIGHT_ARM_WAIST_PITCH': cls.__constants['GROUP_RIGHT_ARM_WAIST_PITCH'],
            'GROUP_RIGHT_ARM_WAIST': cls.__constants['GROUP_RIGHT_ARM_WAIST'],
            'GROUP_DUAL_ARM_WAIST_LIFT': cls.__constants['GROUP_DUAL_ARM_WAIST_LIFT'],
            'GROUP_DUAL_ARM_WAIST_PITCH': cls.__constants['GROUP_DUAL_ARM_WAIST_PITCH'],
            'GROUP_DUAL_ARM_WAIST': cls.__constants['GROUP_DUAL_ARM_WAIST'],
        }

    @property
    def GROUP_LEFT_ARM(self):
        """Message constant 'GROUP_LEFT_ARM'."""
        return Metaclass_EndEffectorPoseControl.__constants['GROUP_LEFT_ARM']

    @property
    def GROUP_RIGHT_ARM(self):
        """Message constant 'GROUP_RIGHT_ARM'."""
        return Metaclass_EndEffectorPoseControl.__constants['GROUP_RIGHT_ARM']

    @property
    def GROUP_DUAL_ARM(self):
        """Message constant 'GROUP_DUAL_ARM'."""
        return Metaclass_EndEffectorPoseControl.__constants['GROUP_DUAL_ARM']

    @property
    def GROUP_LEFT_ARM_WAIST_LIFT(self):
        """Message constant 'GROUP_LEFT_ARM_WAIST_LIFT'."""
        return Metaclass_EndEffectorPoseControl.__constants['GROUP_LEFT_ARM_WAIST_LIFT']

    @property
    def GROUP_LEFT_ARM_WAIST_PITCH(self):
        """Message constant 'GROUP_LEFT_ARM_WAIST_PITCH'."""
        return Metaclass_EndEffectorPoseControl.__constants['GROUP_LEFT_ARM_WAIST_PITCH']

    @property
    def GROUP_LEFT_ARM_WAIST(self):
        """Message constant 'GROUP_LEFT_ARM_WAIST'."""
        return Metaclass_EndEffectorPoseControl.__constants['GROUP_LEFT_ARM_WAIST']

    @property
    def GROUP_RIGHT_ARM_WAIST_LIFT(self):
        """Message constant 'GROUP_RIGHT_ARM_WAIST_LIFT'."""
        return Metaclass_EndEffectorPoseControl.__constants['GROUP_RIGHT_ARM_WAIST_LIFT']

    @property
    def GROUP_RIGHT_ARM_WAIST_PITCH(self):
        """Message constant 'GROUP_RIGHT_ARM_WAIST_PITCH'."""
        return Metaclass_EndEffectorPoseControl.__constants['GROUP_RIGHT_ARM_WAIST_PITCH']

    @property
    def GROUP_RIGHT_ARM_WAIST(self):
        """Message constant 'GROUP_RIGHT_ARM_WAIST'."""
        return Metaclass_EndEffectorPoseControl.__constants['GROUP_RIGHT_ARM_WAIST']

    @property
    def GROUP_DUAL_ARM_WAIST_LIFT(self):
        """Message constant 'GROUP_DUAL_ARM_WAIST_LIFT'."""
        return Metaclass_EndEffectorPoseControl.__constants['GROUP_DUAL_ARM_WAIST_LIFT']

    @property
    def GROUP_DUAL_ARM_WAIST_PITCH(self):
        """Message constant 'GROUP_DUAL_ARM_WAIST_PITCH'."""
        return Metaclass_EndEffectorPoseControl.__constants['GROUP_DUAL_ARM_WAIST_PITCH']

    @property
    def GROUP_DUAL_ARM_WAIST(self):
        """Message constant 'GROUP_DUAL_ARM_WAIST'."""
        return Metaclass_EndEffectorPoseControl.__constants['GROUP_DUAL_ARM_WAIST']


class EndEffectorPoseControl(metaclass=Metaclass_EndEffectorPoseControl):
    """
    Message class 'EndEffectorPoseControl'.

    Constants:
      GROUP_LEFT_ARM
      GROUP_RIGHT_ARM
      GROUP_DUAL_ARM
      GROUP_LEFT_ARM_WAIST_LIFT
      GROUP_LEFT_ARM_WAIST_PITCH
      GROUP_LEFT_ARM_WAIST
      GROUP_RIGHT_ARM_WAIST_LIFT
      GROUP_RIGHT_ARM_WAIST_PITCH
      GROUP_RIGHT_ARM_WAIST
      GROUP_DUAL_ARM_WAIST_LIFT
      GROUP_DUAL_ARM_WAIST_PITCH
      GROUP_DUAL_ARM_WAIST
    """

    __slots__ = [
        '_header',
        '_lifetime',
        '_control_group',
        '_left_end_effector_pose',
        '_right_end_effector_pose',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'lifetime': 'double',
        'control_group': 'uint32',
        'left_end_effector_pose': 'geometry_msgs/Pose',
        'right_end_effector_pose': 'geometry_msgs/Pose',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.lifetime = kwargs.get('lifetime', float())
        self.control_group = kwargs.get('control_group', int())
        from geometry_msgs.msg import Pose
        self.left_end_effector_pose = kwargs.get('left_end_effector_pose', Pose())
        from geometry_msgs.msg import Pose
        self.right_end_effector_pose = kwargs.get('right_end_effector_pose', Pose())

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
        if self.lifetime != other.lifetime:
            return False
        if self.control_group != other.control_group:
            return False
        if self.left_end_effector_pose != other.left_end_effector_pose:
            return False
        if self.right_end_effector_pose != other.right_end_effector_pose:
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
    def lifetime(self):
        """Message field 'lifetime'."""
        return self._lifetime

    @lifetime.setter
    def lifetime(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lifetime' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'lifetime' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._lifetime = value

    @builtins.property
    def control_group(self):
        """Message field 'control_group'."""
        return self._control_group

    @control_group.setter
    def control_group(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'control_group' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'control_group' field must be an unsigned integer in [0, 4294967295]"
        self._control_group = value

    @builtins.property
    def left_end_effector_pose(self):
        """Message field 'left_end_effector_pose'."""
        return self._left_end_effector_pose

    @left_end_effector_pose.setter
    def left_end_effector_pose(self, value):
        if __debug__:
            from geometry_msgs.msg import Pose
            assert \
                isinstance(value, Pose), \
                "The 'left_end_effector_pose' field must be a sub message of type 'Pose'"
        self._left_end_effector_pose = value

    @builtins.property
    def right_end_effector_pose(self):
        """Message field 'right_end_effector_pose'."""
        return self._right_end_effector_pose

    @right_end_effector_pose.setter
    def right_end_effector_pose(self, value):
        if __debug__:
            from geometry_msgs.msg import Pose
            assert \
                isinstance(value, Pose), \
                "The 'right_end_effector_pose' field must be a sub message of type 'Pose'"
        self._right_end_effector_pose = value
