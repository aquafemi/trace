# clash
Physical music generation and playback

* Write music onto a surface
  * Binary data
  * Physical markings on a paper that can be zoomed into
  * First test to see if music can actually read by one of these methods
* Read music using a camera that does automatic playback of what it's seeing
  * Ad hoc mode
  * Continuous mode -> there should be an indicator on the screen (that moves from left to right) indicating at what point in time the current music is playing.
* Can upload music or leave it as is
* Can also play music that wil generate one of the format (call it a "Trace") -> Connect it to a raspberry pi
* Can play multiple traces at the same time as long as they are demarcated ("Clash") -> a straight enough line can become a demarcation
* Can either playback music from phone or send data to server

# Milestone 1
* Play around with the image processing. Try printing out images of sound waves and see if the image processing image can capture it store it somewhere

# Milestone 2
* Play around with the sound processing. Try playing music and see if the sound recorder can pick up on it and print out the signal

# Milestone 3
* Make the app/functionality for capturing picture data (very simple app with some buttons)

# Milestone 4
* Try to move motors and servos to roll some paper

# Milestone 5
* Build physical device. Have raspberry pi control the arduino motors (by possibly take input from the sound sensor).
* Arduino controls the motors and Servos

# Pluses
* Invisible traces. -> Would need to do quite a bit of research in this.
* Sharing platorm and profiles

# Image Processing
* Have phone camera take continuous picture of/stream data
  * Playback from the phone
  * Send the image to the server and perform some work on it
* There needs to be an app or someway of using the phone camera
* Need: Phone camera, Permission to use camera, Phone connected to internet, Server with some compute and storage capabilities

# Sound Processing
* Possibly use a Raspberry Pi. Connect the output of the playing device (with aux cable) to the raspberry pi. Pass it to the sound recorder which outputs some analog/digital data that controls the motor/servo.
* Need: Arduino, raspberry pi, aux cable

# Items needed:
* Aux cable
* Arduino Uno with cable
* Raspberry Pi
* Micro usb cable
* Paper
* Samsung Phone
