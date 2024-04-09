# import RPi.GPIO as GPIO 
# import time 
# import random
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(14, GPIO.IN)
# while True:
#     sensorState=GPIO.input(14)
#     sensorState = 1
#     noise = random.randint(50, 200)
#     reading = (1-sensorState)*700 + noise
#     if sensorState == False:
#         print(reading)
#         print("CO gas detected. Bad Air Quality")
#     else:
#         print(reading)
#         print("Good Air Quality")
#     time.sleep(
