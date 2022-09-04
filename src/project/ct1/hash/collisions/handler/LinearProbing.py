'''
Created on Aug 20, 2022

@author: Ramachandran S

Requirement : 
    Implement doHash table where collisions are handled using linear probing. Keep MAX size of arr in hashtable as 10.  
    
'''

from project.ct1.hash.Hashing import Hashing


class LinearProbing(Hashing):
    
    def _handleCollision(self, conflictedIndex, newValue):
        if (conflictedIndex == self._getLength() -1):
            conflictedIndex = -1
            self._recursiveCount += 1
            
        self._addToIndex(conflictedIndex + 1, newValue);
        