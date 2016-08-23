'''
Created on Aug 23, 2016

@author: shawn.shaohua.wang
'''
import os

aList = ["a", "b", "c"]
bList = ["A", "B", "C"]

allList = [m + n for m in aList for n in bList]
print(allList)

allList = [m + n.lower() for m in aList for n in bList]
print(allList)

numberList = list(range(1, 10))
print([n * n for n in numberList if n%2 == 1])

print(os.cpu_count())
print(os.getcwd())
print(os.getlogin())
#print(help(os))

L = ['Hello', 'World', 18, 'Apple', None]
X = []
for n in L:
    if isinstance(n, str):
        X.append(n.lower())
    else:
        X.append(n)

print(X)

print([n.lower() for n in L if isinstance(n, str)])
#print([n.lower() for n in L])