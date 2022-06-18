# https://programmers.co.kr/learn/courses/30/lessons/68935

'''
자연수 n이 매개변수로 주어집니다.
n을 3진법 상에서 앞뒤로 뒤집은 후,
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
'''

def solution1(n):
    answer = 0
    threes = []
    while n > 0:
        threes.append(n % 3)
        n = n // 3
    for i, e in enumerate(threes):
        if answer == 0 and e == 0: continue
        answer += 3 ** (len(threes) - i - 1) * e
    return answer

def solution2(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer