from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause

pir = MotionSensor(25)
camera = PiCamera()

camera.start_preview()
camera.rotation = 180

i=0

def take_photo():
    global i
    i = i + 1
    camera.capture('/home/pi/Desktop/image_%s.jpg' % i)
    print('photo captured')
    sleep(10)

def stop_camera():
    camera.stop_preview()
    exit()

pir.when_motion = take_photo

pause()