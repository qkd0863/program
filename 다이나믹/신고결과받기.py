def solution(id_list, report, k):
    # 중복 신고 제거
    report = set(report)

    # 각 유저가 신고당한 횟수
    reported_count = {}

    # 각 유저가 신고한 사람 목록
    user_reported = {}

    for user in id_list:
        reported_count[user] = 0
        user_reported[user] = []

    for r in report:
        reporter, reported = r.split()

        reported_count[reported] += 1
        user_reported[reporter].append(reported)

    answer = []

    for user in id_list:
        mail_count = 0

        # user가 신고한 사람 중 정지된 사람이 몇 명인지 확인
        for reported in user_reported[user]:
            if reported_count[reported] >= k:
                mail_count += 1

        answer.append(mail_count)

    return answer질