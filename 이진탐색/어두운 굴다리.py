n = int(input())
m = int(input())
lights = list(map(int, input().split()))

answer = 0

# 시작 지점 0부터 첫 번째 가로등까지 밝혀야 함
answer = max(answer, lights[0] - 0)

# 가로등 사이의 어두운 구간을 확인
for i in range(1, m):
    gap = lights[i] - lights[i - 1]

    # 두 가로등이 양쪽에서 비추므로 필요한 높이는 gap의 절반
    # gap이 홀수면 올림 처리
    height = (gap + 1) // 2

    answer = max(answer, height)

# 마지막 가로등부터 끝 지점 n까지 밝혀야 함
answer = max(answer, n - lights[-1])

print(answer)