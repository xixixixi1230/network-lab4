import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM) #服务端调用socket()创建套接字来启动服务器
serverSocket.bind(('', 12000)) #''代表本机IP，服务端调用bind()指定服务器的套接字地址
while True:
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024) #服务端调用recvfrom()等待接收数据，此时阻塞
    message = message.upper() #小写转大写
    print("接收的消息{}".format(message))
    print("接收的地址{}".format(address))
    if rand < 4: #模拟丢失30%的客户端数据包
        print("数据包丢失")
        continue
    serverSocket.sendto(message, address) #服务器接收到客户端发来的数据后，调用sendto()向客户发送应答数据


