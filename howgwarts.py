import csv

houses = {
    "gryfiin":0,
    "hufflepuff" :0,
    "ravenclaw" : 0,
    "slytherin" : 0
}

with open("username.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        house = row[1]
        houses[house]+=1

for house in houses:
    print(f"{house}: {houses[house]}")