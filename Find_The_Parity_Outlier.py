import unittest

def find_outlier(integers):
    
    evens = [num for num in integers if num % 2 == 0]
    odds = [num for num in integers if num % 2 != 0]
    
    
    return evens[0] if len(evens) == 1 else odds[0]

        


lista = [3,5,79,11,7,0]

print(find_outlier(lista))
        
        
        


    

