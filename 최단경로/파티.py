import sys
import heapq

input = sys.stdin.readline
INF = 10**18

def dijkstra(start, graph):
    dist = [INF] * (N + 1)
    dist[start] = 0

    heap = [(0, start)]

    while heap:
        cost, now = heapq.heappop(heap)

        if dist[now] < cost:
            continue

        for next_node, next_cost in graph[now]:
            new_cost = cost + next_cost

            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return dist


N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, t = map(int, input().split())

    graph[a].append((b, t))
    reverse_graph[b].append((a, t))

go_home = dijkstra(X, graph)
go_party = dijkstra(X, reverse_graph)

answer = 0

for i in range(1, N + 1):
    answer = max(answer, go_party[i] + go_home[i])

print(answer)