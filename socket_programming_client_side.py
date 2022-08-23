import socket

obj = socket.socket()
obj.connect(('localhost', 1818))  # connection

# print(rec_msg.decode('utf-8'))

# for single message
# msg = 'Hello Talha! Hope you are doing well!!!'
# obj.send(msg.encode('utf-8'))  # send msg with encoding format


# for multiple messages
while True:
    msg = input("enter Your msg ==> (exit for terminate process): ")
    if msg == 'exit':
        obj.close()
        break
    else:
        obj.send(msg.encode('utf-8'))  # send msg with encoding format

