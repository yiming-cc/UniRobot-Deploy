# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:srv/AGVNewTask.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AGVNewTask_Request(type):
    """Metaclass of message 'AGVNewTask_Request'."""

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
                'genie_msgs.srv.AGVNewTask_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__agv_new_task__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__agv_new_task__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__agv_new_task__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__agv_new_task__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__agv_new_task__request

            from genie_msgs.msg import TargetStation
            if TargetStation.__class__._TYPE_SUPPORT is None:
                TargetStation.__class__.__import_type_support__()

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


class AGVNewTask_Request(metaclass=Metaclass_AGVNewTask_Request):
    """Message class 'AGVNewTask_Request'."""

    __slots__ = [
        '_header',
        '_task_reqid',
        '_map_id',
        '_target_station_list',
        '_is_loop',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'task_reqid': 'string',
        'map_id': 'uint32',
        'target_station_list': 'sequence<genie_msgs/TargetStation>',
        'is_loop': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'TargetStation')),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.task_reqid = kwargs.get('task_reqid', str())
        self.map_id = kwargs.get('map_id', int())
        self.target_station_list = kwargs.get('target_station_list', [])
        self.is_loop = kwargs.get('is_loop', bool())

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
        if self.task_reqid != other.task_reqid:
            return False
        if self.map_id != other.map_id:
            return False
        if self.target_station_list != other.target_station_list:
            return False
        if self.is_loop != other.is_loop:
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
    def map_id(self):
        """Message field 'map_id'."""
        return self._map_id

    @map_id.setter
    def map_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'map_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'map_id' field must be an unsigned integer in [0, 4294967295]"
        self._map_id = value

    @builtins.property
    def target_station_list(self):
        """Message field 'target_station_list'."""
        return self._target_station_list

    @target_station_list.setter
    def target_station_list(self, value):
        if __debug__:
            from genie_msgs.msg import TargetStation
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
                 all(isinstance(v, TargetStation) for v in value) and
                 True), \
                "The 'target_station_list' field must be a set or sequence and each value of type 'TargetStation'"
        self._target_station_list = value

    @builtins.property
    def is_loop(self):
        """Message field 'is_loop'."""
        return self._is_loop

    @is_loop.setter
    def is_loop(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_loop' field must be of type 'bool'"
        self._is_loop = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AGVNewTask_Response(type):
    """Metaclass of message 'AGVNewTask_Response'."""

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
                'genie_msgs.srv.AGVNewTask_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__agv_new_task__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__agv_new_task__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__agv_new_task__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__agv_new_task__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__agv_new_task__response

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


class AGVNewTask_Response(metaclass=Metaclass_AGVNewTask_Response):
    """Message class 'AGVNewTask_Response'."""

    __slots__ = [
        '_res_header',
        '_req_result',
        '_ret_code',
        '_task_uuid',
        '_task_reqid',
    ]

    _fields_and_field_types = {
        'res_header': 'std_msgs/Header',
        'req_result': 'uint32',
        'ret_code': 'uint32',
        'task_uuid': 'uint32',
        'task_reqid': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.res_header = kwargs.get('res_header', Header())
        self.req_result = kwargs.get('req_result', int())
        self.ret_code = kwargs.get('ret_code', int())
        self.task_uuid = kwargs.get('task_uuid', int())
        self.task_reqid = kwargs.get('task_reqid', str())

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
        if self.req_result != other.req_result:
            return False
        if self.ret_code != other.ret_code:
            return False
        if self.task_uuid != other.task_uuid:
            return False
        if self.task_reqid != other.task_reqid:
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
    def req_result(self):
        """Message field 'req_result'."""
        return self._req_result

    @req_result.setter
    def req_result(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'req_result' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'req_result' field must be an unsigned integer in [0, 4294967295]"
        self._req_result = value

    @builtins.property
    def ret_code(self):
        """Message field 'ret_code'."""
        return self._ret_code

    @ret_code.setter
    def ret_code(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'ret_code' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'ret_code' field must be an unsigned integer in [0, 4294967295]"
        self._ret_code = value

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


class Metaclass_AGVNewTask(type):
    """Metaclass of service 'AGVNewTask'."""

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
                'genie_msgs.srv.AGVNewTask')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__agv_new_task

            from genie_msgs.srv import _agv_new_task
            if _agv_new_task.Metaclass_AGVNewTask_Request._TYPE_SUPPORT is None:
                _agv_new_task.Metaclass_AGVNewTask_Request.__import_type_support__()
            if _agv_new_task.Metaclass_AGVNewTask_Response._TYPE_SUPPORT is None:
                _agv_new_task.Metaclass_AGVNewTask_Response.__import_type_support__()


class AGVNewTask(metaclass=Metaclass_AGVNewTask):
    from genie_msgs.srv._agv_new_task import AGVNewTask_Request as Request
    from genie_msgs.srv._agv_new_task import AGVNewTask_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
