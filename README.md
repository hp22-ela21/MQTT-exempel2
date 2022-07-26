# MQTT-exempel2
Egenskapad klass för enkel MQTT-implementering. Användaren behöver enbart uppge en host samt topic vid publishing samt subscription.
Även i detta exempel publiceras meddelanden inmatade från terminalen via en klient och skrivs ut vid mottagande (för subscribers) via host "broker.hivemq.com".

Filen client.py används för att publicera meddelanden, där inmatning sker från terminalen tills användaren matar in en tom rad. 
Meddelanden publiceras till topic "python/mqtt/topics/1".

Filen server.py används för att ta emot meddelanden från topic "python/mqtt/topics/1" via subscription och skriva ut dessa i terminalen.

Starta filerna var sin enhet, exempelvis client.py på Ubuntu och server.py i Visual Studio 2022 eller på din Raspberry Pi.

Kommentarer har skrivits på engelska, då Python för Visual Studio 2022 inte stödjer å, ä och ö för docstrings.
