// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/WholeBodyStatus.idl
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
#include "genie_msgs/msg/detail/whole_body_status__struct.h"
#include "genie_msgs/msg/detail/whole_body_status__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__whole_body_status__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[50];
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
    assert(strncmp("genie_msgs.msg._whole_body_status.WholeBodyStatus", full_classname_dest, 49) == 0);
  }
  genie_msgs__msg__WholeBodyStatus * ros_message = _ros_message;
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
  {  // right_arm_error
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_arm_error");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->right_arm_error = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // left_arm_error
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_arm_error");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->left_arm_error = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // right_arm_control
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_arm_control");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->right_arm_control = (Py_True == field);
    Py_DECREF(field);
  }
  {  // left_arm_control
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_arm_control");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->left_arm_control = (Py_True == field);
    Py_DECREF(field);
  }
  {  // right_arm_estop
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_arm_estop");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->right_arm_estop = (Py_True == field);
    Py_DECREF(field);
  }
  {  // left_arm_estop
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_arm_estop");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->left_arm_estop = (Py_True == field);
    Py_DECREF(field);
  }
  {  // right_end_error
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_end_error");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->right_end_error = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // left_end_error
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_end_error");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->left_end_error = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // right_end_model
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_end_model");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->right_end_model, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // left_end_model
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_end_model");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->left_end_model, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // waist_error
    PyObject * field = PyObject_GetAttrString(_pymsg, "waist_error");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->waist_error = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // lift_error
    PyObject * field = PyObject_GetAttrString(_pymsg, "lift_error");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->lift_error = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // neck_error
    PyObject * field = PyObject_GetAttrString(_pymsg, "neck_error");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->neck_error = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // chassis_error
    PyObject * field = PyObject_GetAttrString(_pymsg, "chassis_error");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->chassis_error = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__whole_body_status__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of WholeBodyStatus */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._whole_body_status");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "WholeBodyStatus");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__WholeBodyStatus * ros_message = (genie_msgs__msg__WholeBodyStatus *)raw_ros_message;
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
  {  // right_arm_error
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->right_arm_error);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_arm_error", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_arm_error
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->left_arm_error);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_arm_error", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_arm_control
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->right_arm_control ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_arm_control", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_arm_control
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->left_arm_control ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_arm_control", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_arm_estop
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->right_arm_estop ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_arm_estop", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_arm_estop
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->left_arm_estop ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_arm_estop", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_end_error
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->right_end_error);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_end_error", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_end_error
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->left_end_error);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_end_error", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_end_model
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->right_end_model.data,
      strlen(ros_message->right_end_model.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_end_model", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_end_model
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->left_end_model.data,
      strlen(ros_message->left_end_model.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_end_model", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // waist_error
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->waist_error);
    {
      int rc = PyObject_SetAttrString(_pymessage, "waist_error", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lift_error
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->lift_error);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lift_error", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // neck_error
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->neck_error);
    {
      int rc = PyObject_SetAttrString(_pymessage, "neck_error", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // chassis_error
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->chassis_error);
    {
      int rc = PyObject_SetAttrString(_pymessage, "chassis_error", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
