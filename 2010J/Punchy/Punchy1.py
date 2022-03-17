import math

from numpy import longcomplex

a = 0
b = 0


while True:
    tempL = list(input())
    if tempL[0] == "1":
            if tempL[2] == "A":
                    A = int(tempL[4])
            else:
                    B = int(tempL[4])
    elif tempL[0] == "2":
            if tempL[2] == "A":
                    print(A)
                    continue
            else:
                    print(B)
                    continue
    elif tempL[0] == "3":
            if tempL[2] == "A":
                    A = A + B
            else:
                    B = B + A
    elif tempL[0] == "4":
            if tempL[2] == "A":
                    A = A * B
            else:
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
                    A = math.floor(A / B)
            else:
                    B = math.floor(B / A)
    elif tempL[0] == "7":
            exit()