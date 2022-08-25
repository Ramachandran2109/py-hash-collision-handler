'''
Created on Aug 20, 2022

@author: Ramachandran S

Requirement : 
    Implement doHash table where collisions are handled using separate chaining. Keep MAX size of arr in hashtable as 5.
    
@attention: handleCollision logic is implemented by.
    Name : Ramachandran S.
    Registration Number : PA2212005010011
    
'''

from project.ct1.hash.collisions.bean.CollisionInputBean import CollisionInputBean
from project.ct1.hash.collisions.handler.CollisionHandler import CollisionHandler


class SeparateChaining(CollisionHandler):
    
    def handleCollision(self, collisionInputBean: CollisionInputBean):
        resultArray = [];
        oldValue = collisionInputBean.getResultIndexValue();
        newValue = collisionInputBean.getInputValue();
        
        if (type(oldValue) is list):
            oldValue.append(newValue);
            resultArray = oldValue;
        else :
            resultArray.append(oldValue);
            resultArray.append(newValue);
            
        collisionInputBean.getResultArray()[collisionInputBean.getNewResultIndex()] = resultArray;
            