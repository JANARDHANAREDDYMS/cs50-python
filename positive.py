def main():
    i = positive()
    print(i)


def positive():
    while True:
        n=input("Positive Integer:")
        if n>0:
            break
    return n