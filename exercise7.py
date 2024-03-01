digits = list(range(1, 51))


def check_even(number):
    return number % 2 == 0


ans = list(filter(check_even, digits))
print(ans)


digit = list(range(1, 51))

print(list(filter(lambda number: number % 2 == 0, digit)))

def jumoke(p):
    return p ** 2


print(list(map(jumoke, digit)))
print(list(map(lambda p: p ** 2, digit)))

