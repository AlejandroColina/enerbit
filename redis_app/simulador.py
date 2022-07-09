from random import randint
# from uuid import uuid4
# from time import sleep
import datetime
# import requests
# from connection import connection

# from options import send_data


# url_post = 'http://localhost:8000/metrics'


# def get_id():
#     return str(uuid4())


def simulador():
    return {
        "id": 'get_id()',
        "device": str(randint(15, 99)),
        "consumo": ("%i kW" %(randint(50, 150))),
        "date": str(datetime.datetime.now())
    }


# if __name__ == '__main__':    
#     for _ in range(1, 2):
#         send_data(connection, 1)
#         print('Metric sended!')
#         sleep(4)
#     print('The end...')
        
        
        
        
        
        
        
        # res = requests.post(url_post, json = simulador())