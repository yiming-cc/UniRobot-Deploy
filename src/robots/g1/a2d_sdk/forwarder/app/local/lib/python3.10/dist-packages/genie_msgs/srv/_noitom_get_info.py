# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:srv/NoitomGetInfo.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_NoitomGetInfo_Request(type):
    """Metaclass of message 'NoitomGetInfo_Request'."""

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
                'genie_msgs.srv.NoitomGetInfo_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__noitom_get_info__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__noitom_get_info__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__noitom_get_info__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__noitom_get_info__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__noitom_get_info__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NoitomGetInfo_Request(metaclass=Metaclass_NoitomGetInfo_Request):
    """Message class 'NoitomGetInfo_Request'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

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
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


# Import statements for member types

import builtins  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_NoitomGetInfo_Response(type):
    """Metaclass of message 'NoitomGetInfo_Response'."""

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
                'genie_msgs.srv.NoitomGetInfo_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__noitom_get_info__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__noitom_get_info__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__noitom_get_info__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__noitom_get_info__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__noitom_get_info__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NoitomGetInfo_Response(metaclass=Metaclass_NoitomGetInfo_Response):
    """Message class 'NoitomGetInfo_Response'."""

    __slots__ = [
        '_device_sn',
        '_software_version',
        '_hardware_date',
        '_default_ip',
        '_default_port',
    ]

    _fields_and_field_types = {
        'device_sn': 'string',
        'software_version': 'string',
        'hardware_date': 'string',
        'default_ip': 'string',
        'default_port': 'uint16',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.device_sn = kwargs.get('device_sn', str())
        self.software_version = kwargs.get('software_version', str())
        self.hardware_date = kwargs.get('hardware_date', str())
        self.default_ip = kwargs.get('default_ip', str())
        self.default_port = kwargs.get('default_port', int())

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
        if self.device_sn != other.device_sn:
            return False
        if self.software_version != other.software_version:
            return False
        if self.hardware_date != other.hardware_date:
            return False
        if self.default_ip != other.default_ip:
            return False
        if self.default_port != other.default_port:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def device_sn(self):
        """Message field 'device_sn'."""
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'device_sn' field must be of type 'str'"
        self._device_sn = value

    @builtins.property
    def software_version(self):
        """Message field 'software_version'."""
        return self._software_version

    @software_version.setter
    def software_version(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'software_version' field must be of type 'str'"
        self._software_version = value

    @builtins.property
    def hardware_date(self):
        """Message field 'hardware_date'."""
        return self._hardware_date

    @hardware_date.setter
    def hardware_date(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'hardware_date' field must be of type 'str'"
        self._hardware_date = value

    @builtins.property
    def default_ip(self):
        """Message field 'default_ip'."""
        return self._default_ip

    @default_ip.setter
    def default_ip(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'default_ip' field must be of type 'str'"
        self._default_ip = value

    @builtins.property
    def default_port(self):
        """Message field 'default_port'."""
        return self._default_port

    @default_port.setter
    def default_port(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'default_port' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'default_port' field must be an unsigned integer in [0, 65535]"
        self._default_port = value


class Metaclass_NoitomGetInfo(type):
    """Metaclass of service 'NoitomGetInfo'."""

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
                'genie_msgs.srv.NoitomGetInfo')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__noitom_get_info

            from genie_msgs.srv import _noitom_get_info
            if _noitom_get_info.Metaclass_NoitomGetInfo_Request._TYPE_SUPPORT is None:
                _noitom_get_info.Metaclass_NoitomGetInfo_Request.__import_type_support__()
            if _noitom_get_info.Metaclass_NoitomGetInfo_Response._TYPE_SUPPORT is None:
                _noitom_get_info.Metaclass_NoitomGetInfo_Response.__import_type_support__()


class NoitomGetInfo(metaclass=Metaclass_NoitomGetInfo):
    from genie_msgs.srv._noitom_get_info import NoitomGetInfo_Request as Request
    from genie_msgs.srv._noitom_get_info import NoitomGetInfo_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
