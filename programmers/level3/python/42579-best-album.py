# https://programmers.co.kr/learn/courses/30/lessons/42579

from functools import cmp_to_key
def cmp_sum(x, y):
    return y[1] - x[1]
def cmp_by_condition(x, y):
    x_index, x_play = x
    y_index, y_play = y
    if x_play == y_play:
        return x_index - y_index
    else:
        return y_play - x_play

def solution(genres, plays):
    answer = []
    _dict1 = dict()
    _dict2 = dict()
    for i, (genre, play) in enumerate(zip(genres, plays)) :
        if genre not in _dict1.keys():
            _dict1[genre] = [(i, play)]
            _dict2[genre] = play
        else:
            _dict1[genre].append((i, play))
            _dict2[genre] += play
    tmp = sorted(_dict2.items(), key=cmp_to_key(cmp_sum))
    for (genre, _) in tmp:
        new = [x[0] for x in sorted(_dict1[genre], key=cmp_to_key(cmp_by_condition))]
        answer += new[:2]
    return answer