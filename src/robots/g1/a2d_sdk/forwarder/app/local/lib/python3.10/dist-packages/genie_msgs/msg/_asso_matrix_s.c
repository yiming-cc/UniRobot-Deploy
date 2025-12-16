// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/AssoMatrix.idl
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
#include "genie_msgs/msg/detail/asso_matrix__struct.h"
#include "genie_msgs/msg/detail/asso_matrix__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool builtin_interfaces__msg__time__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * builtin_interfaces__msg__time__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__asso_matrix__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[39];
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
    assert(strncmp("genie_msgs.msg._asso_matrix.AssoMatrix", full_classname_dest, 38) == 0);
  }
  genie_msgs__msg__AssoMatrix * ros_message = _ros_message;
  {  // sensor_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "sensor_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->sensor_type = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // sensor_time
    PyObject * field = PyObject_GetAttrString(_pymsg, "sensor_time");
    if (!field) {
      return false;
    }
    if (!builtin_interfaces__msg__time__convert_from_py(field, &ros_message->sensor_time)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // asso_index
    PyObject * field = PyObject_GetAttrString(_pymsg, "asso_index");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->asso_index = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__asso_matrix__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of AssoMatrix */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._asso_matrix");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "AssoMatrix");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__AssoMatrix * ros_message = (genie_msgs__msg__AssoMatrix *)raw_ros_message;
  {  // sensor_type
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->sensor_type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "sensor_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // sensor_time
    PyObject * field = NULL;
    field = builtin_interfaces__msg__time__convert_to_py(&ros_message->sensor_time);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "sensor_time", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // asso_index
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->asso_index);
    {
      int rc = PyObject_SetAttrString(_pymessage, "asso_index", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
