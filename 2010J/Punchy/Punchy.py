import math

A = 0
B = 0

while True:
    tempL = list(input())
    if tempL[0] == "1":
        if tempL[2] == "A":
            if tempL[4] == "-":
                # till the end of the list
                neg1 = tempL[4] + ''.join()(tempL[5:])
                A = int(neg1)
            else:
                A = int(''.join(tempL[4:]))
        elif tempL[2] == "B":
            if tempL[4] == "-":
                neg2 = tempL[4] + ''.join(tempL[5:])
                B = int(neg2)
            else:
                B = int(''.join(tempL[4:]))
    elif tempL[0] == "2":
        if tempL[2] == "A":
            print(int(A))
        elif tempL[2] == "B":
            print(int(B))
    elif tempL[0] == "3":
        if tempL[2] == "A":
            A = A + B
        elif tempL[2] == "B":
            B = B + A
    elif tempL[0] == "4":
        if tempL[2] == "A":
            A = A * B
        elif tempL[2] == "B":
            B = B * A
    elif tempL[0] == "5":
        if tempL[2] == "A" and tempL[4] == "A":
            A = 0
        elif tempL[2] == "B" and tempL[4] == "B":
            B = 0
        elif tempL[2] == "B" and tempL[4] == "A":
            B = B - A
        else:
            A = A - B
    elif tempL[0] == "6":
        if tempL[2] == "A":
            if B == 0:
                pass
            else:
                A = math.floor(A / B)
        else:
            if A == 0:
                pass
            else:
                B = math.floor(B / A)
    elif tempL[0] == "7":
        exit()
