import socket
import sys

s = socket.socket()
print('socket created')

port = 54322

s.bind(('', port))
print('socket behind ' + str(port) + ' port')

s.listen(5)
print('socket listening')

c, addr = s.accept()
print('got connect from ' + str(addr))


while True:
    message = input('💬 -> ')

    c.send(message.encode())

    clientMSG = c.recv(1024).decode()

    if clientMSG == 'quit' or clientMSG == 'exit':
        print('they ended the chat')
        c.close()
        sys.exit()

    print(clientMSG)

    if message == 'quit' or message == 'exit': # check if user wants to end the chat
        print('you ended the chat')
        c.close()
        sys.exit()

    #c.close()

    #break
