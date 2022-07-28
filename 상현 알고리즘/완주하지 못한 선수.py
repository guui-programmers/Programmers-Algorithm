from  collections import Counter
def solution(participant, completion):

    result = list(Counter(participant) - Counter(completion))
    return ''.join(result)