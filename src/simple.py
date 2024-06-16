#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
import serial

# Configuración del puerto serie
ser = serial.Serial('/dev/ttyACM0', 9600)  # Ajusta /dev/ttyACM0 según sea necesario

def read_sensor():
    if ser.in_waiting > 0:
        try:
            line = ser.readline().decode('utf-8').strip()
            value = float(line)
            return value
        except ValueError:
            return None
    return None

def talker():
    pub = rospy.Publisher('force_sensor', Float32, queue_size=10)
    rospy.init_node('force_sensor_publisher', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        sensor_value = read_sensor()
        if sensor_value is not None:
            rospy.loginfo(sensor_value)
            pub.publish(sensor_value)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    finally:
        ser.close()

