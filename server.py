import socket
import sys

s = socket.socket()
s.settimeout(5)
print('socket created')

port = 54322

ip = str(input('ip -> '))
clientMSG = ''

try:
    s.connect((ip, port))
    print('you are a client')

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

except:
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


        if clientMSG == 'quit' or clientMSG == 'exit':
            print('they ended the chat')
            c.close()
            sys.exit()

        clientMSG = c.recv(1024).decode()

        print(clientMSG)

        #c.close()

        #break
