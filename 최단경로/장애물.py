import heapq
import sys

input = sys.stdin.readline
INF = int(1e18)

V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def dijkstra(double_edge=None):
    dist = [INF] * (V + 1)
    prev = [0] * (V + 1)

    dist[1] = 0
    heap = [(0, 1)]

    while heap:
        cost, now = heapq.heappop(heap)

        if cost > dist[now]:
            continue

        for nxt, weight in graph[now]:
            new_weight = weight

            if double_edge is not None:
                a, b = double_edge
                if (now == a and nxt == b) or (now == b and nxt == a):
                    new_weight *= 2

            new_cost = cost + new_weight

            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                prev[nxt] = now
                heapq.heappush(heap, (new_cost, nxt))

    return dist[V], prev


A, prev = dijkstra()

path_edges = []

cur = V
while cur != 1:
    before = prev[cur]
    path_edges.append((before, cur))
    cur = before

answer = 0

for edge in path_edges:
    B, _ = dijkstra(edge)
    answer = max(answer, B - A)

print(answer)