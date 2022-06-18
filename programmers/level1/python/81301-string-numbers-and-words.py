# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution1(s):
    numbers = {
        "zero": "0", "one": "1", "two": "2",
        "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    try:
        return int(s)
    except:
        for number in numbers.keys():
            if number in s:
                s = s.replace(number, numbers[number])
        return int(s)

def solution2(s):
    numbers = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    ]
    try:
        return int(s)
    except:
        for i, number in enumerate(numbers):
            if number in s:
                s = s.replace(number, f'{i}')
        return int(s)