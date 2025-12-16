# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:srv/ArmGetCollisionLevel.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ArmGetCollisionLevel_Request(type):
    """Metaclass of message 'ArmGetCollisionLevel_Request'."""

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
                'genie_msgs.srv.ArmGetCollisionLevel_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__arm_get_collision_level__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__arm_get_collision_level__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__arm_get_collision_level__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__arm_get_collision_level__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__arm_get_collision_level__request

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


class ArmGetCollisionLevel_Request(metaclass=Metaclass_ArmGetCollisionLevel_Request):
    """Message class 'ArmGetCollisionLevel_Request'."""

    __slots__ = [
        '_header',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())

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


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ArmGetCollisionLevel_Response(type):
    """Metaclass of message 'ArmGetCollisionLevel_Response'."""

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
                'genie_msgs.srv.ArmGetCollisionLevel_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__arm_get_collision_level__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__arm_get_collision_level__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__arm_get_collision_level__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__arm_get_collision_level__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__arm_get_collision_level__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ArmGetCollisionLevel_Response(metaclass=Metaclass_ArmGetCollisionLevel_Response):
    """Message class 'ArmGetCollisionLevel_Response'."""

    __slots__ = [
        '_level',
        '_error_code',
    ]

    _fields_and_field_types = {
        'level': 'uint32',
        'error_code': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.level = kwargs.get('level', int())
        self.error_code = kwargs.get('error_code', int())

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
        if self.level != other.level:
            return False
        if self.error_code != other.error_code:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def level(self):
        """Message field 'level'."""
        return self._level

    @level.setter
    def level(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'level' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'level' field must be an unsigned integer in [0, 4294967295]"
        self._level = value

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
            assert value >= -2147483648 and value < 2147483648, \
                "The 'error_code' field must be an integer in [-2147483648, 2147483647]"
        self._error_code = value


class Metaclass_ArmGetCollisionLevel(type):
    """Metaclass of service 'ArmGetCollisionLevel'."""

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
                'genie_msgs.srv.ArmGetCollisionLevel')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__arm_get_collision_level

            from genie_msgs.srv import _arm_get_collision_level
            if _arm_get_collision_level.Metaclass_ArmGetCollisionLevel_Request._TYPE_SUPPORT is None:
                _arm_get_collision_level.Metaclass_ArmGetCollisionLevel_Request.__import_type_support__()
            if _arm_get_collision_level.Metaclass_ArmGetCollisionLevel_Response._TYPE_SUPPORT is None:
                _arm_get_collision_level.Metaclass_ArmGetCollisionLevel_Response.__import_type_support__()


class ArmGetCollisionLevel(metaclass=Metaclass_ArmGetCollisionLevel):
    from genie_msgs.srv._arm_get_collision_level import ArmGetCollisionLevel_Request as Request
    from genie_msgs.srv._arm_get_collision_level import ArmGetCollisionLevel_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
