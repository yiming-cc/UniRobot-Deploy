# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/AGVTaskState.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AGVTaskState(type):
    """Metaclass of message 'AGVTaskState'."""

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
                'genie_msgs.msg.AGVTaskState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__agv_task_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__agv_task_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__agv_task_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__agv_task_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__agv_task_state

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


class AGVTaskState(metaclass=Metaclass_AGVTaskState):
    """Message class 'AGVTaskState'."""

    __slots__ = [
        '_header',
        '_task_uuid',
        '_task_reqid',
        '_curr_station_idx',
        '_finish_state',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'task_uuid': 'uint32',
        'task_reqid': 'string',
        'curr_station_idx': 'int32',
        'finish_state': 'uint32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.task_uuid = kwargs.get('task_uuid', int())
        self.task_reqid = kwargs.get('task_reqid', str())
        self.curr_station_idx = kwargs.get('curr_station_idx', int())
        self.finish_state = kwargs.get('finish_state', int())

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
        if self.task_uuid != other.task_uuid:
            return False
        if self.task_reqid != other.task_reqid:
            return False
        if self.curr_station_idx != other.curr_station_idx:
            return False
        if self.finish_state != other.finish_state:
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
    def task_uuid(self):
        """Message field 'task_uuid'."""
        return self._task_uuid

    @task_uuid.setter
    def task_uuid(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'task_uuid' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'task_uuid' field must be an unsigned integer in [0, 4294967295]"
        self._task_uuid = value

    @builtins.property
    def task_reqid(self):
        """Message field 'task_reqid'."""
        return self._task_reqid

    @task_reqid.setter
    def task_reqid(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'task_reqid' field must be of type 'str'"
        self._task_reqid = value

    @builtins.property
    def curr_station_idx(self):
        """Message field 'curr_station_idx'."""
        return self._curr_station_idx

    @curr_station_idx.setter
    def curr_station_idx(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'curr_station_idx' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'curr_station_idx' field must be an integer in [-2147483648, 2147483647]"
        self._curr_station_idx = value

    @builtins.property
    def finish_state(self):
        """Message field 'finish_state'."""
        return self._finish_state

    @finish_state.setter
    def finish_state(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'finish_state' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'finish_state' field must be an unsigned integer in [0, 4294967295]"
        self._finish_state = value
