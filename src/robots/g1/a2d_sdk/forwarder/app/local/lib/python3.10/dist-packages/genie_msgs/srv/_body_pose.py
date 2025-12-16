# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:srv/BodyPose.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'joint_states'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_BodyPose_Request(type):
    """Metaclass of message 'BodyPose_Request'."""

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
                'genie_msgs.srv.BodyPose_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__body_pose__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__body_pose__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__body_pose__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__body_pose__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__body_pose__request

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


class BodyPose_Request(metaclass=Metaclass_BodyPose_Request):
    """Message class 'BodyPose_Request'."""

    __slots__ = [
        '_header',
        '_body_part',
        '_joint_flag',
        '_joint_states',
        '_block',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'body_part': 'uint32',
        'joint_flag': 'int32',
        'joint_states': 'sequence<float>',
        'block': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.body_part = kwargs.get('body_part', int())
        self.joint_flag = kwargs.get('joint_flag', int())
        self.joint_states = array.array('f', kwargs.get('joint_states', []))
        self.block = kwargs.get('block', bool())

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
        if self.body_part != other.body_part:
            return False
        if self.joint_flag != other.joint_flag:
            return False
        if self.joint_states != other.joint_states:
            return False
        if self.block != other.block:
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
    def body_part(self):
        """Message field 'body_part'."""
        return self._body_part

    @body_part.setter
    def body_part(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'body_part' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'body_part' field must be an unsigned integer in [0, 4294967295]"
        self._body_part = value

    @builtins.property
    def joint_flag(self):
        """Message field 'joint_flag'."""
        return self._joint_flag

    @joint_flag.setter
    def joint_flag(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'joint_flag' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'joint_flag' field must be an integer in [-2147483648, 2147483647]"
        self._joint_flag = value

    @builtins.property
    def joint_states(self):
        """Message field 'joint_states'."""
        return self._joint_states

    @joint_states.setter
    def joint_states(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'joint_states' array.array() must have the type code of 'f'"
            self._joint_states = value
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
                "The 'joint_states' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._joint_states = array.array('f', value)

    @builtins.property
    def block(self):
        """Message field 'block'."""
        return self._block

    @block.setter
    def block(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'block' field must be of type 'bool'"
        self._block = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_BodyPose_Response(type):
    """Metaclass of message 'BodyPose_Response'."""

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
                'genie_msgs.srv.BodyPose_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__body_pose__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__body_pose__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__body_pose__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__body_pose__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__body_pose__response

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


class BodyPose_Response(metaclass=Metaclass_BodyPose_Response):
    """Message class 'BodyPose_Response'."""

    __slots__ = [
        '_res_header',
        '_exec_result',
    ]

    _fields_and_field_types = {
        'res_header': 'std_msgs/Header',
        'exec_result': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.res_header = kwargs.get('res_header', Header())
        self.exec_result = kwargs.get('exec_result', int())

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
        if self.res_header != other.res_header:
            return False
        if self.exec_result != other.exec_result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def res_header(self):
        """Message field 'res_header'."""
        return self._res_header

    @res_header.setter
    def res_header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'res_header' field must be a sub message of type 'Header'"
        self._res_header = value

    @builtins.property
    def exec_result(self):
        """Message field 'exec_result'."""
        return self._exec_result

    @exec_result.setter
    def exec_result(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'exec_result' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'exec_result' field must be an unsigned integer in [0, 255]"
        self._exec_result = value


class Metaclass_BodyPose(type):
    """Metaclass of service 'BodyPose'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('genie_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'genie_msgs.srv.BodyPose')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__body_pose

            from genie_msgs.srv import _body_pose
            if _body_pose.Metaclass_BodyPose_Request._TYPE_SUPPORT is None:
                _body_pose.Metaclass_BodyPose_Request.__import_type_support__()
            if _body_pose.Metaclass_BodyPose_Response._TYPE_SUPPORT is None:
                _body_pose.Metaclass_BodyPose_Response.__import_type_support__()


class BodyPose(metaclass=Metaclass_BodyPose):
    from genie_msgs.srv._body_pose import BodyPose_Request as Request
    from genie_msgs.srv._body_pose import BodyPose_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
