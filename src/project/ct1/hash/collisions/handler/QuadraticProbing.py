'''
Created on Aug 20, 2022

@author: Ramachandran S

Requirement : 
    Implement doHash table where collisions are handled using quadratic probing. Keep MAX size of arr in hashtable as 20.
    
@attention: handleCollision logic is implemented by.
    Name : Anbuselvan Balakrishnan
    Registration Number : 22421005928
    
'''

from project.ct1.hash.Hashing import Hashing

class QuadraticProbing(Hashing):
    
    def _handleCollision(self, conflictedIndex, newValue):
        i=1
        while(1):
            oldValue = self._hashedArray[conflictedIndex]
            if oldValue :
                if conflictedIndex==len(self._hashedArray)-1:
                    conflictedIndex=0
                else: 
                    conflictedIndex=conflictedIndex+ (i*i)
                    i=i+1
            else: 
                if  self._hashedArray[conflictedIndex] != None:
                    self._handleCollision(conflictedIndex,newValue)
                else:
                    self._hashedArray[conflictedIndex]=newValue 
                    break 
        

                