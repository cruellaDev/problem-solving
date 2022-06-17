# https://swexpertacademy.com/

for i in range(5):
    result = ''
    for j in range(5):
        if i == j: result += '#'
        else: result += '+'
    print(result)