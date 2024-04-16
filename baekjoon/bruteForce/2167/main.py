import sys

input = sys.stdin.read
data = input().split()

index = 0

N, M = int(data[index]), int(data[index + 1])
index += 2
board = []

for _ in range(N):
    row = list(map(int, data[index:index + M]))
    index += M
    board.append(row)

K = int(data[index])
index += 1

results = []

for _ in range(K):
    i, j, x, y = map(int, data[index:index + 4])
    index += 4
    i -= 1
    j -= 1
    x -= 1
    y -= 1

    area_sum = 0
    for row in range(i, x + 1):
        area_sum += sum(board[row][j:y + 1])
    results.append(area_sum)

for result in results:
    print(result)


