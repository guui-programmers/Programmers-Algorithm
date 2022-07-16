def solution(answers):
    answer = dict()
    
    answer[1] = answerCheck([1, 2, 3, 4, 5], answers)
    answer[2] = answerCheck([2, 1, 2, 3, 2, 4, 2, 5], answers)
    answer[3] = answerCheck([3, 3, 1, 1, 2, 2, 4, 4, 5, 5], answers)
    
    max_val = max(answer.values())
    for idx, val in answer.items():
        if max_val != val:
            del answer[idx]
    return [key for key in answer]

def answerCheck(supo, answers):
    count = 0
    idx = 0
    for a in answers:
        if idx == len(supo):
            idx = 0
        if a == supo[idx]:
            count += 1
        idx += 1
    return count
