#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

serverPort = input("Enter Port Number: ")
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

    
while True:
#Establish the connection
        print 'Ready to serve...'
        connectionSocket, addr = serverSocket.accept() 
        try:
                message = connectionSocket.recv(1024)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata =f.read() 
        #Send one HTTP header line into socket
       
                connectionSocket.send('Sever Online')
                connectionSocket.send('HTTP/1.1 200 OK\n')

        
        #Send the content of the requested file to the client
                for i in range(1, len(outputdata)):
                        connectionSocket.send(outputdata[i])
                connectionSocket.close()
        except IOError:
                #Send response message for file not found

                connectionSocket.send('404 NOT FOUND')

                #Close client socket

                connectionSocket.close()

serverSocket.close()
