import sys

A, B, N = map(int, sys.stdin.readline().strip().split())
remainder = A % B

for i in range(N):
    remainder *= 10
    digit = remainder // B
    remainder %= B

print(digit)

