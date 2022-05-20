# https://swexpertacademy.com/

T = int(input())
answer = 0
while T > 0:
    div, mod = divmod(T, 10)
    answer += mod
    T = div
print(answer)