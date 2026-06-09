import sys
import heapq

input = sys.stdin.readline

n = int(input())

lectures = []

for _ in range(n):
    p, d = map(int, input().split())
    lectures.append((d, p))

lectures.sort()

heap = []

for d, p in lectures:
    heapq.heappush(heap, p)

    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))