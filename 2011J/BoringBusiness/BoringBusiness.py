"""
I had a version that worked for all cases except the last one, because the time limit exceeded for an unknown reason,
so I had to implement the error handling @sjay05 on GitHub used. Again, the early CCC solutions are practice for me.
"""

grid = [ 
[0, -1], [0, -2], [0, -3], [1, -3], [2, -3], 
[3, -3], [3, -4], [3, -5], [4, -5], [5, -5], 
[5, -4], [5, -3], [6, -3], [7, -3], [7, -4], 
[7, -5], [7, -6], [7, -7], [6, -7], [5, -7], 
[4, -7], [3, -7], [2, -7], [1, -7], [0, -7], 
[-1, -7], [-1, -6], [-1, -5]
]

def calcNext(inputs):
    x = -1
    y = -5
    error = False # Initial assumption
    for i in range(len(inputs)):
        way = inputs[i][0]
        distance = int(inputs[i][1])
        if way == "l":
            for i in range(1, distance+1):
                if [x-i, y] in grid:
                    error = True
            coordinate = [x-distance, y]
        elif way == "r":
            for i in range(1, distance+1):
                if [x+i, y] in grid:
                    error = True
            coordinate = [x+distance, y]
        elif way == "u":
            for i in range(1, distance+1):
                if [x, y+i] in grid:
                    error = True
            coordinate = [x, y+distance]
        elif way == "d":
            for i in range(1, distance+1):
                if [x, y-i] in grid:
                    error = True
            coordinate = [x, y-distance]   
    if error:
        print(coordinate[0], coordinate[1], "DANGER")
        exit()
    else:
        print(coordinate[0], coordinate[1], "safe")

# append directions to a list
inputs = []

while True:
    direction = input().split()
    if "q" in direction:
        break
    else:
        inputs.append(direction)
        calcNext(inputs)


# error-proof it
# notes: check if each increment in the direction is valid
# if it is invalid, the error = True

