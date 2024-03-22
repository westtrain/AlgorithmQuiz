import sys
import math

num1, num2 = map(int, sys.stdin.readline().strip().split())
r = 0
a = num1
b = num2

while b != 0:
   r = a % b
   a = b
   b = r
gcd = a
lcm = (num1 * num2) / gcd
print(gcd)
print(math.floor(lcm))
