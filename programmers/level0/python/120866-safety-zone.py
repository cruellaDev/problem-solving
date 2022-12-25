# https://school.programmers.co.kr/learn/courses/30/lessons/120866
'''
지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.

지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

board는 n * n 배열입니다.
1 ≤ n ≤ 100
지뢰는 1로 표시되어 있습니다.
board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.
'''
def solution(board):
    width = len(board)
    height = len(board[0])
    answer = width * height
    for w in range(width):
        for h in range(height):
            if board[w][h] % 2:
                board[max(0, w-1)][max(0, h-1)] += 2
                board[max(0, w-1)][h] += 2
                board[max(0, w-1)][min(height-1, h+1)] += 2
                board[w][max(0, h-1)] += 2
                board[w][min(height-1, h+1)] += 2
                board[min(width-1, w+1)][max(0, h-1)] += 2
                board[min(width-1, w+1)][h] += 2
                board[min(width-1, w+1)][min(height-1, h+1)] += 2
    for w in range(width):
        for h in range(height):
            if board[w][h] > 0:
                answer -= 1
    return answer
