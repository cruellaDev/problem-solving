# https://programmers.co.kr/learn/courses/30/lessons/12950
# 행렬의 덧셈

def solution1(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        tmp = []
        for i in range(len(a)):
            tmp.append(a[i] + b[i])
        answer.append(tmp)
    return answer

def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        answer2 = []
        for c, d in zip(a, b):
            answer2.append(c + d)
        answer.append(answer2)
    return answer