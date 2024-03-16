import time
from grove.grove_temperature_humidity_sensor import DHT

# DHT11 type
# insert to GPIO pin 5, slot D5
dht11 = DHT("11", 5)

with open("humidity.txt", "w") as file:
    while True:
        # to read humidity and temperature
        humi, temp = dht11.read()

        # String Formatting
        data_str = 'DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(dht11.dht_type, humi, temp)
        print(data_str)
        file.write(data_str + "\n")
        # Sleep for 1 second
        time.sleep(1)