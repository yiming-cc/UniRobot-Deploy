# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/SceneStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SceneStatus(type):
    """Metaclass of message 'SceneStatus'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'RUNNING': 0,
        'SWITCHING': 1,
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
                'genie_msgs.msg.SceneStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__scene_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__scene_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__scene_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__scene_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__scene_status

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'RUNNING': cls.__constants['RUNNING'],
            'SWITCHING': cls.__constants['SWITCHING'],
        }

    @property
    def RUNNING(self):
        """Message constant 'RUNNING'."""
        return Metaclass_SceneStatus.__constants['RUNNING']

    @property
    def SWITCHING(self):
        """Message constant 'SWITCHING'."""
        return Metaclass_SceneStatus.__constants['SWITCHING']


class SceneStatus(metaclass=Metaclass_SceneStatus):
    """
    Message class 'SceneStatus'.

    Constants:
      RUNNING
      SWITCHING
    """

    __slots__ = [
        '_header',
        '_scene_status',
        '_scene_name',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'scene_status': 'uint8',
        'scene_name': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.scene_status = kwargs.get('scene_status', int())
        self.scene_name = kwargs.get('scene_name', str())

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
        if self.scene_status != other.scene_status:
            return False
        if self.scene_name != other.scene_name:
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
    def scene_status(self):
        """Message field 'scene_status'."""
        return self._scene_status

    @scene_status.setter
    def scene_status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'scene_status' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'scene_status' field must be an unsigned integer in [0, 255]"
        self._scene_status = value

    @builtins.property
    def scene_name(self):
        """Message field 'scene_name'."""
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'scene_name' field must be of type 'str'"
        self._scene_name = value
