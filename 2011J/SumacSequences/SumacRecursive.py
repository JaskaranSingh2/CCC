# t(n+2) = t(n) - t(n+1)

def sumac(tn, tnp1):
    termList = [tn, tnp1]
    nextTerm = tn - tnp1
    termList.append(nextTerm)
    if nextTerm > tnp1:
        print(len(termList))
        exit()
    sumac(tnp1, nextTerm)

tn = int(input())
tnp1 = int(input())

sumac(tn, tnp1)