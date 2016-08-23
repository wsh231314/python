'''
Created on Aug 23, 2016

@author: shawn.shaohua.wang
'''
def upperList(s):
    if isinstance(s, str):
        return s[:1].upper() + s[1:].lower()
    return s

L1 = [None, '', 'barT']

print(list(map(upperList, L1)))
    
    