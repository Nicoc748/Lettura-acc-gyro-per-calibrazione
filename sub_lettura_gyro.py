#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
import serial

class gyro(object):
    def __init__(self):
        self.activation = False
        self.stop = False
        self.a = 0
        self.ratex = 0.0
        self.ratey = 0.0
        self.ratez = 0.0

        self.arduinodata=serial.Serial('/dev/ttyUSB0',9600)

    def callback(self,msg):
        self.activation = True

    def callback2(self,msg):
        self.stop = True
    

    def listenergyro(self):
        rospy.init_node('listenergyro', anonymous=True)
        sub1 = rospy.Subscriber('bool', Bool, self.callback)
        sub2 = rospy.Subscriber('bool_stop', Bool, self.callback2)
        self.arduinodata.flushInput()
        while not rospy.is_shutdown():
            while (self.arduinodata.inWaiting()==0):
                pass
            if self.activation:
                print("working")
                self.arduinostring=self.arduinodata.readline()
                self.a = self.a+1
                if (self.a==1):
                    continue
                else:
                    DataArray=" ".join(self.arduinostring.split())   #Eliminazione spazi vuoti
                    DataArray=DataArray.split(",")
                    xratetemp = float(DataArray[3])
                    yratetemp = float(DataArray[4])
                    zratetemp = float(DataArray[5])
                    self.ratex += xratetemp
                    self.ratey += yratetemp
                    self.ratez += zratetemp
                if (self.stop==True):
                    print("stopped")
                    mediaratex = self.ratex/self.a
                    mediaratey = self.ratey/self.a
                    mediaratez = self.ratez/self.a
                    print ("Media_x_gyro = %f, Media_y_gyro = %f, Media_z_gyro = %f" % (mediaratex, mediaratey, mediaratez))
                    break

if __name__ == '__main__':
    item = gyro()
    item.listenergyro()