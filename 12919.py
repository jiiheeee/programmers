def solution(seoul):
    for idx, name in enumerate(seoul):
        if name == "kim":
            return "김서방은 "+f"{idx}"+"에 있다"

print(solution(["jane", "kim"]))