'''
Created on Aug 24, 2016

@author: shawn.shaohua.wang
'''
from _functools import reduce

def plus10(x, y):
    return x * 10 + y

def div10(x, y):
    return x / 10 + y

def str2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

strInput = input("input the float:")
strTemp=strInput.split(".")
print(reduce(plus10, map(str2num, strTemp[0])) + reduce(div10, list(map(str2num, strTemp[1]))[::-1]) / 10)
print(str(reduce(plus10, map(str2num, strTemp[0])) + reduce(div10, list(map(str2num, strTemp[1]))[::-1]) / 10))