import sys

N = int(sys.stdin.readline().strip())
scores = list(map(int, sys.stdin.readline().split()))

max_score = max(scores)
sum = 0
for i in range(N):
  sum = sum + scores[i] / max_score * 100
print(sum/N)
