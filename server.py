import socket
import sys

s = socket.socket()
print('socket created')

port = 54322
clientMSG = ''

ip = str(input('ip -> '))

isServer = False

try:
    s.settimeout(5)
    s.connect((ip, port))
    print('you are a client')

except:
    isServer = True
    

        #c.close()

        #break

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
        message = input('💬 -> ')

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

        clientMSG = c.recv(1024).decode()

        print(clientMSG)

elif isServer == False:
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