import sys

input = sys.stdin.readline

n, m = map(int, input().split())

edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))


edges.sort()

parent = [i for i in range(n + 1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return True


total = 0
max_cost = 0

for cost, a, b in edges:
    if union(a, b):
        total += cost
        max_cost = cost

print(total - max_cost)