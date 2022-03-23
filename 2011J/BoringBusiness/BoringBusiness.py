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

# for x, y in visited:
#     print(x, y)


drill = input().split()
lastPoint = [-1, -5]
sto = []


if drill[0] == "l":
    lastPoint[0] = int(lastPoint[0]) - int(drill[1:])
    sto.append(lastPoint)
elif drill[0] == "r":
    lastPoint[0] = int(lastPoint[0]) + int(drill[1:])
    sto.append(lastPoint)
elif drill[0] == "d":
    lastPoint[1] = int(lastPoint[1]) - int(drill[1:])
    sto.append(lastPoint)
elif drill[0] == "u":
    lastPoint[1] = int(lastPoint[1]) + int(drill[1:])
    sto.append(lastPoint)
elif drill[0] == "q":
    exit()

i = 0
j = 0

while i < len(sto):
    while j < len(visted):
        if sto[i] == visited[j]:
            print(sto[i], "danger")
            exit()
        else:
            j += 1
    i += 1