# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:srv/ForceInfo.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ForceInfo_Request(type):
    """Metaclass of message 'ForceInfo_Request'."""

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
                'genie_msgs.srv.ForceInfo_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__force_info__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__force_info__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__force_info__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__force_info__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__force_info__request

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


class ForceInfo_Request(metaclass=Metaclass_ForceInfo_Request):
    """Message class 'ForceInfo_Request'."""

    __slots__ = [
        '_header',
        '_force_id',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'force_id': 'uint32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.force_id = kwargs.get('force_id', int())

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
        if self.force_id != other.force_id:
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
    def force_id(self):
        """Message field 'force_id'."""
        return self._force_id

    @force_id.setter
    def force_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'force_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'force_id' field must be an unsigned integer in [0, 4294967295]"
        self._force_id = value


# Import statements for member types

# Member 'work_zero_force_data'
# Member 'tool_zero_force_data'
# Member 'zero_force_data'
import array  # noqa: E402, I100

# already imported above
# import builtins

import math  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_ForceInfo_Response(type):
    """Metaclass of message 'ForceInfo_Response'."""

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
                'genie_msgs.srv.ForceInfo_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__force_info__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__force_info__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__force_info__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__force_info__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__force_info__response

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


class ForceInfo_Response(metaclass=Metaclass_ForceInfo_Response):
    """Message class 'ForceInfo_Response'."""

    __slots__ = [
        '_res_header',
        '_exec_result',
        '_work_zero_force_data',
        '_tool_zero_force_data',
        '_zero_force_data',
    ]

    _fields_and_field_types = {
        'res_header': 'std_msgs/Header',
        'exec_result': 'uint8',
        'work_zero_force_data': 'sequence<double>',
        'tool_zero_force_data': 'sequence<double>',
        'zero_force_data': 'sequence<double>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.res_header = kwargs.get('res_header', Header())
        self.exec_result = kwargs.get('exec_result', int())
        self.work_zero_force_data = array.array('d', kwargs.get('work_zero_force_data', []))
        self.tool_zero_force_data = array.array('d', kwargs.get('tool_zero_force_data', []))
        self.zero_force_data = array.array('d', kwargs.get('zero_force_data', []))

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
        if self.exec_result != other.exec_result:
            return False
        if self.work_zero_force_data != other.work_zero_force_data:
            return False
        if self.tool_zero_force_data != other.tool_zero_force_data:
            return False
        if self.zero_force_data != other.zero_force_data:
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
    def exec_result(self):
        """Message field 'exec_result'."""
        return self._exec_result

    @exec_result.setter
    def exec_result(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'exec_result' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'exec_result' field must be an unsigned integer in [0, 255]"
        self._exec_result = value

    @builtins.property
    def work_zero_force_data(self):
        """Message field 'work_zero_force_data'."""
        return self._work_zero_force_data

    @work_zero_force_data.setter
    def work_zero_force_data(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'work_zero_force_data' array.array() must have the type code of 'd'"
            self._work_zero_force_data = value
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
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'work_zero_force_data' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._work_zero_force_data = array.array('d', value)

    @builtins.property
    def tool_zero_force_data(self):
        """Message field 'tool_zero_force_data'."""
        return self._tool_zero_force_data

    @tool_zero_force_data.setter
    def tool_zero_force_data(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'tool_zero_force_data' array.array() must have the type code of 'd'"
            self._tool_zero_force_data = value
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
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'tool_zero_force_data' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._tool_zero_force_data = array.array('d', value)

    @builtins.property
    def zero_force_data(self):
        """Message field 'zero_force_data'."""
        return self._zero_force_data

    @zero_force_data.setter
    def zero_force_data(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'zero_force_data' array.array() must have the type code of 'd'"
            self._zero_force_data = value
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
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'zero_force_data' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._zero_force_data = array.array('d', value)


class Metaclass_ForceInfo(type):
    """Metaclass of service 'ForceInfo'."""

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
                'genie_msgs.srv.ForceInfo')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__force_info

            from genie_msgs.srv import _force_info
            if _force_info.Metaclass_ForceInfo_Request._TYPE_SUPPORT is None:
                _force_info.Metaclass_ForceInfo_Request.__import_type_support__()
            if _force_info.Metaclass_ForceInfo_Response._TYPE_SUPPORT is None:
                _force_info.Metaclass_ForceInfo_Response.__import_type_support__()


class ForceInfo(metaclass=Metaclass_ForceInfo):
    from genie_msgs.srv._force_info import ForceInfo_Request as Request
    from genie_msgs.srv._force_info import ForceInfo_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
