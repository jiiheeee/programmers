def solution(arr, divisor):
    result = []
    for data in arr:
        if data % divisor == 0:
            result.append(data)
            result.sort()
        elif data % divisor != 0:
            pass
    if not result:
        return [-1]
    return result

print(solution([1000,100,30,3], 9))