def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):

            # 맨 왼쪽은 바로 위에서만 내려올 수 있음
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]

            # 맨 오른쪽은 왼쪽 위에서만 내려올 수 있음
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]

            # 가운데는 위쪽 2개 중 큰 값 선택
            else:
                triangle[i][j] += max(
                    triangle[i - 1][j - 1],
                    triangle[i - 1][j]
                )

    return max(triangle[-1])