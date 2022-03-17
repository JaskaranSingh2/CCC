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

for x in range(len(store)): # for x in the range of the length of the list
        if store[x][0] == "1":
                if store[x][2] == "A":
                        A = int(store[x][4])
                else:
                        B = int(store[x][4])
        elif store[x][0] == "2":
                if store[x][2] == "A":
                        print(A)
                        continue
                else:
                        print(B)
                        continue
        elif store[x][0] == "3":
                if store[x][2] == "A":
                        A = A + B
                else:
                        B = B + A
        elif store[x][0] == "4":
                if store[x][2] == "A":
                        A = A * B
                else:
                        B = B * A
        elif store[x][0] == "5":
                if store[x][2] == "A":
                        A = A - B
                else:
                        B = B - A
        elif store[x][0] == "6":
                if store[x][2] == "A":
                        A = math.floor(A / B)
                else:
                        B = math.floor(B / A)
        elif store[x][0] == "7":
                exit()