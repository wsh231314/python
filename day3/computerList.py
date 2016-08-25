'''
Created on Aug 24, 2016

@author: shawn.shaohua.wang
'''
from _functools import reduce

def changeNum(obj):
    if isinstance(obj, str):
        try:
            return int(obj)
        except Exception:
            try:
                return float(obj)
            except Exception:
                return 0
    return 0
    
def changeList(objList):
    return list(map(changeNum, objList))

def prod(x, y):
    return x * y

L1 = [None, '2.1', '3', '2sde']
print(sum(changeList(L1)))
print(reduce(prod, changeList(L1)))