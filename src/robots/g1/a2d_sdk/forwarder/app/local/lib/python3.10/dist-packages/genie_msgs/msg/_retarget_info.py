# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/RetargetInfo.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'target_joint_positions'
# Member 'target_joint_positions_delta'
# Member 'target_joint_velocities'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RetargetInfo(type):
    """Metaclass of message 'RetargetInfo'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'GROUP_HEAD_YAW': 0,
        'GROUP_HEAD_PITCH': 1,
        'GROUP_LEFT_ARM': 2,
        'GROUP_RIGHT_ARM': 3,
        'GROUP_LEFT_TOOL': 4,
        'GROUP_RIGHT_TOOL': 5,
        'GROUP_WAIST_LIFT': 6,
        'GROUP_WAIST_PITCH': 7,
        'GROUP_CHASSIS': 8,
        'INPUT_VR': 51,
        'INPUT_MOCAP': 52,
        'INPUT_HMI': 53,
        'INPUT_GDK': 54,
        'ABS_POSE': 0,
        'DELTA_POSE': 1,
        'END_SPEED': 2,
        'ABS_JOINT': 3,
        'DELTA_JOINT': 4,
        'JOINT_SPEED': 5,
        'PASSIVE': 6,
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
                'genie_msgs.msg.RetargetInfo')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__retarget_info
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__retarget_info
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__retarget_info
            cls._TYPE_SUPPORT = module.type_support_msg__msg__retarget_info
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__retarget_info

            from geometry_msgs.msg import Pose
            if Pose.__class__._TYPE_SUPPORT is None:
                Pose.__class__.__import_type_support__()

            from geometry_msgs.msg import Twist
            if Twist.__class__._TYPE_SUPPORT is None:
                Twist.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'GROUP_HEAD_YAW': cls.__constants['GROUP_HEAD_YAW'],
            'GROUP_HEAD_PITCH': cls.__constants['GROUP_HEAD_PITCH'],
            'GROUP_LEFT_ARM': cls.__constants['GROUP_LEFT_ARM'],
            'GROUP_RIGHT_ARM': cls.__constants['GROUP_RIGHT_ARM'],
            'GROUP_LEFT_TOOL': cls.__constants['GROUP_LEFT_TOOL'],
            'GROUP_RIGHT_TOOL': cls.__constants['GROUP_RIGHT_TOOL'],
            'GROUP_WAIST_LIFT': cls.__constants['GROUP_WAIST_LIFT'],
            'GROUP_WAIST_PITCH': cls.__constants['GROUP_WAIST_PITCH'],
            'GROUP_CHASSIS': cls.__constants['GROUP_CHASSIS'],
            'INPUT_VR': cls.__constants['INPUT_VR'],
            'INPUT_MOCAP': cls.__constants['INPUT_MOCAP'],
            'INPUT_HMI': cls.__constants['INPUT_HMI'],
            'INPUT_GDK': cls.__constants['INPUT_GDK'],
            'ABS_POSE': cls.__constants['ABS_POSE'],
            'DELTA_POSE': cls.__constants['DELTA_POSE'],
            'END_SPEED': cls.__constants['END_SPEED'],
            'ABS_JOINT': cls.__constants['ABS_JOINT'],
            'DELTA_JOINT': cls.__constants['DELTA_JOINT'],
            'JOINT_SPEED': cls.__constants['JOINT_SPEED'],
            'PASSIVE': cls.__constants['PASSIVE'],
        }

    @property
    def GROUP_HEAD_YAW(self):
        """Message constant 'GROUP_HEAD_YAW'."""
        return Metaclass_RetargetInfo.__constants['GROUP_HEAD_YAW']

    @property
    def GROUP_HEAD_PITCH(self):
        """Message constant 'GROUP_HEAD_PITCH'."""
        return Metaclass_RetargetInfo.__constants['GROUP_HEAD_PITCH']

    @property
    def GROUP_LEFT_ARM(self):
        """Message constant 'GROUP_LEFT_ARM'."""
        return Metaclass_RetargetInfo.__constants['GROUP_LEFT_ARM']

    @property
    def GROUP_RIGHT_ARM(self):
        """Message constant 'GROUP_RIGHT_ARM'."""
        return Metaclass_RetargetInfo.__constants['GROUP_RIGHT_ARM']

    @property
    def GROUP_LEFT_TOOL(self):
        """Message constant 'GROUP_LEFT_TOOL'."""
        return Metaclass_RetargetInfo.__constants['GROUP_LEFT_TOOL']

    @property
    def GROUP_RIGHT_TOOL(self):
        """Message constant 'GROUP_RIGHT_TOOL'."""
        return Metaclass_RetargetInfo.__constants['GROUP_RIGHT_TOOL']

    @property
    def GROUP_WAIST_LIFT(self):
        """Message constant 'GROUP_WAIST_LIFT'."""
        return Metaclass_RetargetInfo.__constants['GROUP_WAIST_LIFT']

    @property
    def GROUP_WAIST_PITCH(self):
        """Message constant 'GROUP_WAIST_PITCH'."""
        return Metaclass_RetargetInfo.__constants['GROUP_WAIST_PITCH']

    @property
    def GROUP_CHASSIS(self):
        """Message constant 'GROUP_CHASSIS'."""
        return Metaclass_RetargetInfo.__constants['GROUP_CHASSIS']

    @property
    def INPUT_VR(self):
        """Message constant 'INPUT_VR'."""
        return Metaclass_RetargetInfo.__constants['INPUT_VR']

    @property
    def INPUT_MOCAP(self):
        """Message constant 'INPUT_MOCAP'."""
        return Metaclass_RetargetInfo.__constants['INPUT_MOCAP']

    @property
    def INPUT_HMI(self):
        """Message constant 'INPUT_HMI'."""
        return Metaclass_RetargetInfo.__constants['INPUT_HMI']

    @property
    def INPUT_GDK(self):
        """Message constant 'INPUT_GDK'."""
        return Metaclass_RetargetInfo.__constants['INPUT_GDK']

    @property
    def ABS_POSE(self):
        """Message constant 'ABS_POSE'."""
        return Metaclass_RetargetInfo.__constants['ABS_POSE']

    @property
    def DELTA_POSE(self):
        """Message constant 'DELTA_POSE'."""
        return Metaclass_RetargetInfo.__constants['DELTA_POSE']

    @property
    def END_SPEED(self):
        """Message constant 'END_SPEED'."""
        return Metaclass_RetargetInfo.__constants['END_SPEED']

    @property
    def ABS_JOINT(self):
        """Message constant 'ABS_JOINT'."""
        return Metaclass_RetargetInfo.__constants['ABS_JOINT']

    @property
    def DELTA_JOINT(self):
        """Message constant 'DELTA_JOINT'."""
        return Metaclass_RetargetInfo.__constants['DELTA_JOINT']

    @property
    def JOINT_SPEED(self):
        """Message constant 'JOINT_SPEED'."""
        return Metaclass_RetargetInfo.__constants['JOINT_SPEED']

    @property
    def PASSIVE(self):
        """Message constant 'PASSIVE'."""
        return Metaclass_RetargetInfo.__constants['PASSIVE']


class RetargetInfo(metaclass=Metaclass_RetargetInfo):
    """
    Message class 'RetargetInfo'.

    Constants:
      GROUP_HEAD_YAW
      GROUP_HEAD_PITCH
      GROUP_LEFT_ARM
      GROUP_RIGHT_ARM
      GROUP_LEFT_TOOL
      GROUP_RIGHT_TOOL
      GROUP_WAIST_LIFT
      GROUP_WAIST_PITCH
      GROUP_CHASSIS
      INPUT_VR
      INPUT_MOCAP
      INPUT_HMI
      INPUT_GDK
      ABS_POSE
      DELTA_POSE
      END_SPEED
      ABS_JOINT
      DELTA_JOINT
      JOINT_SPEED
      PASSIVE
    """

    __slots__ = [
        '_group_id',
        '_input_type',
        '_control_type',
        '_frame_id',
        '_target_frame_names',
        '_target_frame_poses',
        '_target_frame_poses_delta',
        '_reference_frame_names',
        '_reference_frame_poses',
        '_target_frame_velocities',
        '_target_joint_positions',
        '_target_joint_positions_delta',
        '_target_joint_velocities',
    ]

    _fields_and_field_types = {
        'group_id': 'uint8',
        'input_type': 'uint8',
        'control_type': 'uint8',
        'frame_id': 'string',
        'target_frame_names': 'sequence<string>',
        'target_frame_poses': 'sequence<geometry_msgs/Pose>',
        'target_frame_poses_delta': 'sequence<geometry_msgs/Pose>',
        'reference_frame_names': 'sequence<string>',
        'reference_frame_poses': 'sequence<geometry_msgs/Pose>',
        'target_frame_velocities': 'sequence<geometry_msgs/Twist>',
        'target_joint_positions': 'sequence<double>',
        'target_joint_positions_delta': 'sequence<double>',
        'target_joint_velocities': 'sequence<double>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Twist')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.group_id = kwargs.get('group_id', int())
        self.input_type = kwargs.get('input_type', int())
        self.control_type = kwargs.get('control_type', int())
        self.frame_id = kwargs.get('frame_id', str())
        self.target_frame_names = kwargs.get('target_frame_names', [])
        self.target_frame_poses = kwargs.get('target_frame_poses', [])
        self.target_frame_poses_delta = kwargs.get('target_frame_poses_delta', [])
        self.reference_frame_names = kwargs.get('reference_frame_names', [])
        self.reference_frame_poses = kwargs.get('reference_frame_poses', [])
        self.target_frame_velocities = kwargs.get('target_frame_velocities', [])
        self.target_joint_positions = array.array('d', kwargs.get('target_joint_positions', []))
        self.target_joint_positions_delta = array.array('d', kwargs.get('target_joint_positions_delta', []))
        self.target_joint_velocities = array.array('d', kwargs.get('target_joint_velocities', []))

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
        if self.group_id != other.group_id:
            return False
        if self.input_type != other.input_type:
            return False
        if self.control_type != other.control_type:
            return False
        if self.frame_id != other.frame_id:
            return False
        if self.target_frame_names != other.target_frame_names:
            return False
        if self.target_frame_poses != other.target_frame_poses:
            return False
        if self.target_frame_poses_delta != other.target_frame_poses_delta:
            return False
        if self.reference_frame_names != other.reference_frame_names:
            return False
        if self.reference_frame_poses != other.reference_frame_poses:
            return False
        if self.target_frame_velocities != other.target_frame_velocities:
            return False
        if self.target_joint_positions != other.target_joint_positions:
            return False
        if self.target_joint_positions_delta != other.target_joint_positions_delta:
            return False
        if self.target_joint_velocities != other.target_joint_velocities:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def group_id(self):
        """Message field 'group_id'."""
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'group_id' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'group_id' field must be an unsigned integer in [0, 255]"
        self._group_id = value

    @builtins.property
    def input_type(self):
        """Message field 'input_type'."""
        return self._input_type

    @input_type.setter
    def input_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'input_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'input_type' field must be an unsigned integer in [0, 255]"
        self._input_type = value

    @builtins.property
    def control_type(self):
        """Message field 'control_type'."""
        return self._control_type

    @control_type.setter
    def control_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'control_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'control_type' field must be an unsigned integer in [0, 255]"
        self._control_type = value

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
    def target_frame_names(self):
        """Message field 'target_frame_names'."""
        return self._target_frame_names

    @target_frame_names.setter
    def target_frame_names(self, value):
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
                "The 'target_frame_names' field must be a set or sequence and each value of type 'str'"
        self._target_frame_names = value

    @builtins.property
    def target_frame_poses(self):
        """Message field 'target_frame_poses'."""
        return self._target_frame_poses

    @target_frame_poses.setter
    def target_frame_poses(self, value):
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
                "The 'target_frame_poses' field must be a set or sequence and each value of type 'Pose'"
        self._target_frame_poses = value

    @builtins.property
    def target_frame_poses_delta(self):
        """Message field 'target_frame_poses_delta'."""
        return self._target_frame_poses_delta

    @target_frame_poses_delta.setter
    def target_frame_poses_delta(self, value):
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
                "The 'target_frame_poses_delta' field must be a set or sequence and each value of type 'Pose'"
        self._target_frame_poses_delta = value

    @builtins.property
    def reference_frame_names(self):
        """Message field 'reference_frame_names'."""
        return self._reference_frame_names

    @reference_frame_names.setter
    def reference_frame_names(self, value):
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
                "The 'reference_frame_names' field must be a set or sequence and each value of type 'str'"
        self._reference_frame_names = value

    @builtins.property
    def reference_frame_poses(self):
        """Message field 'reference_frame_poses'."""
        return self._reference_frame_poses

    @reference_frame_poses.setter
    def reference_frame_poses(self, value):
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
                "The 'reference_frame_poses' field must be a set or sequence and each value of type 'Pose'"
        self._reference_frame_poses = value

    @builtins.property
    def target_frame_velocities(self):
        """Message field 'target_frame_velocities'."""
        return self._target_frame_velocities

    @target_frame_velocities.setter
    def target_frame_velocities(self, value):
        if __debug__:
            from geometry_msgs.msg import Twist
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
                 all(isinstance(v, Twist) for v in value) and
                 True), \
                "The 'target_frame_velocities' field must be a set or sequence and each value of type 'Twist'"
        self._target_frame_velocities = value

    @builtins.property
    def target_joint_positions(self):
        """Message field 'target_joint_positions'."""
        return self._target_joint_positions

    @target_joint_positions.setter
    def target_joint_positions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'target_joint_positions' array.array() must have the type code of 'd'"
            self._target_joint_positions = value
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
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'target_joint_positions' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._target_joint_positions = array.array('d', value)

    @builtins.property
    def target_joint_positions_delta(self):
        """Message field 'target_joint_positions_delta'."""
        return self._target_joint_positions_delta

    @target_joint_positions_delta.setter
    def target_joint_positions_delta(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'target_joint_positions_delta' array.array() must have the type code of 'd'"
            self._target_joint_positions_delta = value
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
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'target_joint_positions_delta' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._target_joint_positions_delta = array.array('d', value)

    @builtins.property
    def target_joint_velocities(self):
        """Message field 'target_joint_velocities'."""
        return self._target_joint_velocities

    @target_joint_velocities.setter
    def target_joint_velocities(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'target_joint_velocities' array.array() must have the type code of 'd'"
            self._target_joint_velocities = value
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
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'target_joint_velocities' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._target_joint_velocities = array.array('d', value)
