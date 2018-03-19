import numpy as np
import os.path
from flask import Flask, Response, send_from_directory, render_template

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def root_dir():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
