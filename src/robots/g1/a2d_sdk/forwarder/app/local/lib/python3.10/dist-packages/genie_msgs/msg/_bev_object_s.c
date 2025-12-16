// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/BevObject.idl
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
#include "genie_msgs/msg/detail/bev_object__struct.h"
#include "genie_msgs/msg/detail/bev_object__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

// Nested array functions includes
#include "genie_msgs/msg/detail/point3_d__functions.h"
// end nested array functions include
bool genie_msgs__msg__point3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__point3_d__convert_to_py(void * raw_ros_message);
bool genie_msgs__msg__point3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__point3_d__convert_to_py(void * raw_ros_message);
bool genie_msgs__msg__point3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__point3_d__convert_to_py(void * raw_ros_message);
bool genie_msgs__msg__point3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__point3_d__convert_to_py(void * raw_ros_message);
bool genie_msgs__msg__point3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__point3_d__convert_to_py(void * raw_ros_message);
bool genie_msgs__msg__point3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__point3_d__convert_to_py(void * raw_ros_message);
bool genie_msgs__msg__point3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__point3_d__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__bev_object__convert_from_py(PyObject * _pymsg, void * _ros_message)
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
    assert(strncmp("genie_msgs.msg._bev_object.BevObject", full_classname_dest, 36) == 0);
  }
  genie_msgs__msg__BevObject * ros_message = _ros_message;
  {  // pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "pos");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'pos'");
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
    if (!genie_msgs__msg__Point3D__Sequence__init(&(ros_message->pos), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__Point3D__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__Point3D * dest = ros_message->pos.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!genie_msgs__msg__point3_d__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // size
    PyObject * field = PyObject_GetAttrString(_pymsg, "size");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'size'");
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
    if (!genie_msgs__msg__Point3D__Sequence__init(&(ros_message->size), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__Point3D__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__Point3D * dest = ros_message->size.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!genie_msgs__msg__point3_d__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // polygon
    PyObject * field = PyObject_GetAttrString(_pymsg, "polygon");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'polygon'");
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
    if (!genie_msgs__msg__Point3D__Sequence__init(&(ros_message->polygon), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__Point3D__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__Point3D * dest = ros_message->polygon.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!genie_msgs__msg__point3_d__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // velocity
    PyObject * field = PyObject_GetAttrString(_pymsg, "velocity");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'velocity'");
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
    if (!genie_msgs__msg__Point3D__Sequence__init(&(ros_message->velocity), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__Point3D__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__Point3D * dest = ros_message->velocity.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!genie_msgs__msg__point3_d__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // acceleration
    PyObject * field = PyObject_GetAttrString(_pymsg, "acceleration");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'acceleration'");
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
    if (!genie_msgs__msg__Point3D__Sequence__init(&(ros_message->acceleration), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__Point3D__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__Point3D * dest = ros_message->acceleration.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!genie_msgs__msg__point3_d__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // euler_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "euler_angle");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'euler_angle'");
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
    if (!genie_msgs__msg__Point3D__Sequence__init(&(ros_message->euler_angle), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__Point3D__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__Point3D * dest = ros_message->euler_angle.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!genie_msgs__msg__point3_d__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // euler_angle_rate
    PyObject * field = PyObject_GetAttrString(_pymsg, "euler_angle_rate");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'euler_angle_rate'");
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
    if (!genie_msgs__msg__Point3D__Sequence__init(&(ros_message->euler_angle_rate), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__Point3D__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__Point3D * dest = ros_message->euler_angle_rate.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!genie_msgs__msg__point3_d__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // confidence
    PyObject * field = PyObject_GetAttrString(_pymsg, "confidence");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->confidence = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__bev_object__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of BevObject */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._bev_object");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "BevObject");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__BevObject * ros_message = (genie_msgs__msg__BevObject *)raw_ros_message;
  {  // pos
    PyObject * field = NULL;
    size_t size = ros_message->pos.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__Point3D * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->pos.data[i]);
      PyObject * pyitem = genie_msgs__msg__point3_d__convert_to_py(item);
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
      int rc = PyObject_SetAttrString(_pymessage, "pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // size
    PyObject * field = NULL;
    size_t size = ros_message->size.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__Point3D * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->size.data[i]);
      PyObject * pyitem = genie_msgs__msg__point3_d__convert_to_py(item);
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
      int rc = PyObject_SetAttrString(_pymessage, "size", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // polygon
    PyObject * field = NULL;
    size_t size = ros_message->polygon.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__Point3D * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->polygon.data[i]);
      PyObject * pyitem = genie_msgs__msg__point3_d__convert_to_py(item);
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
      int rc = PyObject_SetAttrString(_pymessage, "polygon", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // velocity
    PyObject * field = NULL;
    size_t size = ros_message->velocity.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__Point3D * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->velocity.data[i]);
      PyObject * pyitem = genie_msgs__msg__point3_d__convert_to_py(item);
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
      int rc = PyObject_SetAttrString(_pymessage, "velocity", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // acceleration
    PyObject * field = NULL;
    size_t size = ros_message->acceleration.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__Point3D * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->acceleration.data[i]);
      PyObject * pyitem = genie_msgs__msg__point3_d__convert_to_py(item);
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
      int rc = PyObject_SetAttrString(_pymessage, "acceleration", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // euler_angle
    PyObject * field = NULL;
    size_t size = ros_message->euler_angle.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__Point3D * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->euler_angle.data[i]);
      PyObject * pyitem = genie_msgs__msg__point3_d__convert_to_py(item);
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
      int rc = PyObject_SetAttrString(_pymessage, "euler_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // euler_angle_rate
    PyObject * field = NULL;
    size_t size = ros_message->euler_angle_rate.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__Point3D * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->euler_angle_rate.data[i]);
      PyObject * pyitem = genie_msgs__msg__point3_d__convert_to_py(item);
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
      int rc = PyObject_SetAttrString(_pymessage, "euler_angle_rate", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // confidence
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->confidence);
    {
      int rc = PyObject_SetAttrString(_pymessage, "confidence", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
