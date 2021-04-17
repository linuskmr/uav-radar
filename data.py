import random

DRONES = 10

drones = dict()


def random_drone(drone_id):
    return {
        'model': random.choice(['Holybro X500', 'DJI Mini 2', 'DJI Mavic Air 2', 'Hubsan Zino 2', 'Parrot Anafi']),
        'id': drone_id,
        'position': {
            'latitude': round(random.uniform(0.0, 90.0), 5),
            'longitude': round(random.uniform(0.0, 90.0), 5),
            'height': round(random.uniform(0.0, 50.0), 2),
        },
        'battery': {
            'charge_level': round(random.uniform(0.10, 1.0), 2),
            'temperature': round(random.uniform(10.0, 37.0), 2),
        },
        'blockchain': {
            'current_hash': hex(random.randint(0, (1 << 63)-1)),
            'valid': True,
        }
    }


def update_drone(drone):
    drone['position']['latitude'] = round((drone['position']['latitude'] + random.uniform(-5.0, 5.0)) % 90.0, 5)
    drone['position']['longitude'] = round((drone['position']['longitude'] + random.uniform(-5.0, 5.0)) % 90.0, 5)
    drone['position']['height'] = round((drone['position']['height'] + random.uniform(-5.0, 5.0)) % 50.0, 2)
    drone['battery']['charge_level'] = round((drone['battery']['charge_level'] + random.uniform(-0.05, 0.05)) % 1.0, 2)
    drone['battery']['temperature'] = round((drone['battery']['temperature'] + random.uniform(-5.0, 5.0)) % 37.0, 2)
    return drone


def update_random_drone():
    drone_id = random.randint(0, DRONES - 1)
    drone = update_drone(drones[drone_id])
    drones[drone_id] = drone
    return drone


def init():
    for i in range(DRONES):
        drone = random_drone(i)
        drones[drone['id']] = drone


init()
