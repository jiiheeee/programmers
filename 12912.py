def solution(a, b):
    result = 0
    if a<b:
        for data in range(a, b+1):
            result = result + data
            return result
    elif a>b:
        for data in range(b, a+1):
            result = result + data
            return result
    elif a==b:
        return a
