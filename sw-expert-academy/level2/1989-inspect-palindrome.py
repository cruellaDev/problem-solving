# https://swexpertacademy.com/

T = int(input())
for test_case in range(1, T + 1):
    word = input()
    answer = 1 if word == ''.join(reversed(word)) else 0
    print(f'#{test_case} {answer}')