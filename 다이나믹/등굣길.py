def solution(m, n, puddles):
    MOD = 1000000007

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 웅덩이 표시
    for x, y in puddles:
        dp[y][x] = -1

    # 시작 위치
    dp[1][1] = 1

    for y in range(1, n + 1):
        for x in range(1, m + 1):

            # 시작점은 이미 처리했으므로 건너뜀
            if x == 1 and y == 1:
                continue

            # 웅덩이는 갈 수 없는 곳
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue

            # 위쪽 + 왼쪽에서 오는 경우의 수
            dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD

    return dp[n][m]