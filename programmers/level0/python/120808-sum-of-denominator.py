# https://school.programmers.co.kr/learn/courses/30/lessons/120808
'''
첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

0 <denum1, num1, denum2, num2 < 1,000
'''
from math import gcd
def solution1(denum1, num1, denum2, num2):
    _gcd = gcd(num1, num2)
    numerator = denum1 * num2 // _gcd + denum2 * num1 // _gcd
    denominator = num1 * num2 // _gcd
    abbreviation = gcd(numerator, denominator)
    return [numerator // abbreviation, denominator // abbreviation]

def solution2(denum1, num1, denum2, num2):
    numerator = denum1 * num2 + denum2 * num1
    denominator = num1 * num2
    abbreviation = gcd(numerator, denominator)
    return [numerator // abbreviation, denominator // abbreviation]