'''
Created on Aug 20, 2022

@author: Ramachandran S

Requirement : 
    Implement doHash table where collisions are handled using Double hashing. Keep MAX size of arr in hashtable as 10. Try to achieve perfect hashing.  

@attention: handleCollision logic is implemented by.
    Name : Anbuselvan Balakrishnan
    Registration Number : 22421005928

'''

from project.ct1.hash.Hashing import Hashing
from project.ct1.util.NumberUtil import NumberUtil


class DoubleHashing(Hashing):
    
    __counter = None;
    
    def __secondaryHashFunction(self, value):
        prime = NumberUtil.getPrime(len(self._hashedArray));
        return prime - (self._hashCode(value) % prime)
    
    def _handleCollision(self, conflictedIndex, newValue):
        if (conflictedIndex >= self._getLength() -1):
            conflictedIndex = -1;
            self._recursiveCount += 1;
            self.__counter = 0;
        else:
            if (self.__counter is None):
                self.__counter = 0
            
            self.__counter += 1
               
        conflictedIndex =  conflictedIndex + (self.__counter * self.__secondaryHashFunction(newValue))
        if (conflictedIndex >= self._getLength() -1):
            self._handleCollision(conflictedIndex, newValue)
        else:
            self._addToIndex(conflictedIndex, newValue)
                    