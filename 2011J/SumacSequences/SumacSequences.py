# t(n+2) = t(n) - t(n+1)
# Terminate when if t(m-1) < t(m) where m is the last term number
# Output the length of the sequence

# t1, t2 -> integers passed in
def sumac(t1, t2):
    sumacList = [t1, t2]
    i = 1
    while True:
        nextSeq = int(sumacList[i - 1]) - int(sumacList[i])
        sumacList.append(nextSeq)
        i += 1
        if sumacList[i] > sumacList[i - 1]:
            print(len(sumacList))
            exit()


t1 = int(input())
t2 = int(input())
sumac(t1, t2)
