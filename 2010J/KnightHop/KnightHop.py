# Inspired from stuff I found on the internet

x1, y1 = map(int, input().split()) # Get initial x and y
x2, y2 = map(int, input().split()) # Get final x and y
x1, y1, x2, y2 = (x1 - 1), (y1 - 1), (x2 - 1), (y2 - 1) 
# push it back one because indexing the board is 0 to 7 inclusive (see line 11 for explanation)

board = []

# Fill board 8 * 8
for i in range(8):
    board.append([100, 100, 100, 100, 100, 100, 100, 100]) 

# Recursion

def dist(x, y, steps):
    if x <= 7 and x >= 0 and y <= 7 and y >= 0 and steps < board[y][x]:
        board[y][x] = steps
        dist(x + 2, y + 1, steps + 1)
        dist(x + 2, y - 1, steps + 1)
        dist(x - 2, y + 1, steps + 1)
        dist(x - 2, y - 1, steps + 1)
        dist(x + 1, y + 2, steps + 1)
        dist(x + 1, y - 2, steps + 1)
        dist(x - 1, y - 2, steps + 1)
        dist(x - 1, y + 2, steps + 1)


dist(x1, y1, 0)
print(board[y2][x2])
