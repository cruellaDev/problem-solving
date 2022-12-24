# https://school.programmers.co.kr/learn/courses/30/lessons/120863
'''
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.

0 < polynomial에 있는 수 < 100

polynomial에 변수는 'x'만 존재합니다.

polynomial은 0부터 9까지의 정수, 공백, ‘x’, ‘+'로 이루어져 있습니다.

항과 연산기호 사이에는 항상 공백이 존재합니다.

공백은 연속되지 않으며 시작이나 끝에는 공백이 없습니다.

하나의 항에서 변수가 숫자 앞에 오는 경우는 없습니다.

" + 3xx + + x7 + "와 같은 잘못된 입력은 주어지지 않습니다.
'''
def solution(polynomial):
    var, const = 0, 0
    for p in polynomial.split(' '):
        if 'x' in p:
            if len(p) > 1:
                var += int(p[:-1])
            else:
                var += 1
        elif p.isdigit():
            const += int(p)
    answer = []
    if var > 0:
        answer.append(str(var) + 'x' if var > 1 else 'x')
    if const > 0:
        answer.append(str(const))
    return ' + '.join(answer) if answer else '0'