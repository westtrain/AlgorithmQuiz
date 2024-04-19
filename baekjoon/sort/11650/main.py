import sys

N = int(sys.stdin.readline().strip())
positions = [] 

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    positions.append([x, y]) 

positions.sort()

for position in positions:
  print(position[0], position[1])
