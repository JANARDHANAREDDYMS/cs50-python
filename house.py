name =  input("Whats your name:")

match name:
    case "harry"|"hermoine"|"Ron": 
        print("griffindor")
    case "draco":
        print("slytherin")
    case _:
        print("who?")