def splitter():
    temperatures = input().split()
    averages = temperatures[1:]
    return averages

def cycle(arr):
    differences = []
    i = 1 # 1-based indexing
    while i < len(arr):
        differences.append(int(arr[i]) - int(arr[i-1]))
        i+=1
    print(len(set(differences)))
    print(arr[i], arr[i-1]) # Why does it say it's out of range? It was working before...

while True:
    if splitter() == ["0"]:
        exit()
    else:
        cycle(splitter())