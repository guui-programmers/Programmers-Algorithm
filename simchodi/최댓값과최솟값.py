def solution(s):
    s_list = s.split(" ")
    num_list = [int(i) for i in s_list]
    return str(min(num_list))+" "+str(max(num_list))
