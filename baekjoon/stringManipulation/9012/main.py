import sys

T = int(sys.stdin.readline().strip())
answers = []
for _ in range(T):
    parenthesis = sys.stdin.readline().strip()
    parenthes_counter = 0

    for char in parenthesis:
        if char == '(':
            parenthes_counter += 1
        else:
            parenthes_counter -= 1
        if parenthes_counter < 0:
            answers.append('NO')
            break
    else:
        if parenthes_counter == 0:
            answers.append('YES')
        else:
            answers.append('NO')
for answer in answers:
  print(answer)
