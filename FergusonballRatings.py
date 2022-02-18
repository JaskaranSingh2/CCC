P = int(input())  # total num of players

i = 0
count = 0

while i < P:
    sPts = int(input()) * 5  # stars received from points
    sFoul = int(input()) * -3  # stars lost from fouls
    sRating = sPts + sFoul

    if sRating > 40:
        count += 1
    elif sRating <= 40:
        pass
    i += 1

if count < P:
    print(str(count))
else:
    print(str(count) + "+")