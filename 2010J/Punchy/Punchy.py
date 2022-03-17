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
        if store[i][0] == "1":
                if store[i][2] == "A":
                        A = int(store[i][4])
                else:
                        B = int(store[i][4])
        elif store[i][0] == "2":
                if store[i][2] == "A":
                        print(A)
                else:
                        print(B)
        elif store[i][0] == "3":
                if store[i][2] == "A":
                        A = A + B
                else:
                        B = B + A
        elif store[i][0] == "4":
                if store[i][2] == "A":
                        A = A * B
                else:
                        B = B * A
        elif store[i][0] == "5":
                if store[i][2] == "A":
                        A = A - B
                else:
                        B = B - A
        elif store[i][0] == "6":
                if store[i][2] == "A":
                        A = math.floor(A / B)
                else:
                        B = math.floor(B / A)
        elif store[i][0] == "7":
                exit()