'''
Created on Aug 22, 2022

@author: Ramachandran S
'''

from abc import abstractmethod
import abc
from math import ceil, floor
import sys
from project.ct1.util.NumberUtil import NumberUtil


class Hashing(abc.ABC):
    
    __threshold = 0;
    __valueCount = 0;
    __loadFactor = 0.75;
    __initialCapacity = 11;
    
    def __init__(self, maxSize : int, arrayToHash : []):
        self._maxSize = maxSize;
        self._arrayToHash = arrayToHash;
        
        self.__initialCapacity = max(ceil(len(self._arrayToHash) / 2), 3);
        self.__threshold = min(floor(self.__initialCapacity * self.__loadFactor), sys.maxsize + 1);
        
        self.__initHashedArray__(self.__initialCapacity);
        self.__baseValueDivisor = 1;
        
        self._leftOverValues = set();
        self._recursiveCount = 0;
        self._enableRehash = True;
        
    
    def __initHashedArray__(self, capacity):
        self._hashedArray = ["" for _ in range(capacity)];
        self.__nextPrime = NumberUtil.getPrime(self._getLength());
        
        
    def __hashCode(self, value):
        return (hash(value) & 0x7FFFFFFF);
    
    
    def __hashFunction(self, value):
        return (floor(self.__hashCode(value) / self._getBaseValueDivisor())) % (self._getLength());
     
     
    def __handleHashing(self, value):
        
        newIndex = self.__hashFunction(value);
        oldValue = self._hashedArray[newIndex];
        
        if (oldValue == ''):
            self._hashedArray[newIndex] = value;
        else:
            self._handleCollision(newIndex, value);
            
        self.__valueCount+=1;
        
    
    def __rehash(self):
        oldCapacity = self._getLength();
        newCapacity = (oldCapacity << 1) + 1;
        
        if (newCapacity >= self._maxSize):
            if (oldCapacity == self._maxSize):
                return;
            else:
                newCapacity = self._maxSize;
        
        self.__threshold = min(newCapacity * self.__loadFactor, sys.maxsize + 1);
        newHashedArray = self._hashedArray.copy();
        
        self.__initHashedArray__(newCapacity);
        self.__valueCount = 0;
        
        for index in range(len(newHashedArray)):
            value = newHashedArray[index];
            if (type(value) is list):
                for valueIndex in range(len(value)):
                    self.__handleHashing(value[valueIndex]);
            else:    
                self.__handleHashing(newHashedArray[index]);
    
    
        
    @abstractmethod
    def _handleCollision(self, conflictedIndex, newValue):
        self._hashedArray[conflictedIndex] = newValue;    
     
           
    def _getLength(self):
        return len(self._hashedArray);
    
    
    def _getPrime(self):
        return self.__nextPrime;
    
    
    def _getBaseValueDivisor(self):
        return self.__baseValueDivisor;
        
    
    def _setBaseValueDivisor(self, value):
        self.__baseValueDivisor = value;
        
    
    def _getHashedArray(self):
        return self._hashedArray;
    
    
    def _getLeftOverValues(self):
        return self._leftOverValues;
    
    
    def _add(self, value):
        
        if (self.__valueCount >= self.__threshold and self._enableRehash):
            self.__rehash();
            
        self.__handleHashing(value);
    
    
    def doHash(self):
        for index in range(len(self._arrayToHash)):
            self._recursiveCount = 0;
            self._add(self._arrayToHash[index]);
        
        if (len(self._getLeftOverValues()) > 0):
            print("Unable to find index for the values : ", self._getLeftOverValues());
        
        return self._getHashedArray();
    
    
        
        