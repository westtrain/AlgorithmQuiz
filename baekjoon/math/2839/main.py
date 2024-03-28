import sys

N = int(sys.stdin.readline().strip())

count = 0

while N > 0:
    if N % 5 == 0:
        count += N // 5  
        print(count)
        sys.exit()
    N -= 3  
    count += 1 

if N < 0:
    print(-1) 
    sys.exit()

print(count)

