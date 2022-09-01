'''
Created on Aug 20, 2022

@author: Ramachandran S

Requirement : 
    Implement doHash table where collisions are handled using linear probing. Keep MAX size of arr in hashtable as 10.  
    
@attention: handleCollision logic is implemented by.
    Name : Anbuselvan Balakrishnan
    Registration Number : 22421005928
    
'''

from project.ct1.hash.Hashing import Hashing


class LinearProbing(Hashing):
    
    def _handleCollision(self, conflictedIndex, newValue): 
        while(1):
                oldValue = self._hashedArray[conflictedIndex];
                if oldValue :
                    if conflictedIndex==len(self._hashedArray)-1:
                        conflictedIndex=0
                    else:  
                        conflictedIndex=conflictedIndex+1
                else: 
                    if  self._hashedArray[conflictedIndex] != None:
                        self._handleCollision(conflictedIndex,newValue)
                    else:
                        self._hashedArray[conflictedIndex]=newValue
                        break