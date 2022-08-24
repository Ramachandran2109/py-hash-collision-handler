'''
Created on Aug 22, 2022

@author: Ramachandran S
'''
from project.ct1.hash.collisions.CollisionHandlerType import CollisionHandlerType
from project.ct1.hash.collisions.handler.QuadraticProbing import QuadraticProbing
from project.ct1.hash.collisions.handler.SeparateChaining import SeparateChaining
from project.ct1.hash.collisions.handler.LinearProbing import LinearProbing
from project.ct1.hash.collisions.handler.DoubleHashing import DoubleHashing
from project.ct1.hash.collisions.handler.CuckooHashing import CuckooHashing

class Hashing:
    
    @staticmethod
    def getCollisionHandlerInstance(collisionHandlerType : CollisionHandlerType, inputArray : []):
        
        instances = {
            1 : SeparateChaining(inputArray),
            2 : LinearProbing(inputArray),
            3 : QuadraticProbing(inputArray),
            4 : DoubleHashing(inputArray),
            5 : CuckooHashing(inputArray)
        }
        
        return instances[collisionHandlerType];
        