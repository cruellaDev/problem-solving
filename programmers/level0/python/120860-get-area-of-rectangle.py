# https://school.programmers.co.kr/learn/courses/30/lessons/120860
'''
2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.

dots의 길이 = 4
dots의 원소의 길이 = 2
-256 < dots[i]의 원소 < 256
잘못된 입력은 주어지지 않습니다.
'''
def solution(dots):
    x1, y1 = dots.pop(0)
    width = 0
    height = 0
    for x, y in dots:
        new_w = max(x, x1) - min(x, x1)
        width = max(width, new_w)
        new_h = max(y, y1) - min(y, y1)
        height = max(height, new_h)
    return width * height

'''

2
3
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
'''