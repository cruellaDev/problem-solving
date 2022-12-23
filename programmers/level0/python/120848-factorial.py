# https://school.programmers.co.kr/learn/courses/30/lessons/120848
'''
i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.

i! ≤ n

0 < n ≤ 3,628,800
'''
def solution1(n):
    f = 1
    factorial = []
    for i in range(1, 11):
        f = f * i
        factorial.append(f)
    for i, e in enumerate(factorial):
        if e > n:
            return i
        elif e == n:
            return i + 1
    return n

def solution2(n):
    start = 1
    for i in range(1, 11):
        start = start * i
        if start > n:
            return i - 1
    return n