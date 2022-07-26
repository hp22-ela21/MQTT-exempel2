#!/usr/bin/python3

##########################################################################################
# mqtt.py: User friendly MQTT implementation for publishing and subscribing via class
#          mqtt and a few callback functions.
##########################################################################################
import paho.mqtt.client

def client_on_connect(client, data, flags, result_code):
   """
   client_on_connect: Printing connection status after attempted connection.
   """
   if (result_code):
      print("Could not connect to host " + client._host + "!\n")
   else:
      print("Successfully connected to host " + client._host + "!\n")
   return 

def client_on_disconnect(client, data, result_code):
   """
   client_on_disconnect: Printing status during disconnection.
   """
   if (result_code):
      print("Unexpected disconnection from host " + client._host + "!\n")
   else:
      print("Successfully disconnected from host " + client._host + "!\n")
   return

def client_on_message(client, data, message):
   """
   client_on_message: Printing received message, decoded from binary format to utf-8.
   """
   print("Received message from topic " + message.topic + ":", end = " ")
   print("" + message.payload.decode("utf-8") + "\n")
   return

class mqtt:
   """
   mqtt: Class for easy publishing and subscribing. The user has to provide a host when
         the object is created and a topic to publish/subscribe to when calling methods
         publish and subscribe.
   """

   def __init__(self, host, port = 1883):
      """
      __init__: Initializing new object for publishing and subscribing via a specified host.
                A 100 ms delay is used to print connection status in the terminal before
                running program.
      """
      import time
      self.__client = paho.mqtt.client.Client()
      self.__client.on_connect = client_on_connect
      self.__client.on_disconnect = client_on_disconnect 
      self.__client.on_message = client_on_message
      self.__client.connect(host, port)
      if not self.__client.is_connected():
         self.__client.reconnect()
      self.__client.loop_start()
      time.sleep(0.1)
      return

   def __del__(self):
      """
      __del__: Stops running thread and disconnects client when the mqtt object gets destroyed.
      """
      self.disconnect()
      return

   def publish(self, topic, message, qos = 1):
      """
      Publish: Publishing a message to specified topic.
      """
      msg = self.__client.publish(topic = topic, payload = message, qos = qos) 
      msg.wait_for_publish()
      print("Published message " + str(message) + " to topic " + str(topic) + "!\n")
      return

   def subscribe(self, topic, qos = 1):
      """
      subscribe: Subscribing to specified topic with continuous duration. 
      """
      try:
         self.__client.subscribe(topic = topic, qos = qos)
         print("Subscriped to topic " + topic + "!\n")
      except ValueError:
         print("Could not subscribe to topic " + str(topic) + "!\n")
      return

   def unsubscribe(self, topic):
      """
      unsubscribe: Unsubscribe from specified topic.
      """
      try:
         self.__client.unsubscribe(topic = topic)
      except ValueError:
         print("Could not unsubscribe from topic " + str(topic) + "!\n")
      return

   def disconnect(self):
      """
      disconnect: Stops running thread and disconnects client.
      """
      self.__client.loop_stop()
      self.__client.disconnect()
      return



