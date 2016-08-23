'''
Created on Aug 23, 2016

@author: shawn.shaohua.wang
'''
def yanghui():
    arrayList = [1]
    while True:
        yield arrayList
        arrayList = [sum(i) for i in zip([0] + arrayList, arrayList + [0])]

if __name__ == "__main__":
    gene = yanghui()
    i = 0    
    while i < 10:
        print(next(gene))
        i = i + 1
    