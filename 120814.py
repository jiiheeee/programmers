def solution(n):
    if n%7==0:
        return n//7
    elif n%7!=0:
        return n//7+1

print(solution(15))