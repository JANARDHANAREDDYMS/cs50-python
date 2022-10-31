import math


print("Enter the Opertion u wish to perform\n")
print("1)Add 2)Sub 3)Mul 4)Div 5)Sqr 6)Sqroot\n")
c = input("Enter your choice\n")


if c in range(1,4):
    x = int(input("Enter the no\n"))
    y = int(input("Enter another no\n"))
    match c:
        case "1":
           print(x+y)
        case "2":
            print(x-y)
        case "3":
            print(x*y)
        case "4":
            print(x/y)

else:
    match c:
        case "5":
                z = int(input("Enter the no whose sqaue you wish to perform\n"))
                print(math.pow(z,2))
        case "6":
            a = int(input("Enter the no whose sqaue you wish to perform\n"))
            print(math.sqrt(a))
