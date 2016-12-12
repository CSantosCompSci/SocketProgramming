# SocketProgramming
HTTP SERVER
In this exercise, you will develop a web server that handles one HTTP request at a time. Your web
server should accept and parse the HTTP request, get the requested file from the server’s file system,
create an HTTP response message consisting of the requested file preceded by header lines, and then
send the response directly to the client. If the requested file is not present in the server, the server
should send an HTTP “404 Not Found” message back to the client. 

HTTP Client
The http client should request user input for server name/IP, server port, file to retrieve from the server
and file to which the retrieved data is to be written. The client composes the appropriate http header and
sends it to the server, prints the returning data to console as well as to the specified file. 
