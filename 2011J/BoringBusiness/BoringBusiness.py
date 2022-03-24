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


def checker(point, existing, store, dangerous):
    i = 0
    while i < len(existing):
        if point == existing[i]:
            print(point[0], point[1], "DANGER")
            exit()
        else:
            i += 1

    j = 0
    while i < len(store):
        if store.count(point) > 1:
            if point == store[i]:
                print(point[0], point[1], "DANGER")
                exit()

    for x in store:
        for y in existing:
            if x == y:
                print(dangerous[0], dangerous[1], "DANGER")
                exit()

    print(point[0], point[1], "safe")
    return True


lastPoint = [-1, -5]
reference = [-1, -5]
store = []

while True:
    drill = input().split()
    if drill[0] == "l":
        if lastPoint[0] - int(drill[1]) < -201:
            exit()
        x = 1
        while x <= int(drill[1]):
            lastPoint[0] -= 1
            # Copy array by slicing --> instead of pointing to same memory location.
            store.append(lastPoint[:])
            x += 1
        cross = lastPoint[0] + x - int(drill[1]) - 1
        actual = [cross, lastPoint[1]]
        checker(lastPoint, visited, store, actual)
    elif drill[0] == "r":
        if lastPoint[0] + int(drill[1]) > 199:
            exit()
        x = 1
        while x <= int(drill[1]):
            lastPoint[0] += 1
            store.append(lastPoint[:])
            x += 1
        cross = lastPoint[0] - x + int(drill[1]) + 1
        actual = [cross, lastPoint[1]]
        checker(lastPoint, visited, store, actual)
    elif drill[0] == "d":
        if lastPoint[1] - int(drill[1]) > 200:
            exit()
        x = 1
        while x <= int(drill[1]):
            lastPoint[1] -= 1
            store.append(lastPoint[:])
            x += 1
        cross = lastPoint[1] + x - int(drill[1]) - 1
        actual = [lastPoint[0], cross]
        checker(lastPoint, visited, store, actual)
    elif drill[0] == "u":
        if int(drill[1]) + lastPoint[1] > 0:
            exit()
        x = 1
        while x <= int(drill[1]):
            lastPoint[1] += 1
            store.append(lastPoint[:])
            x += 1
        cross = lastPoint[1] - x + int(drill[1]) + 1
        actual = [lastPoint[0], cross]
        checker(lastPoint, visited, store, actual)
    elif drill[0] == "q":
        exit()
