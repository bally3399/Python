def characters(str1, str2):
    return str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]


element = "abc"
element1 = "xyz"
elements = "abcd"
elements1 = "rstu"
print(characters(element, element1))


