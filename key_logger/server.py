import socket
import os
import struct


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("192.168.56.1", 1235)

print(f"Starting Server at {server_address}")

sock.bind(server_address)

sock.listen(5)

count = 0

rec_dir = "./received"

os.makedirs(rec_dir, exist_ok=True)

while True:
    connection, client_address = sock.accept()
    try:
        text_header = connection.recv(4)
        if not text_header:
            continue
        text_file_size = struct.unpack("!I", text_header)[0]
        all_bytes = bytearray()
        text_bytes_received = 0
        while text_bytes_received < text_file_size:
            text_chunck_size = min(4096, text_file_size - text_bytes_received)
            data = connection.recv(text_chunck_size)
            if not data:
                break
            all_bytes.extend(data)
            text_bytes_received += len(data)
        
        text_content = all_bytes.decode('utf-8')
        received_log = f"{rec_dir}/received_log.txt"
        with open(received_log, "a", encoding='utf-8') as txtfile:
            txtfile.write(text_content)

        header = connection.recv(4)
        if not header:
            continue

        file_size = struct.unpack("!I", header)[0]

        bytes_received = 0
        
        file_name = f"{rec_dir}/received_"+str(count)+".jpg"
        
        with open(file_name, "wb") as file:
            while bytes_received < file_size:
                chunck_size = min(4096, file_size - bytes_received)
                data = connection.recv(chunck_size)
                if not data:
                    break
                file.write(data)
                bytes_received += len(data)
        print(f"file {file_name} receieved successfully.")
        count += 1

    except Exception as e:
        print("Error:",e)
        connection.close()
