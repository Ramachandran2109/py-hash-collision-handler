'''
Created on Aug 22, 2022

@author: Ramachandran S
'''
import enum


class CollisionHandlerType(enum.Enum):
    SEPARATE_CHAINING = 1
    LINEAR_PROBING = 2
    QUADRATIC_PROBING = 3
    DOUBLE_HASHING = 4
    CUCKOO = 5
