n = int(input())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))

    time = data[0]
    count = data[1]
    prev_tasks = data[2:]

    if count == 0:
        dp[i] = time
    else:

        latest_prev_time = 0

        for prev in prev_tasks:
            latest_prev_time = max(latest_prev_time, dp[prev])

        dp[i] = latest_prev_time + time

print(max(dp))