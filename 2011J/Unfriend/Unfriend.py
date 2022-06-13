
N = int(input())
N = N if N <= 6 else exit()

tracker = {}

lineN = 0
for i in (range(1, N)):
    lineN += 1
    tracker[lineN] = []
    tracker[lineN].append(int(input()))
    print(tracker[lineN])

visited = set()

def dfs(visited, tracker, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in tracker[node]:
            dfs(visited, tracker, neighbour)

dfs(visited, tracker, 1)