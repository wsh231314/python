'''
Created on Aug 23, 2016

@author: shawn.shaohua.wang
'''
def fact(n):
    if (n == 1):
        return 1
    return n * fact(n - 1)

print(fact(3))