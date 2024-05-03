import sys

n = int(sys.stdin.readline().strip())
string_number = '666'
number = 666
count = 0
while True:
    if string_number in str(number):
        count += 1
    if count == n:
        break
    number += 1
print(number)
