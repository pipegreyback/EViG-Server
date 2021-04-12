from pymongo import MongoClient
import paho.mqtt.client as mqtt


def on_connect(client, userdata):
    print("Connected with result code "+str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def MQTTSetup():
    client = mqtt.Client()
    client.onConnect = on_connect
    client.onMessage = on_message
    client.connect("127.0.0.1")
    return client

   

def dbConnection():
    client = MongoClient(host="127.0.0.1")
    db = client.HEMS
    return db


if __name__ == '__main__':
    mydb = dbConnection()
    client = MQTTSetup()
    client.loop_forever()
    # mycol = mydb["data"]

    # test_data = {
    #     "name":"yiro",
    #     "edad":23
    # }
    # result = mycol.insert_one(test_data)
    mydb.close()