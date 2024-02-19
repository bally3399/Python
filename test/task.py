score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(score)

def length(score):
    count = 0
    for index in score:
        count += 1
    return count



def add_even():
    sum_even = 0
    for index in range(1, length(score), 2):
        sum_even += score[index]
    return sum_even



def add_odd():
    sum_odd = 0
    for index in range(0, length(score), 2):
        sum_odd += score[index]
    return sum_odd


def multiplication():
    multiply = 1
    for index in range(0, length(score), 2):
        multiply *= score[index]
    return multiply



def average_of_list():
    average = 0
    for index in range(0, length(score)):
        average += score[index] / length(score)
    return average


def largest_element():
    largest = score[0]
    for index in range(length(score)):
        if score[index] > largest:
            largest = score[index]
    return largest


def smallest_element():
    smallest = score[0]
    for index in range(length(score)):
        if score[index] < smallest:
            smallest = score[index]
    return smallest

def get_string(words):
    results = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            results.append(word)
    return results

