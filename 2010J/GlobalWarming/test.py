def take():
    takeInput = input().split()
    averages = takeInput[1:]
    print(averages)
    return averages

def stuff(avg):
    differences = []
    i = 1 # start the indexing from position 1
    while i < len(avg): # index <= 6
        differences.append(int(avg[i]) - int(avg[i-1]))
        # print(l1[index], l1[index-1])
        i+=1
    print(differences)
    print(len(set(differences)))
    differences = []

while True:
    if take() == ["0"]:
        exit()
    else:
        stuff(take())