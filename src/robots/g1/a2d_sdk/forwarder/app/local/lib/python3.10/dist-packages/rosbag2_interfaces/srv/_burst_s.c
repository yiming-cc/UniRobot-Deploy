// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from rosbag2_interfaces:srv/Burst.idl
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
#include "rosbag2_interfaces/srv/detail/burst__struct.h"
#include "rosbag2_interfaces/srv/detail/burst__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool rosbag2_interfaces__srv__burst__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
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
    assert(strncmp("rosbag2_interfaces.srv._burst.Burst_Request", full_classname_dest, 43) == 0);
  }
  rosbag2_interfaces__srv__Burst_Request * ros_message = _ros_message;
  {  // num_messages
    PyObject * field = PyObject_GetAttrString(_pymsg, "num_messages");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->num_messages = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * rosbag2_interfaces__srv__burst__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Burst_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("rosbag2_interfaces.srv._burst");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Burst_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  rosbag2_interfaces__srv__Burst_Request * ros_message = (rosbag2_interfaces__srv__Burst_Request *)raw_ros_message;
  {  // num_messages
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->num_messages);
    {
      int rc = PyObject_SetAttrString(_pymessage, "num_messages", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "rosbag2_interfaces/srv/detail/burst__struct.h"
// already included above
// #include "rosbag2_interfaces/srv/detail/burst__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool rosbag2_interfaces__srv__burst__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[45];
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
    assert(strncmp("rosbag2_interfaces.srv._burst.Burst_Response", full_classname_dest, 44) == 0);
  }
  rosbag2_interfaces__srv__Burst_Response * ros_message = _ros_message;
  {  // actually_burst
    PyObject * field = PyObject_GetAttrString(_pymsg, "actually_burst");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->actually_burst = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * rosbag2_interfaces__srv__burst__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Burst_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("rosbag2_interfaces.srv._burst");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Burst_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  rosbag2_interfaces__srv__Burst_Response * ros_message = (rosbag2_interfaces__srv__Burst_Response *)raw_ros_message;
  {  // actually_burst
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->actually_burst);
    {
      int rc = PyObject_SetAttrString(_pymessage, "actually_burst", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
