def solution(s):
    spell = []
    for data in s:
        spell.append(data)
    spell.sort(reverse=True)
    x = "".join(spell)
    return x

print(solution("Zbcdefg"))