import sys

input = sys.stdin.readline

n, c = map(int, input().split())

houses = [int(input()) for _ in range(n)]
houses.sort()

start = 1
end = houses[-1] - houses[0]

answer = 0

while start <= end:
    mid = (start + end) // 2

    # 첫 번째 집에 공유기 설치
    count = 1
    last = houses[0]

    # mid 거리 이상 떨어진 집에 공유기 설치
    for i in range(1, n):
        if houses[i] - last >= mid:
            count += 1
            last = houses[i]

    # 공유기를 C개 이상 설치할 수 있다면
    if count >= c:
        answer = mid
        start = mid + 1

    # C개를 설치할 수 없다면 거리 줄이기
    else:
        end = mid - 1

print(answer)