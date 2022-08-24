'''
Created on Aug 22, 2022

@author: Ramachandran S
'''

from abc import abstractmethod
import abc
from project.ct1.hash.collisions.bean.CollisionInputBean import CollisionInputBean



class CollisionHandler(abc.ABC):
    
    _arrayToHash = [];
    
    def __init__(self, arrayToHash):
        self._arrayToHash = arrayToHash;
    
    @abstractmethod
    def _handleCollision(self, collisionInputBean:CollisionInputBean):
        pass;
    
    def __hashcode(self, val):
        return val % (len(self._arrayToHash));
    
    def doHash(self):
        hashedArray = ["" for index in range(len(self._arrayToHash))];
        for index in range(len(self._arrayToHash)):
            newIndex = self.__hashcode(self._arrayToHash[index]);
            occupiedNewIndexValue = hashedArray[newIndex];
            if (occupiedNewIndexValue == ""):
                hashedArray[newIndex] = self._arrayToHash[index];
            else:
                collisionInputBean = CollisionInputBean(
                    index, occupiedNewIndexValue, self._arrayToHash[index], hashedArray
                );
                self._handleCollision(collisionInputBean);
        
        return hashedArray;
    
    
