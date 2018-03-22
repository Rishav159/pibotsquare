import numpy as np
import os.path
from flask import Flask, Response, send_from_directory, render_template
from camera import VideoCamera
from flask_socketio import SocketIO, emit

app = Flask(__name__,static_url_path='/static')
socketio = SocketIO(app)
#----------------------Reddy-Area-----------------
def forward():
    print("forward")
def backward():
    print("Backward")
def left():
    print("Left")
def right():
    print("Right")
def camera_up():
    print("Camera Up")
def camera_down():
    print("Camera down")

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


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', debug=False)
    #app.run(host='0.0.0.0', debug=False)

