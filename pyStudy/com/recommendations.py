'''
Created on 2017/03/02

@author: shawn.shaohua.wang
'''
from math import sqrt

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

def sim_distance(prefs, person1, person2):
    
    common={}
    
    for item in prefs[person1]:
        if item in prefs[person2]:
            common[item]=1
    
    if len(common) == 0:
        return 0
    
    sum_of_suqares = sum(pow(prefs[person1][item] -prefs[person2][item] , 2) for item in prefs[person1] if item in prefs[person2])
    
    return 1 / (1 + sqrt(sum_of_suqares))

def sim_pearson(prefs, person1, person2):
    
    common = {}
    
    for item in prefs[person1]:
        if item in prefs[person2]:
            common[item] = 1
    
    count = len(common) 
    if count == 0:
        return 0
    
    #sum
    p1_sum = sum(prefs[person1][item] for item in common)
    p2_sum = sum(prefs[person2][item] for item in common)
    
    #square sum
    p1_sqsum = sum(pow(prefs[person1][item], 2) for item in common)
    p2_sqsum = sum(pow(prefs[person2][item], 2) for item in common)
            
    #plus sum
    p_plus_sum = sum(prefs[person1][item] * prefs[person2][item] for item in common)
    
    num = p_plus_sum - (p1_sum * p2_sum) / count
    den = sqrt( (p1_sqsum - pow(p1_sum, 2) / count) * (p2_sqsum - pow(p2_sum, 2) / count) )
    
    return num / den

# get top person
def score_by_person(prefs, person, n = 5, method = sim_pearson):
    score = [(method(prefs, person, other) , other) for other in prefs if person != other]
    score.sort(key=None, reverse=True)
    return score[0:n]