import sys

input = sys.stdin.readline

N, M = map(int, input().split())

groups = []

for _ in range(M):
    a, b = map(int, input().split())
    groups.append((a, b))

groups.sort()


def can_place(D):
    count = 0
    last = -10**30

    for a, b in groups:
        # 현재 그룹에서 처음 앉힐 수 있는 위치
        pos = max(a, last + D)

        if pos > b:
            continue

        # pos부터 b까지 D 간격으로 앉힐 수 있는 학생 수
        add = (b - pos) // D + 1
        count += add

        # 마지막으로 앉힌 학생 위치 갱신
        last = pos + (add - 1) * D

        if count >= N:
            return True

    return False


left = 1
right = 10**18
answer = 0

while left <= right:
    mid = (left + right) // 2

    if can_place(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)