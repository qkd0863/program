n = int(input())

cost = [list(map(int, input().split())) for _ in range(n)]

# dp[i][0] = i번째 집을 빨강으로 칠했을 때 최소 비용
# dp[i][1] = i번째 집을 초록으로 칠했을 때 최소 비용
# dp[i][2] = i번째 집을 파랑으로 칠했을 때 최소 비용
dp = [[0] * 3 for _ in range(n)]

dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(1, n):
    # 현재 집을 빨강으로 칠하면 이전 집은 초록 또는 파랑
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]

    # 현재 집을 초록으로 칠하면 이전 집은 빨강 또는 파랑
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]

    # 현재 집을 파랑으로 칠하면 이전 집은 빨강 또는 초록
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

print(min(dp[n - 1]))