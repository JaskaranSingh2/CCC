def splitter():
    temperatures = input().split()
    if temperatures[0] == "0" or int(temperatures[0]) < 1 or int(temperatures[0]) > 20:
        exit()
    else:
        averages = temperatures[1:]
        return averages


def cycle(arr):
    differences = []
    i = 1  # 1-based indexing
    while i < len(arr):
        if int(arr[i-1]) > 1000 or int(arr[i-1]) < -1000:
            exit()
        else:
            differences.append(int(arr[i]) - int(arr[i-1]))
        i += 1
    if len(set(differences)) == len(differences):
        print(len(differences))
    else:
        print(len(set(differences)))


while True:
    data = splitter()
    if data == 1:
        print(1)
        exit()
    cycle(data)
