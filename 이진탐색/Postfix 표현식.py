postfix = input().strip()

stack = []

for ch in postfix:
    # 알파벳이면 그대로 스택에 넣음
    if 'a' <= ch <= 'z':
        stack.append(ch)

    # 연산자이면 앞의 두 식을 꺼내서 괄호로 묶음
    else:
        right = stack.pop()
        left = stack.pop()

        expression = "(" + left + ch + right + ")"
        stack.append(expression)

print(stack[0])