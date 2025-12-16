# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/MocapNetwork.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MocapNetwork(type):
    """Metaclass of message 'MocapNetwork'."""

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
                'genie_msgs.msg.MocapNetwork')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__mocap_network
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__mocap_network
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__mocap_network
            cls._TYPE_SUPPORT = module.type_support_msg__msg__mocap_network
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__mocap_network

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


class MocapNetwork(metaclass=Metaclass_MocapNetwork):
    """Message class 'MocapNetwork'."""

    __slots__ = [
        '_header',
        '_device_name',
        '_is_connected',
        '_packet_loss_rate',
        '_latency',
        '_frequency',
        '_ip_address',
        '_remote_ip_address',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'device_name': 'string',
        'is_connected': 'boolean',
        'packet_loss_rate': 'float',
        'latency': 'float',
        'frequency': 'float',
        'ip_address': 'string',
        'remote_ip_address': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.device_name = kwargs.get('device_name', str())
        self.is_connected = kwargs.get('is_connected', bool())
        self.packet_loss_rate = kwargs.get('packet_loss_rate', float())
        self.latency = kwargs.get('latency', float())
        self.frequency = kwargs.get('frequency', float())
        self.ip_address = kwargs.get('ip_address', str())
        self.remote_ip_address = kwargs.get('remote_ip_address', str())

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
        if self.device_name != other.device_name:
            return False
        if self.is_connected != other.is_connected:
            return False
        if self.packet_loss_rate != other.packet_loss_rate:
            return False
        if self.latency != other.latency:
            return False
        if self.frequency != other.frequency:
            return False
        if self.ip_address != other.ip_address:
            return False
        if self.remote_ip_address != other.remote_ip_address:
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
    def device_name(self):
        """Message field 'device_name'."""
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'device_name' field must be of type 'str'"
        self._device_name = value

    @builtins.property
    def is_connected(self):
        """Message field 'is_connected'."""
        return self._is_connected

    @is_connected.setter
    def is_connected(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_connected' field must be of type 'bool'"
        self._is_connected = value

    @builtins.property
    def packet_loss_rate(self):
        """Message field 'packet_loss_rate'."""
        return self._packet_loss_rate

    @packet_loss_rate.setter
    def packet_loss_rate(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'packet_loss_rate' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'packet_loss_rate' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._packet_loss_rate = value

    @builtins.property
    def latency(self):
        """Message field 'latency'."""
        return self._latency

    @latency.setter
    def latency(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'latency' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'latency' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._latency = value

    @builtins.property
    def frequency(self):
        """Message field 'frequency'."""
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'frequency' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'frequency' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._frequency = value

    @builtins.property
    def ip_address(self):
        """Message field 'ip_address'."""
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'ip_address' field must be of type 'str'"
        self._ip_address = value

    @builtins.property
    def remote_ip_address(self):
        """Message field 'remote_ip_address'."""
        return self._remote_ip_address

    @remote_ip_address.setter
    def remote_ip_address(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'remote_ip_address' field must be of type 'str'"
        self._remote_ip_address = value
