# https://swexpertacademy.com/

T = int(input())
for test_case in range(1, T + 1):
    string = input()
    word = ''
    for s in string:
        word += s
        string = string[1:]
        if string.index(word) == 0:
            break
    print(f'#{test_case} {len(word)}')