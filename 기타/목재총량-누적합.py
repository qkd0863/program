import sys

input = sys.stdin.readline

M, N = map(int, input().split())

arr = [[0] * (N + 1)]

for _ in range(M):
    row = [0] + list(map(int, input().split()))
    arr.append(row)

prefix = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(1, M + 1):
    for j in range(1, N + 1):
        prefix[i][j] = (
            arr[i][j]
            + prefix[i - 1][j]
            + prefix[i][j - 1]
            - prefix[i - 1][j - 1]
        )

C = int(input())

answer = []

for _ in range(C):
    r1, c1, r2, c2 = map(int, input().split())

    total = (
        prefix[r2][c2]
        - prefix[r1 - 1][c2]
        - prefix[r2][c1 - 1]
        + prefix[r1 - 1][c1 - 1]
    )

    answer.append(str(total))

print("\n".join(answer))