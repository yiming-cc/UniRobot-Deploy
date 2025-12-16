// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/VRNetwork.idl
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
#include "genie_msgs/msg/detail/vr_network__struct.h"
#include "genie_msgs/msg/detail/vr_network__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__vr_network__convert_from_py(PyObject * _pymsg, void * _ros_message)
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
    assert(strncmp("genie_msgs.msg._vr_network.VRNetwork", full_classname_dest, 36) == 0);
  }
  genie_msgs__msg__VRNetwork * ros_message = _ros_message;
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
  {  // device_name
    PyObject * field = PyObject_GetAttrString(_pymsg, "device_name");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->device_name, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // is_connected
    PyObject * field = PyObject_GetAttrString(_pymsg, "is_connected");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->is_connected = (Py_True == field);
    Py_DECREF(field);
  }
  {  // packet_loss_rate
    PyObject * field = PyObject_GetAttrString(_pymsg, "packet_loss_rate");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->packet_loss_rate = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // latency
    PyObject * field = PyObject_GetAttrString(_pymsg, "latency");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->latency = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // frequency
    PyObject * field = PyObject_GetAttrString(_pymsg, "frequency");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->frequency = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ip_address
    PyObject * field = PyObject_GetAttrString(_pymsg, "ip_address");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->ip_address, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // remote_ip_address
    PyObject * field = PyObject_GetAttrString(_pymsg, "remote_ip_address");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->remote_ip_address, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__vr_network__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of VRNetwork */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._vr_network");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "VRNetwork");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__VRNetwork * ros_message = (genie_msgs__msg__VRNetwork *)raw_ros_message;
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
  {  // device_name
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->device_name.data,
      strlen(ros_message->device_name.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "device_name", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // is_connected
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->is_connected ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "is_connected", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // packet_loss_rate
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->packet_loss_rate);
    {
      int rc = PyObject_SetAttrString(_pymessage, "packet_loss_rate", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // latency
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->latency);
    {
      int rc = PyObject_SetAttrString(_pymessage, "latency", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // frequency
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->frequency);
    {
      int rc = PyObject_SetAttrString(_pymessage, "frequency", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ip_address
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->ip_address.data,
      strlen(ros_message->ip_address.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "ip_address", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // remote_ip_address
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->remote_ip_address.data,
      strlen(ros_message->remote_ip_address.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "remote_ip_address", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
