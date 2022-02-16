# number of bids: (1 <= n < 100)
n = int(input())
1 <= n <= 100
# Highest bid thus far:
highestBid = 0  # initially set = 0

# Empty winner variable that will be replace
winner = ""

i = 0
while i < n:
    if (1 <= n <= 100) is True:
        name = str(input())
        currentBid = int(input())
        if currentBid >= 2000:
            raise Exception("")
        elif currentBid > highestBid:
            highestBid = currentBid
            winner = name
        elif currentBid == highestBid:
            pass
        i += 1

print(winner)
