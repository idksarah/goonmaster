import socket
import sys
from interpreter import Interpreter
from openImage import OpenImage

interpreter = Interpreter()
openImage= OpenImage()

s = socket.socket()
s.settimeout(5)
print('socket created')

port = 54322
clientMSG = ''

ip_address = input('ip -> ')

# Create a socket object 
s = socket.socket()

isServer = False

try:
    s.connect((ip_address, port))
    print('you are a client')

except:
    isServer = True
        #c.close()

        #break

s.settimeout(None)

if isServer == True:
    s.close()
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(('', port))
    print('socket behind ' + str(port) + ' port')

    s.listen(5)
    print('socket listening')

    c, addr = s.accept()
    print('got connect from ' + str(addr))


    while True:
        # message = input('msg -> ')
        message = interpreter.interpret()

        c.send(message.encode())

        if message == 'quit' or message == 'exit': # check if user wants to end the chat
            print('you ended the chat')
            c.close()
            sys.exit()

        clientMSG = c.recv(1024).decode()

        if clientMSG == 'quit' or clientMSG == 'exit':
            print('they ended the chat')
            c.close()
            sys.exit()

        print(clientMSG)

elif isServer == False:
    while True:
    # receive data from the server and decoding to get the string.
        serverMSG = s.recv(1024).decode()
        openImage.openImage(serverMSG)
        
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