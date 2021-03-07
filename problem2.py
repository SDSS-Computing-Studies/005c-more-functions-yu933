#!python3
"""
Create a function that finds the missing side in a right triangle.
3 input parameters:
float: one side
float: another side
boolean: indicates whether one of the sides is the hypotenuse

return: float length of the missing side

Sample assertions:
assert hypotenuse(12,5,False) == 13
assert hypotenuse(5,3,True) == 4
(2 points)
"""

import math 
def hypotenuse(x, y, sign):
    if sign:
        return math.pow(math.pow(max(x, y),2) - math.pow(min(x,y), 2), 1/2)
    else:
        return math.pow((math.pow(x,2) + math.pow(y,2)),1/2)