sum_odd = 0
sum_even = 0
num = int(input('Enter number: '))
for idx in range(num):
    if idx % 2 == 0:
        sum_even += idx
    else:
        sum_odd += idx
print(sum_even)
print(sum_odd)


def sum_of_even_and_odd(number):
    sum_of_odd = 0
    sum_of_even = 0
    for idx in range(number):
        if idx % 2 == 0:
            sum_of_even += idx
        else:
            sum_of_odd += idx
    return sum_of_even, sum_of_odd


number = 10
try:
    numbers = int(input("Enter number"))
    sum_even = sum(list(range(1, numbers))[1::2])
    sum_odd = sum(list(range(1, numbers))[::2])
except ValueError:
    print("invalid input")
print(sum_even, sum_odd)


