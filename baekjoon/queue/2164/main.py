import sys
from collections import deque

N = int(sys.stdin.readline().strip())
queue = deque(range(1, N + 1))
while len(queue) > 1:
    queue.popleft() 
    queue.append(queue.popleft()) 
print(queue[0])

