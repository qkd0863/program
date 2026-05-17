n = int(input())

answer = -1

# 5kg 봉지를 최대한 많이 쓰는 경우부터 확인
for five in range(n // 5, -1, -1):
    remain = n - five * 5

    # 남은 무게가 3kg 봉지로 나누어떨어지면 정답
    if remain % 3 == 0:
        three = remain // 3
        answer = five + three
        break

print(answer)