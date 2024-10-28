#def main():
#    print_row(7)

#def print_column(height):
#    for _ in range(height):
#        print("#")


#def print_row(width):
#    print("?" * width)

#main()





def main():
    print_square(6)


def print_square(size):
    
    # For each row in square
    for i in range(size):
        print("#" * size)


main()