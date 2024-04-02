import sys
# Read N and K from input. N is the initial number of bottles, and K is the maximum number of non-empty bottles allowed to carry.
N, K = list(map(int, sys.stdin.readline().strip().split()))

def min_new_bottles(N, K):
    answer = 0
    # Loop until the number of '1's in the binary representation of N is less than or equal to K.
    while bin(N).count("1") > K:
        # Find the position of the lowest '1' bit in the binary representation of N.
        # The position indicates the amount of water (as a power of 2) that should be added in the form of new bottles.
        # 'bin(N)[::-1]' reverses the binary string of N, so 'index("1")' gives the position of the least significant '1'.
        add_bottle = 2 ** (bin(N)[::-1].index("1"))
        # Add the amount of water to N, simulating the addition of water bottles.
        N += add_bottle
        # Also, accumulate this amount in the answer, which represents the need for new bottles.
        answer += add_bottle
    # Return the total number of new bottles needed to ensure the number of non-empty bottles is less than or equal to K.
    return answer

# Print the result of the function, which calculates the minimum number of new bottles required.
print(min_new_bottles(N, K))
