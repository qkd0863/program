import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = int(1e18)
dist = [INF] * (N + 1)
dist[1] = 0

heap = []
heapq.heappush(heap, (0, 1))

while heap:
    cost, now = heapq.heappop(heap)

    if dist[now] < cost:
        continue

    for next_node, next_cost in graph[now]:
        new_cost = cost + next_cost

        if new_cost < dist[next_node]:
            dist[next_node] = new_cost
            heapq.heappush(heap, (new_cost, next_node))

print(dist[N])
