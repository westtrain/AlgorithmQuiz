'''
다음의 3개의 함수를 만든다
  1. 바이러스를 퍼트리는 함수
      재귀로 함수를 돌면서 visited[x][y] 값이 0이면서 2를 만나는 모든 값을 2로 바꾼다
  2. 안전 지대를 계산하는 함수
      행렬안의 0의 개수를 세서 반환한다.
  3. 벽을 세우는 함수
      벽을 세우려면 먼저 matrix에서 0인 좌표를 모두 모은다.
      그리고 배열의 길이와 세울 벽의 수(여기선 3개)로 만들 수 있는 조합을 만든다 (길이가 7이면 7C3)
      배열의 각 인덱스에 좌표가 있으니까 인덱스를 가지고 3개 묶음의 조합을 모두 만든다.
      그러면 총 35개의 조합이 나오고 그 조합을 가지고 배열을 순회하면서 visited 에 1을 채워서 벽을 세운다

코드 프로세스
1. 입력 값에 맞게 matrix를 만든다
2. 3번 함수를 호출해서 3개의 벽을 세운다
3. 함수 내부에서 3개의 벽이 세워질 때마다 1번 함수를 호출한다
4. 1번 함수가 호출되어 벽 외부에 2로 가득차게 만든다
5. 2번 함수를 호출해서 0의 개수를 합산해서 반환한다
6. 개수를 max_safe_area에 담긴 값과 비교해서 크면 저장한다

이 과정이 모두 끝나면 max_safe_area를 출력한다.
'''

import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
matrix=  []
max_safe_area = 0

for _ in range(N):
  row = list(map(int, sys.stdin.readline().strip().split()))
  matrix.append(row)

# 바이러스 퍼트리는 함수
def spreadViruses(x, y, visited):
  if x < 0 or x >= N or y < 0 or y >= M or visited[x][y] == 1 or visited[x][y] == 2:
    return
  visited[x][y] = 2
  spreadViruses(matrix, x+1, y, visited)
  spreadViruses(matrix, x-1, y, visited)
  spreadViruses(matrix, x, y+1, visited)
  spreadViruses(matrix, x, y-1, visited)

# 안전 지대 계산 함수
def calculateSafeArea(visited):
  safe_area = 0
  for x in range(N):
    for y in range(M):
      if visited[x, y] == 0:
        safe_area += 1
  return safe_area

# 벽 세우기 함수
def setWall(matrix):
  visited = [[matrix[y][x] for x in range(M)] for y in range(N)]
  wallCount = 1
  x = 0
  y = 0
  if wallCount == 3:
    spreadViruses(0, 0, visited) 
    return calculateSafeArea(visited)
  for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    if visited[x + dx][y + dy] == 0:
      visited[x][y] = 1
      wallCount += 1
# 아직 미완성..


