#!/usr/bin/python
import sys
import Adafruit_DHT
import time
import datetime
import paho.mqtt.publish as publish
channelID = "1136666"
apiKey = "3GXSCUY59YQ3M7YZ"

topic = "channels/" + channelID + "/publish/" + apiKey
mqttHost = "mqtt.thingspeak.com"
tTransport = "tcp"
tPort = 1883
tTLS = None

print("[INFO] Data prepared to be uploaded")


with open("/home/pi/rpi_weather_station.csv", "a") as log:
    while True:
        now = datetime.datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M")
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        #print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
        log.write("{},{},{}\n".format(timeString, temperature, humidity))
        tPayload = "field1=" + str(temperature) + "&field2=" + str(humidity)
        try:
            publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
            print("[INFO] data sent for 2 fields: ",  temperature, humidity)
        except:
            print("[info] failure in sending data")
        time.sleep(10)
