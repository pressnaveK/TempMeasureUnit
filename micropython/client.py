import network
import machine
import urequests
import time

import onewire, ds18x20

ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)


#Set variable for timeout
timeout = 0
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
networks = wifi.scan()

print(networks)
#Connecting Wifi
SSID = "Your Wifi ID"
Pwd  = "Your Wifi ID password"
LocalIpServer = "Your Express server ip like 192.168.43.44"
wifi.connect(SSID,Pwd)


if not wifi.isconnected():
    print("Connecting...\t")
    while (not wifi.isconnected() and timeout <= 5):
        time.sleep(2)
        print("\n")
        print(timeout)
        timeout += 1

if (wifi.isconnected()):
    print("\n Connected \n")
    print(wifi.ifconfig())
    
    url =f"http://{LocalIpServer}:3001/SensorData" 
    
    
    
    while True:
        try:
            #Getting data from GPIO
            ds_sensor.convert_temp()
            time.sleep_ms(750)
            temp = 0
            for rom in roms:
                temp=float(ds_sensor.read_temp(rom))
            time.sleep(5)
            print(f"temperature :{temp} ")
            payload = {"Temp": temp}
            print(payload)
            response = urequests.post(url, json=payload)
            print("Executed")
            print(response.text)
        except Exception as e:
            print("Exception: ", e) 
        time.sleep(5)

else:
    print('Time Out')
    print('Not Connected')

