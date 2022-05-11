from socket import *

serverIp = input("Enter server IP: ")
serverPort = int(input("Enter server port: "))
message = input("Enter lowercase message: ")

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(message.encode(), (serverIp, serverPort))

modifiedMessage = clientSocket.recvfrom(2048)
print(modifiedMessage[0].decode())
clientSocket.close()