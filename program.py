import paho.mqtt.publish as publish

channelID = "1136666"
apiKey = "3GXSCUY59YQ3M7YZ"

topic = "channels/" + channelID + "/publish/" + apiKey
mqttHost = "mqtt.thingspeak.com"
tTransport = "tcp"
tPort = 1883
tTLS = None

tPayload = "field1=" + str(timeString) + "&field2=" + str(temperature) + "&field3=" + str(humidity)

print("[INFO] Data prepared to be uploaded")

try:
    publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
    print("[INFO] data sent for 3 fields: ", timeString, temperature, humidity)
except:
    print("[info] failure in sendind data")
