import sys

n = int(sys.stdin.readline().strip())
stack = []
result = []
current_number = 1
possible = True

for _ in range(n):
    input_number = int(sys.stdin.readline().strip())
    
    while current_number <= input_number:
        stack.append(current_number)
        result.append('+')
        current_number += 1

    if stack[-1] == input_number:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    print('\n'.join(result))
else:
    print('NO')

