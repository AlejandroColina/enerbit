from redis import Redis
from redis.exceptions import ConnectionError
from os import getenv


try:
    r = Redis(host='localhost', port=3001, charset="utf-8", decode_responses=True )
    print('Connected to redis.')    
except ConnectionError as e:
    print(e)