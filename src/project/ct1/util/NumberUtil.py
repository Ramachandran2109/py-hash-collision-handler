'''
Created on Aug 31, 2022

@author: Ramachandran S

'''
from math import factorial


class NumberUtil :
    
    @staticmethod
    def getPrime(n):
     
        # Base case
        if (n <= 1):
            return 2
     
        prime = n + 1
        found = False
     
        # Loop continuously until isPrime returns
        # True for a number greater than n
        while(not found):
            if factorial(prime - 1) % prime == prime -1:
                found = True
            else:
                prime +=1
     
        return prime