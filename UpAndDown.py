aSteps = int(input())
bSteps = int(input())
cSteps = int(input())
dSteps = int(input())
sTotal = int(input())

countAB = 0
countCD = 0
stepsAB = 0
stepsCD = 0
while countAB != sTotal:
    if sTotal - countAB < countAB:
        countAB += sTotal - countAB
    else:
        countAB += aSteps + bSteps
        stepsAB += aSteps - bSteps
    
while countCD != sTotal:
    if sTotal - countCD >= countCD:
        countCD += sTotal - countCD
    else:
        countCD += cSteps + dSteps
        stepsCD += cSteps - dSteps

print(stepsAB)
print(stepsCD)

if stepsAB > stepsCD:
    print("Nikky")
elif stepsAB == stepsCD:
    print("Tied")
else:
    print("Byron")