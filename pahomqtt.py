import paho.mqtt.subscribe as subscribe
import json

def print_msg(client, userdata, message):
    #print("%s : %s" % (message.topic, message.payload))
    my_json = message.payload.decode('utf8').replace("'",'"')
    print(my_json)

subscribe.callback(print_msg, "tele/HEMS/SENSOR", hostname="127.0.0.1")