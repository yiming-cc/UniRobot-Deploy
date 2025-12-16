// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/Object.idl
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
#include "genie_msgs/msg/detail/object__struct.h"
#include "genie_msgs/msg/detail/object__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

// Nested array functions includes
#include "genie_msgs/msg/detail/asso_matrix__functions.h"
#include "genie_msgs/msg/detail/camera_object__functions.h"
#include "genie_msgs/msg/detail/grasp_point__functions.h"
// end nested array functions include
bool genie_msgs__msg__camera_object__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__camera_object__convert_to_py(void * raw_ros_message);
bool genie_msgs__msg__bev_object__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__bev_object__convert_to_py(void * raw_ros_message);
bool genie_msgs__msg__grasp_point__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__grasp_point__convert_to_py(void * raw_ros_message);
bool genie_msgs__msg__asso_matrix__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__asso_matrix__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__object__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[30];
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
    assert(strncmp("genie_msgs.msg._object.Object", full_classname_dest, 29) == 0);
  }
  genie_msgs__msg__Object * ros_message = _ros_message;
  {  // track_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "track_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->track_id = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // cam_obj
    PyObject * field = PyObject_GetAttrString(_pymsg, "cam_obj");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'cam_obj'");
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
    if (!genie_msgs__msg__CameraObject__Sequence__init(&(ros_message->cam_obj), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__CameraObject__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__CameraObject * dest = ros_message->cam_obj.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!genie_msgs__msg__camera_object__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // bev_obj
    PyObject * field = PyObject_GetAttrString(_pymsg, "bev_obj");
    if (!field) {
      return false;
    }
    if (!genie_msgs__msg__bev_object__convert_from_py(field, &ros_message->bev_obj)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // grasp_point
    PyObject * field = PyObject_GetAttrString(_pymsg, "grasp_point");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'grasp_point'");
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
    if (!genie_msgs__msg__GraspPoint__Sequence__init(&(ros_message->grasp_point), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__GraspPoint__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__GraspPoint * dest = ros_message->grasp_point.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!genie_msgs__msg__grasp_point__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // asso_matrix
    PyObject * field = PyObject_GetAttrString(_pymsg, "asso_matrix");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'asso_matrix'");
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
    if (!genie_msgs__msg__AssoMatrix__Sequence__init(&(ros_message->asso_matrix), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__AssoMatrix__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__AssoMatrix * dest = ros_message->asso_matrix.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!genie_msgs__msg__asso_matrix__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // sensor_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "sensor_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->sensor_type = (int32_t)PyLong_AsLong(field);
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
  {  // grasp_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "grasp_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->grasp_type = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // motion_status
    PyObject * field = PyObject_GetAttrString(_pymsg, "motion_status");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->motion_status = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // tracking_time
    PyObject * field = PyObject_GetAttrString(_pymsg, "tracking_time");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->tracking_time = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // tracking_score
    PyObject * field = PyObject_GetAttrString(_pymsg, "tracking_score");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->tracking_score = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__object__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Object */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._object");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Object");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__Object * ros_message = (genie_msgs__msg__Object *)raw_ros_message;
  {  // track_id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->track_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "track_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // cam_obj
    PyObject * field = NULL;
    size_t size = ros_message->cam_obj.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__CameraObject * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->cam_obj.data[i]);
      PyObject * pyitem = genie_msgs__msg__camera_object__convert_to_py(item);
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
      int rc = PyObject_SetAttrString(_pymessage, "cam_obj", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // bev_obj
    PyObject * field = NULL;
    field = genie_msgs__msg__bev_object__convert_to_py(&ros_message->bev_obj);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "bev_obj", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // grasp_point
    PyObject * field = NULL;
    size_t size = ros_message->grasp_point.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__GraspPoint * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->grasp_point.data[i]);
      PyObject * pyitem = genie_msgs__msg__grasp_point__convert_to_py(item);
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
      int rc = PyObject_SetAttrString(_pymessage, "grasp_point", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // asso_matrix
    PyObject * field = NULL;
    size_t size = ros_message->asso_matrix.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__AssoMatrix * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->asso_matrix.data[i]);
      PyObject * pyitem = genie_msgs__msg__asso_matrix__convert_to_py(item);
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
      int rc = PyObject_SetAttrString(_pymessage, "asso_matrix", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
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
  {  // grasp_type
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->grasp_type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "grasp_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // motion_status
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->motion_status);
    {
      int rc = PyObject_SetAttrString(_pymessage, "motion_status", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tracking_time
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->tracking_time);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tracking_time", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tracking_score
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->tracking_score);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tracking_score", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
