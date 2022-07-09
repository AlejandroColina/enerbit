from os import getenv
from redis import Redis
from uuid import uuid4
from time import sleep
from simulador import simulador

stream_key = getenv("")
MAX_MESSAGES = 2


def connect_to_redis():
    hostname = getenv("REDIS_HOST")
    port = getenv("REDIS_PORT")
    passw = getenv("REDIS_PASS")

    r = Redis(hostname, port, passw, retry_on_timeout=True)
    return r


def send_data(redis_connection, max_messages):
    count = 0
    while count < max_messages:
        try:
            data = simulador()
            resp = redis_connection.hset(stream_key, data)
            print(resp)
            count += 1

        except ConnectionError as e:
            print("ERROR REDIS CONNECTION: {}".format(e))

        sleep(4)


if __name__ == "__main__":
    connection = connect_to_redis()
    send_data(connection, MAX_MESSAGES)