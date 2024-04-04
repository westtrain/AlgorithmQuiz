
n, m = map(int, input().split())  # 사용자로부터 두 개의 숫자를 입력받아 n과 m에 저장합니다.

# 숫자 N에서 2의 배수의 개수를 세는 함수를 만듭니다.


def count2(N):
    # 만약 N이 2보다 작다면, 2의 배수는 없으므로 0을 반환합니다.
    if N < 2:
        return 0
    # N에서 2의 배수의 개수를 세는 부분입니다. N을 2로 나눈 몫을 count에 더하고, N을 2로 나눈 몫을 다시 N에 저장합니다. 이 과정을 N이 2보다 작아질 때까지 반복합니다.
    count = 0
    while N >= 2:
        count += N//2
        N = N//2
    return count

# 숫자 N에서 5의 배수의 개수를 세는 함수를 만듭니다.


def count5(N):
    # 만약 N이 5보다 작다면, 5의 배수는 없으므로 0을 반환합니다
    if N < 5:
        return 0
    # N에서 5의 배수의 개수를 세는 부분입니다. N을 5로 나눈 몫을 count에 더하고, N을 5로 나눈 몫을 다시 N에 저장합니다. 이 과정을 N이 5보다 작아질 때까지 반복합니다.
    count = 0
    while N >= 5:
        count += N//5
        N //= 5
    return count


# n과 m의 조합에서 2의 배수와 5의 배수의 개수를 세는 부분입니다. n에서 m을 뺀 값과 m의 배수의 개수를 n의 배수의 개수에서 빼서 최종 배수의 개수를 구합니다.
two_count = count2(n) - count2(n-m) - count2(m)
five_count = count5(n) - count5(n-m) - count5(m)
# 2의 배수와 5의 배수 중에서 더 적은 개수를 출력합니다. 이 값이 n과 m의 조합에서 0의 개수와 같습니다.
print(min(two_count, five_count))
