#coding: utf-8
from Pubnub import Pubnub


PUBLISH_KEY = 'pub-c-574982bb-d7cc-4ec1-9683-fe1d89b144ad'
SUBSCRIBE_KEY = 'sub-c-9a43842c-a77a-11e4-85d5-0619f8945a4f'
pubnub = Pubnub(publish_key=PUBLISH_KEY, subscribe_key=SUBSCRIBE_KEY, ssl_on=False)

channel = 'cmd'
message = 'Hello World !!!'

import time


def receive(msg):
    print(msg)
    return True

pubnub.subscribe({
'channel' : 'cmd',
'callback' : receive
})


# Synchronous usage
for i in range(200):
    time.sleep(2)
    print pubnub.publish(channel, message)