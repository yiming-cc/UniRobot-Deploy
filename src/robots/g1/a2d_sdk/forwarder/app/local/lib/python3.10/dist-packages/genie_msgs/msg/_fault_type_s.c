// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/FaultType.idl
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
#include "genie_msgs/msg/detail/fault_type__struct.h"
#include "genie_msgs/msg/detail/fault_type__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__fault_type__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[37];
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
    assert(strncmp("genie_msgs.msg._fault_type.FaultType", full_classname_dest, 36) == 0);
  }
  genie_msgs__msg__FaultType * ros_message = _ros_message;
  {  // fault_code
    PyObject * field = PyObject_GetAttrString(_pymsg, "fault_code");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->fault_code = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }
  {  // severity
    PyObject * field = PyObject_GetAttrString(_pymsg, "severity");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->severity = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }
  {  // component
    PyObject * field = PyObject_GetAttrString(_pymsg, "component");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->component, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // description
    PyObject * field = PyObject_GetAttrString(_pymsg, "description");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->description, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // fault_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "fault_type");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->fault_type, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // guide
    PyObject * field = PyObject_GetAttrString(_pymsg, "guide");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->guide, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__fault_type__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of FaultType */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._fault_type");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "FaultType");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__FaultType * ros_message = (genie_msgs__msg__FaultType *)raw_ros_message;
  {  // fault_code
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->fault_code);
    {
      int rc = PyObject_SetAttrString(_pymessage, "fault_code", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // severity
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->severity);
    {
      int rc = PyObject_SetAttrString(_pymessage, "severity", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // component
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->component.data,
      strlen(ros_message->component.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "component", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // description
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->description.data,
      strlen(ros_message->description.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "description", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // fault_type
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->fault_type.data,
      strlen(ros_message->fault_type.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "fault_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // guide
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->guide.data,
      strlen(ros_message->guide.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "guide", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
