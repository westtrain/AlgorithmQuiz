import sys

N = int(sys.stdin.readline().strip())
str_list = []
for _ in range(N):
    str_list.append(sys.stdin.readline().strip())
str_length = len(str_list[0])
for i in range(str_length):
    each_char = str_list[0][i]
    for str in str_list:
        if str[i] != each_char:
            each_char = '?'
            break
    print(each_char, end='')
print()
