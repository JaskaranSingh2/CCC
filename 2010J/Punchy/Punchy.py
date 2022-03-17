import math

# math.floor
A = 0
B = 0

store = []
i = 0
while i < 6:
        store.append(list(input()))
        i+=1
print(store)

for i in range(len(store)): # for i in the range of the length of the list
        if store[i][4] == "a":
                print("yes")
                break