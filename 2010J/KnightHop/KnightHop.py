# inspired from stuff I found on the internet

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
board = []

for i in range(9):
    board.append([100, 100, 100, 100, 100, 100, 100, 100, 100])  # why nine?


def dist(x, y, steps):
    if x < 9 and x > 0 and y < 9 and y > 0 and steps < board[y][x]:
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
