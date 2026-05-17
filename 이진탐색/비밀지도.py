def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # 두 지도 중 하나라도 벽이면 벽이므로 OR 연산 사용
        merged = arr1[i] | arr2[i]

        # 이진수 문자열로 변환
        binary = bin(merged)[2:]

        # 길이가 n보다 짧으면 앞에 0 채우기
        binary = binary.zfill(n)

        # 1은 벽 '#', 0은 공백 ' '으로 변환
        row = binary.replace('1', '#').replace('0', ' ')

        answer.append(row)

    return answer