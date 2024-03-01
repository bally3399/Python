def sample(word):
    list = {}
    for char in word:
        counter = 0
        for words in word:
            if char == words:
                counter += 1
        list[char] = counter
    return list


print(sample("google.com"))

sample = "google.com"
print({k: sample.count(k) for k in sample})