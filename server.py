import socket
import sys

s = socket.socket()
s.settimeout(5)
print('socket created')

port = 54322
clientMSG = ''

import socket 

# Create a socket object 
s = socket.socket()

print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣽⣍⣉⠙⠒⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡉⠙⠛⠷⢦⣤⣄⣉⠙⠒⠢⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⠡⠀⢂⠈⠉⡙⠻⠷⢶⣤⣄⣈⠙⠒⠢⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⠃⢈⠀⢂⠠⠀⡁⠠⠀⠄⠂⠈⠉⠛⠻⠷⣶⣤⣄⣈⠙⠒⠢⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⡁⢀⠂⠀⠄⠂⠀⠄⢁⠠⠈⠠⠁⡐⠀⠄⡀⠈⠉⠛⠻⠷⣶⣤⣄⣈⠙⠒⠢⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⢀⠀⢃⠀⡘⠠⠘⠀⡀⠄⠃⠠⠀⡘⠀⡀⠃⡘⠠⠀⡀⠀⠘⠛⠿⢿⣤⣤⣀⠀⠛⠣⠤⣀⡀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠄⠂⢀⠂⠀⠄⠐⡀⠁⠠⠐⠈⡀⠐⡀⠐⡀⠐⡀⠄⠡⢀⠡⠈⠄⠠⠀⠄⠉⡙⠛⠷⢶⣤⣄⣈⠉⠒⠢⠤⣀⡀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠂⡈⠀⠄⠁⡐⠠⠀⠌⢀⠂⢁⠀⢂⠀⡁⢀⠂⠄⠠⠁⠄⠠⠁⠌⠠⢁⠈⡐⠀⠌⡐⠂⢌⠩⢙⠛⠷⣶⡄⢀⡇')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠌⢀⠂⠠⠐⠀⢂⠠⠐⠀⡈⠀⠄⠐⡀⠄⠈⠄⠂⡈⠐⢈⠠⠁⣀⠢⠐⡉⠔⡠⠉⢄⢂⠂⠌⠂⣿⡇⠀⡇')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⢈⠠⠀⠄⢁⠠⠁⠠⠀⠂⢁⠠⠈⢀⠂⠠⢀⠁⢂⠐⠀⢡⠀⠢⠡⠄⠢⠡⠌⡐⠄⡉⠄⢊⠐⡈⠁⣿⡇⠀⡇')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡃⠀⠄⠂⢈⠀⠄⠂⠁⠄⠡⠀⠄⡈⠀⠄⡁⢀⠂⠄⠢⠉⠤⢈⠡⢂⠡⠁⠆⠡⠐⡈⠐⡈⠄⡡⢀⠁⣿⡇⠀⡇')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⠈⠠⠈⡀⠄⠂⠈⠄⠂⠐⠈⡀⠄⠁⢄⠰⢀⠩⠠⠡⢈⠰⠈⡐⠠⠈⠌⡠⠡⠁⠄⠡⠐⡀⠆⡀⠂⣿⡇⠀⡇')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠆⠀⠡⠐⠀⡐⠈⡀⠂⠌⢀⠁⠠⢂⠉⡀⠢⠈⠄⡁⠢⠈⠄⠡⠠⠡⠈⠔⠠⠁⠌⠠⢁⠡⠐⠠⢀⠁⣾⡇⠀⡇')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⣈⠀⠂⢁⠠⠐⢀⡐⠠⠈⠄⡁⢂⠐⠠⠁⠌⡐⠠⠁⠌⠠⢁⠂⠡⠈⠄⠡⠈⠄⠡⢀⠂⢁⠂⠄⠂⣽⡇⠀⡇')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⢿⣿⣶⣦⣤⣆⣠⠀⠑⡈⠰⢀⠂⠌⠠⢁⠂⠄⠡⠈⠄⠡⠀⠌⡀⠡⢈⠀⠡⢈⠠⠀⠂⠄⢂⠐⡀⢿⡇⠀⡇')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⢿⣿⣷⣶⣤⣄⣈⠄⠁⢂⠐⡈⠐⡈⠐⠠⢁⠂⠐⡀⠂⠈⠄⡀⠂⠁⠌⠐⠠⠀⠄⣻⡇⢀⡇')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⢿⣿⣷⣦⣴⣀⡁⠄⡁⠂⠄⠂⡁⠄⢈⠐⠠⢀⠡⠈⡀⢁⠂⠁⠄⣻⡇⠀⡇')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⡻⣿⣿⣿⣿⢶⣮⣤⣂⡄⢈⠠⠐⢀⠂⢀⠂⠐⠠⢀⠁⠂⣽⡇⠀⡇')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠒⠊⠉⠉⠁⠀⠈⠙⠁⠀⠉⠙⣿⣿⣶⣦⣦⣀⡂⠠⠁⢂⠠⠈⠀⣿⡇⠀⡇')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠴⠒⠓⡒⠒⠲⠤⣄⣀⠀⠀⠀⣞⣛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠉⠙⠛⠿⢿⣿⣶⣦⣤⣈⡐⣺⡇⠀⡇')
print('⠀⠀⠀⢀⣀⠤⡴⠒⢛⡉⠀⣀⣠⠦⠲⢋⣀⡤⠆⠁⡈⠉⠑⠲⠿⣿⣿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠁⠉⢻⠛⠿⠿⣿⣇⣰⡧')
print('⣶⣾⠛⠉⢠⡄⢨⣶⢠⣤⠉⣧⣴⠚⠉⢹⣤⣶⠊⠉⣤⣴⠃⠀⢠⠀⠈⠉⡟⢻⣿⣿⣿⣷⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣴⣾⣿⠀⠀⠀⠀⠀⠈⠀')
print('⠻⠷⣶⣤⣀⡉⠉⠒⠒⠛⣉⣵⠴⠚⢉⣉⡦⠔⢓⣉⡧⠤⢖⢊⣡⠤⠴⡂⣈⡄⠀⣉⠙⠛⠿⣿⣿⣿⣶⣤⣄⣀⣀⣤⣴⣾⣿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠈⠉⠛⠻⠶⣦⣤⣄⡀⠉⠒⠢⠤⣀⡘⠋⠡⠴⣒⣋⡥⠼⡖⢚⣍⡤⠗⠒⣏⣠⠴⠀⢀⡄⠩⠙⠛⠿⢭⣟⡛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠶⣦⣤⣀⡈⠉⠒⠢⠬⣁⡀⠒⣏⣩⠤⠒⢛⣉⡥⠤⠒⣏⣉⠦⠔⢇⣀⡴⠀⢀⠉⠑⠒⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠶⣶⣤⣀⣈⠉⠑⠲⠒⢋⣩⠦⠖⣇⣉⠓⠤⢄⣈⣩⠤⠔⠒⣉⣠⣤⣶⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠷⣶⣤⣄⣀⠁⠋⠋⠤⠕⠒⣉⣠⣦⣶⠾⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠷⠶⠶⠾⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')

print('\n💻???')

collecting_ip = True
ip_address = ''

while collecting_ip:
    button = input('.')
    if button:
        ip_address = ip_address + '.'
    button = input('')
    if button:
        ip_address = ip_address + '0'
    button = input('o')
    if button:
        ip_address = ip_address + '1'
    button = input('oo')
    if button:
        ip_address = ip_address + '2'
    button = input('ooo')
    if button:
        ip_address = ip_address + '3'
    button = input('oooo')
    if button:
        ip_address = ip_address + '4'
    button = input('ooooo')
    if button:
        ip_address = ip_address + '5'
    button = input('oooooo')
    if button:
        ip_address = ip_address + '6'
    button = input('ooooooo')
    if button:
        ip_address = ip_address + '7'
    button = input('oooooooo')
    if button:
        ip_address = ip_address + '8'
    button = input('ooooooooo')
    if button:
        ip_address = ip_address + '9'
    button = input('✔️')
    if button:
        collecting_ip = False

print(ip_address)

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