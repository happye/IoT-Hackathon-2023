import base64
import socket

# Setting the IP address and port number of the Arduino application
arduino_ip = '127.0.0.1'
arduino_port = 1234

# Open the MP3 file and read the binary data
mp3_file = 'C:/UnisysWorkFolder/Tutorials/IoT Hackathon/ioT sound file/bird sing.mp3'
with open(mp3_file, 'rb') as file:
    mp3_data = file.read()

# Convert MP3 data to Base64 encoded string
base64_data = base64.b64encode(mp3_data).decode('utf-8')

# Create a TCP socket and connect to the Arduino application
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((arduino_ip, arduino_port))

# Send Base64 encoded data to the Arduino application
sock.sendall(base64_data.encode('utf-8'))

# Close the socket connection
sock.close()
