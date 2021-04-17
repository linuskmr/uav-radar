# uav-radar

Shows a map of UAVs flying above Brunswick.
Click on a drone to see its details.

Live demo [uav-radar.herokuapp.com](https://uav-radar.herokuapp.com).
Run with `python3 wsgi.py`.

Map from [maps.google.com](maps.google.com).

## API

### Flight Map

`GET /api/flight_map`

Get the positions of all drones.

### Drone Info

`GET /api/info/<drone-id>`

Get all information about the drone with `drone-id`.
