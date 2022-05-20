'''
# https://programmers.co.kr/learn/courses/4008/lessons/13340

알파벳 출력하기

입력으로 0이 주어지면 영문 소문자 알파벳을,
입력으로 1이 주어지면 영문 대문자 알파벳을 사전 순으로 출력하는 코드를 짜세요.
'''

num = int(input().strip())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet) if num else print(alphabet.lower())


'''

# https://programmers.co.kr/learn/courses/4008/lessons/12729

파이썬은 이런 데이터를 상수(constants)로 정의해놓았습니다.

import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789

'''

import string 
num = int(input().strip())
print(string.ascii_uppercase) if num else print(string.ascii_lowercase)