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
    if i > len(runs1) | i > len(runs2):
        print(0)
    elif check == check2:
        equalDay = len(range(0, i + 1))
        break
    else:
        i += 1
        x += 1
print(equalDay)
