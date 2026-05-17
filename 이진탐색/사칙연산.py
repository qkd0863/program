t = int(input())

for _ in range(t):

    # 수식을 공백 기준으로 분리
    # 예: "3 * 2 = 6"
    a, op, b, equal, c = input().split()

    # 숫자로 변환
    a = int(a)
    b = int(b)
    c = int(c)

    result = 0

    # 연산자에 따라 계산
    if op == '+':
        result = a + b

    elif op == '-':
        result = a - b

    elif op == '*':
        result = a * b

    elif op == '/':
        result = a // b

    # 계산 결과 비교
    if result == c:
        print("correct")
    else:
        print("wrong answer")



#Description
#사칙연산은 덧셈, 뺄셈, 곱셈, 나눗셈으로 이루어져 있으며, 컴퓨터 프로그램에서 이를 표현하는 기호는 +, -, *, / 와 같다. 아래는 컴퓨터 프로그램에서 표현한 사칙 연산의 예제이다.
#3 * 2 = 6
#문제와 답이 주어졌을 때, 이를 계산하여 올바른 수식인지 계산하는산 프로그램을 만들려고 한다. 만약 주어진 데이터가 3 * 2 = 6 이라면 정답으로, 3 * 2 = 7 이면 오답으로 채점을 하면 된다. 문제와 답이 주어졌을 때, 이를 채점하는 프로그램을 작성하시오.