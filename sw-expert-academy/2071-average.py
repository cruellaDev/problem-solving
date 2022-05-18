T = int(input())

for take in range(1, T + 1):
    numbers = list(map(int, input().split()))
    total = sum(numbers)
    divide = len(numbers)
    print(f'#{take} {round(total / divide)}')