from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

throttle = ColorSensor(Port.A)
brake = ColorSensor(Port.C)

last_throttle = None
last_brake = None

THRESHOLD = 30

while True:
    throttle_val = throttle.hsv()[2]
    brake_val = brake.hsv()[2]

    if (
        last_throttle is None
        or abs(throttle_val - last_throttle) >= THRESHOLD
        or abs(brake_val - last_brake) >= THRESHOLD
    ):
        print(f"{throttle_val}.{brake_val}")

        last_throttle = throttle_val
        last_brake = brake_val

    wait(100)