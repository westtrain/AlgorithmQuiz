import sys

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
sorted_numbers = sorted(numbers)

for number in sorted_numbers:
    sys.stdout.write(str(number) + '\n')

