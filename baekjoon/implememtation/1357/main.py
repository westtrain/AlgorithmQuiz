import sys

def rev_num(num):
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num = num // 10
    return rev_num

X, Y = list(map(int, sys.stdin.readline().split()))

print(rev_num(rev_num(X) + rev_num(Y)))
