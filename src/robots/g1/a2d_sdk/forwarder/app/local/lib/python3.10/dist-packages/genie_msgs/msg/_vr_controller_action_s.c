// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/VRControllerAction.idl
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
#include "genie_msgs/msg/detail/vr_controller_action__struct.h"
#include "genie_msgs/msg/detail/vr_controller_action__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__vr_controller_action__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[56];
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
    assert(strncmp("genie_msgs.msg._vr_controller_action.VRControllerAction", full_classname_dest, 55) == 0);
  }
  genie_msgs__msg__VRControllerAction * ros_message = _ros_message;
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
  {  // left_amplitude
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_amplitude");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->left_amplitude = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // right_amplitude
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_amplitude");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->right_amplitude = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // left_duration_ms
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_duration_ms");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->left_duration_ms = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // right_duration_ms
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_duration_ms");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->right_duration_ms = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // left_frequency_hz
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_frequency_hz");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->left_frequency_hz = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // right_frequency_hz
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_frequency_hz");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->right_frequency_hz = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__vr_controller_action__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of VRControllerAction */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._vr_controller_action");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "VRControllerAction");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__VRControllerAction * ros_message = (genie_msgs__msg__VRControllerAction *)raw_ros_message;
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
  {  // left_amplitude
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->left_amplitude);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_amplitude", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_amplitude
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->right_amplitude);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_amplitude", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_duration_ms
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->left_duration_ms);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_duration_ms", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_duration_ms
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->right_duration_ms);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_duration_ms", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_frequency_hz
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->left_frequency_hz);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_frequency_hz", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_frequency_hz
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->right_frequency_hz);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_frequency_hz", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
