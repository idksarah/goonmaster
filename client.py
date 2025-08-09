# Import socket module 
import socket 
import sys          

#keyboard.wait('esc')

# Create a socket object 
s = socket.socket()         

# Define the port on which you want to connect 
port = 54322       

# connect to the server on local computer 
s.connect(('172.20.10.2', port)) 

while True:
    # receive data from the server and decoding to get the string.
    serverMSG = s.recv(1024).decode()
    
    if serverMSG == 'quit' or serverMSG == 'exit':
        print('They ended the chat.')
        s.close()
        sys.exit()

    print (serverMSG)

    message = input('type your message: ')

    s.send(message.encode())

    if message == 'quit' or message == 'exit':
        print('You ended the chat.')
        s.close()
        sys.exit()