import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #medium #proctocol          socket is mainly door 
# ip address
# ip_address = "192.168.26.194"
ip_address = "127.0.0.1"      #localhost
port_no = 2525

my_address = (ip_address,port_no)
s.bind(my_address)

while True:
    data = s.recvfrom(100)
    # print(data)
    message = data[0]
    sender_address = data[1] #(ip,port)
    sender_ip = sender_address[0]
    message = message.decode("ascii")
    # ip address, message
    # file handling
    with open(str(sender_ip)+".txt",'a+') as file:
        file.write(message+"\n")
    print(message)   