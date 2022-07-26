#!/usr/bin/python3

##########################################################################################
# server.py: Example of MQTT subscription, where received data from multiple topics at
#            host "broker.hivemq.com" is printed in the terminal.
##########################################################################################
import mqtt

def main():
   """
   main: Connecting to host "broker.hivemq.com", subscribing to topic "python/mqtt/topics/1".
         Received messages are printed in the terminal.
   """
   server1 = mqtt.mqtt(host = "broker.hivemq.com")
   server1.subscribe(topic = "python/mqtt/topics/1")
   while True:
      pass
   return

# Calling the main function to start the program if this is the startup file:
if __name__ == "__main__":
   main()

