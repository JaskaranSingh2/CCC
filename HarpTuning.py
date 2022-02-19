ins = list((input()))
i = 0

while ins[i] != "+":
    insA = ins[0 : i + 1]
    i += 1
    firstIns = "".join(insA)
print(firstIns + " tighten " + ins[i + 1])

x = 0

while ins[x] != "-":
    insB = ins[i + 2 : x + 1]
    x += 1
    secondIns = "".join(insB)
print(secondIns + " loosen " + ins[x + 1])

z = 0 

while ins[]

# nah man