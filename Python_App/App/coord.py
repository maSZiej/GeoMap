import os
from confluent_kafka import SerializingProducer
import simplejson as json
from datetime import datetime,timedelta
import random
import uuid
import time
from main import check_polygon

RZESZOW_COORD = {
    "Latitude":50.0374,
    "Longitude":22.0049
}
TARNOW_COORD = {
"Latitude": 50.0125,
"Longitude": 20.9884
}



LATITUDE_INCREMENT = (TARNOW_COORD["Latitude"]-RZESZOW_COORD["Latitude"])/100

print(LATITUDE_INCREMENT)

LONGITUDE_INCREMENT = (TARNOW_COORD["Longitude"]-RZESZOW_COORD["Longitude"])/100

print(LONGITUDE_INCREMENT)


KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS','localhost:9092')

MAIN_TOPIC = os.getenv('NAME_TOPIC','name_data')
#SATURATION_TOPIC = os.getenv('SATURATION_TOPIC','saturation_data')
#GPS_TOPIC = os.getenv('GPS_TOPIC','gps_data')
#PULSE_TOPIC = os.getenv('PULSE_TOPIC','pulse_data')


#start_time = datetime.now()
#start_location = RZESZOW_COORD.copy()
def get_next_time():

    global start_time
    start_time = datetime.now()
    start_time += timedelta(seconds=random.randint(30, 60))
    return start_time
#trzeba dorobic jeszcze jakies prawdopodobienstwa wagowe do pulsu i saturacji
def get_pulse():
    pulse = random.randint(20,220)
    return pulse

def get_saturation():
    saturation = random.randint(40,98)
    return saturation
def generate_main_data(device_id):
    points = [
        (50.1210, 21.9232),
        (49.9752, 21.8511),
        (50.1122, 22.2713),
        (49.9500, 22.2652)
    ]
    location = check_polygon.generate_random_point_inside_polygon(points)
    return{
        'id':uuid.uuid4(),
        'device_id':device_id,
        'timestamp':get_next_time().isoformat(),
        'location':location,
        'saturation':get_saturation(),
        'pulse':get_pulse()
    }

def simulate_journey(producer,device_id):
    while True:
        main_data=generate_main_data(device_id)
        print(main_data)
        time.sleep(2)

if __name__ == "__main__":
    producer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,

        'error_cb':lambda err:print(f'Kafka error: {err}')
    }
    producer = SerializingProducer(producer_config)

    try:
        simulate_journey(producer, 'Maciek xyz')
        pass
    except KeyboardInterrupt:
        print('simulation ended by the user')
    except Exception as e:
        print(f'{e}')