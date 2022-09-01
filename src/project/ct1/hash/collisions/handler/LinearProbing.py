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
                if conflictedIndex==len(self._hashedArray)-1:
                    oldValue = self._hashedArray[conflictedIndex]
                    if oldValue :
                        conflictedIndex=0
                    else:  
                        #Calculating Next Possible Index
                        self._hashedArray[conflictedIndex]=newValue
                elif conflictedIndex<len(self._hashedArray)-1:  
                    oldValue = self._hashedArray[conflictedIndex]
                    if oldValue : 
                        conflictedIndex=conflictedIndex+1
                    else:  
                        #Calculating Next Possible Index 
                        self._hashedArray[conflictedIndex]=newValue
                else:
                    #if  hash id is greater than table index then new hashid will be start from index 0 in cyclic order
                    conflictedIndex=0