x, y = map(int, input().split())
startPos = (x, y)

x, y = map(int, input().split())
endPos = (x, y)

board = []

i = 1
while i <= 8:
    board.append([100, 100, 100, 100, 100, 100, 100, 100])
    i+=1
print(board)


def distance(x, y, steps):
    if x < 9 and x > 0 and y < 9 and y > 0 and steps != board[y][x]:
        board[y][x] = 
        distance(x, y, steps)