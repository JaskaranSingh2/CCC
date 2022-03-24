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
    reference = [-1, -5]
    i = 0
    while i < len(existing):
        if point == existing[i]:
            print(point[0], point[1], "danger")
            exit()
        else:
            i += 1

    print(point[0], point[1], "safe")
    return True

lastPoint = [-1, -5]


while True:
    drill = input().split()
    if drill[0] == "l":
        x = 1
        while x <= int(drill[1]):
            lastPoint[0] -= 1      
                visited.append(lastPoint[:]) # Copy array by slicing --> instead of pointing to same memory location.
                x += 1
        checker(lastPoint, visited)
    elif drill[0] == "r":
        x = 1
        while x <= int(drill[1]):
            lastPoint[0] += 1      
                visited.append(lastPoint[:])
                x += 1
        checker(lastPoint, visited)
    elif drill[0] == "d":
        x = 1
        while x <= int(drill[1]): 
            lastPoint[1] -= 1              
                visited.append(lastPoint[:])
                x += 1
        checker(lastPoint, visited)
    elif drill[0] == "u":
        x = 1
        while x <= int(drill[1]):
            lastPoint[1] += 1              
                visited.append(lastPoint[:])
                x += 1
        checker(lastPoint, visited)
    elif drill[0] == "q":
        exit()