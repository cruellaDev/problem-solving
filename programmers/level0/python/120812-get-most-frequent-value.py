# https://school.programmers.co.kr/learn/courses/30/lessons/120812
'''
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

0 < array의 길이 < 100
0 ≤ array의 원소 < 1000
'''
def solution(array):
    dic = {}
    for a in array:
        if a not in dic:
            dic[a] = 1
        else:
            dic[a] += 1
    max_cnt = max(dic.values())
    answer = []
    for nmbr, cnt in dic.items():
        if cnt == max_cnt:
            answer.append(nmbr)
    return -1 if len(answer) > 1 else answer[0]