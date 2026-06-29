from pybricks.pupdevices import Motor, ForceSensor
from pybricks.parameters import Port
from pybricks.tools import wait

steering = Motor(Port.C)
stop_button = ForceSensor(Port.F)
engine_motor = Motor(Port.E)
turn_signal_motor = Motor(Port.A)


last_angle = None
last_button = None

while True:
    angle = steering.angle()
    state = int(stop_button.pressed())

    print(f"{angle}.{state}")

    wait(5)