// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/CameraObject.idl
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
#include "genie_msgs/msg/detail/camera_object__struct.h"
#include "genie_msgs/msg/detail/camera_object__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"
#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

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

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__camera_object__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[43];
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
    assert(strncmp("genie_msgs.msg._camera_object.CameraObject", full_classname_dest, 42) == 0);
  }
  genie_msgs__msg__CameraObject * ros_message = _ros_message;
  {  // camera_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "camera_id");
    if (!field) {
      return false;
    }
    {
      PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'camera_id'");
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
      if (!rosidl_runtime_c__String__Sequence__init(&(ros_message->camera_id), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create String__Sequence ros_message");
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      rosidl_runtime_c__String * dest = ros_message->camera_id.data;
      for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject * item = PySequence_Fast_GET_ITEM(seq_field, i);
        if (!item) {
          Py_DECREF(seq_field);
          Py_DECREF(field);
          return false;
        }
        assert(PyUnicode_Check(item));
        PyObject * encoded_item = PyUnicode_AsUTF8String(item);
        if (!encoded_item) {
          Py_DECREF(seq_field);
          Py_DECREF(field);
          return false;
        }
        rosidl_runtime_c__String__assign(&dest[i], PyBytes_AS_STRING(encoded_item));
        Py_DECREF(encoded_item);
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
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
  {  // corner
    PyObject * field = PyObject_GetAttrString(_pymsg, "corner");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'corner'");
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
    if (!genie_msgs__msg__Point3D__Sequence__init(&(ros_message->corner), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__Point3D__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__Point3D * dest = ros_message->corner.data;
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
  {  // mask
    PyObject * field = PyObject_GetAttrString(_pymsg, "mask");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'mask'");
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
    if (!genie_msgs__msg__Point3D__Sequence__init(&(ros_message->mask), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__Point3D__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__Point3D * dest = ros_message->mask.data;
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
  {  // instance_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "instance_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->instance_id = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // ground_point
    PyObject * field = PyObject_GetAttrString(_pymsg, "ground_point");
    if (!field) {
      return false;
    }
    if (!genie_msgs__msg__point3_d__convert_from_py(field, &ros_message->ground_point)) {
      Py_DECREF(field);
      return false;
    }
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
  {  // class_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "class_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->class_type = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // sub_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "sub_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->sub_type = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__camera_object__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of CameraObject */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._camera_object");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "CameraObject");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__CameraObject * ros_message = (genie_msgs__msg__CameraObject *)raw_ros_message;
  {  // camera_id
    PyObject * field = NULL;
    size_t size = ros_message->camera_id.size;
    rosidl_runtime_c__String * src = ros_message->camera_id.data;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    for (size_t i = 0; i < size; ++i) {
      PyObject * decoded_item = PyUnicode_DecodeUTF8(src[i].data, strlen(src[i].data), "replace");
      if (!decoded_item) {
        return NULL;
      }
      int rc = PyList_SetItem(field, i, decoded_item);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "camera_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
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
  {  // corner
    PyObject * field = NULL;
    size_t size = ros_message->corner.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__Point3D * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->corner.data[i]);
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
      int rc = PyObject_SetAttrString(_pymessage, "corner", field);
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
  {  // mask
    PyObject * field = NULL;
    size_t size = ros_message->mask.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__Point3D * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->mask.data[i]);
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
      int rc = PyObject_SetAttrString(_pymessage, "mask", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // instance_id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->instance_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "instance_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ground_point
    PyObject * field = NULL;
    field = genie_msgs__msg__point3_d__convert_to_py(&ros_message->ground_point);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "ground_point", field);
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
  {  // class_type
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->class_type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "class_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // sub_type
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->sub_type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "sub_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
