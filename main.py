import subprocess
import threading
import vgamepad as vg

gamepad = vg.VDS4Gamepad()
gamepad_lock = threading.Lock()

MIN_ANGLE = -450
MAX_ANGLE = 450

def convert_angle(angle):
    angle = max(MIN_ANGLE, min(MAX_ANGLE, angle))
    normalized = angle / MAX_ANGLE
    normalized_angle = int(128 + normalized * 128)
    return int(max(0, min(255, normalized_angle)))


def steering():
    cmd = ["pybricksdev", "run", "ble", "--name", "hub_1", "pedals.py"]
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    last_button = None

    for line in p.stdout:
        try:
            angle_str, button_str = line.rstrip().split(".", 1)

            x_val = convert_angle(int(angle_str))

            with gamepad_lock:
                gamepad.left_joystick(
                    x_value=x_val,
                    y_value=128
                )

                if button_str != last_button:
                    if button_str == "1":
                        gamepad.press_button(
                            button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS
                        )
                    else:
                        gamepad.release_button(
                            button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS
                        )

                    last_button = button_str

                gamepad.update()

        except Exception:
            pass


def pedal():
    cmd = ["pybricksdev", "run", "ble", "--name", "hub_2", "steering-wheel.py"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)

    for line in p.stdout:
        try:
            throttle = int(line.strip().split(".")[0])
            brake = int(line.strip().split(".")[1])

            throttle_normalized = throttle // 30 * 32767
            brake_normalized = brake // 30 * 32767

            with gamepad_lock:
                gamepad.right_joystick(x_value=brake_normalized, y_value=throttle_normalized)
                gamepad.update()
        except Exception:
            pass

if __name__ == "__main__":
    thread_steering = threading.Thread(target=steering, daemon=True)
    thread_pedal = threading.Thread(target=pedal, daemon=True)

    thread_pedal.start()
    thread_steering.start()


    try:
        thread_steering.join()
        thread_pedal.join()
    except KeyboardInterrupt:
        print("\nРабота завершена.")