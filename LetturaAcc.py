import serial
import time

ACCLX=[]
ACCLY=[]
ACCLZ=[]
accxsomma = 0.0
accysomma = 0.0
acczsomma = 0.0
ratex = 0.0
ratey = 0.0
ratez = 0.0

a = 0
arduinodata=serial.Serial('/dev/ttyUSB0',9600) 

for k in range(1000):
    while (arduinodata.inWaiting()==0):
        pass
    arduinostring=arduinodata.readline()
    a = a+1
    if (a==1):
        continue
    else:
        DataArray=" ".join(arduinostring.split())   #Eliminazione spazi vuoti
        DataArray=DataArray.split(",")
        accxtemp = float(DataArray[0])
        accytemp = float(DataArray[1])
        accztemp = float(DataArray[2])
        xratetemp = float(DataArray[3])
        yratetemp = float(DataArray[4])
        zratetemp = float(DataArray[5])
        accxsomma += accxtemp
        accysomma += accytemp
        acczsomma += accztemp
        ratex += xratetemp
        ratey += yratetemp
        ratez += zratetemp
    if (a%100==0):
        print a
print accxsomma
print accysomma
print acczsomma
print ratex
print ratey
print ratez

mediax = accxsomma/1000
mediay = accysomma/1000
mediaz = acczsomma/1000
mediaratex = ratex/1000
mediaratey = ratey/1000
mediaratez = ratez/1000
print ("Media_x = %f, Media_y = %f, Media_z = %f" % (mediax, mediay, mediaz))
print ("Media_x_gyro = %f, Media_y_gyro = %f, Media_z_gyro = %f" % (mediaratex, mediaratey, mediaratez))
