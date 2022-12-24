# https://school.programmers.co.kr/learn/courses/30/lessons/120912
'''
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.

1 ≤ array의 길이 ≤ 100
0 ≤ array의 원소 ≤ 100,000
'''
def solution(array):
    return ''.join(map(str, array)).count('7')