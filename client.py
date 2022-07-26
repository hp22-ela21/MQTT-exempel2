#!/usr/bin/python3

##########################################################################################
# client.py: Example of MQTT publish by mqtt class, where data entered by the user 
#            is published to a specified topic at host "broker.hivemq.com".
##########################################################################################
import mqtt

def readline():
   """
   readline: Returing a line of text read from the terminal.
   """
   s = input()
   print()
   return s

def main():
   """
   main: Connecting to host "broker.hivemq.com", subscribing to topic "python/mqtt/topics/1".
         Received messages are printed in the terminal.
   """
   client1 = mqtt.mqtt(host = "broker.hivemq.com")
   while True:
      print("Enter a message to publish or a blank line to finish:")
      s = readline()
      if (s):
         client1.publish(topic = "python/mqtt/topics/1", message = s)
      else:
         break
   print("Bye!\n")
   return

# Calling the main function to start the program if this is the startup file:
if __name__ == "__main__":
   main()


