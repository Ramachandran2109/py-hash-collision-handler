'''
Created on Aug 20, 2022

@author: Ramachandran S

Requirement : 
    Implement doHash table where collisions are handled using Double hashing. Keep MAX size of arr in hashtable as 10. Try to achieve perfect hashing.  

@attention: handleCollision logic is implemented by.
    Name : Anbuselvan Balakrishnan
    Registration Number : 22421005928

'''

from project.ct1.hash.Hashing import Hashing


class DoubleHashing(Hashing):
    
    def _handleCollision(self, conflictedIndex, newValue):
        
            oldValue = self._hashedArray[conflictedIndex];
            if oldValue:
                Secondary_conflictedIndex=self.nearestPrime() - (newValue % self.nearestPrime()) 
                if Secondary_conflictedIndex==len(self._hashedArray)-1:
                    Secondary_conflictedIndex=0 
                else: 
                    conflictedIndex=(conflictedIndex + Secondary_conflictedIndex) % len(self._hashedArray)
                    if  self._hashedArray[conflictedIndex] != None:
                            self._handleCollision(conflictedIndex,newValue)
            