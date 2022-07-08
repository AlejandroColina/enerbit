from conection import red
from redis.exceptions import ResponseError

def save_info(key:str, data:dict):
    try:
        red.hset(name=key, mapping=data)
    except Exception as e :
        print(e)