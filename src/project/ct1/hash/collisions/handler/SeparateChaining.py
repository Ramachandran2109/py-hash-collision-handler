'''
Created on Aug 20, 2022

@author: Ramachandran S

Requirement : 
    Implement doHash table where collisions are handled using separate chaining. Keep MAX size of arr in hashtable as 5.
'''

from project.ct1.hash.collisions.handler.CollisionHandler import CollisionHandler

class SeparateChaining(CollisionHandler):
    
    def _handleCollision(self, oldValue, newValue):
        resultArray = [];
        if (type(oldValue) is list):
            oldValue.append(newValue);
            resultArray = oldValue;
        else :
            resultArray.append(oldValue);
            resultArray.append(newValue);
            
        return resultArray;
            