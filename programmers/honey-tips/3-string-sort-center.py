'''
# https://programmers.co.kr/learn/courses/4008/lessons/13326

문자열 정렬하기

문자열 s와 자연수 n이 입력으로 주어집니다.
문자열 s를 좌측 / 가운데 / 우측 정렬한 길이 n인 문자열을 한 줄씩 프린트해보세요.

abc      
   abc   
      abc
'''

s, n = input().split()
n = int(n)
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))