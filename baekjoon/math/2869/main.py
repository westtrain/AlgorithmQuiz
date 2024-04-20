import sys
import math

A, B, V = map(int, sys.stdin.readline().split())
days = math.ceil((V - B) / (A - B))

print(days)

