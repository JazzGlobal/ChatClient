import socket, json, sys
import message

message = message.Message(sys.argv[1], sys.argv[2])
to_send = json.dumps(message.export()).encode('utf-8')

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(to_send, (UDP_IP, UDP_PORT))