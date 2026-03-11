import serial.tools.list_ports
import time


def serial_ports():
    ports = list(serial.tools.list_ports.comports())
    for port_no, description, address in ports:
        if 'USB' in description:
            return port_no


def CRC(command):
    crc = 0xFFFF
    for b in command:
        crc ^= b
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    command.append(crc & 0xFF)
    command.append((crc >> 8) & 0xFF)
    return command


class Gripper():
    def __init__(self, portname):
        self.ser = serial.Serial(portname, 115200, timeout=1)

    def ClearrACT(self):
        activate_command = [0x09, 0x10, 0x03, 0xE8, 0x00, 0x03, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x73, 0x30]
        self.ser.write(bytes(activate_command))
        time.sleep(0.1)
        response = self.ser.read(8)
        return response

    def activate(self):
        activate_command = [0x09, 0x10, 0x03, 0xE8, 0x00, 0x03, 0x06, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x72, 0xE1]
        self.ser.write(bytes(activate_command))
        time.sleep(0.1)
        response = self.ser.read(8)
        return response

    def isavtivated(self):
        activate_command = [0x09, 0x04, 0x07, 0xD0, 0x00, 0x01, 0x30, 0x0F]
        self.ser.write(bytes(activate_command))
        time.sleep(0.1)
        response = self.ser.read(7)
        if response[3] == 0x31:
            return True
        return False

    def grip(self, command):
        grip_command = [0x09, 0x10, 0x03, 0xE8, 0x00, 0x03, 0x06, 0x09, 0x00, 0x00, command[0], command[1], command[2]]
        self.ser.write(bytes(CRC(grip_command)))
        time.sleep(0.1)
        response = self.ser.read(8)

    def ReadGripperStatus(self):
        feedback_command = [0x09, 0x04, 0x07, 0xD0, 0x00, 0x03, 0xB1, 0xCE]
        self.ser.write(bytes(feedback_command))
        time.sleep(0.1)
        response = self.ser.read(11)
        position = round((-50 / 255) * response[7] + 50, 2)
        return (response[3], response[7], position)

    def serclose(self):
        self.ser.close()


class CtrlGrp():
    def __init__(self, portname):
        print(portname)
        self.grp = Gripper(portname)

    def ACT(self):
        self.grp.ClearrACT()
        self.grp.activate()
        while not self.isACTed():
            None
        print('Gripper is activaited')

    def isACTed(self):
        while not self.grp.isavtivated():
            None
        return self.grp.isavtivated()

    def GTO(self, PosSpdFrc):
        self.grp.grip(PosSpdFrc)
        while self.OBJ()[0] == 0x39:
            None

    def OBJ(self):
        return self.grp.ReadGripperStatus()

    def SerClose(self):
        self.grp.serclose()
