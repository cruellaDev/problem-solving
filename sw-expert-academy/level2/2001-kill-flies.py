# https://swexpertacademy.com/

T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    N, M = map(int, input().split())
    flies = []
    for n in range(N):
        flies.append(list(map(int, input().split())))
    max_kill = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = 0
            for a in range(M):
                for b in range(M):
                    temp += flies[i +a][j+b]
            if temp > max_kill:
                max_kill = temp
    print(f'#{test_case} {max_kill}')