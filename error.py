def main():
    x = get_int()
    print(f"x is {x}")


def get_int(): #or get_int(prompt)
    while True:
        try:
            x = int(input("WHats x?"))  #or int(input(prompt))
        except ValueError:
            print("X is not an integer") #or just use pass
        else:
            return x    


main()