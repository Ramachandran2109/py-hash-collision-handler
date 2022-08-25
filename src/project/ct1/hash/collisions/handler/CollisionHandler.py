'''
Created on Aug 22, 2022

@author: Ramachandran S
'''

from abc import abstractmethod
import abc
from project.ct1.hash.collisions.bean.CollisionInputBean import CollisionInputBean



class CollisionHandler(abc.ABC):
    
    @abstractmethod
    def handleCollision(self, collisionInputBean:CollisionInputBean):
        pass;
    
    
