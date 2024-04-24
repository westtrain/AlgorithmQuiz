import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
matrix = []
visited = []
for i in range(N):
  row = list(map(int, sys.stdin.readline().strip()))
  matrix.append(row)
  visitedRow = [0 for j in range(M)]
  visited.append(visitedRow)
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
queue = deque([[0, 0]])
visited[0][0] = 1
while queue:
  y, x = queue.popleft()
  if y == N-1 and x == M-1:
    break
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and matrix[ny][nx] == 1:
        visited[ny][nx] = visited[y][x] + 1
        queue.append([ny, nx])
print(visited[N-1][M-1])

'''
행의 개수 = 행렬의 행 개수
열의 개수 = 행렬의 열 개수
방문 = 행의 개수 x 열의 개수 크기의 2차원 불리언 배열

큐 생성
큐에 시작점 추가
방문[시작점] = 1

방향 = [(1,0), (0,1), (-1,0), (0,-1)]  # 상, 하, 좌, 우 이동

거리 = 0

반복(큐가 비어있지 않는 동안):
    현재 큐의 크기 = 큐의 길이
    반복(현재 큐의 크기만큼):
        현재 노드 = 큐에서 꺼내기

        만약 현재 노드가 목표점이라면:
            반환 거리

        반복(각 방향에 대해):
            새 행 위치 = 현재 노드의 행 + 방향의 행 변화
            새 열 위치 = 현재 노드의 열 + 방향의 열 변화

            만약 새 위치가 행렬 내에 있고, 아직 방문하지 않았다면:
                큐에 새 위치 추가
                방문[새 위치] = True

    거리 += 1

반환 -1  # 목표점에 도달할 수 없는 경우
'''
