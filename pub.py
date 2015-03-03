#coding: utf-8
import threading
from Pubnub import Pubnub
from config import REDIS_SERVERS, PUBLISH_KEY, SUBSCRIBE_KEY
import redis


pubnub = Pubnub(publish_key=PUBLISH_KEY, subscribe_key=SUBSCRIBE_KEY, ssl_on=False)

channel = 'cmd'
message = {'a':1}

import time


def putmsg(channel,message):
    for i in range(20):
        print pubnub.publish(channel, message)

def callback(message):
    print(message)

# Synchronous usage
# thread_list = []
# for i in range(3):
#     t = threading.Thread(target=putmsg, args=(channel, i))
#     t.start()
#     thread_list.append(t)
#
# for i in thread_list:
#     # i.start()
#     i.join()
r = redis.StrictRedis(host='localhost', port=6379, db=0)

message = r.info()
# for i in range(20):
pubnub.publish(channel, message, callback=callback, error=callback)