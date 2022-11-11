name = input("whats ur name\n")

file = open("names.txt","a")
file.write(f"{name}\n")
file.close()