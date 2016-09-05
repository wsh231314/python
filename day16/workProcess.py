'''
Created on Sep 5, 2016

@author: shawn.shaohua.wang
'''
from multiprocessing.managers import BaseManager
import time

class ProcessManager(BaseManager):
    pass

ProcessManager.register("get_task_queue")
ProcessManager.register("get_result_queue")

manager = ProcessManager(address=('127.0.0.1', 5000), authkey=b'Wsh')

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = task.get(timeout=1)
    print("We have received:%s" % n)
    r = '%d * %d : %d' % (n, n, n*n)
    result.put(r)
    
print(time.localtime())
print('work is ok')
    