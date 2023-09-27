import RPi.GPIO as GPIO
import time

IR_sensor = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_sensor, GPIO.IN)

try:
  while True:
    print(GPIO.input(IR_sensor))
  time.sleep(0.1)

except KeyboardInterrupt:
  GPIO.cleanup()
