def splitter():
    temperatures = input().split()
    if temperatures[0] == "0":
        exit()
    averages = temperatures[1:]
    return averages

def cycle(arr):
    differences = []
    i = 1 # 1-based indexing
    while i < len(arr):
        differences.append(int(arr[i]) - int(arr[i-1]))
        i+=1
    print(len(set(differences)))
    
while True:
    data = splitter()
    cycle(data)