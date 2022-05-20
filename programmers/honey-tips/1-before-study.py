'''
# https://programmers.co.kr/learn/courses/4008/lessons/13254
정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다.
mylist에 들은 각 원소의 길이를 담은 리스트를 리턴하도록 solution 함수를 작성해주세요.
'''
'''
return a list which has length of elements in mylist
'''

def solution1(mylist):
    return [len(x) for x in mylist]

def solution2(mylist):
    return list(map(len, mylist))

'''
# https://programmers.co.kr/learn/courses/4008/lessons/13171
iterable : 자신의 멤버를 한 번에 하나씩 리턴. list, str, tuple, dict, ...
    sequence : int 타입 인덱스를 통해, 원소에 접근할 수 있는 iterable. list, str, tuple
'''