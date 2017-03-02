'''
Created on 2017/03/02

@author: shawn.shaohua.wang
'''
from com.recommendations import critics, score_by_person, sim_distance

for person in critics:
    print("%s, your best people is :" % person)
    value = score_by_person(critics, person, 3, sim_distance)
    
    for item in value:
        print("Name: %s, score: %s " % (item[1], item[0]))
        
    print("")