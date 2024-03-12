def count(sentence1):
    counter = 0
    count1 = 0

    for index in sentence1:
        if index.isnumeric():
            counter += 1
        if index.isalpha():

            count1 += 1
    return f"LETTERS {counter} DIGIT {count1}"
