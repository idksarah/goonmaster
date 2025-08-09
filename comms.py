import socket

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

    message = input('type your message')

    c.send(message.encode())

    #c.close()

    #break
