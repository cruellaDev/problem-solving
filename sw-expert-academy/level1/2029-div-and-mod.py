# https://swexpertacademy.com/

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    div, mod = divmod(a, b)
    print(f'#{test_case} {div} {mod}')