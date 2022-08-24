'''
Created on Aug 24, 2022

@author: Ramachandran S
'''

class CollisionInputBean:
    
    def __init__(self, currentIndex : int, newIndex : int, inputValue, resultArray : list):
        self.__currentIndex = currentIndex;
        self.__newResultIndex = newIndex;
        self.__inputValue = inputValue;
        self.__resultArray = resultArray;

    def getCurrentIndex(self):
        return self.__currentIndex;
    
    def getNewResultIndex(self):
        return self.__newResultIndex;
    
    def getInputValue(self):
        return self.__inputValue;
    
    def getResultArray(self):
        return self.__resultArray;
    
    def getResultIndexValue(self):
        return self.__resultArray[self.__newResultIndex];
    
