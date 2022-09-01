'''
Created on Aug 20, 2022

@author: Ramachandran S

Requirement : 
    Implement doHash table where collisions are handled using separate chaining. Keep MAX size of arr in hashtable as 5.
    
@attention: handleCollision logic is implemented by.
    Name : Ramachandran S.
    Registration Number : PA2212005010011
    
'''

from project.ct1.hash.Hashing import Hashing


class SeparateChaining(Hashing):
    
    def __init__(self, maxSize : int, arrayToHash : []):
        self._enableRehash = False
        super().__init__(maxSize, arrayToHash)
        
    
    def _handleCollision(self, conflictedIndex, newValue):
        oldValue = self._hashedArray[conflictedIndex]
        if (type(oldValue) is list):
            oldValue.append(newValue)
        else:
            self._hashedArray[conflictedIndex] = [oldValue, newValue]
        
    
