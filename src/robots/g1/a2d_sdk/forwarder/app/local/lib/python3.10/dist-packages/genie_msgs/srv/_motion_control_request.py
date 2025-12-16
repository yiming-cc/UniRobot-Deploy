# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:srv/MotionControlRequest.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MotionControlRequest_Request(type):
    """Metaclass of message 'MotionControlRequest_Request'."""

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
                'genie_msgs.srv.MotionControlRequest_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__motion_control_request__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__motion_control_request__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__motion_control_request__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__motion_control_request__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__motion_control_request__request

            from genie_msgs.msg import RetargetInfo
            if RetargetInfo.__class__._TYPE_SUPPORT is None:
                RetargetInfo.__class__.__import_type_support__()

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


class MotionControlRequest_Request(metaclass=Metaclass_MotionControlRequest_Request):
    """Message class 'MotionControlRequest_Request'."""

    __slots__ = [
        '_header',
        '_retarget_groups',
        '_speed_scale',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'retarget_groups': 'sequence<genie_msgs/RetargetInfo>',
        'speed_scale': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'RetargetInfo')),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.retarget_groups = kwargs.get('retarget_groups', [])
        self.speed_scale = kwargs.get('speed_scale', float())

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
        if self.retarget_groups != other.retarget_groups:
            return False
        if self.speed_scale != other.speed_scale:
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
    def retarget_groups(self):
        """Message field 'retarget_groups'."""
        return self._retarget_groups

    @retarget_groups.setter
    def retarget_groups(self, value):
        if __debug__:
            from genie_msgs.msg import RetargetInfo
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
                 all(isinstance(v, RetargetInfo) for v in value) and
                 True), \
                "The 'retarget_groups' field must be a set or sequence and each value of type 'RetargetInfo'"
        self._retarget_groups = value

    @builtins.property
    def speed_scale(self):
        """Message field 'speed_scale'."""
        return self._speed_scale

    @speed_scale.setter
    def speed_scale(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'speed_scale' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'speed_scale' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._speed_scale = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_MotionControlRequest_Response(type):
    """Metaclass of message 'MotionControlRequest_Response'."""

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
                'genie_msgs.srv.MotionControlRequest_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__motion_control_request__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__motion_control_request__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__motion_control_request__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__motion_control_request__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__motion_control_request__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MotionControlRequest_Response(metaclass=Metaclass_MotionControlRequest_Response):
    """Message class 'MotionControlRequest_Response'."""

    __slots__ = [
        '_error_code',
        '_error_msg',
    ]

    _fields_and_field_types = {
        'error_code': 'uint8',
        'error_msg': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
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


class Metaclass_MotionControlRequest(type):
    """Metaclass of service 'MotionControlRequest'."""

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
                'genie_msgs.srv.MotionControlRequest')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__motion_control_request

            from genie_msgs.srv import _motion_control_request
            if _motion_control_request.Metaclass_MotionControlRequest_Request._TYPE_SUPPORT is None:
                _motion_control_request.Metaclass_MotionControlRequest_Request.__import_type_support__()
            if _motion_control_request.Metaclass_MotionControlRequest_Response._TYPE_SUPPORT is None:
                _motion_control_request.Metaclass_MotionControlRequest_Response.__import_type_support__()


class MotionControlRequest(metaclass=Metaclass_MotionControlRequest):
    from genie_msgs.srv._motion_control_request import MotionControlRequest_Request as Request
    from genie_msgs.srv._motion_control_request import MotionControlRequest_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
