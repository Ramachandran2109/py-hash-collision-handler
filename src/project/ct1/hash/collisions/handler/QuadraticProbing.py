'''
Created on Aug 20, 2022

@author: Ramachandran S

Requirement : 
    Implement doHash table where collisions are handled using quadratic probing. Keep MAX size of arr in hashtable as 20.
    
@attention: handleCollision logic is implemented by.
    Name : Anbuselvan Balakrishnan
    Registration Number : 22421005928
    
'''

from project.ct1.hash.Hashing import Hashing

class QuadraticProbing(Hashing):
    
    __counter = None;
    
    def _handleCollision(self, conflictedIndex, newValue):
        if (conflictedIndex >= self._getLength() -1):
            conflictedIndex = -1;
            self._recursiveCount += 1;
            self.__counter = 0;
        else:
            if (self.__counter is None):
                self.__counter = 0
            
            self.__counter += 1
               
        conflictedIndex =  conflictedIndex + (self.__counter * self.__counter)
        if (conflictedIndex >= self._getLength() -1):
            self._handleCollision(conflictedIndex, newValue)
        else:
            self._addToIndex(conflictedIndex, newValue)
        
                

                