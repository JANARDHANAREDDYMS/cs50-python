def main():
    x = int(input("Whats x:"))
    y = int(input("Whats y:"))

    maxval = first(x,y)

    print("The max value is",maxval)
def first(x,y):
    if x < y:
        return x
    else:
        return y

main()        