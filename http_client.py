"""
program written by Christopher Santos
project is a simple python socket program that prompts user for
IP address, port number, and a file name to send a request to a server matching
that criteria. The respnse is then saved locally to a file name the user specifies and
displays the contents on the terminal
"""
from socket import *
#prompt user for IP address
serverName = raw_input("Enter Server Name/IP: ")
#prompt user for Port Number
serverPort = input("Enter Port Number: ")
#prompt user for file to retrive from server
fileName = raw_input("Enter file to retrieve from server: ")
#prompt user for local save location of retrieved data
localFileName = raw_input("Enter file to save data from server to: ")
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
#send the name of the requested file to the specified server IP through port number specified
clientSocket.send('Get /' + fileName + ' HTTP/1.1\n')
#this is the response of the server to the request
serverResponse = clientSocket.recv(2048)
#receive file from server
requestedFile = clientSocket.recv(2048)

#open file and save contents of server Response to user specified file
file = open(localFileName,'a')
file.write(serverResponse)
file.write(requestedFile)
file.close()
#display contents of response from server
print serverResponse
print requestedFile
#close current socket
clientSocket.close()
