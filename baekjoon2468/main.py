import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline().strip())

matrix = []
visited = []
peak = 0
for _ in range(N):
  row = list(map(int, sys.stdin.readline().strip().split()))
  peak = max(peak, max(row))
  matrix.append(row)

def dfs(x, y, matrix, h):
  if x < 0 or x >= N or y < 0 or y >= N or matrix[x][y] <= h or visited[x][
      y] == 1:
    return
  visited[x][y] = 1
  dfs(x + 1, y, matrix, h)
  dfs(x - 1, y, matrix, h)
  dfs(x, y + 1, matrix, h)
  dfs(x, y - 1, matrix, h)


maxCount = 0
for h in range(peak):
  visited = [[0 for _ in range(N)] for _ in range(N)]
  count = 0
  for i in range(N):
    for j in range(N):
      if matrix[i][j] > h and visited[i][j] == 0:
        dfs(i, j, matrix, h)
        count += 1
  maxCount = max(maxCount, count)

print(maxCount)

