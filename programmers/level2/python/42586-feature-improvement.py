'''
# https://programmers.co.kr/learn/courses/30/lessons/42586

'''

def solution(progresses, speeds):
    wait_for_complete = []
    for progress, speed in zip(progresses, speeds):
        div, mod = divmod((100 - progress), speed)
        if mod > 0 :
            wait_for_complete.append(div + 1)
        else:
            wait_for_complete.append(div)
    marking = [0, wait_for_complete.pop(0)]
    answer = [1]
    while wait_for_complete:
        second = wait_for_complete.pop(0)
        if second <= marking[1]:
            answer[marking[0]] += 1
        else:
            marking[0] += 1
            answer.append(1)
            marking[1] = second
    return answer