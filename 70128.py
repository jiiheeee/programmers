def solution(a, b):
    numbers_list = []
    for idx in range(len(a)):
        x = a[idx]*b[idx]
        numbers_list.append(x)
    result = 0
    for data in numbers_list:
        result += data
    return result
print(solution([1,2,3,4], [-3,-1,0,2]))