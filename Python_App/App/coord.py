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