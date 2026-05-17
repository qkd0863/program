def solution(money):
    def rob(arr):
        dp = [0] * len(arr)

        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, len(arr)):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

        return dp[-1]

    # 첫 번째 집을 터는 경우 → 마지막 집은 못 턺
    case1 = rob(money[:-1])

    # 첫 번째 집을 안 터는 경우 → 마지막 집 가능
    case2 = rob(money[1:])

    return max(case1, case2)