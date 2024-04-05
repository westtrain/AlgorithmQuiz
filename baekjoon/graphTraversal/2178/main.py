import sys

size = sys.stdin.readline().strip().split(' ')
N = int(size[0])
M = int(size[1])
matrix = []
visited = []
for i in range(N):
  row = list(map(int, sys.stdin.readline().strip()))
  matrix.append(row)
  visitedRow = [0 for j in range(M)]
  visited.append(visitedRow)
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
queue = [[0,0]]
destination = [N-1, M-1]
visited[0][0] = 1
while queue:
  current = queue.pop(0)
  y = current[0]
  x = current[1]
  if y == destination[0] and x == destination[1]:
    break
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and matrix[ny][nx] == 1:
        visited[ny][nx] = visited[y][x] + 1
        queue.append([ny, nx])
print(visited[N-1][M-1])
