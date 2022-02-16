n = int(input())
runs1 = list(map(int, input().split()))
runs2 = list(map(int, input().split()))

# print(max(runs1))
# Max runs can't be greater than 20

i = 1
x = 0

while True:
    check = runs1[x * i] + runs1[i]
    check2 = runs2[x * i] + runs2[i]
    if check == check2:
        equalDay = len(range(0, i + 1))
        break
    elif bool(runs1[i] | runs2[i] | runs1[x * i] | runs2[x * i]) == False:
        print(0)
        break
    else:
        x += 1
        i += 1
print(equalDay)
