sG = int(input())
sN = []
i = 0
while i < sG:
    sN += list(map(str, input().split()))
    i += 1

dG = int(input())
dN = []
i = 0

while i < dG:
    dN += list(map(str, input().split()))
    i += 1


thrSG = int(input())
thrSN = []
i = 0
while i < thrSG:
    thrSN += list(map(str, input().split()))
    i += 1

constraints = sG + dG + thrSG
