# 정렬 arr.sort() 오름차순
# 정렬 arr.sort(reverse=True) 내림차순

number_list = []
def solution(n):
    n = str(n)
    for data in n:
        number_list.append(data)
    number_list.sort(reverse=True)
    x = "".join(number_list)
    return x

print(solution(118372))