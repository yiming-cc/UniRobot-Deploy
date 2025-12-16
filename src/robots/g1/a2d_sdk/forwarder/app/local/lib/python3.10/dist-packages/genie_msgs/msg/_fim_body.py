# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/FimBody.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FimBody(type):
    """Metaclass of message 'FimBody'."""

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
                'genie_msgs.msg.FimBody')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__fim_body
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__fim_body
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__fim_body
            cls._TYPE_SUPPORT = module.type_support_msg__msg__fim_body
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__fim_body

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


class FimBody(metaclass=Metaclass_FimBody):
    """Message class 'FimBody'."""

    __slots__ = [
        '_header',
        '_fim_waist',
        '_waist_err_code',
        '_fim_lift',
        '_lift_err_code',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'fim_waist': 'uint8',
        'waist_err_code': 'uint16',
        'fim_lift': 'uint8',
        'lift_err_code': 'uint16',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.fim_waist = kwargs.get('fim_waist', int())
        self.waist_err_code = kwargs.get('waist_err_code', int())
        self.fim_lift = kwargs.get('fim_lift', int())
        self.lift_err_code = kwargs.get('lift_err_code', int())

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
        if self.fim_waist != other.fim_waist:
            return False
        if self.waist_err_code != other.waist_err_code:
            return False
        if self.fim_lift != other.fim_lift:
            return False
        if self.lift_err_code != other.lift_err_code:
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
    def fim_waist(self):
        """Message field 'fim_waist'."""
        return self._fim_waist

    @fim_waist.setter
    def fim_waist(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'fim_waist' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'fim_waist' field must be an unsigned integer in [0, 255]"
        self._fim_waist = value

    @builtins.property
    def waist_err_code(self):
        """Message field 'waist_err_code'."""
        return self._waist_err_code

    @waist_err_code.setter
    def waist_err_code(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'waist_err_code' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'waist_err_code' field must be an unsigned integer in [0, 65535]"
        self._waist_err_code = value

    @builtins.property
    def fim_lift(self):
        """Message field 'fim_lift'."""
        return self._fim_lift

    @fim_lift.setter
    def fim_lift(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'fim_lift' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'fim_lift' field must be an unsigned integer in [0, 255]"
        self._fim_lift = value

    @builtins.property
    def lift_err_code(self):
        """Message field 'lift_err_code'."""
        return self._lift_err_code

    @lift_err_code.setter
    def lift_err_code(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'lift_err_code' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'lift_err_code' field must be an unsigned integer in [0, 65535]"
        self._lift_err_code = value
