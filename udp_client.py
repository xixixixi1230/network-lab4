from socket import*
import time
clientSocket=socket(AF_INET,SOCK_DGRAM) #客户端创建套接字
#使用settimeout函数限制recvfrom()函数的等待时间为1秒
clientSocket.settimeout(1)
count=0 #ping报文失败次数
start=0 #第一次成功接收ping报文
totaltime=0 #计算平均RRT
#发送10次ping报文
for i in range(10):
    print("test_"+str(i)+":",end='') #报文内容
    t1=time.perf_counter() #计时
    #将信息转换为byte后发送到指定服务器端
    clientSocket.sendto("ping".encode("utf-8"),("10.22.166.2",12000))
    try:
        #调用recvfrom()函数接收服务器发来的应答数据
        message,address=clientSocket.recvfrom(1024)
        #超时处理，等到时间超过1秒，捕获抛出的异常后打印丢失报文，进行下一步操作
    except:
        print("out of time!!!")
        count=count+1
        continue
    t2=time.perf_counter() #RRT结束计数时间
    #计算ping消息的最小、最大和平均RRT，并计算丢包率
    RTT=(t2-t1)*1000
    if(start==0):
        mintime=RTT/2
        maxtime=RTT/2
        start=1
    elif(RTT/2<mintime):
        mintime=RTT/2
    elif(RTT/2>maxtime):
        maxtime=RTT/2
    totaltime=totaltime+RTT/2
    print('%.15f'%(RTT/2))
print('min_RRT:'+str(mintime))
print('max_RRT:'+str(maxtime))
print('average_RRT:'+str(totaltime/(10-count)))
print('packet loss rate:'+str(count/10))