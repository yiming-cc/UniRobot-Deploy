# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:srv/CallConnect.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CallConnect_Request(type):
    """Metaclass of message 'CallConnect_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'CALL_CONNECT_START': 1,
        'CALL_CONNECT_FINISH': 2,
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
                'genie_msgs.srv.CallConnect_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__call_connect__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__call_connect__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__call_connect__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__call_connect__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__call_connect__request

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'CALL_CONNECT_START': cls.__constants['CALL_CONNECT_START'],
            'CALL_CONNECT_FINISH': cls.__constants['CALL_CONNECT_FINISH'],
        }

    @property
    def CALL_CONNECT_START(self):
        """Message constant 'CALL_CONNECT_START'."""
        return Metaclass_CallConnect_Request.__constants['CALL_CONNECT_START']

    @property
    def CALL_CONNECT_FINISH(self):
        """Message constant 'CALL_CONNECT_FINISH'."""
        return Metaclass_CallConnect_Request.__constants['CALL_CONNECT_FINISH']


class CallConnect_Request(metaclass=Metaclass_CallConnect_Request):
    """
    Message class 'CallConnect_Request'.

    Constants:
      CALL_CONNECT_START
      CALL_CONNECT_FINISH
    """

    __slots__ = [
        '_header',
        '_call_req',
        '_requester',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'call_req': 'uint32',
        'requester': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.call_req = kwargs.get('call_req', int())
        self.requester = kwargs.get('requester', str())

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
        if self.call_req != other.call_req:
            return False
        if self.requester != other.requester:
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
    def call_req(self):
        """Message field 'call_req'."""
        return self._call_req

    @call_req.setter
    def call_req(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'call_req' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'call_req' field must be an unsigned integer in [0, 4294967295]"
        self._call_req = value

    @builtins.property
    def requester(self):
        """Message field 'requester'."""
        return self._requester

    @requester.setter
    def requester(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'requester' field must be of type 'str'"
        self._requester = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_CallConnect_Response(type):
    """Metaclass of message 'CallConnect_Response'."""

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
                'genie_msgs.srv.CallConnect_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__call_connect__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__call_connect__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__call_connect__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__call_connect__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__call_connect__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CallConnect_Response(metaclass=Metaclass_CallConnect_Response):
    """Message class 'CallConnect_Response'."""

    __slots__ = [
        '_result',
    ]

    _fields_and_field_types = {
        'result': 'uint32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.result = kwargs.get('result', int())

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
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def result(self):
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'result' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'result' field must be an unsigned integer in [0, 4294967295]"
        self._result = value


class Metaclass_CallConnect(type):
    """Metaclass of service 'CallConnect'."""

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
                'genie_msgs.srv.CallConnect')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__call_connect

            from genie_msgs.srv import _call_connect
            if _call_connect.Metaclass_CallConnect_Request._TYPE_SUPPORT is None:
                _call_connect.Metaclass_CallConnect_Request.__import_type_support__()
            if _call_connect.Metaclass_CallConnect_Response._TYPE_SUPPORT is None:
                _call_connect.Metaclass_CallConnect_Response.__import_type_support__()


class CallConnect(metaclass=Metaclass_CallConnect):
    from genie_msgs.srv._call_connect import CallConnect_Request as Request
    from genie_msgs.srv._call_connect import CallConnect_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
