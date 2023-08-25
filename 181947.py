a, b = map(int, input().strip().split(' '))
data = [a, '+', b, '=', a+b]
print(*data)