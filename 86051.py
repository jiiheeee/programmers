def solution(numbers):
    number_list = []
    for data in range(10):
        number_list.append(data)
    for i in numbers:
        number_list.remove(i)
    result = 0
    for plus in number_list:
        result += plus
    return result