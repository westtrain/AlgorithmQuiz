import sys

left_stack = list(sys.stdin.readline().strip())
right_stack = []
M = int(sys.stdin.readline().strip())

for _ in range(M):
    command = sys.stdin.readline().split()
    
    if command[0] == 'L' and left_stack:
        right_stack.append(left_stack.pop())
    elif command[0] == 'D' and right_stack:
        left_stack.append(right_stack.pop())
    elif command[0] == 'B' and left_stack:
        left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[1])

result = ''.join(left_stack + right_stack[::-1])
print(result)

