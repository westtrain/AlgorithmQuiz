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

# 메모리 32604 KB
# 속도 2992 ms 

# 재귀 대신 스택을 사용해서 성능 개선
import sys

N = int(sys.stdin.readline().strip())
matrix = []
peak = 0
for _ in range(N):
  row = list(map(int, sys.stdin.readline().strip().split()))
  peak = max(peak, max(row))
  matrix.append(row)

def dfs(h):
    count = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > h and visited[i][j] == 0:
                stack = [(i, j)]
                visited[i][j] = 1
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] > h and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            stack.append((nx, ny))
                count += 1
    return count

maxCount = 0
for h in range(peak):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    maxCount = max(maxCount, dfs(h))

print(maxCount)

# 메모리 31120 KB 
# 시간 656 ms
