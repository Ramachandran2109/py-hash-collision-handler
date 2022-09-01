'''
Created on Aug 21, 2022

@author: Ramachandran S
'''

import ast

from project.ct1.hash.collisions.CollisionHandlerType import CollisionHandlerType
from project.ct1.hash.HashFactory import HashFactory


inputArray = []
hashedArray = []
enableRehash = False
collisionHandlerType = 0

#criteria given for the max array size in the assignment
max_size = {1:10, 2:10, 3:20, 4:10, 5:6}

def getCollisionHandlerType():
    
    collisionHandlerTypes = list(CollisionHandlerType)
    for i in range(len(collisionHandlerTypes)) :
        print (collisionHandlerTypes[i].value,". ", collisionHandlerTypes[i].name) 
        
    global collisionHandlerType
    while True:
        collisionHandlerTypeInput = input("Select Collision Type Index/Name from the list : ")
        match collisionHandlerTypeInput.upper():
            case "1" | "SEPARATE_CHAINING":
                collisionHandlerType = 1
                break
            case "2" | "LINEAR_PROBING":
                collisionHandlerType = 2
                break
            case "3" | "QUADRATIC_PROBING":
                collisionHandlerType = 3
                break
            case "4" | "DOUBLE_HASHING":
                collisionHandlerType = 4
                break
            case "5" | "CUCKOO":
                collisionHandlerType = 5
                break
            case _:
                print("Invalid Input, Please select a valid collision type")
                for i in range(len(collisionHandlerTypes)) :
                    print (collisionHandlerTypes[i].value,". ", collisionHandlerTypes[i].name)


def getUserInputs():
    while True:
        print("")
        totalValues = ast.literal_eval(input("Enter number of values to be inserted (Max : {}) : ".format(max_size.get(collisionHandlerType))))
        if (totalValues <= max_size.get(collisionHandlerType)):
            global inputArray
            inputArray = [None for i in range(totalValues)]
            
            global hashedArray
            hashedArray = []
            
            for i in range(totalValues):
                inputArray[i] = ast.literal_eval(input("Enter " + str(i + 1) + " value : "))
            break
        else:
            print("Value should not exceed more than {}".format(max_size.get(collisionHandlerType)))
    
    if (collisionHandlerType != 1):
        global enableRehash
        canEnableRehashStr = input("Enable Rehashing (Y/N) : ")
        match canEnableRehashStr.upper() :
            case "Y" | "T" | "YES" | "TRUE":
                enableRehash = True
            case _:
                enableRehash = False
                
   
                   
def execute():
    print("")
    print("Input values : ", inputArray)
    print("Collision Handler : ", CollisionHandlerType(collisionHandlerType).name)
    print("Rehashing Enabled : ", enableRehash)
    
    hashing = HashFactory.getInstance(collisionHandlerType, max_size.get(collisionHandlerType), enableRehash, inputArray)
    hashedArray = hashing.doHash()
    
    print("")
    print("After Hashing : ", hashedArray)
    print("")
    
    print("Result Array : ")
    for i in range(len(hashedArray)):
        if (hashedArray[i] is not None) :
            print(" Index : ", i, " Value : ", hashedArray[i])


def main():
    print("*****BEGIN*****")
    print("")
    
    getCollisionHandlerType()
    getUserInputs()
    execute()
    
    print("")
    print("*****END*****")
    

if __name__=="__main__":
    main()
