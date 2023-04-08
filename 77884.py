def solution(left, right):
    add_list = []
    for data in range(left, right+1):
        divisor_list = []
        for a in range(1, data+1):
            if data%a==0:
                divisor_list.append(a)
        if len(divisor_list)%2==0:
            add_list.append(data)
        elif len(divisor_list)%2!=0:
            add_list.append(-data)
    result = 0
    for b in add_list:
        result += b
    return result
print(solution(13, 17))
