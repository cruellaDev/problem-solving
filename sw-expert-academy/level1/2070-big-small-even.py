# https://swexpertacademy.com/

T = int(input())
for test_case in range(1, T + 1):
    a, b = input().split()
    c = int(a) - int(b)
    result = '=' if c == 0 else '>' if c > 0 else '<'
    print(f'#{test_case} {result}')