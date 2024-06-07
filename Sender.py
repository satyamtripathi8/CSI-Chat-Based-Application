import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# TARGET_ip_address = "192.168.26.194"
TARGET_ip_address = "127.0.0.1"      #localhost
port_no = 2525

target_address = (TARGET_ip_address,port_no)
quiet=True
while quiet:
    message = input("please enter your message : ")
    message_encrypted = message.encode('ascii')
    s.sendto(message_encrypted,target_address)
    print("your message has been send")
    user_input = input("do yo want to quit it press Y/N : ")
    if user_input == "Y" or user_input =="y":
        quiet = False