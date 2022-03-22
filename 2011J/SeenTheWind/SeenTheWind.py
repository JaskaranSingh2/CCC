# A = −6t^4 + ht^3 + 2t^2 +t 

h = int(input())
M = int(input())

t = 1 

while t <= M:
    if ((-6*(t**4)) + (h*(t**3)) + (2*(t**2)) + t) <= 0:
        print(f"The balloon first touches ground at hour:\n{t}")
        exit()
    elif t == M:
        print("The balloon does not touch ground in the given time.")
    t += 1