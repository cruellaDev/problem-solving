# https://swexpertacademy.com/
'''
3, 6, 9가 있는 숫자는 3, 6, 9 개수만큼 박수를 침
박수는 '-'로 표기
'''

T = int(input())
for t in range(1, T + 1):
    str_t = str(t)
    cnt = 0
    answer = ""
    cnt += str_t.count("3")
    cnt += str_t.count("6")
    cnt += str_t.count("9")
    if cnt > 0:
        answer = cnt * "-"
    else:
        answer = str_t
    print(answer, end=' ')