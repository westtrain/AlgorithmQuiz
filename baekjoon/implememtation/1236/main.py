import sys

N, M = list(map(int, sys.stdin.readline().split()))
castle = [sys.stdin.readline().strip() for _ in range(N)]
row_count = 0
col_count = 0
for floor in castle:
  if floor.find('X') == -1:
    row_count += 1
for j in range(M):
  i = 0
  while i < N:
    if castle[i][j] == 'X':
      break
    i += 1
  if i == N:
    col_count += 1

if row_count > col_count:
  print(row_count)
else:
  print(col_count)
