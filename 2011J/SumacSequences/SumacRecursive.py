# t(n+2) = t(n) - t(n+1)
# t(1+2) = t(1) - t(2)
# This doesn't work as of yet
def sumac(t1, t2):
    sumacList = [t1, t2]
    nextSeq = t1 - t2
    sumacList.append(nextSeq)
    if nextSeq < t2:
        sumac(t1, nextSeq)
    else:
        print(len(sumacList))
        exit()


tO = int(input())
tT = int(input())

sumac(tO, tT)
