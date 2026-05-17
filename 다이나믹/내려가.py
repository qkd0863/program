import sys

input = sys.stdin.readline

n = int(input())

max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

for _ in range(n):
    a, b, c = map(int, input().split())

    # 현재 줄까지의 최대 점수
    new_max = [
        max(max_dp[0], max_dp[1]) + a,
        max(max_dp[0], max_dp[1], max_dp[2]) + b,
        max(max_dp[1], max_dp[2]) + c
    ]

    # 현재 줄까지의 최소 점수
    new_min = [
        min(min_dp[0], min_dp[1]) + a,
        min(min_dp[0], min_dp[1], min_dp[2]) + b,
        min(min_dp[1], min_dp[2]) + c
    ]

    max_dp = new_max
    min_dp = new_min

print(max(max_dp), min(min_dp))