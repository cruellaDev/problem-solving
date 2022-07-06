# https://swexpertacademy.com/

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}')
    star_num = int(input())
    arr = [[0] * star_num for i in range(star_num)]
    for i in range(star_num):
        for j in range(star_num):
            if j == 0 or j == star_num - 1:
                arr[i][j] = str(1)
            else:
                arr[i][j] = str(int(arr[i-1][j-1]) + int(arr[i-1][j]))
        print(' '.join(arr[i][:i + 1]))
