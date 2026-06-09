import sys
import heapq

input = sys.stdin.readline

C, N = map(int, input().split())

chickens = [int(input()) for _ in range(C)]
cows = [tuple(map(int, input().split())) for _ in range(N)]

chickens.sort()
cows.sort()

heap = []
idx = 0
answer = 0

for t in chickens:
    while idx < N and cows[idx][0] <= t:
        a, b = cows[idx]
        heapq.heappush(heap, b)
        idx += 1


    while heap and heap[0] < t:
        heapq.heappop(heap)


    if heap:
        heapq.heappop(heap)
        answer += 1

print(answer)