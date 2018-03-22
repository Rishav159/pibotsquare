import numpy as np
import os.path
from flask import Flask, Response, send_from_directory, render_template
from camera import VideoCamera

app = Flask(__name__,static_url_path='/static')

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

if __name__ == '__main__':
    app.run()
