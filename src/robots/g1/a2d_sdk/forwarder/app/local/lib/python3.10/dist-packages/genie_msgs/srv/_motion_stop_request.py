# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:srv/MotionStopRequest.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MotionStopRequest_Request(type):
    """Metaclass of message 'MotionStopRequest_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'INPUT_VR': 51,
        'INPUT_MOCAP': 52,
        'INPUT_HMI': 53,
        'INPUT_GDK': 54,
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
                'genie_msgs.srv.MotionStopRequest_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__motion_stop_request__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__motion_stop_request__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__motion_stop_request__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__motion_stop_request__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__motion_stop_request__request

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'INPUT_VR': cls.__constants['INPUT_VR'],
            'INPUT_MOCAP': cls.__constants['INPUT_MOCAP'],
            'INPUT_HMI': cls.__constants['INPUT_HMI'],
            'INPUT_GDK': cls.__constants['INPUT_GDK'],
        }

    @property
    def INPUT_VR(self):
        """Message constant 'INPUT_VR'."""
        return Metaclass_MotionStopRequest_Request.__constants['INPUT_VR']

    @property
    def INPUT_MOCAP(self):
        """Message constant 'INPUT_MOCAP'."""
        return Metaclass_MotionStopRequest_Request.__constants['INPUT_MOCAP']

    @property
    def INPUT_HMI(self):
        """Message constant 'INPUT_HMI'."""
        return Metaclass_MotionStopRequest_Request.__constants['INPUT_HMI']

    @property
    def INPUT_GDK(self):
        """Message constant 'INPUT_GDK'."""
        return Metaclass_MotionStopRequest_Request.__constants['INPUT_GDK']


class MotionStopRequest_Request(metaclass=Metaclass_MotionStopRequest_Request):
    """
    Message class 'MotionStopRequest_Request'.

    Constants:
      INPUT_VR
      INPUT_MOCAP
      INPUT_HMI
      INPUT_GDK
    """

    __slots__ = [
        '_header',
        '_input_type',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'input_type': 'uint8',
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
        self.header = kwargs.get('header', Header())
        self.input_type = kwargs.get('input_type', int())

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
        if self.input_type != other.input_type:
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


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_MotionStopRequest_Response(type):
    """Metaclass of message 'MotionStopRequest_Response'."""

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
                'genie_msgs.srv.MotionStopRequest_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__motion_stop_request__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__motion_stop_request__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__motion_stop_request__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__motion_stop_request__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__motion_stop_request__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MotionStopRequest_Response(metaclass=Metaclass_MotionStopRequest_Response):
    """Message class 'MotionStopRequest_Response'."""

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


class Metaclass_MotionStopRequest(type):
    """Metaclass of service 'MotionStopRequest'."""

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
                'genie_msgs.srv.MotionStopRequest')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__motion_stop_request

            from genie_msgs.srv import _motion_stop_request
            if _motion_stop_request.Metaclass_MotionStopRequest_Request._TYPE_SUPPORT is None:
                _motion_stop_request.Metaclass_MotionStopRequest_Request.__import_type_support__()
            if _motion_stop_request.Metaclass_MotionStopRequest_Response._TYPE_SUPPORT is None:
                _motion_stop_request.Metaclass_MotionStopRequest_Response.__import_type_support__()


class MotionStopRequest(metaclass=Metaclass_MotionStopRequest):
    from genie_msgs.srv._motion_stop_request import MotionStopRequest_Request as Request
    from genie_msgs.srv._motion_stop_request import MotionStopRequest_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
