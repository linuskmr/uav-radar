import json
import random
from time import sleep
import flask
from flask import Flask, render_template
from markupsafe import Markup
import data

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/flight_map')
def flight_map():
    current_map = dict()
    for drone_id, drone in data.drones.items():
        current_map[drone_id] = {
            'id': drone['id'],
            'position': drone['position']
            # Ignore all other values
        }
    return current_map


def event():
    pass
    for i in range(10):
        sleep(random.uniform(0.01, 2.0))
        drone = data.update_random_drone()
        yield f'data: {json.dumps(drone)}\n\n'.encode('utf-8')


@app.route('/stream')
def stream():
    return flask.Response(event(), mimetype="text/event-stream")


def print_dict(content, nested=2):
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
