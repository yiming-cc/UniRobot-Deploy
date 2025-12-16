# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:srv/FeatSetCtrlMode.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FeatSetCtrlMode_Request(type):
    """Metaclass of message 'FeatSetCtrlMode_Request'."""

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
                'genie_msgs.srv.FeatSetCtrlMode_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__feat_set_ctrl_mode__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__feat_set_ctrl_mode__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__feat_set_ctrl_mode__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__feat_set_ctrl_mode__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__feat_set_ctrl_mode__request

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


class FeatSetCtrlMode_Request(metaclass=Metaclass_FeatSetCtrlMode_Request):
    """Message class 'FeatSetCtrlMode_Request'."""

    __slots__ = [
        '_header',
        '_online',
        '_remote_mode',
        '_ctrl_mode',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'online': 'uint8',
        'remote_mode': 'uint8',
        'ctrl_mode': 'uint16',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.online = kwargs.get('online', int())
        self.remote_mode = kwargs.get('remote_mode', int())
        self.ctrl_mode = kwargs.get('ctrl_mode', int())

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
        if self.online != other.online:
            return False
        if self.remote_mode != other.remote_mode:
            return False
        if self.ctrl_mode != other.ctrl_mode:
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
    def online(self):
        """Message field 'online'."""
        return self._online

    @online.setter
    def online(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'online' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'online' field must be an unsigned integer in [0, 255]"
        self._online = value

    @builtins.property
    def remote_mode(self):
        """Message field 'remote_mode'."""
        return self._remote_mode

    @remote_mode.setter
    def remote_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'remote_mode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'remote_mode' field must be an unsigned integer in [0, 255]"
        self._remote_mode = value

    @builtins.property
    def ctrl_mode(self):
        """Message field 'ctrl_mode'."""
        return self._ctrl_mode

    @ctrl_mode.setter
    def ctrl_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'ctrl_mode' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'ctrl_mode' field must be an unsigned integer in [0, 65535]"
        self._ctrl_mode = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_FeatSetCtrlMode_Response(type):
    """Metaclass of message 'FeatSetCtrlMode_Response'."""

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
                'genie_msgs.srv.FeatSetCtrlMode_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__feat_set_ctrl_mode__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__feat_set_ctrl_mode__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__feat_set_ctrl_mode__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__feat_set_ctrl_mode__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__feat_set_ctrl_mode__response

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


class FeatSetCtrlMode_Response(metaclass=Metaclass_FeatSetCtrlMode_Response):
    """Message class 'FeatSetCtrlMode_Response'."""

    __slots__ = [
        '_res_header',
        '_exec_result',
    ]

    _fields_and_field_types = {
        'res_header': 'std_msgs/Header',
        'exec_result': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.res_header = kwargs.get('res_header', Header())
        self.exec_result = kwargs.get('exec_result', int())

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


class Metaclass_FeatSetCtrlMode(type):
    """Metaclass of service 'FeatSetCtrlMode'."""

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
                'genie_msgs.srv.FeatSetCtrlMode')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__feat_set_ctrl_mode

            from genie_msgs.srv import _feat_set_ctrl_mode
            if _feat_set_ctrl_mode.Metaclass_FeatSetCtrlMode_Request._TYPE_SUPPORT is None:
                _feat_set_ctrl_mode.Metaclass_FeatSetCtrlMode_Request.__import_type_support__()
            if _feat_set_ctrl_mode.Metaclass_FeatSetCtrlMode_Response._TYPE_SUPPORT is None:
                _feat_set_ctrl_mode.Metaclass_FeatSetCtrlMode_Response.__import_type_support__()


class FeatSetCtrlMode(metaclass=Metaclass_FeatSetCtrlMode):
    from genie_msgs.srv._feat_set_ctrl_mode import FeatSetCtrlMode_Request as Request
    from genie_msgs.srv._feat_set_ctrl_mode import FeatSetCtrlMode_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
