# https://swexpertacademy.com/

T = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for t in T:
    print(alphabet.find(t) + 1, end = ' ')