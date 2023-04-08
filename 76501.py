def solution(absolutes, signs):
    for idx, value in enumerate(signs):
        if value==False:
            absolutes[idx]= -int(absolutes[idx])
    
    result = 0
    for data in absolutes:
        result += data
        
    return result

print(solution([1,2,3], [False,False,True]))