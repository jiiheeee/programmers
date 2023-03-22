def solution(x):
    result = 0
    x = str(x)
    for data in x:
        result += int(data)
    if int(x)%result == 0:
        return True
    else:
        return False
    
print(solution(10))