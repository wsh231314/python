'''
Created on Sep 6, 2016

@author: shawn.shaohua.wang
'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []

while True:
    b = s.recv(1024)
    if b:
        buffer.append(b)
    else:
        break
    
data = b''.join(buffer)

s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header)
print(header.decode('utf-8'))

with open('sina.txt', 'wb') as f:
    f.write(html)
    

