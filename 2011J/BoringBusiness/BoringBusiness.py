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

def checker(point, existing):
    i = 0
    while i < len(existing):
        if point == existing[i]:
            print(point, "danger")
            print(existing[i], i)
            exit()
        else:
            i += 1

    print(point, "safe")

lastPoint = [-1, -5]

while True:
    drill = input().split()
    if drill[0] == "l":
        lastPoint[0] -= int(drill[1])
        checker(lastPoint, visited)
        visited.append(lastPoint[:]) # Copy array instead of pointing to same memory location.
    elif drill[0] == "r":
        lastPoint[0] += int(drill[1])
        checker(lastPoint, visited)
        visited.append(lastPoint[:])
    elif drill[0] == "d":
        lastPoint[1] -= int(drill[1])
        checker(lastPoint, visited)
        visited.append(lastPoint[:])
    elif drill[0] == "u":
        lastPoint[1] += int(drill[1])
        checker(lastPoint, visited)
        visited.append(lastPoint[:])
    elif drill[0] == "q":
        exit()