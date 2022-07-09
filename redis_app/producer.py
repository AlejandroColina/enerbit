from random import randint
from connection import r
from redis.exceptions import ResponseError
import datetime
from time import sleep


def simulador():
    return {
        "device": str(randint(15, 99)),
        "consumo": ("%i kW" %(randint(50, 150))),
        "date": str(datetime.datetime.now())
    }


def save_hash(data:dict):
    try:
        r.xadd('STREAM', data)
    except ResponseError as e:
        print(e)


if __name__ == '__main__':    
    for _ in range(10, 30):
        save_hash(simulador())
        print('Metric sended!')
        sleep(4)
    print('The end...')