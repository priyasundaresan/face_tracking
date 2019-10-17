# face_tracking

A Raspberry Pi-controlled, 3d-printed pan-tilt camera mechanism that uses OpenCV to track a face and follow it laterally and vertically.

Hardware setup:
* First, connect the signal wires coming off the servo motors (middle wire, orange) to the Raspberry Pi GPIO pins (13, 5) as in this diagram: https://www.raspberrypi.org/documentation/usage/gpio/
* Connect the grounded wires of the servos, AND one of the Raspberry Pi ground pins from the diagram linked above to ground on your breadboard.
* Connect the power signal wires coming off the servo motors (edge wire, red) to power on your breadboard. 
* Insert the camera module into the pi: the PiCamera is a small camera with a white thin strip cable attached. This cable slides right into the Pi's camera slot on the board where it says 'Camera'. Don't force the cable in; to insert it, you'll need to release the black anchors on the sides of the camera insertion slot, gently push the cable in, and then press the anchors down to secure the camera. The metal ends of the cable should be (almost) fully inserted and not visible once the black anchors snap back into place. 
* Next, we will power both the Pi and the Servos, SEPARATELY. This is because the Pi and any I/O devices draw too much power for the board to supply at once. Use the white Micro-USB to attach 'PWR-IN' on the Pi board to any USB slot on the Amazon Hub, and plug the Amazon Hub into a wall outlet. Next, take the 12V external supply (black rectangular device with two leads coming off of it), and hook its leads up to the voltage regulator (the device with the copper coil on it). Using a voltmeter, with the ground alligator clip attached to the black lead and the red alligator clip attached to the read lead, check that about 5 - 5.2 volts are being measured. If it is reading -5V, you'll need to switch how the two leads are inserted into the voltage regulator device. Now, plug the ground wire coming off the voltage regulator to ground on your breadboard, and red to the power rail of your breadboard. It is alright if you hear the servos in the pan-tilt device power on -- that means it is set up!

Software setup:
* Connect a monitor, keyboard, and mouse to the Pi via HDMI/USB. 
* When the board is powered on via the Amazon hub, you should see Raspbian (the OS for the Rasp Pi) start to boot. You can ignore any warnings about low voltage detected.
* Once it boots, you will be taken to the Desktop. You can run this script as follows:
```
cd Desktop/face_tracking
python pantilt.py
```

Troubleshooting:
* If the Pi powers off when you run the above program, it probably means the camera & servos are together drawing too much power. Check that your Amazon hub is working as expected and that the external supply to the servos is reading 5V. Try reducing the camera-frame rate -- perhaps it's demanding too much of the Pi!
* If the camera feed looks noisy/strange, try to remove it and re-insert it into the board. Ensure that it is securely placed and fully inserted. On the software side, check that your framerate is reasonable -- i.e. with a low frame-rate, we expect lag and a lack of light -- not always a hardware bug!
* Servos not moving/moving incorrectly: make sure you have specified your GPIO pins in your scripts correctly -- these are not magic numbers, so refer to the diagram linked above to check that your code matches your circuit.
* General tips: make sure that for whatever I/O devices you are using, the following check out:
  * Are you grounding the right wires? Is the power wire for a particular circuit component actually connected to the power rail of your breadboard? Is your breadboard appropriately grounded/hooked up to power? Are your signal wires connected to input pins on the Pi and not pins for power/ground?
  * Are your power supplies actually working?
* Software/OS issues - most of these are honestly caused by the Pi not having enough RAM. If you run
```
df -H
``` 
it shows you approximately how much disk space is taken up. The Pi is really not equipped to do heavy duty things that your typical Linux machine can -- avoid installing whatever you can!
