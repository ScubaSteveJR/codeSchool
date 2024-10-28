# name = input("What's your name? ")
#
# # Remove whitespace Captialize name
# name = name.strip().title()
#
# # split into first and last name
# first, last = name.split(" ")
#
# # F string
# #print(f"hello, {first}")
#

def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()
