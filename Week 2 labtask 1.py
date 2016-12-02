import math

def findHighestSquare(number):
    if(number<0):             
        return "Negative Input"
    squareRoot = math.sqrt(number)# find the square root
    floor = math.floor(squareRoot)# finds the floor of n
    answer = floor*floor# finds square of floor	
    return int(answer)
    
number = int(raw_input("Enter a number: "))
print findHighestSquare(number)
