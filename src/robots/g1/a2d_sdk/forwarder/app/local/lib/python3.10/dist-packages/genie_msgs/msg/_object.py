# generated from rosidl_generator_py/resource/_idl.py.em
# with input from genie_msgs:msg/Object.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Object(type):
    """Metaclass of message 'Object'."""

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
                'genie_msgs.msg.Object')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__object
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__object
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__object
            cls._TYPE_SUPPORT = module.type_support_msg__msg__object
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__object

            from genie_msgs.msg import AssoMatrix
            if AssoMatrix.__class__._TYPE_SUPPORT is None:
                AssoMatrix.__class__.__import_type_support__()

            from genie_msgs.msg import BevObject
            if BevObject.__class__._TYPE_SUPPORT is None:
                BevObject.__class__.__import_type_support__()

            from genie_msgs.msg import CameraObject
            if CameraObject.__class__._TYPE_SUPPORT is None:
                CameraObject.__class__.__import_type_support__()

            from genie_msgs.msg import GraspPoint
            if GraspPoint.__class__._TYPE_SUPPORT is None:
                GraspPoint.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Object(metaclass=Metaclass_Object):
    """Message class 'Object'."""

    __slots__ = [
        '_track_id',
        '_cam_obj',
        '_bev_obj',
        '_grasp_point',
        '_asso_matrix',
        '_sensor_type',
        '_class_type',
        '_sub_type',
        '_grasp_type',
        '_motion_status',
        '_tracking_time',
        '_tracking_score',
    ]

    _fields_and_field_types = {
        'track_id': 'int32',
        'cam_obj': 'sequence<genie_msgs/CameraObject>',
        'bev_obj': 'genie_msgs/BevObject',
        'grasp_point': 'sequence<genie_msgs/GraspPoint>',
        'asso_matrix': 'sequence<genie_msgs/AssoMatrix>',
        'sensor_type': 'int32',
        'class_type': 'int32',
        'sub_type': 'int32',
        'grasp_type': 'int32',
        'motion_status': 'int32',
        'tracking_time': 'float',
        'tracking_score': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'CameraObject')),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'BevObject'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'GraspPoint')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['genie_msgs', 'msg'], 'AssoMatrix')),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.track_id = kwargs.get('track_id', int())
        self.cam_obj = kwargs.get('cam_obj', [])
        from genie_msgs.msg import BevObject
        self.bev_obj = kwargs.get('bev_obj', BevObject())
        self.grasp_point = kwargs.get('grasp_point', [])
        self.asso_matrix = kwargs.get('asso_matrix', [])
        self.sensor_type = kwargs.get('sensor_type', int())
        self.class_type = kwargs.get('class_type', int())
        self.sub_type = kwargs.get('sub_type', int())
        self.grasp_type = kwargs.get('grasp_type', int())
        self.motion_status = kwargs.get('motion_status', int())
        self.tracking_time = kwargs.get('tracking_time', float())
        self.tracking_score = kwargs.get('tracking_score', float())

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
        if self.track_id != other.track_id:
            return False
        if self.cam_obj != other.cam_obj:
            return False
        if self.bev_obj != other.bev_obj:
            return False
        if self.grasp_point != other.grasp_point:
            return False
        if self.asso_matrix != other.asso_matrix:
            return False
        if self.sensor_type != other.sensor_type:
            return False
        if self.class_type != other.class_type:
            return False
        if self.sub_type != other.sub_type:
            return False
        if self.grasp_type != other.grasp_type:
            return False
        if self.motion_status != other.motion_status:
            return False
        if self.tracking_time != other.tracking_time:
            return False
        if self.tracking_score != other.tracking_score:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def track_id(self):
        """Message field 'track_id'."""
        return self._track_id

    @track_id.setter
    def track_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'track_id' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'track_id' field must be an integer in [-2147483648, 2147483647]"
        self._track_id = value

    @builtins.property
    def cam_obj(self):
        """Message field 'cam_obj'."""
        return self._cam_obj

    @cam_obj.setter
    def cam_obj(self, value):
        if __debug__:
            from genie_msgs.msg import CameraObject
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
                 all(isinstance(v, CameraObject) for v in value) and
                 True), \
                "The 'cam_obj' field must be a set or sequence and each value of type 'CameraObject'"
        self._cam_obj = value

    @builtins.property
    def bev_obj(self):
        """Message field 'bev_obj'."""
        return self._bev_obj

    @bev_obj.setter
    def bev_obj(self, value):
        if __debug__:
            from genie_msgs.msg import BevObject
            assert \
                isinstance(value, BevObject), \
                "The 'bev_obj' field must be a sub message of type 'BevObject'"
        self._bev_obj = value

    @builtins.property
    def grasp_point(self):
        """Message field 'grasp_point'."""
        return self._grasp_point

    @grasp_point.setter
    def grasp_point(self, value):
        if __debug__:
            from genie_msgs.msg import GraspPoint
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
                 all(isinstance(v, GraspPoint) for v in value) and
                 True), \
                "The 'grasp_point' field must be a set or sequence and each value of type 'GraspPoint'"
        self._grasp_point = value

    @builtins.property
    def asso_matrix(self):
        """Message field 'asso_matrix'."""
        return self._asso_matrix

    @asso_matrix.setter
    def asso_matrix(self, value):
        if __debug__:
            from genie_msgs.msg import AssoMatrix
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
                 all(isinstance(v, AssoMatrix) for v in value) and
                 True), \
                "The 'asso_matrix' field must be a set or sequence and each value of type 'AssoMatrix'"
        self._asso_matrix = value

    @builtins.property
    def sensor_type(self):
        """Message field 'sensor_type'."""
        return self._sensor_type

    @sensor_type.setter
    def sensor_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'sensor_type' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'sensor_type' field must be an integer in [-2147483648, 2147483647]"
        self._sensor_type = value

    @builtins.property
    def class_type(self):
        """Message field 'class_type'."""
        return self._class_type

    @class_type.setter
    def class_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'class_type' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'class_type' field must be an integer in [-2147483648, 2147483647]"
        self._class_type = value

    @builtins.property
    def sub_type(self):
        """Message field 'sub_type'."""
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'sub_type' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'sub_type' field must be an integer in [-2147483648, 2147483647]"
        self._sub_type = value

    @builtins.property
    def grasp_type(self):
        """Message field 'grasp_type'."""
        return self._grasp_type

    @grasp_type.setter
    def grasp_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'grasp_type' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'grasp_type' field must be an integer in [-2147483648, 2147483647]"
        self._grasp_type = value

    @builtins.property
    def motion_status(self):
        """Message field 'motion_status'."""
        return self._motion_status

    @motion_status.setter
    def motion_status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'motion_status' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'motion_status' field must be an integer in [-2147483648, 2147483647]"
        self._motion_status = value

    @builtins.property
    def tracking_time(self):
        """Message field 'tracking_time'."""
        return self._tracking_time

    @tracking_time.setter
    def tracking_time(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'tracking_time' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'tracking_time' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._tracking_time = value

    @builtins.property
    def tracking_score(self):
        """Message field 'tracking_score'."""
        return self._tracking_score

    @tracking_score.setter
    def tracking_score(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'tracking_score' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'tracking_score' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._tracking_score = value
