# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/ModelPredict.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'body_joint_positions'
# Member 'target_velocities'
# Member 'target_efforts'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ModelPredict(type):
    """Metaclass of message 'ModelPredict'."""

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
                'genie_msgs.msg.ModelPredict')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__model_predict
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__model_predict
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__model_predict
            cls._TYPE_SUPPORT = module.type_support_msg__msg__model_predict
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__model_predict

            from geometry_msgs.msg import Pose
            if Pose.__class__._TYPE_SUPPORT is None:
                Pose.__class__.__import_type_support__()

            from sensor_msgs.msg import JointState
            if JointState.__class__._TYPE_SUPPORT is None:
                JointState.__class__.__import_type_support__()

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


class ModelPredict(metaclass=Metaclass_ModelPredict):
    """Message class 'ModelPredict'."""

    __slots__ = [
        '_header',
        '_body_joint_names',
        '_body_joint_positions',
        '_model_output_type',
        '_target_link_names',
        '_target_poses',
        '_target_joint_states',
        '_target_velocities',
        '_target_efforts',
        '_model_sleep_time',
        '_trajectory_reference_time',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'body_joint_names': 'sequence<string>',
        'body_joint_positions': 'sequence<double>',
        'model_output_type': 'uint8',
        'target_link_names': 'sequence<string>',
        'target_poses': 'sequence<geometry_msgs/Pose>',
        'target_joint_states': 'sequence<sensor_msgs/JointState>',
        'target_velocities': 'sequence<float>',
        'target_efforts': 'sequence<float>',
        'model_sleep_time': 'double',
        'trajectory_reference_time': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['sensor_msgs', 'msg'], 'JointState')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.body_joint_names = kwargs.get('body_joint_names', [])
        self.body_joint_positions = array.array('d', kwargs.get('body_joint_positions', []))
        self.model_output_type = kwargs.get('model_output_type', int())
        self.target_link_names = kwargs.get('target_link_names', [])
        self.target_poses = kwargs.get('target_poses', [])
        self.target_joint_states = kwargs.get('target_joint_states', [])
        self.target_velocities = array.array('f', kwargs.get('target_velocities', []))
        self.target_efforts = array.array('f', kwargs.get('target_efforts', []))
        self.model_sleep_time = kwargs.get('model_sleep_time', float())
        self.trajectory_reference_time = kwargs.get('trajectory_reference_time', float())

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
        if self.body_joint_names != other.body_joint_names:
            return False
        if self.body_joint_positions != other.body_joint_positions:
            return False
        if self.model_output_type != other.model_output_type:
            return False
        if self.target_link_names != other.target_link_names:
            return False
        if self.target_poses != other.target_poses:
            return False
        if self.target_joint_states != other.target_joint_states:
            return False
        if self.target_velocities != other.target_velocities:
            return False
        if self.target_efforts != other.target_efforts:
            return False
        if self.model_sleep_time != other.model_sleep_time:
            return False
        if self.trajectory_reference_time != other.trajectory_reference_time:
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
    def body_joint_names(self):
        """Message field 'body_joint_names'."""
        return self._body_joint_names

    @body_joint_names.setter
    def body_joint_names(self, value):
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
                "The 'body_joint_names' field must be a set or sequence and each value of type 'str'"
        self._body_joint_names = value

    @builtins.property
    def body_joint_positions(self):
        """Message field 'body_joint_positions'."""
        return self._body_joint_positions

    @body_joint_positions.setter
    def body_joint_positions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'body_joint_positions' array.array() must have the type code of 'd'"
            self._body_joint_positions = value
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
                "The 'body_joint_positions' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._body_joint_positions = array.array('d', value)

    @builtins.property
    def model_output_type(self):
        """Message field 'model_output_type'."""
        return self._model_output_type

    @model_output_type.setter
    def model_output_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'model_output_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'model_output_type' field must be an unsigned integer in [0, 255]"
        self._model_output_type = value

    @builtins.property
    def target_link_names(self):
        """Message field 'target_link_names'."""
        return self._target_link_names

    @target_link_names.setter
    def target_link_names(self, value):
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
                "The 'target_link_names' field must be a set or sequence and each value of type 'str'"
        self._target_link_names = value

    @builtins.property
    def target_poses(self):
        """Message field 'target_poses'."""
        return self._target_poses

    @target_poses.setter
    def target_poses(self, value):
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
                "The 'target_poses' field must be a set or sequence and each value of type 'Pose'"
        self._target_poses = value

    @builtins.property
    def target_joint_states(self):
        """Message field 'target_joint_states'."""
        return self._target_joint_states

    @target_joint_states.setter
    def target_joint_states(self, value):
        if __debug__:
            from sensor_msgs.msg import JointState
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
                 all(isinstance(v, JointState) for v in value) and
                 True), \
                "The 'target_joint_states' field must be a set or sequence and each value of type 'JointState'"
        self._target_joint_states = value

    @builtins.property
    def target_velocities(self):
        """Message field 'target_velocities'."""
        return self._target_velocities

    @target_velocities.setter
    def target_velocities(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'target_velocities' array.array() must have the type code of 'f'"
            self._target_velocities = value
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
                "The 'target_velocities' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._target_velocities = array.array('f', value)

    @builtins.property
    def target_efforts(self):
        """Message field 'target_efforts'."""
        return self._target_efforts

    @target_efforts.setter
    def target_efforts(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'target_efforts' array.array() must have the type code of 'f'"
            self._target_efforts = value
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
                "The 'target_efforts' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._target_efforts = array.array('f', value)

    @builtins.property
    def model_sleep_time(self):
        """Message field 'model_sleep_time'."""
        return self._model_sleep_time

    @model_sleep_time.setter
    def model_sleep_time(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'model_sleep_time' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'model_sleep_time' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._model_sleep_time = value

    @builtins.property
    def trajectory_reference_time(self):
        """Message field 'trajectory_reference_time'."""
        return self._trajectory_reference_time

    @trajectory_reference_time.setter
    def trajectory_reference_time(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'trajectory_reference_time' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'trajectory_reference_time' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._trajectory_reference_time = value
