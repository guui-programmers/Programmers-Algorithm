def solution(participant, completion):
    participant.sort()
    completion.sort()
    for idx, par in enumerate(participant):
        if idx < len(completion):
            if completion[idx] != par:
                return par
        elif idx == len(completion):
            return par

