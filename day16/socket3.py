'''
Created on Sep 6, 2016

@author: shawn.shaohua.wang
'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

init_flg = False

while True:
    x = input('Me:')
    
    if x == 'Exit':
        break
    
    s.send(x.encode('utf_8'))
    
    if not init_flg:
        data = s.recv(1024)
        print('Server: %s' % data.decode('utf-8'))
        init_flg = True
    
    data = s.recv(1024)
    print('Server: %s' % data.decode('utf-8'))

