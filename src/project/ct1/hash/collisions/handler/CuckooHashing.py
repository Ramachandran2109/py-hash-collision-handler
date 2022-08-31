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


class CuckooHashing(Hashing):
    
    def _handleCollision(self, conflictedIndex, newValue):
        pass;
            