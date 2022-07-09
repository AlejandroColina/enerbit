from connection import r
from redis.exceptions import ResponseError
import requests
# from time import sleep

url_post = 'http://localhost:8000/metrics'


def consumer():
    try:
        response = r.xread({'STREAM':b'0-0'})
        if len(response):
            for line in response[0][1]:
                res = requests.post(url_post, json=line[1])
                if res.status_code == 201:
                    print('Metric processed!')
                    r.xdel('STREAM', line[0].encode("ascii"))

        else:
            print('There are no messages in redis to process.')
    except ResponseError as e:
        print(e)


if __name__ == '__main__':
    consumer()
