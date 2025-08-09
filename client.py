# Import socket module 
import socket             

# Create a socket object 
s = socket.socket()         

# Define the port on which you want to connect 
port = 54322       

# connect to the server on local computer 
s.connect(('172.20.10.2', port)) 

while True:
    # receive data from the server and decoding to get the string.
    print (s.recv(1024).decode())
    
    message = input('type your message: ')

    s.send(message.encode())    

    # close the connection 
    #s.close()     
     