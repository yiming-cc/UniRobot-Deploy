// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from genie_msgs:msg/PeriStatus.idl
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
#include "genie_msgs/msg/detail/peri_status__struct.h"
#include "genie_msgs/msg/detail/peri_status__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool genie_msgs__msg__peri_status__convert_from_py(PyObject * _pymsg, void * _ros_message)
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
    assert(strncmp("genie_msgs.msg._peri_status.PeriStatus", full_classname_dest, 38) == 0);
  }
  genie_msgs__msg__PeriStatus * ros_message = _ros_message;
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
  {  // shut_down_compute_center_request
    PyObject * field = PyObject_GetAttrString(_pymsg, "shut_down_compute_center_request");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->shut_down_compute_center_request = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // soft_emergency_stop_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "soft_emergency_stop_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->soft_emergency_stop_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // pedal_emergency_stop
    PyObject * field = PyObject_GetAttrString(_pymsg, "pedal_emergency_stop");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->pedal_emergency_stop = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // button_emergency_stop
    PyObject * field = PyObject_GetAttrString(_pymsg, "button_emergency_stop");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->button_emergency_stop = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // hub1_reset_request_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "hub1_reset_request_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->hub1_reset_request_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // hub2_reset_request_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "hub2_reset_request_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->hub2_reset_request_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // left_arm_reset_request_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_arm_reset_request_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->left_arm_reset_request_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // right_arm_reset_request_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_arm_reset_request_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->right_arm_reset_request_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // left_end_reset_request_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_end_reset_request_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->left_end_reset_request_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // right_end_reset_request_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_end_reset_request_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->right_end_reset_request_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // waist_pitch_motor_reset_request_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "waist_pitch_motor_reset_request_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->waist_pitch_motor_reset_request_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // lift_motor_reset_request_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "lift_motor_reset_request_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->lift_motor_reset_request_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // head_yaw_motor_reset_request_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "head_yaw_motor_reset_request_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->head_yaw_motor_reset_request_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // head_pitch_motor_reset_request_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "head_pitch_motor_reset_request_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->head_pitch_motor_reset_request_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // agv_reset_request_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "agv_reset_request_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->agv_reset_request_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // power_pcb_work_mode
    PyObject * field = PyObject_GetAttrString(_pymsg, "power_pcb_work_mode");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->power_pcb_work_mode = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // feature_status
    PyObject * field = PyObject_GetAttrString(_pymsg, "feature_status");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->feature_status = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // left_arm_power_ctrl_req_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_arm_power_ctrl_req_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->left_arm_power_ctrl_req_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // right_arm_power_ctrl_req_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_arm_power_ctrl_req_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->right_arm_power_ctrl_req_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // left_end_power_ctrl_req_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_end_power_ctrl_req_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->left_end_power_ctrl_req_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // right_end_power_ctrl_req_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_end_power_ctrl_req_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->right_end_power_ctrl_req_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // waist_pitch_motor_power_ctrl_req_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "waist_pitch_motor_power_ctrl_req_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->waist_pitch_motor_power_ctrl_req_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // lift_motor_power_ctrl_req_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "lift_motor_power_ctrl_req_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->lift_motor_power_ctrl_req_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // head_yaw_motor_power_ctrl_req_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "head_yaw_motor_power_ctrl_req_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->head_yaw_motor_power_ctrl_req_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // head_pitch_motor_power_ctrl_req_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "head_pitch_motor_power_ctrl_req_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->head_pitch_motor_power_ctrl_req_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // agv_power_ctrl_req_feedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "agv_power_ctrl_req_feedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->agv_power_ctrl_req_feedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // power_ctrl_req_failreason
    PyObject * field = PyObject_GetAttrString(_pymsg, "power_ctrl_req_failreason");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->power_ctrl_req_failreason = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // left_end_current
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_end_current");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->left_end_current = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // right_end_current
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_end_current");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->right_end_current = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // waist_pitch_motor_current
    PyObject * field = PyObject_GetAttrString(_pymsg, "waist_pitch_motor_current");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->waist_pitch_motor_current = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // lift_motor_current
    PyObject * field = PyObject_GetAttrString(_pymsg, "lift_motor_current");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lift_motor_current = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // head_yaw_motor_current
    PyObject * field = PyObject_GetAttrString(_pymsg, "head_yaw_motor_current");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->head_yaw_motor_current = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // head_pitch_motor_current
    PyObject * field = PyObject_GetAttrString(_pymsg, "head_pitch_motor_current");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->head_pitch_motor_current = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // agv_current
    PyObject * field = PyObject_GetAttrString(_pymsg, "agv_current");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->agv_current = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // left_end_voltage
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_end_voltage");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->left_end_voltage = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // right_end_voltage
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_end_voltage");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->right_end_voltage = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // waist_pitch_motor_voltage
    PyObject * field = PyObject_GetAttrString(_pymsg, "waist_pitch_motor_voltage");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->waist_pitch_motor_voltage = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // lift_motor_voltage
    PyObject * field = PyObject_GetAttrString(_pymsg, "lift_motor_voltage");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lift_motor_voltage = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // head_yaw_motor_voltage
    PyObject * field = PyObject_GetAttrString(_pymsg, "head_yaw_motor_voltage");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->head_yaw_motor_voltage = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // head_pitch_motor_voltage
    PyObject * field = PyObject_GetAttrString(_pymsg, "head_pitch_motor_voltage");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->head_pitch_motor_voltage = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // agv_voltage
    PyObject * field = PyObject_GetAttrString(_pymsg, "agv_voltage");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->agv_voltage = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // emergency_stop_err_fedback
    PyObject * field = PyObject_GetAttrString(_pymsg, "emergency_stop_err_fedback");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->emergency_stop_err_fedback = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // power_board_software_version
    PyObject * field = PyObject_GetAttrString(_pymsg, "power_board_software_version");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->power_board_software_version, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // power_board_hardware_version
    PyObject * field = PyObject_GetAttrString(_pymsg, "power_board_hardware_version");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->power_board_hardware_version, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // power_board_serial_number
    PyObject * field = PyObject_GetAttrString(_pymsg, "power_board_serial_number");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->power_board_serial_number, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * genie_msgs__msg__peri_status__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of PeriStatus */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("genie_msgs.msg._peri_status");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "PeriStatus");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  genie_msgs__msg__PeriStatus * ros_message = (genie_msgs__msg__PeriStatus *)raw_ros_message;
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
  {  // shut_down_compute_center_request
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->shut_down_compute_center_request);
    {
      int rc = PyObject_SetAttrString(_pymessage, "shut_down_compute_center_request", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // soft_emergency_stop_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->soft_emergency_stop_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "soft_emergency_stop_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pedal_emergency_stop
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->pedal_emergency_stop);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pedal_emergency_stop", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // button_emergency_stop
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->button_emergency_stop);
    {
      int rc = PyObject_SetAttrString(_pymessage, "button_emergency_stop", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // hub1_reset_request_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->hub1_reset_request_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "hub1_reset_request_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // hub2_reset_request_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->hub2_reset_request_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "hub2_reset_request_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_arm_reset_request_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->left_arm_reset_request_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_arm_reset_request_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_arm_reset_request_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->right_arm_reset_request_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_arm_reset_request_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_end_reset_request_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->left_end_reset_request_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_end_reset_request_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_end_reset_request_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->right_end_reset_request_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_end_reset_request_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // waist_pitch_motor_reset_request_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->waist_pitch_motor_reset_request_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "waist_pitch_motor_reset_request_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lift_motor_reset_request_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->lift_motor_reset_request_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lift_motor_reset_request_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // head_yaw_motor_reset_request_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->head_yaw_motor_reset_request_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "head_yaw_motor_reset_request_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // head_pitch_motor_reset_request_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->head_pitch_motor_reset_request_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "head_pitch_motor_reset_request_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // agv_reset_request_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->agv_reset_request_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "agv_reset_request_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // power_pcb_work_mode
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->power_pcb_work_mode);
    {
      int rc = PyObject_SetAttrString(_pymessage, "power_pcb_work_mode", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // feature_status
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->feature_status);
    {
      int rc = PyObject_SetAttrString(_pymessage, "feature_status", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_arm_power_ctrl_req_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->left_arm_power_ctrl_req_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_arm_power_ctrl_req_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_arm_power_ctrl_req_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->right_arm_power_ctrl_req_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_arm_power_ctrl_req_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_end_power_ctrl_req_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->left_end_power_ctrl_req_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_end_power_ctrl_req_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_end_power_ctrl_req_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->right_end_power_ctrl_req_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_end_power_ctrl_req_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // waist_pitch_motor_power_ctrl_req_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->waist_pitch_motor_power_ctrl_req_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "waist_pitch_motor_power_ctrl_req_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lift_motor_power_ctrl_req_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->lift_motor_power_ctrl_req_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lift_motor_power_ctrl_req_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // head_yaw_motor_power_ctrl_req_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->head_yaw_motor_power_ctrl_req_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "head_yaw_motor_power_ctrl_req_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // head_pitch_motor_power_ctrl_req_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->head_pitch_motor_power_ctrl_req_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "head_pitch_motor_power_ctrl_req_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // agv_power_ctrl_req_feedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->agv_power_ctrl_req_feedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "agv_power_ctrl_req_feedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // power_ctrl_req_failreason
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->power_ctrl_req_failreason);
    {
      int rc = PyObject_SetAttrString(_pymessage, "power_ctrl_req_failreason", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_end_current
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->left_end_current);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_end_current", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_end_current
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->right_end_current);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_end_current", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // waist_pitch_motor_current
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->waist_pitch_motor_current);
    {
      int rc = PyObject_SetAttrString(_pymessage, "waist_pitch_motor_current", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lift_motor_current
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lift_motor_current);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lift_motor_current", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // head_yaw_motor_current
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->head_yaw_motor_current);
    {
      int rc = PyObject_SetAttrString(_pymessage, "head_yaw_motor_current", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // head_pitch_motor_current
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->head_pitch_motor_current);
    {
      int rc = PyObject_SetAttrString(_pymessage, "head_pitch_motor_current", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // agv_current
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->agv_current);
    {
      int rc = PyObject_SetAttrString(_pymessage, "agv_current", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_end_voltage
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->left_end_voltage);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_end_voltage", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_end_voltage
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->right_end_voltage);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_end_voltage", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // waist_pitch_motor_voltage
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->waist_pitch_motor_voltage);
    {
      int rc = PyObject_SetAttrString(_pymessage, "waist_pitch_motor_voltage", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lift_motor_voltage
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lift_motor_voltage);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lift_motor_voltage", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // head_yaw_motor_voltage
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->head_yaw_motor_voltage);
    {
      int rc = PyObject_SetAttrString(_pymessage, "head_yaw_motor_voltage", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // head_pitch_motor_voltage
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->head_pitch_motor_voltage);
    {
      int rc = PyObject_SetAttrString(_pymessage, "head_pitch_motor_voltage", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // agv_voltage
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->agv_voltage);
    {
      int rc = PyObject_SetAttrString(_pymessage, "agv_voltage", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // emergency_stop_err_fedback
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->emergency_stop_err_fedback);
    {
      int rc = PyObject_SetAttrString(_pymessage, "emergency_stop_err_fedback", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // power_board_software_version
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->power_board_software_version.data,
      strlen(ros_message->power_board_software_version.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "power_board_software_version", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // power_board_hardware_version
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->power_board_hardware_version.data,
      strlen(ros_message->power_board_hardware_version.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "power_board_hardware_version", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // power_board_serial_number
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->power_board_serial_number.data,
      strlen(ros_message->power_board_serial_number.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "power_board_serial_number", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
