n = int(input())
arr = list(map(int, input().split()))

# dp[i] = arr[i]를 마지막 원소로 하는 증가 부분 수열의 최대 합
dp = arr[:]

for i in range(n):
    for j in range(i):
        # arr[j]가 arr[i]보다 작아야 증가하는 수열이 됨
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))