'''
Created on Aug 20, 2022

@author: Ramachandran S

Requirement : 
    Implement doHash table where collisions are handled using cuckoo hashing. Keep MAX size of arr in hashtable as 6
    
    
@attention: handleCollision logic is implemented by 
    Name : Ramachandran S.
    Registration Number : PA2212005010011

'''

from project.ct1.hash.Hashing import Hashing
from project.ct1.hash.collisions.handler import CuckooHashing


class CuckooHashing(Hashing):
    
    __secondaryHashing = None;
    
    
    def _getHashedArray(self):
        if (self.__secondaryHashing is not None):
            self._hashedArray.extend(self.__secondaryHashing._hashedArray);
        return self._hashedArray;
    
    
    def _getLeftOverValues(self):
        if (self.__secondaryHashing is not None):
            return self._leftOverValues | self.__secondaryHashing._leftOverValues;
            
        else :
            return self._leftOverValues;
    
    def _handleCollision(self, conflictedIndex, newValue):
        
        if (self.__secondaryHashing is None and self._getBaseValueDivisor() == 1):
            self.__secondaryHashing = CuckooHashing(self._maxSize, self._arrayToHash);
            self.__secondaryHashing._setBaseValueDivisor(self.__secondaryHashing._getPrime());
            self.__secondaryHashing.__primaryHashing = self;
            
        if (self._recursiveCount >= 100):
            if (newValue != ''):
                self._leftOverValues.add(newValue);
            return; 
        
        oldValue = self._hashedArray[conflictedIndex];
        self._hashedArray[conflictedIndex] = newValue;
        
        newValue = oldValue;
        self._recursiveCount += 1;
        if (self._getBaseValueDivisor() == 1):
            self.__secondaryHashing._recursiveCount += 1;
            self.__secondaryHashing._add(newValue);
        else :
            self.__primaryHashing._recursiveCount += 1;
            self.__primaryHashing._add(newValue);
        
