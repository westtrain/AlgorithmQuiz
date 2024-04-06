import sys

def backtrack(cards, M, start, depth, current_sum, max_sum):
  if current_sum > M or depth == 3:
      if current_sum <= M:
          max_sum[0] = max(max_sum[0], current_sum)
      return

  for i in range(start, len(cards)):
      backtrack(cards, M, i+1, depth+1, current_sum+cards[i], max_sum)

N, M = list(map(int, sys.stdin.readline().strip().split()))
cards = list(map(int, sys.stdin.readline().strip().split()))

max_sum = [0]
backtrack(cards, M, 0, 0, 0, max_sum)

print(max_sum[0])
