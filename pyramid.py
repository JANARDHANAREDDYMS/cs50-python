def main():
    height = int(input("whats height"))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print(i,end="")
        print("#"*(i+1))

if __name__ == "__main__":
    main()    