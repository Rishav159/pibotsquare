import numpy as np
import os.path
from flask import Flask, Response, send_from_directory, render_template
from camera import VideoCamera
from flask_socketio import SocketIO, emit

import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setup(4, GPIO.OUT)  # right
GPIO.setup(17, GPIO.OUT) # right
GPIO.setup(27, GPIO.OUT)  # left
GPIO.setup(22, GPIO.OUT)   # left

app = Flask(__name__,static_url_path='/static')
socketio = SocketIO(app)
#----------------------Reddy-Area-----------------

def forward():
        GPIO.output(4, True)
        GPIO.output(17, False)
        GPIO.output(27, True)
        GPIO.output(22, False)

def backward():
        GPIO.output(4, False)
        GPIO.output(17, True)
        GPIO.output(27, False)
        GPIO.output(22, True)

def left():
        GPIO.output(4, True)
        GPIO.output(17, False)
        GPIO.output(27, False)
        GPIO.output(22, False)

def right():
        GPIO.output(4, False)
        GPIO.output(17, False)
        GPIO.output(27, True)
        GPIO.output(22, False)

def stop():
        GPIO.output(4, False)
        GPIO.output(17, False)
        GPIO.output(27, False)
        GPIO.output(22, False)



def camera_up():
    print("Camera Up")
def camera_down():
    print("Camera down")
def camera_left():
    print("Camera Left")
def camera_right():
    print("Camera Right")
#-------------------------------------------------

@app.route('/')
def root_dir():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@socketio.on('move')
def handle_message(move):
    print (move)
    if move == 'f':
        forward()
    elif move == 'b':
        backward()
    elif move == 'l':
        left()
    elif move == 'r':
        right()
    elif move == 'u':
        camera_up()
    elif move == 'd':
        camera_down()
    elif move == 'x':
        camera_left()
    elif move == 'y':
        camera_right()
    else:
        GPIO.cleanup()

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', debug=False)
    #app.run(host='0.0.0.0', debug=False)
