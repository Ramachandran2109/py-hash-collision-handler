'''
Created on Aug 31, 2022

@author: Ramachandran S
'''
from project.ct1.hash.Hashing import Hashing
from project.ct1.hash.collisions import CollisionHandlerType
from project.ct1.hash.collisions.handler.CuckooHashing import CuckooHashing
from project.ct1.hash.collisions.handler.DoubleHashing import DoubleHashing
from project.ct1.hash.collisions.handler.LinearProbing import LinearProbing
from project.ct1.hash.collisions.handler.QuadraticProbing import QuadraticProbing
from project.ct1.hash.collisions.handler.SeparateChaining import SeparateChaining


class HashFactory:
    
    @staticmethod
    def getInstance(collisionHandlerType : CollisionHandlerType, maxSize : int, arrayToHash : []):
        
        match collisionHandlerType:
            case 1:
                return SeparateChaining(maxSize, arrayToHash);
            case 2:
                return LinearProbing(maxSize, arrayToHash);
            case 3:
                return QuadraticProbing(maxSize, arrayToHash);
            case 4:
                return DoubleHashing(maxSize, arrayToHash);
            case 5:
                return CuckooHashing(maxSize, arrayToHash);
            case _:
                return Hashing(maxSize, arrayToHash);
                
