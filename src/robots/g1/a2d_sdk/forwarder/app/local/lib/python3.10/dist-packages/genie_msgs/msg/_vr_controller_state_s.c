// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/VRControllerState.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "genie_msgs/msg/detail/vr_controller_state__struct.h"
#include "genie_msgs/msg/detail/vr_controller_state__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool geometry_msgs__msg__vector3__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * geometry_msgs__msg__vector3__convert_to_py(void * raw_ros_message);
ROSIDL_GENERATOR_C_IMPORT
bool geometry_msgs__msg__quaternion__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * geometry_msgs__msg__quaternion__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__vr_controller_state__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[54];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("genie_msgs.msg._vr_controller_state.VRControllerState", full_classname_dest, 53) == 0);
  }
  genie_msgs__msg__VRControllerState * ros_message = _ros_message;
  {  // name
    PyObject * field = PyObject_GetAttrString(_pymsg, "name");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->name, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // id
    PyObject * field = PyObject_GetAttrString(_pymsg, "id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->id = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // key_one
    PyObject * field = PyObject_GetAttrString(_pymsg, "key_one");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->key_one = (Py_True == field);
    Py_DECREF(field);
  }
  {  // key_two
    PyObject * field = PyObject_GetAttrString(_pymsg, "key_two");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->key_two = (Py_True == field);
    Py_DECREF(field);
  }
  {  // hand_trig
    PyObject * field = PyObject_GetAttrString(_pymsg, "hand_trig");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->hand_trig = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // index_trig
    PyObject * field = PyObject_GetAttrString(_pymsg, "index_trig");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->index_trig = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // axis_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "axis_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->axis_x = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // axis_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "axis_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->axis_y = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // axis_click
    PyObject * field = PyObject_GetAttrString(_pymsg, "axis_click");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->axis_click = (Py_True == field);
    Py_DECREF(field);
  }
  {  // position
    PyObject * field = PyObject_GetAttrString(_pymsg, "position");
    if (!field) {
      return false;
    }
    if (!geometry_msgs__msg__vector3__convert_from_py(field, &ros_message->position)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // orientation
    PyObject * field = PyObject_GetAttrString(_pymsg, "orientation");
    if (!field) {
      return false;
    }
    if (!geometry_msgs__msg__quaternion__convert_from_py(field, &ros_message->orientation)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__vr_controller_state__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of VRControllerState */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._vr_controller_state");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "VRControllerState");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__VRControllerState * ros_message = (genie_msgs__msg__VRControllerState *)raw_ros_message;
  {  // name
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->name.data,
      strlen(ros_message->name.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "name", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // id
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // key_one
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->key_one ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "key_one", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // key_two
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->key_two ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "key_two", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // hand_trig
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->hand_trig);
    {
      int rc = PyObject_SetAttrString(_pymessage, "hand_trig", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // index_trig
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->index_trig);
    {
      int rc = PyObject_SetAttrString(_pymessage, "index_trig", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // axis_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->axis_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "axis_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // axis_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->axis_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "axis_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // axis_click
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->axis_click ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "axis_click", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // position
    PyObject * field = NULL;
    field = geometry_msgs__msg__vector3__convert_to_py(&ros_message->position);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "position", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // orientation
    PyObject * field = NULL;
    field = geometry_msgs__msg__quaternion__convert_to_py(&ros_message->orientation);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "orientation", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
