def solution(price, money, count):
    a = []
    for data in range(1, count+1):
        a.append(price * data)
    result = 0
    for i in a:
        result += i
    if money-result>0:
        return 0
    else:
        return abs(money-result)

print(solution(3,40,4))