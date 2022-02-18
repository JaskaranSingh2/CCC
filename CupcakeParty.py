regBox = int(input()) * 8
smBox = int(input()) * 3
eachStudent = 28
total = regBox + smBox
if (regBox >= 0) | (smBox >= 0):
    print(total - eachStudent)