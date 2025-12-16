// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/Position.idl
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
#include "genie_msgs/msg/detail/position__struct.h"
#include "genie_msgs/msg/detail/position__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

// Nested array functions includes
#include "genie_msgs/msg/detail/motor_state__functions.h"
// end nested array functions include
ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);
bool genie_msgs__msg__motor_state__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * genie_msgs__msg__motor_state__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__position__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[34];
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
    assert(strncmp("genie_msgs.msg._position.Position", full_classname_dest, 33) == 0);
  }
  genie_msgs__msg__Position * ros_message = _ros_message;
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
  {  // agv_status
    PyObject * field = PyObject_GetAttrString(_pymsg, "agv_status");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->agv_status = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // position_conf
    PyObject * field = PyObject_GetAttrString(_pymsg, "position_conf");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->position_conf = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // agv_pos_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "agv_pos_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->agv_pos_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // agv_pos_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "agv_pos_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->agv_pos_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // agv_pos_z
    PyObject * field = PyObject_GetAttrString(_pymsg, "agv_pos_z");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->agv_pos_z = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // agv_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "agv_angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->agv_angle = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // odom_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "odom_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->odom_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // odom_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "odom_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->odom_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // odom_z
    PyObject * field = PyObject_GetAttrString(_pymsg, "odom_z");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->odom_z = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // odom_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "odom_angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->odom_angle = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // linear_speed
    PyObject * field = PyObject_GetAttrString(_pymsg, "linear_speed");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->linear_speed = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // angular_speed
    PyObject * field = PyObject_GetAttrString(_pymsg, "angular_speed");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->angular_speed = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // acc_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "acc_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->acc_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // acc_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "acc_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->acc_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // acc_z
    PyObject * field = PyObject_GetAttrString(_pymsg, "acc_z");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->acc_z = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // gyro_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "gyro_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->gyro_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // gyro_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "gyro_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->gyro_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // gyro_z
    PyObject * field = PyObject_GetAttrString(_pymsg, "gyro_z");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->gyro_z = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // roll
    PyObject * field = PyObject_GetAttrString(_pymsg, "roll");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->roll = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pitch
    PyObject * field = PyObject_GetAttrString(_pymsg, "pitch");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pitch = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // yaw
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // map_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "map_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->map_id = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // chassis_error
    PyObject * field = PyObject_GetAttrString(_pymsg, "chassis_error");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->chassis_error = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // motor_states
    PyObject * field = PyObject_GetAttrString(_pymsg, "motor_states");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'motor_states'");
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
    if (!genie_msgs__msg__MotorState__Sequence__init(&(ros_message->motor_states), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create genie_msgs__msg__MotorState__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    genie_msgs__msg__MotorState * dest = ros_message->motor_states.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!genie_msgs__msg__motor_state__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__position__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Position */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._position");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Position");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__Position * ros_message = (genie_msgs__msg__Position *)raw_ros_message;
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
  {  // agv_status
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->agv_status);
    {
      int rc = PyObject_SetAttrString(_pymessage, "agv_status", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // position_conf
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->position_conf);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position_conf", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // agv_pos_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->agv_pos_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "agv_pos_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // agv_pos_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->agv_pos_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "agv_pos_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // agv_pos_z
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->agv_pos_z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "agv_pos_z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // agv_angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->agv_angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "agv_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // odom_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->odom_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "odom_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // odom_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->odom_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "odom_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // odom_z
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->odom_z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "odom_z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // odom_angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->odom_angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "odom_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // linear_speed
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->linear_speed);
    {
      int rc = PyObject_SetAttrString(_pymessage, "linear_speed", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // angular_speed
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->angular_speed);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angular_speed", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // acc_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->acc_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "acc_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // acc_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->acc_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "acc_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // acc_z
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->acc_z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "acc_z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // gyro_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->gyro_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "gyro_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // gyro_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->gyro_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "gyro_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // gyro_z
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->gyro_z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "gyro_z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // roll
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->roll);
    {
      int rc = PyObject_SetAttrString(_pymessage, "roll", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pitch
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pitch);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pitch", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // yaw
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // map_id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->map_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "map_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // chassis_error
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->chassis_error);
    {
      int rc = PyObject_SetAttrString(_pymessage, "chassis_error", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // motor_states
    PyObject * field = NULL;
    size_t size = ros_message->motor_states.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    genie_msgs__msg__MotorState * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->motor_states.data[i]);
      PyObject * pyitem = genie_msgs__msg__motor_state__convert_to_py(item);
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
      int rc = PyObject_SetAttrString(_pymessage, "motor_states", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
