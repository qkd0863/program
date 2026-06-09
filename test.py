import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = int(1e18)
dist = [INF] * (N + 1)
dist[1] = 0

heap = []
heapq.heappush(heap, (0, 1))