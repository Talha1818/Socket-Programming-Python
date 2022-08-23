import socket

obj = socket.socket()  # create an object
print("Socket Created!")
obj.bind(('localhost', 1818))  # check on itself laptop (2301 is a port number)
obj.listen(4)  # can listen 4 people
print("Waiting for Connection!!!")

client_obj, addr = obj.accept()  # return client object and address
print("Server is ready to accept connection")
print("connected with this address ", addr)
# obj.send(bytes("Welcome to Talha Circle", 'utf-8'))

# for single message
# msg = client_obj.recv(1024) # receive data 1MB (1024kb)
# msg = msg.decode('utf-8') # decoding the msg format
# print(msg)

# for multiple messages
while True:
    msg = client_obj.recv(1024)  # receive data 1MB (1024kb)
    msg = msg.decode('utf-8')  # decoding the msg format
    if len(msg) == 0:
        obj.close()
        break
    else:
        print(msg)
