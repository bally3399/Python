name1 = "bolaji"
name2 = "dayo"
name3 = "chichi"
sentence = "welcome to semicolon africa"

print(name1 == name2)
print(name1 < name2)
print(ord('B'))
print("c" in name3)
print(f'[{name1:10} {name2:10}]')
print(f'[{name1:>10}]')
print(f'[{name1:<10}]')
print(f'[{name1:^10}]')
print(f'{name1} {name2} {name3}')
print(name1 + name2 + name3)
print(name1 * 5)
name4 = "  muhammed  "
print(len(name4.strip()))
print(len(name4))
print(name1.upper())
print(name3.lower())
print(name2.capitalize())
print(sentence.title())
print(name1.casefold())
print(sentence.count("e"))
print(sentence.index("e"))
print(sentence.rindex("e"))

name = input("enter yah name: ").strip()
if name.isalpha():
    print("valid name")
else:
    print("invalid name")

print(sentence.replace("africa", "World"))
print(sentence.split("to"))
print(sentence.partition("to"))
names = ["jane", "janet", "john", "joseph"]
print("-".join(names))




