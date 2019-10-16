# PROTOTYPE PACKET SENDER

import socket, json, sys
import message

message_dict = message.Message(sys.argv[1], sys.argv[2]).export()
message_dict['sender_host_name'] = socket.gethostname()
message_dict['sender_ip_address'] = socket.gethostbyname(message_dict['sender_host_name'])

to_send = json.dumps(message_dict).encode('utf-8')

UDP_IP = "192.168.0.194"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(to_send, (UDP_IP, UDP_PORT))