# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/AGVTargetStation.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AGVTargetStation(type):
    """Metaclass of message 'AGVTargetStation'."""

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
                'genie_msgs.msg.AGVTargetStation')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__agv_target_station
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__agv_target_station
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__agv_target_station
            cls._TYPE_SUPPORT = module.type_support_msg__msg__agv_target_station
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__agv_target_station

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


class AGVTargetStation(metaclass=Metaclass_AGVTargetStation):
    """Message class 'AGVTargetStation'."""

    __slots__ = [
        '_header',
        '_station_id',
        '_station_name',
        '_station_action',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'station_id': 'uint32',
        'station_name': 'string',
        'station_action': 'uint32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.station_id = kwargs.get('station_id', int())
        self.station_name = kwargs.get('station_name', str())
        self.station_action = kwargs.get('station_action', int())

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
        if self.station_id != other.station_id:
            return False
        if self.station_name != other.station_name:
            return False
        if self.station_action != other.station_action:
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
    def station_id(self):
        """Message field 'station_id'."""
        return self._station_id

    @station_id.setter
    def station_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'station_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'station_id' field must be an unsigned integer in [0, 4294967295]"
        self._station_id = value

    @builtins.property
    def station_name(self):
        """Message field 'station_name'."""
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'station_name' field must be of type 'str'"
        self._station_name = value

    @builtins.property
    def station_action(self):
        """Message field 'station_action'."""
        return self._station_action

    @station_action.setter
    def station_action(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'station_action' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'station_action' field must be an unsigned integer in [0, 4294967295]"
        self._station_action = value
