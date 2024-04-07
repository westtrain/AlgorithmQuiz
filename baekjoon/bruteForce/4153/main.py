import sys

while True:
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    if sum(numbers) == 0:
        break

    numbers.sort()
    A, B, C = numbers

    if A**2 + B**2 == C**2:
        print('right')
    else:
        print('wrong')
