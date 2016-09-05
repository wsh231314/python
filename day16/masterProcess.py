'''
Created on Sep 5, 2016

@author: shawn.shaohua.wang
'''

import queue
from multiprocessing.managers import BaseManager
import random

class ProcessManager(BaseManager):
    pass

#
task_queue = queue.Queue()
#
result_queue = queue.Queue()

ProcessManager.register("get_task_queue", callable=lambda : task_queue)
ProcessManager.register("get_result_queue", callable = lambda : result_queue)

manager = ProcessManager(address=('127.0.0.1', 5000), authkey=b'Wsh')

manager.start()

task = manager.get_task_queue();
result = manager.get_result_queue();

for i in range(10):
    intNum = random.randint()
    print('put %s in to queue' % intNum)
    task.put(intNum)
    
print('wait ')

for i in range(10):
    r = result.get(timeout=10)
    print('Result:%s' % r)
    
#shutdown
manager.shutdown()
print('Exit system')