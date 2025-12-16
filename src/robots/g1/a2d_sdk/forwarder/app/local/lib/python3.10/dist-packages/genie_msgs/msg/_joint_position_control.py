# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/JointPositionControl.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'left_arm_joint_positions'
# Member 'right_arm_joint_positions'
# Member 'left_tool_joint_positions'
# Member 'right_tool_joint_positions'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_JointPositionControl(type):
    """Metaclass of message 'JointPositionControl'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'GROUP_HEAD_YAW': 1,
        'GROUP_HEAD_PITCH': 2,
        'GROUP_LEFT_ARM': 4,
        'GROUP_RIGHT_ARM': 8,
        'GROUP_WAIST_LIFT': 16,
        'GROUP_WAIST_PITCH': 32,
        'GROUP_LEFT_TOOL': 128,
        'GROUP_RIGHT_TOOL': 256,
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
                'genie_msgs.msg.JointPositionControl')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__joint_position_control
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__joint_position_control
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__joint_position_control
            cls._TYPE_SUPPORT = module.type_support_msg__msg__joint_position_control
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__joint_position_control

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

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
            'GROUP_WAIST_LIFT': cls.__constants['GROUP_WAIST_LIFT'],
            'GROUP_WAIST_PITCH': cls.__constants['GROUP_WAIST_PITCH'],
            'GROUP_LEFT_TOOL': cls.__constants['GROUP_LEFT_TOOL'],
            'GROUP_RIGHT_TOOL': cls.__constants['GROUP_RIGHT_TOOL'],
        }

    @property
    def GROUP_HEAD_YAW(self):
        """Message constant 'GROUP_HEAD_YAW'."""
        return Metaclass_JointPositionControl.__constants['GROUP_HEAD_YAW']

    @property
    def GROUP_HEAD_PITCH(self):
        """Message constant 'GROUP_HEAD_PITCH'."""
        return Metaclass_JointPositionControl.__constants['GROUP_HEAD_PITCH']

    @property
    def GROUP_LEFT_ARM(self):
        """Message constant 'GROUP_LEFT_ARM'."""
        return Metaclass_JointPositionControl.__constants['GROUP_LEFT_ARM']

    @property
    def GROUP_RIGHT_ARM(self):
        """Message constant 'GROUP_RIGHT_ARM'."""
        return Metaclass_JointPositionControl.__constants['GROUP_RIGHT_ARM']

    @property
    def GROUP_WAIST_LIFT(self):
        """Message constant 'GROUP_WAIST_LIFT'."""
        return Metaclass_JointPositionControl.__constants['GROUP_WAIST_LIFT']

    @property
    def GROUP_WAIST_PITCH(self):
        """Message constant 'GROUP_WAIST_PITCH'."""
        return Metaclass_JointPositionControl.__constants['GROUP_WAIST_PITCH']

    @property
    def GROUP_LEFT_TOOL(self):
        """Message constant 'GROUP_LEFT_TOOL'."""
        return Metaclass_JointPositionControl.__constants['GROUP_LEFT_TOOL']

    @property
    def GROUP_RIGHT_TOOL(self):
        """Message constant 'GROUP_RIGHT_TOOL'."""
        return Metaclass_JointPositionControl.__constants['GROUP_RIGHT_TOOL']


class JointPositionControl(metaclass=Metaclass_JointPositionControl):
    """
    Message class 'JointPositionControl'.

    Constants:
      GROUP_HEAD_YAW
      GROUP_HEAD_PITCH
      GROUP_LEFT_ARM
      GROUP_RIGHT_ARM
      GROUP_WAIST_LIFT
      GROUP_WAIST_PITCH
      GROUP_LEFT_TOOL
      GROUP_RIGHT_TOOL
    """

    __slots__ = [
        '_header',
        '_lifetime',
        '_control_group',
        '_head_yaw_joint_position',
        '_head_pitch_joint_position',
        '_left_arm_joint_positions',
        '_right_arm_joint_positions',
        '_waist_lift_joint_position',
        '_waist_pitch_joint_position',
        '_left_tool_joint_positions',
        '_right_tool_joint_positions',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'lifetime': 'double',
        'control_group': 'uint32',
        'head_yaw_joint_position': 'double',
        'head_pitch_joint_position': 'double',
        'left_arm_joint_positions': 'sequence<double>',
        'right_arm_joint_positions': 'sequence<double>',
        'waist_lift_joint_position': 'double',
        'waist_pitch_joint_position': 'double',
        'left_tool_joint_positions': 'sequence<double>',
        'right_tool_joint_positions': 'sequence<double>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.lifetime = kwargs.get('lifetime', float())
        self.control_group = kwargs.get('control_group', int())
        self.head_yaw_joint_position = kwargs.get('head_yaw_joint_position', float())
        self.head_pitch_joint_position = kwargs.get('head_pitch_joint_position', float())
        self.left_arm_joint_positions = array.array('d', kwargs.get('left_arm_joint_positions', []))
        self.right_arm_joint_positions = array.array('d', kwargs.get('right_arm_joint_positions', []))
        self.waist_lift_joint_position = kwargs.get('waist_lift_joint_position', float())
        self.waist_pitch_joint_position = kwargs.get('waist_pitch_joint_position', float())
        self.left_tool_joint_positions = array.array('d', kwargs.get('left_tool_joint_positions', []))
        self.right_tool_joint_positions = array.array('d', kwargs.get('right_tool_joint_positions', []))

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
        if self.head_yaw_joint_position != other.head_yaw_joint_position:
            return False
        if self.head_pitch_joint_position != other.head_pitch_joint_position:
            return False
        if self.left_arm_joint_positions != other.left_arm_joint_positions:
            return False
        if self.right_arm_joint_positions != other.right_arm_joint_positions:
            return False
        if self.waist_lift_joint_position != other.waist_lift_joint_position:
            return False
        if self.waist_pitch_joint_position != other.waist_pitch_joint_position:
            return False
        if self.left_tool_joint_positions != other.left_tool_joint_positions:
            return False
        if self.right_tool_joint_positions != other.right_tool_joint_positions:
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
    def head_yaw_joint_position(self):
        """Message field 'head_yaw_joint_position'."""
        return self._head_yaw_joint_position

    @head_yaw_joint_position.setter
    def head_yaw_joint_position(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'head_yaw_joint_position' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'head_yaw_joint_position' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._head_yaw_joint_position = value

    @builtins.property
    def head_pitch_joint_position(self):
        """Message field 'head_pitch_joint_position'."""
        return self._head_pitch_joint_position

    @head_pitch_joint_position.setter
    def head_pitch_joint_position(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'head_pitch_joint_position' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'head_pitch_joint_position' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._head_pitch_joint_position = value

    @builtins.property
    def left_arm_joint_positions(self):
        """Message field 'left_arm_joint_positions'."""
        return self._left_arm_joint_positions

    @left_arm_joint_positions.setter
    def left_arm_joint_positions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'left_arm_joint_positions' array.array() must have the type code of 'd'"
            self._left_arm_joint_positions = value
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
                "The 'left_arm_joint_positions' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._left_arm_joint_positions = array.array('d', value)

    @builtins.property
    def right_arm_joint_positions(self):
        """Message field 'right_arm_joint_positions'."""
        return self._right_arm_joint_positions

    @right_arm_joint_positions.setter
    def right_arm_joint_positions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'right_arm_joint_positions' array.array() must have the type code of 'd'"
            self._right_arm_joint_positions = value
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
                "The 'right_arm_joint_positions' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._right_arm_joint_positions = array.array('d', value)

    @builtins.property
    def waist_lift_joint_position(self):
        """Message field 'waist_lift_joint_position'."""
        return self._waist_lift_joint_position

    @waist_lift_joint_position.setter
    def waist_lift_joint_position(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'waist_lift_joint_position' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'waist_lift_joint_position' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._waist_lift_joint_position = value

    @builtins.property
    def waist_pitch_joint_position(self):
        """Message field 'waist_pitch_joint_position'."""
        return self._waist_pitch_joint_position

    @waist_pitch_joint_position.setter
    def waist_pitch_joint_position(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'waist_pitch_joint_position' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'waist_pitch_joint_position' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._waist_pitch_joint_position = value

    @builtins.property
    def left_tool_joint_positions(self):
        """Message field 'left_tool_joint_positions'."""
        return self._left_tool_joint_positions

    @left_tool_joint_positions.setter
    def left_tool_joint_positions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'left_tool_joint_positions' array.array() must have the type code of 'd'"
            self._left_tool_joint_positions = value
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
                "The 'left_tool_joint_positions' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._left_tool_joint_positions = array.array('d', value)

    @builtins.property
    def right_tool_joint_positions(self):
        """Message field 'right_tool_joint_positions'."""
        return self._right_tool_joint_positions

    @right_tool_joint_positions.setter
    def right_tool_joint_positions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'right_tool_joint_positions' array.array() must have the type code of 'd'"
            self._right_tool_joint_positions = value
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
                "The 'right_tool_joint_positions' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._right_tool_joint_positions = array.array('d', value)
