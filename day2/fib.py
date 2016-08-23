'''
Created on Aug 23, 2016

@author: shawn.shaohua.wang
'''
def fib(maxNum):
    n, a, b = 0, 0, 1
    while n < maxNum:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(20)