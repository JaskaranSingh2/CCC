# Person 1
# a steps forward, b steps backward

# Person 2
# c steps forward, d steps backward

# a >= b
# c >= d
# Same total number of steps, not same distance
# Nicky and Byron both step forward on their first steps at the same time

a = int(input())
b = int(input()) 
c = int(input())
d = int(input())
S = int(input()) # Total length of step


positionFromStart1 = a - b
currentTotal1 = a + b
positionFromStart2 = c - d
currentTotal2 = c + d

while currentTotal1 != S:
    currentTotal1 += (a + b) 
    positionFromStart1 += (a - b)

print(currentTotal1)
print(positionFromStart1)

while currentTotal2 != S:
    if currentTotal2 + (c+d) > S:
        positionFromStart2 += S - currentTotal2
        break
    else:
        currentTotal2 += (c+d)
        positionFromStart2 += (c - d)     

print(currentTotal2)
print(positionFromStart2)
"""
what I need to do:
The position from start for one sequence is a-b/c-d
The total number of steps is a+b/c+d while it does not equal S
The total number of steps must not exceed S
If a+b/c+d adds to make the total number of steps greater than S, then we will add S - total number of steps
"""
