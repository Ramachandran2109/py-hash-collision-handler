'''
Created on Aug 21, 2022

@author: Ramachandran S
'''

import ast

from project.ct1.hash.collisions.CollisionHandlerType import CollisionHandlerType
from project.ct1.hash.HashFactory import HashFactory


inputArray = [];
hashedArray = [];
collisionHandlerType = 0;

#criteria given for the max array size in the assignment
max_size = {1:10, 2:10, 3:20, 4:10, 5:6};

def getCollisionHandlerType():
    
    collisionHandlerTypes = list(CollisionHandlerType);
    for i in range(len(collisionHandlerTypes)) :
        print (collisionHandlerTypes[i].value,". ", collisionHandlerTypes[i].name); 
        
    global collisionHandlerType
    while True:
        collisionHandlerTypeInput = input("Select Collision Type Index/Name from the list : ");
        match collisionHandlerTypeInput.upper():
            case "1" | "SEPARATE_CHAINING":
                collisionHandlerType = 1;
                break;
            case "2" | "LINEAR_PROBING":
                collisionHandlerType = 2;
                break;
            case "3" | "QUADRATIC_PROBING":
                collisionHandlerType = 3;
                break;
            case "4" | "DOUBLE_HASHING":
                collisionHandlerType = 4;
                break;
            case "5" | "CUCKOO":
                collisionHandlerType = 5;
                break;
            case _:
                print("Invalid Input, Please select a valid collision type");
                for i in range(len(collisionHandlerTypes)) :
                    print (collisionHandlerTypes[i].value,". ", collisionHandlerTypes[i].name);

def getUserInputs():
    while True:
        print("");
        totalValues = ast.literal_eval(input("Enter number of values to be inserted (Max : {}) : ".format(max_size.get(collisionHandlerType))));
        if (totalValues <= max_size.get(collisionHandlerType)):
            global inputArray
            inputArray = ["" for i in range(totalValues)];
            
            global hashedArray
            hashedArray = [];
            
            for i in range(totalValues):
                inputArray[i] = ast.literal_eval(input("Enter " + str(i + 1) + " value : "));
            break;
        else:
            print("Value should not exceed more than {}".format(max_size.get(collisionHandlerType)));
   
                    
def execute():
    print("");
    print("Input values : ", inputArray);
    print("Collision Handler : ", CollisionHandlerType(collisionHandlerType).name);
    
    hashing = HashFactory.getInstance(collisionHandlerType, max_size.get(collisionHandlerType), inputArray);
    hashedArray = hashing.doHash();
    
    print("");
    print("After Hashing : ", hashedArray);
    print("");
    

getCollisionHandlerType();
getUserInputs();
execute();

while True:
    tryOtherCollision = input("Do you wish to try any other collision with the same input (Y/N) ?");
    match tryOtherCollision.upper():
        case "Y":
            getCollisionHandlerType();
            execute();
        case "N":
            break;
        case _:
            print("Invalid input try again...");
            
while True:
    tryOtherCollision = input("Do you wish to try any other collision with the different input (Y/N) ?");
    match tryOtherCollision.upper():
        case "Y":
            getCollisionHandlerType();
            getUserInputs();
            execute();
        case "N":
            break;
        case _:
            print("Invalid input try again...");

print("");
print("*****END*****")
