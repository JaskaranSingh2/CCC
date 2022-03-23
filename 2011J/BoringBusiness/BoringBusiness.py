visited = [
    [0, -1], 
    [0, -2], 
    [0, -3], 
    [1, -3], 
    [2, -3], 
    [3, -3], 
    [3, -4], 
    [3, -5], 
    [4, -5], 
    [5, -5], 
    [5, -4], 
    [5, -3], 
    [6, -3], 
    [7, -3], 
    [7, -4], 
    [7, -5],
    [7, -6], 
    [7, -7], 
    [6, -7], 
    [5, -7], 
    [4, -7], 
    [3, -7], 
    [2, -7], 
    [1, -7],
    [0, -7], 
    [-1, -7], 
    [-1, -6], 
    [-1, -5]
    ]

def checker(point, existing, added):
    i = 0
    while i < len(existing):
        if point == existing[i]:
            print(point, "danger")
            exit()
        else:
            i += 1
    
    j = 0
    while j < len(added):
        if added.count(point) > 1:
            print(point, "danger")
            exit()
        else:
            j += 1

    print(point, "safe")

drill = input().split()
lastPoint = [-1, -5]
sto = []

while True:
    if drill[0] == "l":
        lastPoint[0] -= int(drill[1])
        sto.append(lastPoint)
        checker(lastPoint, visited, sto)
    elif drill[0] == "r":
        lastPoint[0] += int(drill[1])
        sto.append(lastPoint)
        checker(lastPoint, visited, sto)
    elif drill[0] == "d":
        lastPoint[1] -= int(drill[1])
        sto.append(lastPoint)
        checker(lastPoint, visited, sto)
    elif drill[0] == "u":
        lastPoint[1] += int(drill[1])
        sto.append(lastPoint)
        checker(lastPoint, visited, sto)
    elif drill[0] == "q":
        exit()