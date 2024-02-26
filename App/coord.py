import os
from confluent_kafka import SerializingProducer
import simplejson as json
from datetime import datetime
import random


RZESZOW_COORD = {
    "Latitude":50.0374,
    "Longitude":22.0049
}
TARNOW_COORD = {
"Latitude": 50.0125,
"Longitude": 20.9884
}



# Współrzędne punktów
points = [
    (50.1210, 21.9232),
    (49.9752, 21.8511),
    (50.1122, 22.2713),
    (49.9500, 22.2652)
]


# Funkcja sprawdzająca, czy punkt znajduje się wewnątrz figury
def is_inside_polygon(x, y, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


# Generowanie losowego punktu wewnątrz figury
def generate_random_point_inside_polygon(polygon):
    min_x = min(point[0] for point in polygon)
    max_x = max(point[0] for point in polygon)
    min_y = min(point[1] for point in polygon)
    max_y = max(point[1] for point in polygon)

    while True:
        random_x = random.uniform(min_x, max_x)
        random_y = random.uniform(min_y, max_y)

        if is_inside_polygon(random_x, random_y, polygon):
            return random_x, random_y


# Wygenerowanie losowego punktu wewnątrz figury
random_point_inside_polygon = generate_random_point_inside_polygon(points)
print("Losowy punkt wewnątrz figury:")
print("Latitude:", random_point_inside_polygon[0])
print("Longitude:", random_point_inside_polygon[1])





LATITUDE_INCREMENT = (TARNOW_COORD["Latitude"]-RZESZOW_COORD["Latitude"])/100

print(LATITUDE_INCREMENT)

LONGITUDE_INCREMENT = (TARNOW_COORD["Longitude"]-RZESZOW_COORD["Longitude"])/100

print(LONGITUDE_INCREMENT)


KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS','localhost:9092')

NAME_TOPIC = os.getenv('NAME_TOPIC','name_data')
SATURATION_TOPIC = os.getenv('SATURATION_TOPIC','saturation_data')
GPS_TOPIC = os.getenv('GPS_TOPIC','gps_data')
PULSE_TOPIC = os.getenv('PULSE_TOPIC','pulse_data')


start_time = datetime.now()
start_location = RZESZOW_COORD.copy()



def simulate_journey(producer,device_id):
    while True:
       # name_data=generate_name_data(device_id)
        #print(name_data)
        pass

if __name__ == "__main__":
    producer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,

        'error_cb':lambda err:print(f'Kafka error: {err}')
    }
    producer = SerializingProducer(producer_config)

    try:
        #simulate_journey(producer, 'Maciek xyz')
        pass
    except KeyboardInterrupt:
        print('simulation ended by the user')
    except Exception as e:
        print(f'{e}')