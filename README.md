# clash
Physical music generation and playback

* Write music onto a surface
  * Physical markings on a paper that can be zoomed into: [transloadit api](https://transloadit.com/demos/audio-encoding/generate-a-waveform-image-from-an-audio-file)
  * First test to see if music can actually read this way
* Read music using a camera that does automatic playback of what it's seeing
  * Ad hoc mode
  * Continuous mode -> there should be an indicator on the screen (that moves from left to right) indicating at what point in time the current music is playing.
* Can upload music or leave it as is
* Can also play music that wil generate one of the format (call it a "Trace") -> Connect it to a raspberry pi
* Can play multiple traces at the same time as long as they are demarcated ("Clash") -> a straight enough line can become a demarcation
* Can either playback music from phone or send data to server

# Milestone 0
* Have the website running
* Be able to go to the website and upload a sound file, maybe even name it?
* Have the server take this sound file and upload to transloadit
* Have it save this file somewhere where it can be retrieved later by another client

# Milestone 1
* Play around with the image processing. Try printing out images of sound waves and see if the image processing image can capture it store it somewhere
* With my phone, go to the website. It will ask to take a picture of a waveform [idea 1](https://hackerluddite.wordpress.com/2012/04/15/getting-access-to-a-phones-camera-from-a-web-page/) [idea 2](http://www.codepool.biz/take-a-photo-and-upload-it-on-mobile-phones-with-html5.html) [google search](https://www.google.com/search?client=ubuntu&channel=fs&q=django+web+app+use+camera&ie=utf-8&oe=utf-8#channel=fs&q=django+web+app+use+phone+camera). Once this is done it posts the image and the server stores the image in a way that will make it convenient to do some image processing.

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

# Sound => Image
1. Get out your phone
2. Go to clash.xyz
3. It will ask you if you want to create a trace or play a trace, or possibly both.
4. If you choose to create a trace, it will ask you ~~either 1. plug aux cable from phone to raspberry pi which will control arduino to make the trace in real time as your music plays to it (this will require some usage of the sound recorder and signal analysis). 2.~~ to choose a audio file to upload from your phone, send it to the server and the server will queue the new trace. The raspberry pi will act as a client to the server and will have some mechanism for polling the queue to tell the arduino what to do. There isn't much space to make the trace so the servos have to be very precise

# Image => Sound
1. Get out your phone
2. Go to clash.xyz
3. It will ask you if you want to create a trace or play a trace, or possibly both.
4. If you choose to play a trace, the website will either 1. ask you to take a picture of the trace 2. hold the camera steady over a trace until it recognizes it 3. move the camera very close to the trace and drag it over as it plays it back to you
5. In addition to this there is a line/cursor that goes over the trace and plays it back to you (once it's "read" the trace and you press the play/start button)
