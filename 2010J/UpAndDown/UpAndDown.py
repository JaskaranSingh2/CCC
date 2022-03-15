a = int(input())
b = int(input()) 
c = int(input())
d = int(input())
S = int(input()) # Total length of step


positionFromStart1 = a - b
currentTotal1 = a + b
positionFromStart2 = c - d
currentTotal2 = c + d

while currentTotal1 <= S:
    if currentTotal1 + (a + b) > S:
        difference1 = S - currentTotal1
        currentTotal1 += difference1
        positionFromStart1 += difference1
        break
    else:
        currentTotal1 += (a + b) 
        positionFromStart1 += (a - b)

while currentTotal2 <= S:
    if currentTotal2 + (c + d) > S:
        difference2 = S - currentTotal2 
        currentTotal2 += difference2
        positionFromStart2 += difference2
        break
    else:
        currentTotal2 += (c + d)
        positionFromStart2 += (c - d)     

if positionFromStart1 > positionFromStart2:
    print("Nikky")
elif positionFromStart1 == positionFromStart2:
    print("Tied")
else:
    print("Byron")
