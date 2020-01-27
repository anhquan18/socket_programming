#!/bin/env python 3
import socket

HOST = '127.0.0.1' # Standard loopback interface address (local host)
PORT = 65432       # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Use the socket object without calling s.close()
    ''' argv for socket specify the adrress family and socket type
        AF_INET specify  IPv4
        SOCK_STREAM specify the socket type for TCP
    '''
    s.bind((HOST, PORT))   
    # bind used to associate the socket with a specific network interface and port number
    # based on the address argv pass to bind will be different
    print ('listening:', s.listen())              
    # listen enable a server to accept connections.it specifies the number of
    # unaccepted connections that the system will allow before refusing new connections
    conn, addr = s.accept()  # getting the client socket object for communication 
    with conn:  # use with statement with con to automatically close the socket at the end of the block
        print ('Connected by', addr)
        while True:
            data = conn.recv(1024)  # a blocking call function, receive the data sent by client 
            if not data: # if receive empty bytes object break the loop
                break  # with statement automatically close the server without using s.close()
            conn.sendall(data)  # echo the received data back to client 
