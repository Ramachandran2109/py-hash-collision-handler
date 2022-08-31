'''
Created on Aug 22, 2022

@author: Ramachandran S
'''
from abc import abstractmethod
import abc
from math import ceil, floor
import sys


class Hashing(abc.ABC):
    
    __threshold = 0;
    __valueCount = 0;
    __loadFactor = 0.75;
    __initialCapacity = 11;
    
    @abstractmethod
    def _handleCollision(self, conflictedIndex, newValue):
        self._hashedArray[conflictedIndex] = newValue;
    
    
    def __init__(self, maxSize : int, arrayToHash : []):
        self.__maxSize = maxSize;
        self.__arrayToHash = arrayToHash;
        
        self.__initialCapacity = max(ceil(len(self.__arrayToHash) / 2), 3);
        self.__threshold = min(floor(self.__initialCapacity * self.__loadFactor), sys.maxsize + 1);
        
        self._hashedArray = ["" for _ in range(self.__initialCapacity)];
        
    
    def __hashCode(self, value):
        return (hash(value) & 0x7FFFFFFF);
    
        
    def __hashIndex(self, value):
        return self.__hashCode(value) % (self.__getLength());
    
    
    def __rehash(self):
        oldCapacity = self.__getLength();
        newCapacity = (oldCapacity << 1) + 1;
        
        if (newCapacity >= self.__maxSize):
            if (oldCapacity == self.__maxSize):
                return;
            else:
                newCapacity = self.__maxSize;
        
        self.__threshold = min(newCapacity * self.__loadFactor, sys.maxsize + 1);
        newHashedArray = self._hashedArray.copy();
        self._hashedArray = ["" for _ in range(newCapacity)];
        
        self.__valueCount = 0;
        for index in range(len(newHashedArray)):
            value = newHashedArray[index];
            if (type(value) is list):
                for valueIndex in range(len(value)):
                    self.__handleHashing(value[valueIndex]);
            else:    
                self.__handleHashing(newHashedArray[index]);
    
    
    def __handleHashing(self, value):
        newIndex = self.__hashIndex(value);
        oldValue = self._hashedArray[newIndex];
        if (oldValue == ''):
            self._hashedArray[newIndex] = value;
        else:
            self._handleCollision(newIndex, value);
            
        self.__valueCount+=1;
            
            
    def __getLength(self):
        return len(self._hashedArray);
    
    
    def _add(self, value):
        
        if (self.__valueCount >= self.__threshold):
            self.__rehash();
            
        self.__handleHashing(value);
    
    
    def doHash(self):
        for index in range(len(self.__arrayToHash)):
            self._add(self.__arrayToHash[index]);
        
        return self._hashedArray;
    
    
        
        