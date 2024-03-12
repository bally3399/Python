def count(sentence):
    count = 0
    count1 = 0

    for index in sentence:
        if index.isupper():
            count += 1
        if index.islower():
            count1 += 1
    return f"UPPER CASE {count} LOWER CASE {count1}"
