def solution(n, s, a, b, fares):
    INF = 10**15

    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0

    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    answer = INF

    for k in range(1, n + 1):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])

    return answer