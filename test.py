N = int(input())
List = list(map(int, input().split()))
List.sort()
M = int(input())

start = List[0]
end = List[-1]
answer = 0

while end >= start:
    total = 0
    mid = (start + end) // 2

    for L in List:
        if L <= mid:
            total += L
        else:
            total += mid
    if total <= M:
        start = mid + 1
        answer=mid
    else:
        end = mid - 1

print(answer)
