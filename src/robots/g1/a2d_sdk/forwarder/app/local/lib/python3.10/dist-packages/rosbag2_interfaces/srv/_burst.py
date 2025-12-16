# generated from rosidl_generator_py/resource/_idl.py.em
# with input from rosbag2_interfaces:srv/Burst.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Burst_Request(type):
    """Metaclass of message 'Burst_Request'."""

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
            module = import_type_support('rosbag2_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'rosbag2_interfaces.srv.Burst_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__burst__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__burst__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__burst__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__burst__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__burst__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Burst_Request(metaclass=Metaclass_Burst_Request):
    """Message class 'Burst_Request'."""

    __slots__ = [
        '_num_messages',
    ]

    _fields_and_field_types = {
        'num_messages': 'uint64',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.num_messages = kwargs.get('num_messages', int())

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
        if self.num_messages != other.num_messages:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def num_messages(self):
        """Message field 'num_messages'."""
        return self._num_messages

    @num_messages.setter
    def num_messages(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'num_messages' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'num_messages' field must be an unsigned integer in [0, 18446744073709551615]"
        self._num_messages = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Burst_Response(type):
    """Metaclass of message 'Burst_Response'."""

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
            module = import_type_support('rosbag2_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'rosbag2_interfaces.srv.Burst_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__burst__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__burst__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__burst__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__burst__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__burst__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Burst_Response(metaclass=Metaclass_Burst_Response):
    """Message class 'Burst_Response'."""

    __slots__ = [
        '_actually_burst',
    ]

    _fields_and_field_types = {
        'actually_burst': 'uint64',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.actually_burst = kwargs.get('actually_burst', int())

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
        if self.actually_burst != other.actually_burst:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def actually_burst(self):
        """Message field 'actually_burst'."""
        return self._actually_burst

    @actually_burst.setter
    def actually_burst(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'actually_burst' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'actually_burst' field must be an unsigned integer in [0, 18446744073709551615]"
        self._actually_burst = value


class Metaclass_Burst(type):
    """Metaclass of service 'Burst'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('rosbag2_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'rosbag2_interfaces.srv.Burst')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__burst

            from rosbag2_interfaces.srv import _burst
            if _burst.Metaclass_Burst_Request._TYPE_SUPPORT is None:
                _burst.Metaclass_Burst_Request.__import_type_support__()
            if _burst.Metaclass_Burst_Response._TYPE_SUPPORT is None:
                _burst.Metaclass_Burst_Response.__import_type_support__()


class Burst(metaclass=Metaclass_Burst):
    from rosbag2_interfaces.srv._burst import Burst_Request as Request
    from rosbag2_interfaces.srv._burst import Burst_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
