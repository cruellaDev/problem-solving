# https://programmers.co.kr/learn/courses/30/lessons/12933

'''
함수 solution은 정수 n을 매개변수로 입력받습니다.
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
예를들어 n이 118372면 873211을 리턴하면 됩니다.
'''

def solution(n):
    answer = 0
    numbers = []
    while n > 0:
        numbers.append(n % 10)
        n = n // 10
    numbers.sort()
    for i, n in enumerate(numbers):
        answer += 10 ** i * n
    return answer