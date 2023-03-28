def solution(phone_number):
    return (int(len(phone_number))-4)*"*"+phone_number[-4:]

print(solution("01086736352"))