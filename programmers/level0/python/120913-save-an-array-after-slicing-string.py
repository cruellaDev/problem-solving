# https://school.programmers.co.kr/learn/courses/30/lessons/120913
'''
문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

1 ≤ my_str의 길이 ≤ 100
1 ≤ n ≤ my_str의 길이
my_str은 알파벳 소문자, 대문자, 숫자로 이루어져 있습니다.
'''
def solution(my_str, n):
    answer = []
    for i, e in enumerate(my_str):
        if i % n == 0:
            answer.append(e)
        else:
            answer[-1] += e
    return answer