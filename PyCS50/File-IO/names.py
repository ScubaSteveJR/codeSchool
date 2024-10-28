# names = []
#
# for _ in range(3):
#     name = input("What's your name? ")
#     names.append(name)
#
# for name in sorted(names):
#     print(f"hello, {name}")

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hellow, {name}")
