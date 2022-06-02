# https://swexpertacademy.com/

p, k = map(int, input().split())
if p < k:
    print(p - k + 1000)
else:
    print(p - k + 1)