import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

left = 0
right = n - 1
answer = 0

while left < right:
    total = arr[left] + arr[right]

    if total == x:
        answer += 1
        left += 1
        right -= 1

    elif total < x:
        left += 1

    else:
        right -= 1

print(answer)