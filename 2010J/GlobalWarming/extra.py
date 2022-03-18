d = [(1, 2, 3), (3, 4, 5), (5, 6, 7)]
for x, y, z in d:
    print(x, y, z)

    # unpacking tuples in a list

    numbers = [12, 23, 3, 4, 52, 6]

    copy = [ALL for ALL in numbers]
    print(copy)
    greater = [gThanTen for gThanTen in numbers if gThanTen > 10]
    print(greater)
