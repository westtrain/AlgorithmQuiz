import sys

A, B = list(sys.stdin.readline().strip().split())
# 최소 차이를 최대로 설정
min_diff = len(B)

# A를 B와 같은 길이로 만들 수 있는 모든 경우를 고려
for start in range(len(B) - len(A) + 1):
    diff = 0
    # A와 B의 길이를 같게 만들어 준 후, 차이를 계산
    for i in range(len(A)):
        if A[i] != B[start+i]:
            diff += 1
    # 최소 차이 갱신
    min_diff = min(min_diff, diff)

# 최소 차이 출력
print(min_diff)

