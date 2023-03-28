def solution(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        cnt = 0
        while True:
            if num%2==0:
                num = num//2
            elif num%2!=0:
                num = (num*3)+1
            cnt += 1

            if cnt >= 500:
                return -1
            if num == 1:
                break
        answer = cnt
    return answer

print(solution(6))