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
            i=1
            PreviouseIndex=0
            while(1):  
                if conflictedIndex==len(self._hashedArray)-1:
                    oldValue = self._hashedArray[conflictedIndex]; 
                    if oldValue: 
                        conflictedIndex=0 
                    else:  
                        self._hashedArray[conflictedIndex]=newValue
                elif conflictedIndex<len(self._hashedArray)-1: 
                    oldValue = self._hashedArray[conflictedIndex]; 
                    if oldValue: 
                        #Calculating Next Possible Index
                        Secondary_conflictedIndex=self.nearestPrime() - (newValue % self.nearestPrime()) 
                        Secondary_conflictedIndex=(conflictedIndex + (i*Secondary_conflictedIndex)) % len(self._hashedArray)
                        PreviouseIndex=conflictedIndex
                        conflictedIndex=Secondary_conflictedIndex
                        i+=1
                    else: 
                        self._hashedArray[conflictedIndex]=newValue
                else:
                    #if  hash id is greater than table index then new hashid will be start from index 0 in cyclic order
                    conflictedIndex= ((0+conflictedIndex) -(len(self._hashedArray)-PreviouseIndex))-1
            