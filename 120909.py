import math
def solution(n):
    x = str(math.sqrt(n)).split(".")
    if x[1] == "0":
        return 1
    else:
        return 2

print(solution(232))