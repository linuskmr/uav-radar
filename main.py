import json
import platform
import psutil
import random
import re
import socket
import uuid
from time import sleep
import flask
from flask import Flask, render_template
from markupsafe import Markup

import data

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

@app.route('/stats')
def stats():
    uname = platform.uname()
    cpufreq = psutil.cpu_freq()
    svmem = psutil.virtual_memory()
    return {
        'system': uname.system,
        'node name': uname.node,
        'release': uname.release,
        'version': uname.version,
        'machine': uname.machine,
        'processor': uname.processor,
        'physical cores': psutil.cpu_count(logical=False),
        'logical cores': psutil.cpu_count(logical=True),
        'max frequency': cpufreq.max,
        'min frequency': cpufreq.min,
        'current frequency': cpufreq.current,
        'cpu usage': psutil.cpu_percent(percpu=False),
        'total mem': get_size(svmem.total),
        'available mem': get_size(svmem.available),
        'used mem': get_size(svmem.used),
    }


@app.route('/api/flight_map')
def flight_map():
    # Return only the Id's and position of the drones to save data.
    # Detailed information can be retrieved with /api/info/<drone_id>.
    current_map = dict()
    for drone_id, drone in data.drones.items():
        current_map[drone_id] = {
            'id': drone['id'],
            'position': drone['position']
            # Ignore all other values
        }
    return current_map


def event():
    # Sever Sent Event sends updates to all connected browsers when a change occurs (For simplicity, this function
    # itself causes the change, but this could also come from outside and notify this function)
    for i in range(10):
        sleep(random.uniform(0.01, 2.0))
        drone = data.update_random_drone()
        yield f'data: {json.dumps(drone)}\n\n'.encode('utf-8')


@app.route('/stream')
def stream():
    return flask.Response(event(), mimetype="text/event-stream")


def print_dict(content, nested=2):
    # Prints a directory.
    # Creates headlines for each nested dict.
    output = ''
    for key, value in content.items():
        key = key.replace('_', ' ').capitalize()
        if isinstance(value, dict):
            output += f'<h{nested}>{key}</h{nested}>'
            output += print_dict(value)
        else:
            output += f'<p>{key}: {value}</p>'
    return output


@app.route('/api/info/<drone_id>')
def api_drone_info(drone_id):
    drone_id = int(drone_id)
    if drone_id not in data.drones:
        return f'Error: Could not find drone with id {drone_id}.'
    return data.drones[drone_id]


@app.route('/info/<drone_id>')
def drone_info(drone_id):
    return render_template('info.html', content=Markup(print_dict(api_drone_info(drone_id))))
