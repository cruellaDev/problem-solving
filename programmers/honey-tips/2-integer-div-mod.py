'''
# https://programmers.co.kr/learn/courses/4008/lessons/13323
# https://programmers.co.kr/learn/courses/4008/lessons/12732

divmod는 작은 숫자를 다룰 때는 a // b, a % b 보다 느림
'''
a, b = map(int, input().strip().split(' '))
print(a // b, a % b)
div, mod = divmod(a, b)
print(div, mod)
