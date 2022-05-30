from pyparsing import traceParseAction


N = int(input())
N = N if N <= 6 else exit()

tracker = {
    
}
lineN = 0
for i in (range(1, N)):
    lineN += 1
    tracker[lineN] = []
    tracker[lineN].append(int(input()))
    print(tracker[lineN])