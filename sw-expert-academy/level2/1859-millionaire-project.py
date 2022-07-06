# https://swexpertacademy.com/

T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    count = 0
    prev = 10001
    t = int(input())
    numbers = list(map(int, input().split()))
    for i, e in enumerate(numbers):
        if i == 0:
            count += 1
            answer -= e
            prev = e
        elif 0 < i < len(numbers) - 1:
            if e > prev and e > numbers[i+1]:
                answer += count * e
                count = 0
                prev = e
            elif e > prev and e <= numbers[i+1]:
                answer -= e
                count += 1
                prev = e
            elif e <= prev:
                answer -= e
                count += 1
                prev = e
        elif i == len(numbers) - 1:
            answer += count * e
    print(f'#{test_case} {max(answer, 0)}')