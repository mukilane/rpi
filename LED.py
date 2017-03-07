import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
while True:
    GPIO.output(12, GPIO.HIGH)
    print "ON"
    sleep(1)
    GPIO.output(12, GPIO.LOW)
    print "OFF"
    sleep(1)
