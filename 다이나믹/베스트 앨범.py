from collections import defaultdict

def solution(genres, plays):
    answer = []

    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        # 장르별 총 재생 수
        genre_total[genre] += play

        # 장르별 노래 정보: 재생 수, 고유 번호
        genre_songs[genre].append((play, i))

    # 총 재생 수가 많은 장르 순서로 정렬
    sorted_genres = sorted(
        genre_total.keys(),
        key=lambda x: genre_total[x],
        reverse=True
    )

    for genre in sorted_genres:
        # 장르 안에서는 재생 수 내림차순, 고유 번호 오름차순
        songs = sorted(
            genre_songs[genre],
            key=lambda x: (-x[0], x[1])
        )

        # 장르별 최대 2곡 선택
        for play, idx in songs[:2]:
            answer.append(idx)

    return answer