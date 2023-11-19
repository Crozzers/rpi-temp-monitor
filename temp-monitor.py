import json
import logging
import os
import socket
from typing import TypedDict
from time import time, sleep

from w1thermsensor import Unit, W1ThermSensor


class Metadata(TypedDict):
    ip: str
    host: str
    start: float
    '''when the program started running'''


class ThermData(TypedDict):
    time: float
    temp: float
    '''in degrees celsius'''


class LogData(TypedDict):
    meta: list[Metadata]
    data: list[ThermData]


def get_ip_addr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('0.0.0.0', 1))
    return s.getsockname()[0]

def load_data() -> LogData:
    with open('data.json', 'r', encoding='utf-8') as f:
        data: LogData = json.load(f)
    data.setdefault('meta', [])
    data.setdefault('data', [])
    return data


def save_data(data: LogData):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


if __name__ == '__main__':
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    logging.info(f'Temp monitor started. Working dir: {os.getcwd()}')
    HOSTNAME = socket.gethostname()
    IP_ADDR = get_ip_addr()
    logging.debug(f'{HOSTNAME=}, {IP_ADDR=}')

    DELAY = 600  # 10 mins

    data = load_data()
    data['meta'].append(Metadata(ip=IP_ADDR, host=HOSTNAME, start=time()))

    while True:
        try:
            sensor = W1ThermSensor()
            assert sensor.exists()
        except Exception:
            logging.exception('failed to init sensor')
        else:
            therm = ThermData(time=time(), temp=sensor.get_temperature(Unit.DEGREES_C))
            data['data'].append(therm)
            logging.info(f'reading: {therm!r}')

        save_data(data)
        time.sleep(DELAY)