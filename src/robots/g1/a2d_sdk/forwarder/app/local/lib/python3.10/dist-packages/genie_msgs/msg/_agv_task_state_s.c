// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/AGVTaskState.idl
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
#include "genie_msgs/msg/detail/agv_task_state__struct.h"
#include "genie_msgs/msg/detail/agv_task_state__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__agv_task_state__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[44];
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
    assert(strncmp("genie_msgs.msg._agv_task_state.AGVTaskState", full_classname_dest, 43) == 0);
  }
  genie_msgs__msg__AGVTaskState * ros_message = _ros_message;
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
  {  // task_uuid
    PyObject * field = PyObject_GetAttrString(_pymsg, "task_uuid");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->task_uuid = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // task_reqid
    PyObject * field = PyObject_GetAttrString(_pymsg, "task_reqid");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->task_reqid, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // curr_station_idx
    PyObject * field = PyObject_GetAttrString(_pymsg, "curr_station_idx");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->curr_station_idx = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // finish_state
    PyObject * field = PyObject_GetAttrString(_pymsg, "finish_state");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->finish_state = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__agv_task_state__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of AGVTaskState */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._agv_task_state");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "AGVTaskState");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__AGVTaskState * ros_message = (genie_msgs__msg__AGVTaskState *)raw_ros_message;
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
  {  // task_uuid
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->task_uuid);
    {
      int rc = PyObject_SetAttrString(_pymessage, "task_uuid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // task_reqid
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->task_reqid.data,
      strlen(ros_message->task_reqid.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "task_reqid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // curr_station_idx
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->curr_station_idx);
    {
      int rc = PyObject_SetAttrString(_pymessage, "curr_station_idx", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // finish_state
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->finish_state);
    {
      int rc = PyObject_SetAttrString(_pymessage, "finish_state", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
