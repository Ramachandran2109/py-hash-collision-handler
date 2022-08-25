'''
Created on Aug 22, 2022

@author: Ramachandran S
'''
from project.ct1.hash.collisions.CollisionHandlerType import CollisionHandlerType
from project.ct1.hash.collisions.bean.CollisionInputBean import CollisionInputBean
from project.ct1.hash.collisions.handler.CuckooHashing import CuckooHashing
from project.ct1.hash.collisions.handler.DoubleHashing import DoubleHashing
from project.ct1.hash.collisions.handler.LinearProbing import LinearProbing
from project.ct1.hash.collisions.handler.QuadraticProbing import QuadraticProbing
from project.ct1.hash.collisions.handler.SeparateChaining import SeparateChaining


class Hashing:
    
    def __init__(self, collisionHandlerType : CollisionHandlerType, arrayToHash : []):
        self.__arrayToHash = arrayToHash;
        self.__inputArrayLength = len(arrayToHash);
        self.__collisionHandlerType = collisionHandlerType;
        
    
    def __hashcode(self, val):
        return val % (self.__inputArrayLength);
    
    
    def __getCollisionHandlerInstance(self, collisionHandlerType : CollisionHandlerType):
        
        instances = {
            1 : SeparateChaining(),
            2 : LinearProbing(),
            3 : QuadraticProbing(),
            4 : DoubleHashing(),
            5 : CuckooHashing()
        }
        
        return instances[collisionHandlerType];
    
    def doHash(self):
        hashedArray = ["" for index in range(self.__inputArrayLength)];
        handler = self.__getCollisionHandlerInstance(self.__collisionHandlerType);
        
        for index in range(self.__inputArrayLength):
            newIndex = self.__hashcode(self.__arrayToHash[index]);
            occupiedNewIndexValue = hashedArray[newIndex];
            if (occupiedNewIndexValue == ""):
                hashedArray[newIndex] = self.__arrayToHash[index];
            else:
                collisionInputBean = CollisionInputBean(
                    index, occupiedNewIndexValue, self.__arrayToHash[index], hashedArray
                );
                handler.handleCollision(collisionInputBean);
        
        return hashedArray;
        