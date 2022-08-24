'''
Created on Aug 21, 2022

@author: Ramachandran S
'''

import ast

from project.ct1.hash.Hashing import Hashing
from project.ct1.hash.collisions.CollisionHandlerType import CollisionHandlerType


inputArray = [];
collisionHandlerType = 0;

def getUserInputs():
    totalValues = ast.literal_eval(input("Enter number of values to be inserted : "));
    global inputArray
    inputArray = ["" for i in range(totalValues)];
    
    for i in range(totalValues):
        inputArray[i] = ast.literal_eval(input("Enter " + str(i + 1) + " value : "));

def getCollisionHandlerType():
    
    print("");
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
                    
def execute():
    getCollisionHandlerType();
    print("");
    print("Input values : ", inputArray);
    print("Collision Handler : ", CollisionHandlerType(collisionHandlerType).name);
    
    hashing = Hashing.getCollisionHandlerInstance(collisionHandlerType, inputArray);
    hashedArray = hashing.doHash();
    
    print("");
    print("After Hashing : ", hashedArray);
    print("");

getUserInputs();
execute();

while True:
    tryOtherCollision = input("Do you wish to try any other collision with the same input (Y/N) ?");
    match tryOtherCollision.upper():
        case "Y":
            execute();
        case "N":
            break;
        case _:
            print("Invalid input try again...");
            
while True:
    tryOtherCollision = input("Do you wish to try any other collision with the different input (Y/N) ?");
    match tryOtherCollision.upper():
        case "Y":
            getUserInputs();
            execute();
        case "N":
            break;
        case _:
            print("Invalid input try again...");

print("");
print("................")
