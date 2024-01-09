import sys
sys.setrecursionlimit(10000) # 재귀 깊이 제한 설정

T = int(sys.stdin.readline().strip())
M = 0
N = 0

def dfs(y, x, matrix):
  if y < 0 or y >= M or x < 0 or x >= N or matrix[y][x] == 0:
    return
  matrix[y][x] = 0

  dfs(y, x+1, matrix)
  dfs(y, x-1, matrix)
  dfs(y+1, x, matrix)
  dfs(y-1, x, matrix)

for _ in range(T):
    count = 0
    M, N, K = map(int, sys.stdin.readline().strip().split())
    matrix = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().strip().split())
        matrix[x][y] = 1
    for i in range(M):
      for j in range(N):
        if matrix[i][j] == 1:
          dfs(i, j, matrix)
          count += 1
    print(count)
