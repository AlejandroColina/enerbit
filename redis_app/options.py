# from connection import connect_to_redis
# from redis.exceptions import ResponseError
# from time import sleep

# def send_data(redis_connection, max_messages):
#     count = 0
#     while count < max_messages:
#         try:
#             data = {
#                 "producer": 'producer',
#                 "some_id": 'uuid4().hex',  # Just some random data
#                 "count": count,
#             }
#             resp = redis_connection.xadd('stream_key', data)
#             print(resp)
#             count += 1

#         except ConnectionError as e:
#             print("ERROR REDIS CONNECTION: {}".format(e))

#         sleep(0.5)