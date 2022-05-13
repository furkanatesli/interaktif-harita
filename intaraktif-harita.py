# -*- coding: utf-8 -*-
from flask import Flask, render_template
import run
import multitasking

app = Flask(__name__)

@multitasking.task
def run_schedule():
    run.run_schedule()

run_schedule()

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
