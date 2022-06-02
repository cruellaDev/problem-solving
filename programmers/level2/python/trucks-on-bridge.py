'''
https://programmers.co.kr/learn/courses/30/lessons/42583

다리를 지나는 트럭
'''

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for i in range(bridge_length)]
    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            sum_weights = sum(bridge)
            if sum_weights + truck_weights[0] > weight:
                bridge.append(0)
            else:
                bridge.append(truck_weights.pop(0))
    return answer