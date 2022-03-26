"""
I had a version that worked for all cases except the last one, because the time limit exceeded for an unknown reason,
so I had to implement the error handling @sjay05 on GitHub used (even though his solution was wrong!). Again, the early CCC solutions are practice for me.
"""

grid = [ 
[0, -1], [0, -2], [0, -3], [1, -3], [2, -3], 
[3, -3], [3, -4], [3, -5], [4, -5], [5, -5], 
[5, -4], [5, -3], [6, -3], [7, -3], [7, -4], 
[7, -5], [7, -6], [7, -7], [6, -7], [5, -7], 
[4, -7], [3, -7], [2, -7], [1, -7], [0, -7], 
[-1, -7], [-1, -6], [-1, -5]
]

# error-proof it
# notes: check if each increment in the direction is valid
# if it is invalid, the error = True

def calcNext(inputs): # so this function reruns everytime
    x = -1
    y = -5
    goneTo = []
    error = False # Initial assumption
    for i in range(len(inputs)): 
        # (l. 24) will run all inputs in the list we have --> It works for the latest input we inputted because it's the last thing it runs in that instance, and the most updated x and y
        # It's like the function just resets itself to the beginning again, and doesn't pick up from the last spot
        way = inputs[i][0]
        distance = int(inputs[i][1])
        if way == "l":
            for i in range(1, distance+1):
                goneTo.append([x-i, y]) # append the goneTo list to include every point we've crossed
                if [x-i, y] in grid: # if it is found in our grid
                    error = True
                elif goneTo.count([x-i, y]) > 1: # That point we've gone to will already be there once, so we check if it's there more than once. If so, it means that the error is True.
                    error = True
            x -= distance # subtract the distance because 
        elif way == "r":
            for i in range(1, distance+1):
                goneTo.append([x+i, y])
                if [x+i, y] in grid:
                    error = True
                elif goneTo.count([x+i, y]) > 1:
                    error = True
            x += distance
        elif way == "u":
            for i in range(1, distance+1):
                goneTo.append([x, y+i])
                if [x, y+i] in grid:
                    error = True
                elif goneTo.count([x, y+i]) > 1:
                    error = True
            y += distance
        elif way == "d":
            for i in range(1, distance+1):
                goneTo.append([x, y-i])
                if [x, y-i] in grid:
                    error = True
                elif goneTo.count([x, y-i]) > 1:
                    error = True
            y -= distance   
    if error:
        print(str(x), str(y), "DANGER")
        exit()
    else:
        print(str(x), str(y), "safe")

# append directions to a list
inputs = []

while True:
    direction = input().split()
    if "q" in direction:
        break
    else:
        inputs.append(direction)
        calcNext(inputs)




