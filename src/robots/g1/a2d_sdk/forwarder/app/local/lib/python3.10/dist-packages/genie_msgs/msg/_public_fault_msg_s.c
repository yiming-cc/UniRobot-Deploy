// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/PublicFaultMsg.idl
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
#include "genie_msgs/msg/detail/public_fault_msg__struct.h"
#include "genie_msgs/msg/detail/public_fault_msg__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

// Nested array functions includes
#include "genie_msgs/msg/detail/fault_type__functions.h"
// end nested array functions include
ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);
bool genie_msgs__msg__fault_type__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__fault_type__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__public_fault_msg__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[48];
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
    assert(strncmp("genie_msgs.msg._public_fault_msg.PublicFaultMsg", full_classname_dest, 47) == 0);
  }
  genie_msgs__msg__PublicFaultMsg * ros_message = _ros_message;
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
  {  // fault_codes
    PyObject * field = PyObject_GetAttrString(_pymsg, "fault_codes");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'fault_codes'");
    if (!seq_field) {
      Py_DECREF(field);
      return false;
    }
    Py_ssize_t size = PySequence_Size(field);
    if (-1 == size) {
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    if (!genie_msgs__msg__FaultType__Sequence__init(&(ros_message->fault_codes), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__FaultType__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__FaultType * dest = ros_message->fault_codes.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!genie_msgs__msg__fault_type__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // publish_ptp_ts
    PyObject * field = PyObject_GetAttrString(_pymsg, "publish_ptp_ts");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->publish_ptp_ts = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }
  {  // publisher_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "publisher_id");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->publisher_id, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // counter
    PyObject * field = PyObject_GetAttrString(_pymsg, "counter");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->counter = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }
  {  // publish_ts
    PyObject * field = PyObject_GetAttrString(_pymsg, "publish_ts");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->publish_ts = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__public_fault_msg__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of PublicFaultMsg */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._public_fault_msg");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "PublicFaultMsg");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__PublicFaultMsg * ros_message = (genie_msgs__msg__PublicFaultMsg *)raw_ros_message;
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
  {  // fault_codes
    PyObject * field = NULL;
    size_t size = ros_message->fault_codes.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__FaultType * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->fault_codes.data[i]);
      PyObject * pyitem = genie_msgs__msg__fault_type__convert_to_py(item);
      if (!pyitem) {
        Py_DECREF(field);
        return NULL;
      }
      int rc = PyList_SetItem(field, i, pyitem);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "fault_codes", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // publish_ptp_ts
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->publish_ptp_ts);
    {
      int rc = PyObject_SetAttrString(_pymessage, "publish_ptp_ts", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // publisher_id
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->publisher_id.data,
      strlen(ros_message->publisher_id.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "publisher_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // counter
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->counter);
    {
      int rc = PyObject_SetAttrString(_pymessage, "counter", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // publish_ts
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->publish_ts);
    {
      int rc = PyObject_SetAttrString(_pymessage, "publish_ts", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
