import sys

input = sys.stdin.readline

n = int(input())
requests = list(map(int, input().split()))
m = int(input())

start = 0
end = max(requests)

answer = 0

while start <= end:
    mid = (start + end) // 2

    total = 0
    for money in requests:
        total += min(money, mid)

    # 총 예산 안에서 배정 가능하면 상한액을 더 올려본다
    if total <= m:
        answer = mid
        start = mid + 1

    # 총 예산을 초과하면 상한액을 낮춰야 한다
    else:
        end = mid - 1

print(answer)