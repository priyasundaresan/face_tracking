from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import RPi.GPIO as GPIO
import time
from numpy import interp

pan_pin = 13
pan_MAXDUTY = 11.5
pan_MINDUTY = 3.5

tilt_pin = 5
tilt_MAXDUTY = 9.5
tilt_MINDUTY = 3.5

GPIO.setmode(GPIO.BCM)

GPIO.setup(pan_pin, GPIO.OUT)
pan = GPIO.PWM(pan_pin, 50)
pan.start(7.5)

GPIO.setup(tilt_pin, GPIO.OUT)
tilt = GPIO.PWM(tilt_pin, 50)
tilt.start(7.5)

camera = PiCamera()
camera.resolution = (160, 128)
camera.framerate = 40
rawCapture = PiRGBArray(camera, size=(160, 128))

time.sleep(0.1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        ex_mid = (x + (x+w))/2
        ey_mid = (y + (y+h))/2
        pan_duty_cycle = interp(ex_mid, [50, 120], [pan_MAXDUTY, pan_MINDUTY])
        tilt_duty_cycle = interp(ey_mid, [50, 90], [tilt_MAXDUTY, tilt_MINDUTY])
        try:
            pan.ChangeDutyCycle(pan_duty_cycle)
            time.sleep(0.05)
            tilt.ChangeDutyCycle(tilt_duty_cycle)
            time.sleep(0.05)
        except KeyboardInterrupt:
            GPIO.cleanup()
    img = cv2.resize(img, (0, 0), fx=4, fy=4)
    cv2.imshow('img', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    rawCapture.truncate(0)
        


GPIO.cleanup()
