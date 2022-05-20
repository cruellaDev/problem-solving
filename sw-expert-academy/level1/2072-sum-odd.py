# https://swexpertacademy.com/

T = int(input())
for take in range(1, T + 1):
    _sum = 0
    numbers = list(map(int, input().split()))
    for number in numbers:
        if number % 2:
            _sum += number
    print(f'#{take} {_sum}')
