# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:srv/MocapMapping.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'request_data'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MocapMapping_Request(type):
    """Metaclass of message 'MocapMapping_Request'."""

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
                'genie_msgs.srv.MocapMapping_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__mocap_mapping__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__mocap_mapping__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__mocap_mapping__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__mocap_mapping__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__mocap_mapping__request

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


class MocapMapping_Request(metaclass=Metaclass_MocapMapping_Request):
    """Message class 'MocapMapping_Request'."""

    __slots__ = [
        '_header',
        '_request_data',
        '_enable_request',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'request_data': 'sequence<int32>',
        'enable_request': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.request_data = array.array('i', kwargs.get('request_data', []))
        self.enable_request = kwargs.get('enable_request', int())

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
        if self.request_data != other.request_data:
            return False
        if self.enable_request != other.enable_request:
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
    def request_data(self):
        """Message field 'request_data'."""
        return self._request_data

    @request_data.setter
    def request_data(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'i', \
                "The 'request_data' array.array() must have the type code of 'i'"
            self._request_data = value
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
                 all(isinstance(v, int) for v in value) and
                 all(val >= -2147483648 and val < 2147483648 for val in value)), \
                "The 'request_data' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._request_data = array.array('i', value)

    @builtins.property
    def enable_request(self):
        """Message field 'enable_request'."""
        return self._enable_request

    @enable_request.setter
    def enable_request(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'enable_request' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'enable_request' field must be an integer in [-2147483648, 2147483647]"
        self._enable_request = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_MocapMapping_Response(type):
    """Metaclass of message 'MocapMapping_Response'."""

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
                'genie_msgs.srv.MocapMapping_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__mocap_mapping__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__mocap_mapping__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__mocap_mapping__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__mocap_mapping__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__mocap_mapping__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MocapMapping_Response(metaclass=Metaclass_MocapMapping_Response):
    """Message class 'MocapMapping_Response'."""

    __slots__ = [
        '_success',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())

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
        if self.success != other.success:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value


class Metaclass_MocapMapping(type):
    """Metaclass of service 'MocapMapping'."""

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
                'genie_msgs.srv.MocapMapping')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__mocap_mapping

            from genie_msgs.srv import _mocap_mapping
            if _mocap_mapping.Metaclass_MocapMapping_Request._TYPE_SUPPORT is None:
                _mocap_mapping.Metaclass_MocapMapping_Request.__import_type_support__()
            if _mocap_mapping.Metaclass_MocapMapping_Response._TYPE_SUPPORT is None:
                _mocap_mapping.Metaclass_MocapMapping_Response.__import_type_support__()


class MocapMapping(metaclass=Metaclass_MocapMapping):
    from genie_msgs.srv._mocap_mapping import MocapMapping_Request as Request
    from genie_msgs.srv._mocap_mapping import MocapMapping_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
