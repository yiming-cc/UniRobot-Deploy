// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/SetAGVInfo.idl
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
#include "genie_msgs/msg/detail/set_agv_info__struct.h"
#include "genie_msgs/msg/detail/set_agv_info__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__set_agv_info__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[40];
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
    assert(strncmp("genie_msgs.msg._set_agv_info.SetAGVInfo", full_classname_dest, 39) == 0);
  }
  genie_msgs__msg__SetAGVInfo * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // set_max_linear_speed
    PyObject * field = PyObject_GetAttrString(_pymsg, "set_max_linear_speed");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->set_max_linear_speed = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // set_max_angular_speed
    PyObject * field = PyObject_GetAttrString(_pymsg, "set_max_angular_speed");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->set_max_angular_speed = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // set_min_collision_distance
    PyObject * field = PyObject_GetAttrString(_pymsg, "set_min_collision_distance");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->set_min_collision_distance = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__set_agv_info__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of SetAGVInfo */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._set_agv_info");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "SetAGVInfo");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__SetAGVInfo * ros_message = (genie_msgs__msg__SetAGVInfo *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // set_max_linear_speed
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->set_max_linear_speed);
    {
      int rc = PyObject_SetAttrString(_pymessage, "set_max_linear_speed", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // set_max_angular_speed
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->set_max_angular_speed);
    {
      int rc = PyObject_SetAttrString(_pymessage, "set_max_angular_speed", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // set_min_collision_distance
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->set_min_collision_distance);
    {
      int rc = PyObject_SetAttrString(_pymessage, "set_min_collision_distance", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
