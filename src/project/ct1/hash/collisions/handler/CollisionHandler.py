'''
Created on Aug 22, 2022

@author: Ramachandran S
'''

from abc import abstractmethod
import abc


class CollisionHandler(abc.ABC):
    
    _arrayToHash = [];
    
    def __init__(self, arrayToHash):
        self._arrayToHash = arrayToHash;
    
    @abstractmethod
    def _handleCollision(self, oldValue, newValue):
        pass;
    
    def __hashcode(self, val):
        return val % (len(self._arrayToHash) - 1);
    
    def doHash(self):
        hashedArray = ["" for i in range(len(self._arrayToHash))];
        for i in range(len(self._arrayToHash)):
            index = self.__hashcode(self._arrayToHash[i]);
            oldValue = hashedArray[index];
            if (oldValue == ""):
                hashedArray[index] = self._arrayToHash[i];
            else:
                hashedArray[index] = self._handleCollision(oldValue, self._arrayToHash[i]);
        
        return hashedArray;
    
    
