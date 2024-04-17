import sys

N = int(sys.stdin.readline().strip())
count = [0] * (100001)

for _ in range(N):
    number = int(sys.stdin.readline())
    count[number] += 1

for i in range(100001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)
