

# send_radio_test_message_try_this.py   # change

from microbit import *
import radio

radio.on()

sleep(1000)

print("micro:bit radio sender")

while True:
    radio.config(channel = 7)           # move to here
    message = "Hello from channel 7!"   # change
    print("Send: ", message)
    radio.send(message)

    sleep(1000)                         # add

    radio.config(channel = 14)          # add
    message = "Hello from channel 14!"  # add
    print("Send: ", message)            # add
    radio.send(message)                 # add
    
    print("Done!")
    sleep(1000)                         # change
