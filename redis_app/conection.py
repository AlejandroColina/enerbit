from redis import Redis
from redis.exceptions import ConnectionError
from os import getenv

try:
    red = Redis(
        host= getenv("REDIS_HOST"),
        port= getenv("REDIS_PORT"),
        password= getenv("REDIS_PASS"),
        ssl=True    
    )
    print('Connected to Redis')

except ConnectionError as e:
    print(e)
