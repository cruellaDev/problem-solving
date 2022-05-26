# https://swexpertacademy.com/

day = [-99, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for test_case in range(1, T + 1):
    YYYYMMDD = input()
    YYYY = YYYYMMDD[:4]
    MM = YYYYMMDD[4:6]
    DD = YYYYMMDD[6:]
    mm = int(MM)
    dd = int(DD)
    if (mm == 0 or mm > 12) or (dd == 0 or dd > day[mm]):
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {YYYY}/{MM}/{DD}')